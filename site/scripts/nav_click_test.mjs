import { chromium } from 'playwright-core';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const BASE = 'https://homgorn.github.io/argymaq-seo-case';
const browser = await chromium.launch({ executablePath: chromePath, headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });

const clicks = [
  { from: '/', link: 'План', expect: '/plan/' },
  { from: '/plan/', link: 'Аудит', expect: '/audit/' },
  { from: '/audit/', link: 'Что сделали', expect: '/work/' },
  { from: '/work/', link: 'Результат', expect: '/result/' },
  { from: '/result/', link: 'argymaq.kg', expect: '/' },
];

let failed = 0;
for (const c of clicks) {
  await page.goto(`${BASE}${c.from}`, { waitUntil: 'networkidle', timeout: 30000 });
  await page.getByRole('link', { name: new RegExp(c.link) }).first().click();
  await page.waitForLoadState('networkidle');
  const ok = page.url().startsWith(`${BASE}${c.expect}`);
  console.log(`${ok ? 'OK  ' : 'FAIL'} click "${c.link}" on ${c.from} -> ${page.url()}`);
  if (!ok) failed++;
}

await browser.close();
process.exit(failed ? 1 : 0);