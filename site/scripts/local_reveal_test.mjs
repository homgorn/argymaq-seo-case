import { chromium } from 'playwright-core';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const b = await chromium.launch({ executablePath: chromePath, headless: true });
const pg = await b.newPage({ viewport: { width: 1280, height: 1100 } });
await pg.goto('http://localhost:4590/argymaq-seo-case/kase/argymaq-kg/audit/', {
  waitUntil: 'networkidle', timeout: 30000,
});

// прокручиваем до конца, чтобы триггернуть все IntersectionObserver
await pg.evaluate(async () => {
  await new Promise((resolve) => {
    let y = 0;
    const t = setInterval(() => {
      y += 400;
      window.scrollTo(0, y);
      if (y >= document.body.scrollHeight + 400) { clearInterval(t); resolve(); }
    }, 30);
  });
});
await pg.waitForTimeout(400);

const stats = await pg.evaluate(() => {
  const els = [...document.querySelectorAll('.issue.reveal')];
  const visible = els.filter((e) => getComputedStyle(e).opacity === '1').length;
  const hidden = els.filter((e) => getComputedStyle(e).opacity !== '1').length;
  return { total: els.length, visible, hidden };
});
console.log('issue cards:', JSON.stringify(stats));

await pg.screenshot({ path: '../work/shots/audit-full.png', fullPage: true });
await b.close();