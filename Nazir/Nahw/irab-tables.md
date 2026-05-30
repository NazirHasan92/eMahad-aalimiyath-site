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

# Nahw — I'rab Tables (Markdown, harakaat-perfect)

> **All Nahw i'rab paradigm tables and case-marking grids live here.**
>
> Why tables (not Mermaid): I'rab grids are inherently 2-axis (noun type × case, or kalimah category × i'rab status). Markdown tables match this naturally.
>
> **Source verification:** Every table is annotated with its source PNG. PNG > table always.

---

## Standard table formats

### I'rab master grid (9 noun categories × 3 cases)

| Noun category | Raf' (مرفوع) | Nasb (منصوب) | Jarr (مجرور) |
|---|---|---|---|
| Mufrad muzakkar | ضمّہ — كتابٌ | فتحہ — كتابًا | كسرہ — كتابٍ |
| Jam' muzakkar saalim | واو — مسلمونَ | يا — مسلمينَ | يا — مسلمينَ |
| ... | ... | ... | ... |

**Source**: `Nahw/.pages/p-NN.png`

### Per-sentence tarkeeb (i'rab analysis)

```
Sentence: ضَرَبَ زَيْدٌ عَمْرًا
```

| Lafz | Type | I'rab | Sabab |
|---|---|---|---|
| ضَرَبَ | Fi'l Maazi | Mabni 'ala al-fath | Fi'l hai |
| زَيْدٌ | Ism (Faail) | Marfu' bi al-damma | Faail ka raf' |
| عَمْرًا | Ism (Maf'ul) | Mansub bi al-fatha | Maf'ool ka nasb |

**Source**: `Nahw/.pages/p-NN.png`

---

## Table index

| # | Table | Source page | Added |
|---|-------|-------------|-------|
| 1 | Zameer Marfu' Muttasil — 14 forms (ضَرَبْتُ ... ضَرَبْنَ paradigm) | PDF p-18 | 2026-05-29 |
| 2 | Zameer Marfu' Munfasil — 14 forms (اَنَا ... هُنَّ paradigm) | PDF p-18 | 2026-05-29 |
| 3 | Zameer Mansoob Muttasil — 14 forms (ضَرَبَنِيْ ... ضَرَبَهُنَّ paradigm) | PDF p-19 | 2026-05-29 |
| 4 | Zameer Mansoob Munfasil — 14 forms (اِیَّایَ ... اِیَّاهُنَّ paradigm) | PDF p-19 | 2026-05-29 |
| 5 | Zameer Majroor bi Harf-e-Jarr — 14 forms (لِيْ ... لَهُنَّ paradigm) | PDF p-19 | 2026-05-29 |
| 6 | Zameer Majroor bi Idafa — 14 forms (دَارِيْ ... دَارُهُنَّ paradigm) **MUKAMMAL** | PDF p-19 (top) + p-20 (bottom) | 2026-05-29 |

---

## Table 1 — ضمیر مرفوع متصل (Zameer Marfu' Muttasil) — 14 forms

**Source:** PDF p-18 / book p-۱۷, Fasl 5 Block 3.

**PDF tareef:** *"ضمیر مرفوع متصل (یعنی فاعل کی وہ ضمیر جو فعل سے ملی ہو) چودہ ہیں"*

**Concept:** Fa'il ki wo Zameer jo Fi'l ke saath **chipki hui** (attached) hoti. Fi'l ke baad suffix-form mein appear hoti. Example verb used by book: **ضَرَبَ** (to hit) — past tense gardaan ke 14 forms.

**Reading order:** Right-to-left (Urdu/Arabic convention). Internal sequence: **Mutakallim → Mukhatab → Ghaayb** (per Block 6 footnote 3-person framework).

| # | Form (PDF-verbatim) | Person | Number | Gender | Tarjuma (mera gloss — book mein nahi) |
|---|---------------------|--------|--------|--------|---------------------------------------|
| 1 | **ضَرَبْتُ** | Mutakallim | Singular | — | "Main ne maara" |
| 2 | **ضَرَبْنَا** | Mutakallim | Plural | — | "Hum ne maara" |
| 3 | **ضَرَبْتَ** | Mukhatab | Singular | Masc | "Tu ne maara" |
| 4 | **ضَرَبْتُمَا** | Mukhatab | Dual | Masc | "Tum dono (m) ne maara" |
| 5 | **ضَرَبْتُمْ** | Mukhatab | Plural | Masc | "Tum sab (m) ne maara" |
| 6 | **ضَرَبْتِ** | Mukhatab | Singular | Fem | "Tu (f) ne maara" |
| 7 | **ضَرَبْتُمَا** | Mukhatab | Dual | Fem | "Tum dono (f) ne maara" — **same form as #4** |
| 8 | **ضَرَبْتُنَّ** | Mukhatab | Plural | Fem | "Tum sab (f) ne maara" |
| 9 | **ضَرَبَ** | Ghaayb | Singular | Masc | "Us (m) ne maara" |
| 10 | **ضَرَبَا** | Ghaayb | Dual | Masc | "Un dono (m) ne maara" |
| 11 | **ضَرَبُوْا** | Ghaayb | Plural | Masc | "Un sab (m) ne maara" |
| 12 | **ضَرَبَتْ** | Ghaayb | Singular | Fem | "Us (f) ne maara" |
| 13 | **ضَرَبَتَا** | Ghaayb | Dual | Fem | "Un dono (f) ne maara" |
| 14 | **ضَرَبْنَ** | Ghaayb | Plural | Fem | "Un sab (f) ne maara" |

**Notes**:
- Person/Number/Gender columns are **mera labeling system** (book ne table mein cell-specific labels nahi diye, sirf 14 forms tarteeb se diye). Labeling derived from Block 6 footnote 3-person framework + standard Arabic morphology.
- Forms #4 and #7 (ضَرَبْتُمَا) are identical — masc dual = fem dual in 2nd person past tense.
- **Suffix mechanic** (mera observation): Mutakallim + Mukhatab forms (cells 1-8) ke saath attached suffix nazar aata (تُ، نَا، تَ، تُمَا، تُمْ، تِ، تُمَا، تُنَّ — Fi'l-stem ضَرَبْ ke baad). Ghaayb forms (cells 9-14) mein suffix yaa to nil (ضَرَبَ), yaa fatha-based (ا، تْ، تَا)، yaa noon-based (نَ، وْا). Yahi attached pattern asal Marfu' Muttasil zameer hai.

---

## Table 2 — ضمیر مرفوع منفصل (Zameer Marfu' Munfasil) — 14 forms

**Source:** PDF p-18 / book p-۱۷, Fasl 5 Block 4.

**PDF tareef:** *"ضمیر مرفوع منفصل (یعنی فاعل کی وہ ضمیر جو فعل سے جدا ہو) چودہ ہیں"*

**Concept:** Fa'il ki wo Zameer jo Fi'l se **جدا** (separated/independent) hoti — standalone kalimah ke taur par jumlay mein.

**Reading order:** Same as Table 1 — Mutakallim → Mukhatab → Ghaayb.

| # | Form (PDF-verbatim) | Person | Number | Gender | Tarjuma (mera gloss — book mein nahi) |
|---|---------------------|--------|--------|--------|---------------------------------------|
| 1 | **اَنَا** | Mutakallim | Singular | — | "Main" |
| 2 | **نَحْنُ** | Mutakallim | Plural | — | "Hum" |
| 3 | **اَنْتَ** | Mukhatab | Singular | Masc | "Tu (m)" |
| 4 | **اَنْتُمَا** | Mukhatab | Dual | Masc | "Tum dono (m)" |
| 5 | **اَنْتُمْ** | Mukhatab | Plural | Masc | "Tum sab (m)" |
| 6 | **اَنْتِ** | Mukhatab | Singular | Fem | "Tu (f)" |
| 7 | **اَنْتُمَا** | Mukhatab | Dual | Fem | "Tum dono (f)" — **same form as #4** |
| 8 | **اَنْتُنَّ** | Mukhatab | Plural | Fem | "Tum sab (f)" |
| 9 | **هُوَ** | Ghaayb | Singular | Masc | "Wo (m)" |
| 10 | **هُمَا** | Ghaayb | Dual | Masc | "Wo dono (m)" |
| 11 | **هُمْ** | Ghaayb | Plural | Masc | "Wo sab (m)" |
| 12 | **هِيَ** | Ghaayb | Singular | Fem | "Wo (f)" |
| 13 | **هُمَا** | Ghaayb | Dual | Fem | "Wo dono (f)" — **same form as #10** |
| 14 | **هُنَّ** | Ghaayb | Plural | Fem | "Wo sab (f)" |

**Notes**:
- Same labeling caveat as Table 1.
- Forms #4 = #7 (اَنْتُمَا dual symmetry) and #10 = #13 (هُمَا dual symmetry) — book's table shows these identically.
- **Tanbeeh** (book footnote, complete via p-18 + p-19 continuation): *"ضمیر مرفوع علاوہ فاعل کے دوسرے مرفوعات کے لیے بھی آتی ہے، یہاں آسانی کے لیے صرف فاعل کا ذکر کیا گیا"* — Zameer-e-Marfu' sirf Fa'il ke liye nahi, doosray Marfu' positions ke liye bhi; book ne asaani ke liye sirf Fa'il ka zikr kiya.

---

## Table 3 — ضمیر منصوب متصل (Zameer Mansoob Muttasil) — 14 forms

**Source:** PDF p-19 / book p-۱۸, Fasl 5 Block 2.

**PDF tareef:** *"ضمیر منصوب متصل (یعنی مفعول کی وہ ضمیر جو فعل سے ملی ہو) چودہ ہیں"*

**Concept:** Maf'ool ki Zameer jo Fi'l ke saath **chipki hui** hoti — Fi'l ke baad suffix-form mein. Yahaan **Fa'il constant = هُوَ (implicit "he")**, **Maf'ool varies** across 14 person-number-gender variants. Example verb: **ضَرَبَ** (he hit X).

**Reading order:** Same as Tables 1-2 — Mutakallim → Mukhatab → Ghaayb.

| # | Form (PDF-verbatim) | Person (Maf'ool) | Number | Gender | Tarjuma (mera gloss — book mein nahi) |
|---|---------------------|--------------------|--------|--------|---------------------------------------|
| 1 | **ضَرَبَنِيْ** | Mutakallim | Singular | — | "Us ne mujhe maara" |
| 2 | **ضَرَبَنَا** | Mutakallim | Plural | — | "Us ne hamein maara" |
| 3 | **ضَرَبَكَ** | Mukhatab | Singular | Masc | "Us ne tujhe maara" |
| 4 | **ضَرَبَكُمَا** | Mukhatab | Dual | Masc | "Us ne tum dono (m) ko maara" |
| 5 | **ضَرَبَكُمْ** | Mukhatab | Plural | Masc | "Us ne tum sab (m) ko maara" |
| 6 | **ضَرَبَكِ** | Mukhatab | Singular | Fem | "Us ne tujhe (f) maara" |
| 7 | **ضَرَبَكُمَا** | Mukhatab | Dual | Fem | "Us ne tum dono (f) ko maara" — **same form as #4** |
| 8 | **ضَرَبَكُنَّ** | Mukhatab | Plural | Fem | "Us ne tum sab (f) ko maara" |
| 9 | **ضَرَبَهُ** | Ghaayb | Singular | Masc | "Us ne usay (m) maara" |
| 10 | **ضَرَبَهُمَا** | Ghaayb | Dual | Masc | "Us ne un dono (m) ko maara" |
| 11 | **ضَرَبَهُمْ** | Ghaayb | Plural | Masc | "Us ne un sab (m) ko maara" |
| 12 | **ضَرَبَهَا** | Ghaayb | Singular | Fem | "Us ne usay (f) maara" |
| 13 | **ضَرَبَهُمَا** | Ghaayb | Dual | Fem | "Us ne un dono (f) ko maara" — **same form as #10** |
| 14 | **ضَرَبَهُنَّ** | Ghaayb | Plural | Fem | "Us ne un sab (f) ko maara" |

**Notes**:
- **Tarkeeb walkthrough** (book Block 3 par): Cell #1 ضَرَبَنِيْ break-down: ضَرَبَ (Fi'l) + هُوَ (hidden Fa'il) + نون وقایہ (نِ) + یْ (Mutakallim Maf'ool zameer) = Jumla Fi'liya Khabariya.
- **Noon Wiqayah (نون وقایہ)** = "protective noon" — Fi'l ke aakhir aur Mutakallim ya ke darmiyaan aati. Forward-ref Sarf — sirf cell #1 ki tarkeeb mein book ne use kiya, formal tareef nahi di.

---

## Table 4 — ضمیر منصوب منفصل (Zameer Mansoob Munfasil) — 14 forms

**Source:** PDF p-19 / book p-۱۸, Fasl 5 Block 4.

**PDF tareef:** *"ضمیر منصوب منفصل (یعنی مفعول کی وہ ضمیر جو فعل سے جدا ہو) چودہ ہیں"*

**Concept:** Maf'ool ki Zameer jo Fi'l **se جدا** standalone. Common prefix **اِیَّا** (kasra-alif + fatha-shadda-ya) — yahi independence indicator. Phir person-suffix.

| # | Form (PDF-verbatim) | Person (Maf'ool) | Number | Gender | Tarjuma (mera gloss — book mein nahi) |
|---|---------------------|--------------------|--------|--------|---------------------------------------|
| 1 | **اِیَّایَ** | Mutakallim | Singular | — | "Sirf mujhe / mujhe hi" |
| 2 | **اِیَّانَا** | Mutakallim | Plural | — | "Sirf hamein" |
| 3 | **اِیَّاكَ** | Mukhatab | Singular | Masc | "Sirf tujhe (m)" |
| 4 | **اِیَّاكُمَا** | Mukhatab | Dual | Masc | "Sirf tum dono (m) ko" |
| 5 | **اِیَّاكُمْ** | Mukhatab | Plural | Masc | "Sirf tum sab (m) ko" |
| 6 | **اِیَّاكِ** | Mukhatab | Singular | Fem | "Sirf tujhe (f)" |
| 7 | **اِیَّاكُمَا** | Mukhatab | Dual | Fem | "Sirf tum dono (f) ko" — **same form as #4** |
| 8 | **اِیَّاكُنَّ** | Mukhatab | Plural | Fem | "Sirf tum sab (f) ko" |
| 9 | **اِیَّاهُ** | Ghaayb | Singular | Masc | "Sirf usay (m)" |
| 10 | **اِیَّاهُمَا** | Ghaayb | Dual | Masc | "Sirf un dono (m) ko" |
| 11 | **اِیَّاهُمْ** | Ghaayb | Plural | Masc | "Sirf un sab (m) ko" |
| 12 | **اِیَّاهَا** | Ghaayb | Singular | Fem | "Sirf usay (f)" |
| 13 | **اِیَّاهُمَا** | Ghaayb | Dual | Fem | "Sirf un dono (f) ko" — **same form as #10** |
| 14 | **اِیَّاهُنَّ** | Ghaayb | Plural | Fem | "Sirf un sab (f) ko" |

**Notes**:
- **Tanbeeh for Mansoob** (book Block 5): *"ضمیر منصوب علاوہ مفعول کے دوسرے منصوبات کے لیے بھی آتی ہے، یہاں آسانی کے لیے صرف مفعول کا ذکر کیا گیا"* — same structural Tanbeeh as Marfu' Tanbeeh.
- **اِیَّاكَ ka classical Quranic usage** Surah Fatiha mein widely-recited form (verbatim Quran quote NAHI di — book ne Quran ka misaal nahi diya yahaan).

---

## Table 5 — ضمیر مجرور بہ حرف جر (Zameer Majroor bi Harf-e-Jarr) — 14 forms

**Source:** PDF p-19 / book p-۱۸, Fasl 5 Block 7.

**PDF intro:** *"ضمیر مجرور متصل بھی چودہ ہیں، اور یہ دو طرح کی ہوتی ہے: ایک تو وہ جس پر حرف جر داخل ہو، دوسری وہ جس پر مضاف داخل ہو"*

**Concept:** Majroor zameer ki **pehli sub-type** — jis par **Harf-e-Jarr daakhil ho** (preposition). Yahaan Harf-e-Jarr **لِ** ("for/to") use ki gayi.

| # | Form (PDF-verbatim) | Person (Majroor) | Number | Gender | Tarjuma (mera gloss — book mein nahi) |
|---|---------------------|--------------------|--------|--------|---------------------------------------|
| 1 | **لِيْ** | Mutakallim | Singular | — | "Mere liye" |
| 2 | **لَنَا** | Mutakallim | Plural | — | "Hamare liye" |
| 3 | **لَكَ** | Mukhatab | Singular | Masc | "Tere liye (m)" |
| 4 | **لَكُمَا** | Mukhatab | Dual | Masc | "Tum dono (m) ke liye" |
| 5 | **لَكُمْ** | Mukhatab | Plural | Masc | "Tum sab (m) ke liye" |
| 6 | **لَكِ** | Mukhatab | Singular | Fem | "Tere liye (f)" |
| 7 | **لَكُمَا** | Mukhatab | Dual | Fem | "Tum dono (f) ke liye" — **same form as #4** |
| 8 | **لَكُنَّ** | Mukhatab | Plural | Fem | "Tum sab (f) ke liye" |
| 9 | **لَهُ** | Ghaayb | Singular | Masc | "Uske liye (m)" |
| 10 | **لَهُمَا** | Ghaayb | Dual | Masc | "Un dono (m) ke liye" |
| 11 | **لَهُمْ** | Ghaayb | Plural | Masc | "Un sab (m) ke liye" |
| 12 | **لَهَا** | Ghaayb | Singular | Fem | "Uske liye (f)" |
| 13 | **لَهُمَا** | Ghaayb | Dual | Fem | "Un dono (f) ke liye" — **same form as #10** |
| 14 | **لَهُنَّ** | Ghaayb | Plural | Fem | "Un sab (f) ke liye" |

**Notes**:
- **Harakah-shift observation** (mera): Cell #1 (لِيْ) ka lam par **kasra**, baqi 13 forms ka lam par **fatha**. Mutakallim ya ke saath harakah-shift — book ne yahan rule nahi diya.

---

## Table 6 — ضمیر مجرور باِضافت (Zameer Majroor bi Idafa) — 14 forms **MUKAMMAL**

**Source:** PDF p-19 / book p-۱۸ (top row cells 1-7, Fasl 5 Block 8) + PDF p-20 / book p-۱۹ (bottom row cells 8-14).

**PDF intro context:** Majroor zameer ki **doosri sub-type** — jis par **Mudaf daakhil ho** (Idafa structure mein Mudaf Ilayh role). Example noun: **دَار** (house) — pehla hissa ka Mudaf, zameer = Mudaf Ilayh.

| # | Form (PDF-verbatim) | Person (Mudaf Ilayh) | Number | Gender | Tarjuma (mera gloss — book mein nahi) |
|---|---------------------|--------------------------|--------|--------|---------------------------------------|
| 1 | **دَارِيْ** | Mutakallim | Singular | — | "Mera ghar" |
| 2 | **دَارُنَا** | Mutakallim | Plural | — | "Hamara ghar" |
| 3 | **دَارُكَ** | Mukhatab | Singular | Masc | "Tera (m) ghar" |
| 4 | **دَارُكُمَا** | Mukhatab | Dual | Masc | "Tum dono (m) ka ghar" |
| 5 | **دَارُكُمْ** | Mukhatab | Plural | Masc | "Tum sab (m) ka ghar" |
| 6 | **دَارُكِ** | Mukhatab | Singular | Fem | "Tera (f) ghar" |
| 7 | **دَارُكُمَا** | Mukhatab | Dual | Fem | "Tum dono (f) ka ghar" — **same form as #4** |
| 8 | **دَارُكُنَّ** | Mukhatab | Plural | Fem | "Tum sab (f) ka ghar" |
| 9 | **دَارُهُ** | Ghaayb | Singular | Masc | "Uska (m) ghar" |
| 10 | **دَارُهُمَا** | Ghaayb | Dual | Masc | "Un dono (m) ka ghar" |
| 11 | **دَارُهُمْ** | Ghaayb | Plural | Masc | "Un sab (m) ka ghar" |
| 12 | **دَارُهَا** | Ghaayb | Singular | Fem | "Uska (f) ghar" |
| 13 | **دَارُهُمَا** | Ghaayb | Dual | Fem | "Un dono (f) ka ghar" — **same form as #10** |
| 14 | **دَارُهُنَّ** | Ghaayb | Plural | Fem | "Un sab (f) ka ghar" |

**Notes**:
- **Same harakah-shift pattern** as Table 5 — cell #1 (دَارِيْ) ka ra par **kasra**, baqi 13 forms ka ra par **damma** (دَارُ-).
- **Mudmaraat (Qism #1 of Ism Ghair Mutamakkin) ab definitionally MUKAMMAL** — 5 qismein with **6 paradigm tables** (Majroor Muttasil ki 2 sub-types: bi Harf-e-Jarr + bi Idafa) × 14 forms = **84 forms** full coverage (Tables 1-6).

---

## Pending tables (after Mudmaraat mukammal)

Mudmaraat (Qism #1) mukammal. Fasl 5 ki **baqi 7 qismein** ke specific Asma/forms (Mausoolah, Ishara, Af'aal, Aswaat, Zuroof, Kinayaat, Murakkab Bina'i) aage ke pages par. **Asma-e-Mausoolah (Qism #2)** ki 10-form table p-20 par mil chuki — yeh `irab-tables.md` mein add ho sakti (decision Nazir ki), ya `notes.md` Section 15 ki Mausoolah table sufficient hai (chote paradigm table).
