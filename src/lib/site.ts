export const SITE = {
  title: 'Gasol 的技術與投資筆記',
  description:
    '記錄半導體／DDIC 領域的通用技術知識，以及個人的投資研究與複盤。內容為個人學習筆記，不構成任何投資建議。',
  author: 'Gasol',
  lang: 'zh-TW',
};

export type CategorySlug = 'invest' | 'work';

export const CATEGORIES: { slug: CategorySlug; label: string; blurb: string }[] = [
  {
    slug: 'invest',
    label: '投資',
    blurb: '市場觀察、資產配置、投資複盤。個人紀錄，不構成投資建議。',
  },
  {
    slug: 'work',
    label: '工作',
    blurb: '半導體與顯示驅動 IC 的通用技術知識、工具方法與工程思維。',
  },
];

export const categoryLabel = (slug: CategorySlug): string =>
  CATEGORIES.find((c) => c.slug === slug)?.label ?? slug;
