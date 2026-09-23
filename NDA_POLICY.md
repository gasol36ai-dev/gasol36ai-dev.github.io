# NDA 內容政策（強制）

> **本網站為公開網站。任何公司相關機密，絕對不得上網。**

## 一、絕對禁止（無任何例外）

以下內容**一律不得**出現在本 repo 的任何檔案中（含程式碼、註解、commit message、圖片）：

1. **暫存器相關設定**
   - 暫存器名稱、位址、數值（`REG_*`、`0xNN`、位元欄位 `[15:8]` 等）
   - register map / setting / table
   - I2C / SPI 的讀寫序列

2. **公司識別資訊**
   - 公司名稱、內部專案代號、客戶名稱
   - 標示機密、內部使用、限閱之文件內容

3. **公式**
   - 見下方第二節：**預設拒絕**，需逐行人工放行

## 二、公式：預設拒絕（default-deny）

公式是本政策**最高風險項**。任何公式（LaTeX、等號運算式、函式定義式）**預設一律攔阻**。

若某條公式確認為**公開領域的通用知識**（例如教科書上的歐姆定律），必須在**該行末尾**加上放行標記：

```markdown
V = I × R  <!-- nda-ok: 歐姆定律，國中教科書通用公式 -->
```

- 標記格式：`<!-- nda-ok: 理由 -->`，**理由必填**
- 沒有標記 → 檢查器攔阻 → **無法部署**
- 每一條公式都要各自標記，不會因為同檔案有一條放行就全部放行

## 三、文章必填聲明

每篇文章的 frontmatter 必須包含：

```yaml
nda_cleared: true
nda_notes: '說明本文為何不含公司機密（例如：全部為公開領域通用知識）'
```

- 缺少 `nda_cleared: true` → Astro 建置失敗 ＋ 檢查器攔阻
- `nda_notes` 少於 10 字元 → 攔阻

## 四、三道防線

| 防線 | 機制 | 攔阻時機 |
|---|---|---|
| 1 | Astro content schema（`nda_cleared` 必填） | `pnpm build` |
| 2 | git pre-commit hook（`.githooks/pre-commit`） | `git commit` |
| 3 | GitHub Actions gate（`scripts/nda_check.py`） | push 後的部署前 |

> 三道防線互相獨立。任一道攔下，內容就上不了網。

## 五、本機 hook 啟用方式（新環境）

```bash
git config core.hooksPath .githooks
```

## 六、緊急處置

若不慎已推送機密內容：

1. **立即**在 GitHub 將 repo 改為 private（`gh repo edit --visibility private`）
2. 以 `git filter-repo` 或 BFG 清除歷史（**force push 不足以移除**，commit 仍可被 API 取得）
3. 通報公司

> 注意：公開 repo 的內容可能已被搜尋引擎與第三方快取。**事後補救遠比事前攔阻困難。**
