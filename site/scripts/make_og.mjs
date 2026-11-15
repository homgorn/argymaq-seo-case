import { chromium } from 'playwright-core';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const browser = await chromium.launch({ executablePath: chromePath, headless: true });
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });

await page.setContent(`<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body { margin:0; width:1200px; height:630px; background:#09090b; color:#fff;
         font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
         display:flex; flex-direction:column; justify-content:center; padding:64px; }
  .eyebrow { font-size:15px; text-transform:uppercase; letter-spacing:0.12em; color:#a1a1aa; margin-bottom:26px; }
  h1 { font-size:58px; line-height:1.08; letter-spacing:-0.032em; margin:0 0 20px; max-width:1000px; font-weight:700; }
  .grad { background:linear-gradient(100deg,#60a5fa,#a78bfa 55%,#f472b6);
          -webkit-background-clip:text; background-clip:text; color:transparent; }
  .sub { font-size:19px; color:#a1a1aa; margin:0; }
</style></head>
<body>
  <div class="eyebrow">argymaq.kg — аудит · ноябрь 2026</div>
  <h1>Сайт есть. <span class="grad">Его не видно.</span></h1>
  <p class="sub">25 проблем в 10 категориях · план из 4 приоритетов · всё измерено</p>
</body></html>`);

await page.screenshot({ path: 'public/og-default.png' });
await browser.close();
console.log('og-default.png written (neutral, case-only)');