/**
 * Проверка живого сайта Refertur.net (homgorn.github.io/argymaq-seo-case) через Playwright:
 * консольные ошибки, размеры canvas, горизонтальный скролл, мобильная вёрстка.
 *
 * Запуск:  node scripts/visual_check.mjs
 */
import { chromium } from 'playwright-core';
import { mkdirSync } from 'fs';
import { join } from 'path';

const BASE = 'https://homgorn.github.io/argymaq-seo-case';
const PAGES = [
  { path: '/', name: 'home' },
  { path: '/kase/argymaq-kg/', name: 'case' },
  { path: '/kase/argymaq-kg/audit/', name: 'audit' },
  { path: '/kase/argymaq-kg/result/', name: 'result' },
  { path: '/ceny/', name: 'ceny' },
  { path: '/kontakty/', name: 'kontakty' },
  { path: '/uslugi/geo/', name: 'geo' },
];
const OUT = 'H:/susa ai 500/argymaq.kg/work/shots';

mkdirSync(OUT, { recursive: true });

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const browser = await chromium.launch({ executablePath: chromePath, headless: true });

const report = [];
let failed = 0;

for (const theme of [{ name: 'desktop', width: 1280, height: 800 },
                     { name: 'mobile', width: 390, height: 844 }]) {
  console.log(`\n=== ${theme.name.toUpperCase()} (${theme.width}x${theme.height}) ===`);
  for (const p of PAGES) {
    const url = `${BASE}${p.path}`;
    const page = await browser.newPage({ viewport: { width: theme.width, height: theme.height } });
    const errors = [];
    page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
    page.on('requestfailed', (r) => errors.push('requestfailed: ' + r.url() + ' :: ' + (r.failure()?.errorText || '')));

    let status = 0;
    try {
      const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
      status = resp ? resp.status() : 0;
    } catch (e) {
      errors.push('goto: ' + e.message);
    }

    // Горизонтальный скролл (ошибка вёрстки)
    const hscroll = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 2);

    // H1
    const h1 = await page.locator('h1').count();

    // Canvas внутри графиков (если есть)
    const canvas = await page.locator('canvas').evaluateAll((els) =>
      els.map((el) => ({ w: el.width, h: el.height, visible: el.offsetWidth > 0 }))
    );

    // График нарисован? (canvas имеет ненулевой размер)
    for (const c of canvas) {
      if (c.visible && (c.w < 10 || c.h < 10)) errors.push('canvas has near-zero size');
    }

    const shot = join(OUT, `${theme.name}-${p.name}.png`);
    await page.screenshot({ path: shot, fullPage: false });

    const ok = status === 200 && h1 === 1 && errors.length === 0 && !hscroll;
    if (!ok) failed++;
    report.push({ theme: theme.name, path: p.path, status, h1, hscroll, errors, shot });
    console.log(`${ok ? 'OK  ' : 'FAIL'} ${p.path.padEnd(28)} status=${status} h1=${h1} hscroll=${hscroll} errors=${errors.length}`);
    if (errors.length) errors.forEach((e) => console.log('     - ' + e.slice(0, 160)));
    await page.close();
  }
}

await browser.close();
console.log(`\n=== ИТОГ: ${OUT_SIZE()} снимков, неудачных проверок: ${failed} ===`);
function OUT_SIZE() { return PAGES.length * 2; }
process.exit(failed ? 1 : 0);
