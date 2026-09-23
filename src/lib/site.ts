export const SITE = {
  title: 'Gasol 的技術與投資筆記',
  description:
    '記錄半導體／DDIC 領域的通用技術知識，以及個人的投資研究與複盤。內容為個人學習筆記，不構成任何投資建議。',
  author: 'Gasol',
  lang: 'zh-TW',
};

export const PAGE_SIZE = 30;

export type CategorySlug = 'invest' | 'work';

export interface Category {
  slug: CategorySlug;
  label: string;
  blurb: string;
}

export const CATEGORIES: Category[] = [
  {
    slug: 'invest',
    label: '投資',
    blurb: '市場觀察、能源與 AI 主題追蹤、黃金、台股 IPO，以及研究筆記。個人紀錄，不構成投資建議。',
  },
  {
    slug: 'work',
    label: '工作',
    blurb: '半導體與顯示驅動 IC 的通用技術知識、工具方法與工程思維。',
  },
];

export interface Topic {
  slug: string;
  label: string;
  blurb: string;
}

/** 投資分類 —— 對應 Telegram「資訊站（8865）」的 topic 結構（末項為彙整桶） */
export const INVEST_TOPICS: Topic[] = [
  { slug: 'warroom', label: '每日戰情室', blurb: '每日市場戰情與即時判讀。' },
  { slug: 'energy', label: '能源追蹤', blurb: '電力、核能、鈾與清潔能源相關追蹤。' },
  { slug: 'ai-robotics', label: 'AI 與機器人', blurb: '機器人、具身智能與空間智能。' },
  { slug: 'gold', label: '黃金分析', blurb: '黃金與貴金屬市場分析。' },
  { slug: 'ipo', label: '台股 IPO', blurb: '台股公開申購與抽籤監控。' },
  { slug: 'display', label: '顯示驅動市場', blurb: '面板與顯示驅動 IC 市場動態。' },
  { slug: 'ai-glasses', label: 'AI 眼鏡', blurb: 'AR／VR／MR 頭戴裝置市場。' },
  { slug: 'research', label: '研究筆記', blurb: '宏觀、量子金融、技術分析與量化指標等研究紀錄。' },
];

const TOPIC_BY_LABEL = new Map(INVEST_TOPICS.map((t) => [t.label, t.slug]));

export const topicSlugByLabel = (label: string): string =>
  TOPIC_BY_LABEL.get(label) ?? 'research';

export const topicBySlug = (slug: string): Topic | undefined =>
  INVEST_TOPICS.find((t) => t.slug === slug);

export const categoryLabel = (slug: string): string =>
  CATEGORIES.find((c) => c.slug === slug)?.label ?? slug;
