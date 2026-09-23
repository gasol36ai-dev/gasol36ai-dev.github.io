import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string().default(''),
    pubDate: z.coerce.date(),
    category: z.enum(['invest', 'work']),
    /** 投資子分類（對應資訊站 8865 的 topic）；工作類留空 */
    topic: z.string().default(''),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    /** 來源檔（wiki 相對路徑），僅供追溯 */
    source: z.string().default(''),
    // ── NDA 硬性防線：缺這兩欄，pnpm build 直接失敗 ──
    nda_cleared: z.literal(true),
    nda_notes: z.string().min(10),
  }),
});

export const collections = { posts };
