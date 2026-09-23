import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// TODO: 待 VIP 提供自有網域後，把 site 換成正式網域（影響 canonical / sitemap / RSS 絕對路徑）
export default defineConfig({
  site: 'https://gasol36ai.github.io',
  base: '/',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
  markdown: {
    shikiConfig: { theme: 'github-dark' },
  },
});
