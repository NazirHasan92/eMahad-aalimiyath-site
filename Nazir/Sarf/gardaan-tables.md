<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');
  @font-face {
    font-family: 'UrduArabicScript';
    src: local('Noori Nastaliq'), local('Jameel Noori Nastaleeq'), local('Alvi Nastaleeq'),
         local('Faiz Lahori Nastaleeq'), local('Noto Nastaliq Urdu'),
         local('Scheherazade New'), local('Amiri');
    unicode-range: U+0600-06FF, U+0750-077F, U+FB50-FDFF, U+FE70-FEFF;
    size-adjust: 140%;
    font-display: swap;
  }
  body, .markdown-body {
    font-family: 'UrduArabicScript', 'Noto Nastaliq Urdu', -apple-system, 'Segoe UI', sans-serif;
    font-size: 20px; line-height: 2.05; max-width: 1100px; margin: 0 auto; padding: 2rem 2.5rem; color: #1a1a1a;
  }
  h1 { font-size: 2.3em; color: #064e3b; border-bottom: 3px solid #064e3b; padding-bottom: 0.35em; }
  h2 { font-size: 1.8em; color: #064e3b; border-bottom: 2px solid #ddd; padding-bottom: 0.3em; margin-top: 2.2em; }
  h3 { font-size: 1.45em; color: #0e7490; margin-top: 1.8em; }
  table { border-collapse: collapse; margin: 1.5em 0; width: 100%; }
  th, td { padding: 0.85em 1.1em; border: 1px solid #ccc; line-height: 2.1; vertical-align: middle; text-align: center; }
  th { background: #e8f4f4; font-weight: 700; color: #064e3b; }
  tr:nth-child(even) td { background: #fafafa; }
  blockquote { border-left: 5px solid #064e3b; padding: 0.7em 1.3em; background: #f3faf6; margin: 1.3em 0; }
  code { background: #f4f4f4; padding: 0.18em 0.45em; border-radius: 3px; color: #be123c; font-size: 0.9em; }
</style>

# Sarf — Gardaan Tables (Markdown, harakaat-perfect)

> **All Sarf paradigm tables (conjugation grids) live here.**
>
> Why tables (not Mermaid): Paradigm grids are inherently two-dimensional; forcing them into Mermaid produces unreadable output. Markdown tables match the natural 2-axis structure (person/gender × number, or sheegha # × bab).
>
> **Source verification:** Every table is annotated with its source PNG (`p-NNN`). PNG > table always. If harakaat appears unclear in PNG, mark with `[?]` rather than guessing.

---

## Standard table format

For a single bab's gardaan (e.g., Fi'l-e-Maazi Maaloom, Bab Nasara):

| # | Sheegha (Arabic + harakaat) | Roman | Tarjuma | Person · Gender · Number |
|---|---|---|---|---|
| 1 | نَصَرَ | nasara | us ne madad ki | Ghaa'ib · muzakkar · wahid |
| 2 | نَصَرَا | nasaraa | un dono ne madad ki | Ghaa'ib · muzakkar · tasniya |
| ... | ... | ... | ... | ... |

**Source**: `Sarf/.pages/p-NNN.png`

---

## Table index

*(Built up session by session. One table per bab/paradigm.)*

| # | Concept | Source | Type | Added |
|---|---|---|---|---|
| 1 | مُعرَب Fi'l ka aakhri harakah عامل ke saath badalna | Sarf p-020, Slide 8 | starter / i'rab demonstration | 2026-05-28 (backfill) |

> **Note:** Pehla **classical 14-form gardaan** Topic 2.0 (Fi'l-e-Maazi) par expected hai. Table 1 niche **paradigm-style starter** hai — Slide 8 ke Mu'arrab examples ko organized form mein dikha raha hai.

---

## Table 1 — مُعرَب Fi'l ka aakhri harakah عامل ke saath badalna

**Concept:** Sub Topic 1.2 Slide 8 par book ne **یَعْلَمُ** ki misaal se dikhayi ke **مُعرَب Fi'l** ka **aakhri harakah** **عامل ke aane se badalta hai**. Yeh starter paradigm us tabdeeli ko table form mein arrange karta hai.

**Source:** Sarf PDF p-020, Slide 8 (مُعرَب Fi'l ki misaal).

**Verbatim PDF text:** *"فعل معرب: وہ فعل ہے جس کا آخر عامل کے بدلنے سے بدل جائے، جیسے: **یَعْلَمُ، اَنْ یَعْلَمَ، لَنْ یَعْلَمَ، لَمْ یَعْلَمْ** ۔"*

| # | Form (PDF) | عامل | Aakhri harakah | Tabdeeli |
|---|---|---|---|---|
| 1 | **یَعْلَمُ** | (default — koi عامل nahi) | **ـُ (pesh / damma)** | Base form |
| 2 | **اَنْ یَعْلَمَ** | **اَنْ** | **ـَ (zabar / fatha)** | pesh → zabar |
| 3 | **لَنْ یَعْلَمَ** | **لَنْ** | **ـَ (zabar / fatha)** | pesh → zabar |
| 4 | **لَمْ یَعْلَمْ** | **لَمْ** | **ـْ (sukoon)** | pesh → sukoon |

**Reading guide:**
- **Row 1** = "default" form jab koi عامل nahi (يَعْلَمُ ka aakhir پر pesh)
- **Rows 2-4** = mukhtalif عوامل (amils) lagne par aakhir badalti hai
- Yeh **مُعرَب** ki khasiyat: عامل ke saath aakhri harakah change hota hai

**Mohim baat:**
- Yeh **mini-paradigm** hai — sirf ek Fi'l (یَعْلَمُ) ki **i'rab tabdeeli** dikha raha hai
- Classical **14-form gardaan** (person × number × gender matrix) Topic 2.0 par aayega — wahan **مکمل bab gardaan** hoga
- Iss table ka maqsad: visualize karna ke "**Mu'arrab = aakhir badalta hai**" ka asal matlab

**Status:** PDF-VERIFIED 2026-05-28 (backfill). PDF text verbatim. Table 1 ka structure pedagogically organized hai — content sirf PDF se hai.

---

*Next paradigm table: Topic 2.0 (Fi'l-e-Maazi) ka **pehla full bab gardaan** — woh 14 sheeghas ka mukammal matrix hoga.*
