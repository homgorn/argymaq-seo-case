import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// GitHub Pages: сайт лежит в подкаталоге <repo>/
// Для своего домена поставь base: '/' и site: 'https://digitalgrowth.kg'
const REPO = 'argymaq-seo-case';

export default defineConfig({
  site: `https://homgorn.github.io`,
  base: `/${REPO}`,
  output: 'static',
  trailingSlash: 'ignore',
  build: {
    assets: '_astro',
    inlineStylesheets: 'auto',
  },
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});