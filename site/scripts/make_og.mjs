import { chromium } from 'playwright-core';
import { execSync } from 'child_process';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const browser = await chromium.launch({ executablePath: chromePath, headless: true });
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });

await page.setContent(`<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body { margin:0; width:1200px; height:630px; background:#09090b; color:#fff;
         font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
         display:flex; flex-direction:column; justify-content:center; padding:64px; }
  .brand { display:flex; align-items:center; gap:14px; font-size:21px; font-weight:700; margin-bottom:34px; }
  .badge { width:44px; height:44px; border-radius:10px; background:#fff; color:#09090b;
           display:grid; place-items:center; font-size:22px; font-weight:800; }
  h1 { font-size:52px; line-height:1.12; letter-spacing:-0.03em; margin:0 0 18px;
       max-width:900px; font-weight:700; }
  .grad { background:linear-gradient(100deg,#60a5fa,#a78bfa 55%,#f472b6);
          -webkit-background-clip:text; background-clip:text; color:transparent; }
  .sub { font-size:20px; color:#a1a1aa; margin:0; }
</style></head>
<body>
  <div class="brand"><div class="badge">R</div>Refertur.net</div>
  <h1>Приводим клиентов из поиска, соцсетей и <span class="grad">нейросетей</span> — с понятными цифрами</h1>
  <p class="sub">SEO · Карты · Реклама · Сайты под ключ — Бишкек, Кыргызстан</p>
</body></html>`);

await page.screenshot({ path: 'public/og-default.png' });
await browser.close();
console.log('og-default.png written');