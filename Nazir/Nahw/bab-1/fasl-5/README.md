<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');
  @font-face {
    font-family: 'UrduArabicScript';
    src: local('Noori Nastaliq'), local('Jameel Noori Nastaleeq'), local('Alvi Nastaleeq'),
         local('Faiz Lahori Nastaleeq'), local('Noto Nastaliq Urdu'),
         local('Scheherazade New'), local('Amiri');
    unicode-range: U+0600-06FF, U+0750-077F, U+FB50-FDFF, U+FE70-FEFF;
    size-adjust: 135%;
    font-display: swap;
  }
  body, .markdown-body {
    font-family: 'UrduArabicScript', 'Noto Nastaliq Urdu', -apple-system, BlinkMacSystemFont,
                 'Segoe UI', system-ui, sans-serif;
    font-size: 20px;
    line-height: 2.05;
    max-width: 1100px;
    margin: 0 auto;
    padding: 2rem 2.5rem;
    color: #1a1a1a;
  }
  h1 { font-size: 2.3em; color: #064e3b; border-bottom: 3px solid #064e3b; padding-bottom: 0.35em; line-height: 1.5; }
  h2 { font-size: 1.8em; color: #064e3b; border-bottom: 2px solid #ddd; padding-bottom: 0.3em; margin-top: 2.2em; line-height: 1.5; }
  h3 { font-size: 1.45em; color: #0e7490; margin-top: 1.8em; line-height: 1.5; }
  h4 { font-size: 1.22em; color: #b45309; margin-top: 1.4em; line-height: 1.5; }
  p, li { margin: 0.9em 0; line-height: 2.1; }
  ul, ol { padding-left: 1.7em; }
  table { border-collapse: collapse; margin: 1.5em 0; width: 100%; }
  th, td { padding: 0.75em 1em; border: 1px solid #ccc; line-height: 1.95; vertical-align: top; text-align: left; }
  th { background: #e8f4f4; font-weight: 700; color: #064e3b; }
  tr:nth-child(even) td { background: #fafafa; }
  blockquote { border-left: 5px solid #064e3b; padding: 0.7em 1.3em; background: #f3faf6; margin: 1.3em 0; color: #2a2a2a; }
  blockquote p { margin: 0.5em 0; }
  strong { font-weight: 700; color: #0a0a0a; }
  code { background: #f4f4f4; padding: 0.18em 0.45em; border-radius: 3px; color: #be123c; font-size: 0.9em; font-family: 'Cascadia Code', 'Fira Code', Consolas, monospace; }
  pre { background: #f7f7f7; padding: 1em 1.2em; border-radius: 6px; border: 1px solid #eee; overflow-x: auto; line-height: 1.6; font-family: 'Cascadia Code', 'Fira Code', Consolas, monospace; font-size: 0.92em; }
  hr { border: none; border-top: 1px solid #ddd; margin: 2.3em 0; }
  a { color: #0e7490; text-decoration: none; border-bottom: 1px dotted #0e7490; }
  a:hover { color: #064e3b; border-bottom-style: solid; }
</style>

# Fasl 5 — اسم غیر متمکن کے اقسام (Ism Ghair Mutamakkin ke Aqsam)

> **Status:** 🏁 **MUKAMMAL** — All 8 qismein of Ism Ghair Mutamakkin documented across Sections 13-20 (PDF p-18 → p-25).
>
> **Scope per backup TOC:** *Mabni Asma ki systematic taxonomy*.
>
> **Source-of-truth:** [../../IlmUnNahwAlBushraColor (1).pdf](../../IlmUnNahwAlBushraColor%20(1).pdf), pages 18-25.
>
> **Pre-split history:** This Fasl was migrated 2026-05-30 from monolithic `Nahw/notes.md` (pre-split backup at `Nahw/_archive/notes-pre-split-2026-05-30.md`, lines 2700-4965) into 8 per-Section files under this folder. Content is byte-identical to the backup. Migration plan: [../../_planning/architecture-v2.md](../../_planning/architecture-v2.md).

---

## Section TOC

| Section | PDF page | Book page | File | Snapshot (from backup TOC) |
|---|---|---|---|---|
| 13 | p-18 | p-۱۷ | [section-13.md](section-13.md) | Fasl 5 ka aaghaaz: Ism Ghair Mutamakkin ki 8 qismein + Mudmaraat ki 5 qismein + 14 Zameer Marfu' Muttasil + 14 Zameer Marfu' Munfasil + Tanbeeh + Mudmar/Zameer footnote |
| 14 | p-19 | p-۱۸ | [section-14.md](section-14.md) | Mansoob 2 qismein + Majroor 2 types (Mudmaraat ka khaatma start) |
| 15 | p-20 | p-۱۹ | [section-15.md](section-15.md) | Mudmaraat MUKAMMAL (Table 6 bottom row) + Faida-e-Zameer-e-Shaan o Qissa + Asma-e-Mausoolah ka shuru (10 forms + 3 exceptions + Mausool ki poori tareef + Sila + 4-layer Tarkeeb) |
| 16 | p-21 | p-۲۰ | [section-16.md](section-16.md) | Exercise 1 (Mausoolah ke 5 jumlay tarkeeb) + Qism #3 اسمائے اشارہ ka shuru: Ishara Qareeb 5 + Ba'eed 5 = 10 forms + Mushar Ilayh ki poori tareef + Tarkeeb walkthrough + Exercise 2 (5 Ishara jumlay) |
| 17 | p-22 | p-۲۱ | [section-17.md](section-17.md) | Qism #4 اَسْمَائے اَفْعَال ka aaghaaz (2 sub-qismein, 7+3=10 forms) + Qism #5 اَسْمَائے اَصْوَات (5 awaz misaalein) + Qism #6 اَسْمَائے ظُرُوْف ka taaruf + ظَرْفِ زَمان sub-qism (a) — 12-item list + اِذْ ki tafseel (maazi) + اِذَا ki tafseel (mustaqbil — TRUNCATED) + Quran ayah ﴿اِذَا جَاءَ نَصْرُ اللهِ﴾ verbatim no-attribution |
| 18 | p-23 | p-۲۲ | [section-18.md](section-18.md) | Zarf-e-Zaman sub-qism (a) MUKAMMAL: اِذَا ka teesra use (مفاجات) + items 3-12 ki sab tafseel (مَتٰی / کَیْفَ / اَیَّانَ / اَمْسِ / مُذْ + مُنْذُ / قَطُّ / عَوْضُ / قَبْلُ + بَعْدُ) + 2 Quran ayahs (1 no-attribution + 1 book-attributed as "اللہ تعالیٰ کا فرمان") |
| 19 | p-24 | p-۲۳ | [section-19.md](section-19.md) | قَبْلُ/بَعْدُ tafseer khaatma + 2 nayi misaalein (Mudaf Ilayh poshida) + Zarf-e-Makaan sub-qism (b) ka shuru: 9-item list + حَیْثُ + قُدَّامْ/خَلْفْ + تَحْتُ/فَوْقُ + عِنْدَ + أَیْنَ/اَنّٰی (3 uses + 3rd Quran ayah ﴿فَأْتُوْا حَرْثَکُمْ أَنّٰی شِئْتُمْ﴾ book-attributed as "کَقَوْلِہٖ تَعَالٰی") + لَدٰی/لَدُنْ tareef start (compared to عِنْدَ — TRUNCATED) |
| 20 | p-25 | p-۲۴ | [section-20.md](section-20.md) | **🏁 FASL 5 MUKAMMAL 🏁** — لَدٰی/لَدُنْ khaatma + فَائِدَہ ۱ (Mabni-ending classification) + فَائِدَہ ۲ (non-mabni zarf Mudaf-to-jumla rule + 4th Quran ayah ﴿هٰذَا یَوْمُ یَنْفَعُ الصَّادِقِیْنَ صِدْقُہُمْ﴾ + naye forms یَوْمَئِذٍ/حِیْنَئِذٍ) + Qism #7 اَسْمَائے کِنَایَات (tareef + 4 misaalein) + Qism #8 مُرَکَّب بِنَائی (naam + misaal اَحَدَ عَشَرَ — definition Section 6 cross-ref) |

---

## Navigation

- ⬆ Up: [Bab 1 README](../README.md)
- 📖 Top: [Nahw index](../../index.md)
- 📐 Charts: [../../charts.md](../../charts.md)
- 📋 I'rab tables: [../../irab-tables.md](../../irab-tables.md)
