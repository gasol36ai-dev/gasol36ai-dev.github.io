# Gasol 的技術與投資筆記

個人筆記站。Astro 靜態網站，部署於 GitHub Pages。

## 快速開始

```bash
pnpm install
pnpm dev        # http://localhost:4321
pnpm build      # 產出 dist/
pnpm preview    # 本機預覽 dist/
```

## 新增文章

在 `src/content/posts/` 新增 `.md` 檔即可，frontmatter 格式：

```yaml
---
title: '文章標題'
description: '一句話摘要，會顯示在列表與 SEO description'
pubDate: 2026-09-23
category: 'invest'   # invest（投資）或 work（工作）
tags: ['標籤1', '標籤2']
draft: false         # true = 不輸出到站台
---
```

檔名即網址：`src/content/posts/foo.md` → `/posts/foo/`

## 內容原則（**上線前必守**）

- **工作類文章只放公開領域的通用技術知識**，不得包含任職公司的內部資訊、客戶資料、未公開技術細節或可識別的專案代號。
- **投資類文章為個人紀錄，不構成投資建議**，不推薦特定標的、不揭露具體持倉。
- 敏感草稿請設 `draft: true`，或放在 `src/content/posts/` 之外。

## 站台設定

- 站名／描述／作者：`src/lib/site.ts`
- 網域（canonical / sitemap / RSS 用）：`astro.config.mjs` 的 `site`
- 自訂網域：需同時放置 `public/CNAME`（內容為網域，如 `blog.example.com`）

## 部署

推送到 `main` 分支後，GitHub Actions（`.github/workflows/deploy.yml`）自動建置並部署到 GitHub Pages。

首次需在 repo 的 **Settings → Pages → Source** 選 **GitHub Actions**。

## 目錄

```
src/
  content/posts/     文章（Markdown）
  layouts/           版型
  components/        元件
  pages/             路由
  lib/site.ts        站台常數
  styles/global.css  樣式
public/              靜態資源（favicon、CNAME）
```
