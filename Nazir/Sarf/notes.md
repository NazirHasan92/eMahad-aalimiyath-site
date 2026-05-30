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

# Sarf — Page-by-page Notes (Nazir)

> **Built incrementally during live teaching sessions.** Hierarchy: **Topic → Sub Topic → Slide N (PDF p-NNN)**.
>
> - **Source of truth**: `Sarf/Muallim u Sarf_ebook_New_15_jan.pdf` (135 pages) — read directly via Read tool with `pages:` parameter (PNG fallback deprecated since 2026-05-28)
> - **Sister files**: `charts.md` (Mermaid concept charts), `gardaan-tables.md` (paradigm tables)

---

## Format per slide

```
#### Slide N — <Title from PDF header> (PDF p-NNN)

**PDF par jo hai:**
- bullet summary of literally visible content (header bar text, titles, tables)

[Verbatim Arabic quotes + Roman Urdu explanation]

**Status:** PRE-BUILD (YYYY-MM-DD) — Nazir ko verify karna hai
```

`Naye terms`, `Yaad rakho`, `Sabak sawal` aate hain har Sub Topic ke end mein (rollup).

---

## Table of Contents

> Pages p-001 to p-017 = front matter. Asal mazmoon p-018 se shuru.

### Topic 1.0 — Istilahaat (اصطلاحات)

- **Sub Topic 1.1** — Tareef, Mauzu, Gharaz, Wadi, Ahmiyat
  - Slide 1 (p-018) — Topic 1.0 cover + 7 Sub Topics ki table
  - Slide 2 (p-018) — Sub Topic 1.1 cover
  - Slide 3 (p-018) — اصطلاحات + Tareef + Mauzu + Gharaz ki definitions
  - Slide 4 (p-019) — Waadi (4 aqwaal) + Ahmiyat (الصرف ام العلوم...)
  - Slide 5 (p-019) — Exercise/review bar `[?]`
- **Sub Topic 1.2** — Kalimah ki tareef + 3 aqsam + Fi'l ki sub-divisions + Huroof Tahajji
  - Slide 6 (p-019) — Sub Topic 1.2 cover
  - Slide 7 (p-019) — Kalimah ki tareef + Ism + Fi'l + 3 zamane
  - Slide 8 (p-020) — Fi'l ki taqseem: Ithbat/Nafi + Muarrab/Mabni
  - Slide 9 (p-020) — Fi'l ki taqseem: Ma'lum/Majhul + Fa'il/Maf'ul fa'ida
  - Slide 10 (p-021) — **Harf ki tareef** + 6-misaal table + sample jumla
  - Slide 11 (p-021) — Huroof Tahajji + 2 qismein (Sahih 25 / Illat 3 = Waa'i) + Alif/Hamza note
  - Slide 12 (p-022) — Huroof taqseem (harkat se): Mutaharrik/Saakin/Mushaddad/Munawwan + buniyadi vocab (Harakah/Fath/Kasra/Damma)
  - Slide 13 (p-022) — Reference table: ~30 common Arabic particles in 1 dense table
  - Slide 14 (p-022) — Exercise bar `[?]`
- **Sub Topic 1.3** — Ism ki derivational morphology: Jamid / Masdar / Mushtaq
  - Slide 15 (p-023) — Sub Topic 1.3 cover
  - Slide 16 (p-023) — اسم کی اقسام: Jamid + Masdar + Mushtaq tareef + misaal + 12-mushtaq Note
  - Slide 17 (p-023) — اسم مصدر سے بننے والے ۶ فعل: Madhi / Mudaari' / Jahd / Nafi / Amr / Nahi
  - Slide 18 (p-024) — اسم مصدر سے بننے والے ۶ اسم (part 1 of 2): Fa'il + Maf'ul + Tafzeel + Zarf (Zaman/Makan sub-types)
  - Slide 19 (p-024) — اسم qismein (part 2 of 2): Aalah + Sifat-e-Mushabbaha + matching exercise table (اسماء مشتقہ آپس میں ملائیں)
  - Slide 20 (p-024) — Exercise bar `[?]` (Sub Topic 1.3 ka khatima)
- **Sub Topic 1.4** — حروف اصلی کی پہچان (root letter identification via wazn — **WAZN formally introduced**) — **MUKAMMAL**
  - Slide 21 (p-025) — Sub Topic 1.4 cover
  - Slide 22 (p-025) — وزن نکالنے کا طریقہ: Mauzun/Meezan/Wazn ki tareefein + method + 3-pair example table
  - Slide 23 (p-025) — حروف اصلی ki pehchaan: فا کلمہ / عین کلمہ / لام کلمہ terminology + عَالِم/ضَرْب examples
  - Slide 24 (p-026) — حروف اصلی (مادہ) کی پہچان: 7-misaal table (لفظ | وزن | حروف اصلیہ | زائدہ/علامات) + مادہ taaruf
  - Slide 25 (p-026) — اسم کے اوزان: 3/4/5 harfi taqseem (3 sub-tables) + paragraph rule + forward-ref Note
  - Slide 26 (p-026) — Exercise bar `[?]` (Sub Topic 1.4 ka khatima)
- **Sub Topic 1.5** — فعل کے چھ ابواب (Fi'l ke 6 chapters/categories — **major Sarf milestone**) — **MUKAMMAL**
  - Slide 27 (p-027) — Sub Topic 1.5 cover
  - Slide 28 (p-027) — افعال کے وزن نکالنے کا طریقہ + فعل ماضی/مضارع ke 3+3 waznein (6+6 examples)
  - Slide 29 (p-027) — عین کلمہ pe mukhtalif harakaat → 9 logical → 6 مستعمل = **چھ ابواب** concept formally introduced
  - Slide 30 (p-028) — فَعَلَ / فَعِلَ / فَعُلَ se 3 + 2 + 1 = **6 سیٹ** ka algebraic derivation
  - Slide 31 (p-028) — مذکورہ چھ ابواب کے اوزان اور مثالیں — **canonical 6 ابواب formally PDF-introduced** (ضَرَبَ، فَتَحَ، نَصَرَ، حَسِبَ، سَمِعَ، شَرُفَ) + Note ke alternate misaalein
  - Slide 32 (p-029) — حرکات کے اعتبار سے ابواب کے گروپ (ماضی 3+2+1 + مضارع 2+2+2) + فائدہ: ماضی مجہول **فُعِلَ** + مضارع مجہول **یُفْعَلُ** universal
  - Slide 33 (p-029) — مذکورہ ابواب کی **علامات** — 6 ابواب ke unique harakaat-signatures (مفتوح/مکسور/مضموم العین terminology)
  - Slide 34 (p-029) — Exercise bar — **Sub Topic 1.5 ka khatima**
- **Sub Topic 1.6** — حروف اصلی (مادہ) کے اعتبار سے اسم و فعل کی اقسام (**ششش اقسام**) — **MUKAMMAL**
  - Slide 35 (p-030) — Sub Topic 1.6 cover
  - Slide 36 (p-030) — اسم ki 3 main qismein (ثلاثی، رباعی، خماسی) + 3×2=6 sub-categories (mujarrad + mazid fih) table
  - Slide 37 (p-030) — ششش اقسام ki وضاحت — 6 ism waznein + misaalein + zaayid letters + forward-ref to معلم الابواب والخصائص
  - Slide 38 (p-031) — فعل ki 2 main qismein (ثلاثی، رباعی — **NO خماسی فعل**) + 2×2=4 sub-categories (mujarrad + mazid fih) table
  - Slide 39 (p-031) — فعل side کی 4 qismein ki وضاحت — 4 fi'l waznein + misaalein + zaayid letters
  - Slide 40 (p-031) — Exercise bar — **Sub Topic 1.6 ka khatima**
- **Sub Topic 1.7** — مزاج حروف کے اعتبار سے اسم اور فعل کی اقسام (**هَفْت اقسام** = 7 categories) — **MUKAMMAL** ✅
  - Slide 41 (p-032) — Sub Topic 1.7 cover
  - Slide 42 (p-032) — هَفْت اقسام formally introduced — **7-names PDF-attested** (صحیح، مثال، اجوف، ناقص، لفیف، مہموز، مضاعف) + صحیح tareef + مثال/اجوف/ناقص master rule (wao/yaa at fa/ain/laam position)
  - Slide 43 (p-032) — **مثال + اجوف** ki وضاحت — har ek ki 2 sub-types (واوی + یائی) + misaalein; **ناقص** ka header tareef (sub-types p-033 par expected)
  - Slide 44 (p-033) — **ناقص** ki 2 sub-types (واوی + یائی) + misaalein; **☆ لفیف** tareef + 2 sub-types (مفروق + مقرون) + 3 misaalein; **☆ مہموز** ka header tareef (sub-types Slide 45 par)
  - Slide 45 (p-033) — **مہموز** ki 3 sub-types (الفاء + العین + اللام) + misaalein (`[?]` STANDALONE on العین hamza kursi-form — likely-resolved per Slide 47 nakshah; Nazir physical-confirm pending); **☆ مضاعف** tareef + 2 sub-types (ثلاثی + رباعی) + misaalein (مَدَدٌ + مَدَّ pair; زَلْزَلَۃٌ + زَلْزَلَ pair); **4-position terminology** (فا + لام اوّل + عین + لام ثانی) PDF-introduced
  - Slide 46 (p-034) — **نقشہ برائے ہفت اقسام** comprehensive consolidation table (top half, 7 rows: صحیح + مثال/اجوف/ناقص sub-types) — 6-column structural breakdown (حرف اصلی | ف | ع | ل (اوّل) | ل (ثانی) | مثالیں)
  - Slide 47 (p-034) — نقشہ table continuation (bottom half, 7 rows: لفیف + مہموز + مضاعف sub-types); **مہموزالعین orthographic `[?]` LIKELY-RESOLVED** (standalone ء per nakshah cell-isolation rendering; Nazir physical-confirm pending); only مضاعف رباعی row mein ل(ثانی) filled — STRUCTURAL PROOF of 4-position-only-on-رباعی rule
  - Slide 48 (p-034) — **🎯 Sub Topic 1.7 + TOPIC 1.0 MUKAMMAL exercise bar** (parallel to Slides 5/14/20/26/34/40 Sub Topic khatima pattern)

---

## Topic 1.0 — Istilahaat (اصطلاحات)

**Topic 1.0 ka maqsad:** Sarf ke khaas **fanni alfaaz** (technical terms) seekhna, taake aage ki baat samjh sakein.

**Andar 7 Sub Topics hain** (1.1 se 1.7 tak) — Slide 1 ki table mein har Sub Topic apne starting Slide number ke saath listed hai.

---

### Sub Topic 1.1 — Tareef, Mauzu, Gharaz, Wadi, Ahmiyat (تعریف، موضوع، غرض، واضع، اہمیت)

**Sub Topic 1.1 ka maqsad:** Sarf ke baare mein **5 buniyadi cheezein** jaano. Yeh wese hi hai jaise koi bhi naya fan/kitab parhne se pehle 5 sawal puchna.

---

#### Aaj ki kahani / آج کی کہانی (Sub Topic 1.1 ka intro)

**Roman Urdu:** Bhai, aaj **Sarf ki asal padhai shuru** ho rahi hai. Pichle 17 pages cover, fihrist, taqreez aur muqaddama the — aaj se asal silsila.

Lekin pehle ek dilchasp baat: Arabic ke aalim hazraat ka ek qaida hai — koi bhi naya fan parhne se pehle **5 cheezein zaroor jaano**. Yeh wese hi hai jaise aap nayi gaadi khareedne se pehle 5 sawal puchte ho: yeh hai kya? Kis cheez ka faida? Kis ne banayi? Kitni achi hai? Kya mere kaam ki hai?

Bilkul wese hi Sarf ka pehla sabaq yeh hai: **Sarf ke baare mein 5 buniyadi cheezein**. Phir aage asal mehfil shuru hogi.

**Urdu:** بھائی، آج صرف کی اصل پڑھائی شروع ہو رہی ہے۔ پچھلے ۱۷ صفحے سرورق، فہرست، تقریظ اور مقدمہ تھے۔ اب سے اصل مضمون۔

پہلے ایک بات یاد رکھو: عرب علماء کا قاعدہ ہے کہ کوئی بھی نیا فن پڑھنے سے پہلے ۵ چیزیں ضرور جاننی چاہئیں۔ یہ صفحے یہی ۵ چیزیں متعارف کراتے ہیں اور تعریف بھی دیتے ہیں۔

---

#### Slide 1 — Topic 1.0 cover (PDF p-018)

**PDF par jo hai:**
- Top header strip: blank | blank | **Slide 1** | blank | blank
- Bara styled title: **اصطلاحات TOPIC 1.0**
- 7-row table jismein har Sub Topic apne starting Slide number aur Arabic title ke saath listed hai (neeche transcribed)

**Slide 1 ki table — PDF se verbatim:**

| Sub Topic | Slide | Arabic title (PDF se) |
|---|---|---|
| **1.1** | 02 | تعریف، موضوع، غرض، واضع، اہمیت |
| **1.2** | 06 | کلمہ کی تعریف و اقسام `[?]` |
| **1.3** | 15 | جامد، مصدر، مشتق `[?]` |
| **1.4** | 21 | وزن کے ذریعے صرف کی پہچان `[?]` |
| **1.5** | 27 | وزن کے اعتبار سے فعل کا باب `[?]` |
| **1.6** | 35 | تعداد حروف کے اعتبار سے فعل کی اقسام `[?]` |
| **1.7** | 41 | صحت `[?]` کے اعتبار سے فعل کی اقسام |

**Note (post back-validation):** Slide numbers (02/06/15/21/27/35/41) PDF se confirmed ✅. Sirf row 1.1 ka Arabic title large/clear hai. Rows 1.2-1.7 ke Arabic titles **chhote font** mein hain colored bars par — best-effort transcription di gayi hai magar Nazir physical kitab se har row ka exact Arabic verify kare.

**"Istilahaat" ka matlab kya?**

- **Roman:** "Istilahaat" ka asal Urdu/Arabic lafz hai **istilah** — yaani *fanni alfaaz* (technical terms). Har fan apne khaas alfaaz banata hai.
  - Cricket walay banate hain: "wicket", "googly", "yorker"
  - Doctor banate hain: "blood pressure", "ECG", "diagnosis"
  - Wese hi Sarf walay banate hain: "fi'l", "ism", "harf", "wazn", "baab"
- **Urdu:** اصطلاحات یعنی فنی الفاظ — ہر فن کے اپنے خاص الفاظ۔

To **Topic 1.0 ka maqsad:** Sarf ke khaas alfaaz seekhna, taake aage ki baat samjh sakein.

**Status:** RESTRUCTURED 2026-05-28 (post back-validation iteration 2) — Slide numbers (02/06/15/21/27/35/41) PDF-verified ✅. Sub Topic Arabic titles (rows 1.2-1.7) small-font; best-effort transcription with `[?]` markers — Nazir physical book se verify kare. Row 1.1 large-font, fully verified ✅.

---

#### Slide 2 — Sub Topic 1.1 cover (PDF p-018)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.1 | [Arabic title cell — small font: تعریف، موضوع، غرض، واضع [اہمیت `[?]`]] | Slide 2 | اصطلاحات | Topic 1.0**
- Slide 3 bar clearly shows full 5-word phrase: **تعریف، موضوع، غرض، واضع، اہمیت** ✅. Slide 2 bar same cell par 4 ya 5 words `[?]` — small font hone ki wajah se Nazir physical book se verify kare.
- Body khaali — sirf cover slide hai

Sirf cover slide hai. Kuch teaching content nahi — bas Slide 3 ka taaruf.

**Status:** PDF-VERIFIED 2026-05-28 (post back-validation iteration 2) — main bar layout + Slide 3 reference clear. Slide 2 ke Arabic title cell mein اہمیت ka inclusion `[?]` — small font.

---

#### Slide 3 — اصطلاحات + Tareef + Mauzu + Gharaz ki definitions (PDF p-018)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.1 | Slide 3 | تعریف، موضوع، غرض، واضع، اہمیت** (3-column bar)
- Body title: **اصطلاحات** (styled red)
- Opening sentence (verbatim): *"ہر علم کو شروع کرنے سے پہلے چند چیزوں کا جاننا ضروری ہے:۔"*
- Numbered list (verbatim): **(۱) تعریف (۲) موضوع (۳) غرض (۴) واضع (۵) اہمیت**
- Phir pehli 3 ki definitions:
  - **تعریف:** body paragraph
  - **موضوع:** body paragraph
  - **غرض:** body paragraph
- (Waadi aur Ahmiyat Slide 4 par hain.)

---

**Kitab ka jumla (verbatim from PDF):**

> **"ہر علم کو شروع کرنے سے پہلے چند چیزوں کا جاننا ضروری ہے:۔"**

Yaani: **har** ilm jo bhi ho, uske parhne se pehle kuch buniyadi sawal ka jawab maaloom hona chahiye. Yeh hain:

**(۱) تعریف (۲) موضوع (۳) غرض (۴) واضع (۵) اہمیت**

---

##### (۱) تعریف ki definition (PDF verbatim)

> **"تعریف:** علم صرف ایسے علم کا نام ہے جس کے ذریعے ایک کلمے کو دوسرے کلمے سے بنانے کا طریقہ یعنی ایک صیغے کو دوسرے صیغے سے بنانے کا طریقہ معلوم ہو، جیسے: `[?]` — PDF par yeh tasreef chain small font mein hai; Nazir physical kitab se exact verbatim transcribe kare — وغیرہ، یعنی لفظی تبدیلی کا نام علم الصرف ہے۔"

**Roman summary:** Ilm-e-Sarf = woh ilm jisme aap seekhte ho ke ek lafz se doosra lafz, ek sigha se doosra sigha kaise banta hai. Yaani **alfaaz ki tabdeeli** ka ilm.

##### (۲) موضوع ki definition (PDF verbatim)

> **"موضوع:** علم صرف کا موضوع کلمہ ہے۔ اس علم میں کلمے کی شکل اور بناوٹ (ایک کلمے سے دوسرا کلمہ تیار کرنے) سے بحث کی جاتی ہے۔"

**Roman summary:** Sarf ka **mauzu** (subject matter) = **kalimah** (lafz). Sarf bahas karta hai kalimah ki shakal aur banaawat par.

##### (۳) غرض ki definition (PDF verbatim)

> **"غرض:** طالب علم کے ذہن کو کلام عرب میں صیغے کی غلطی سے بچانا تا کہ تمام الفاظ صحیح طور پر پڑھنا آ جائیں۔"

**Roman summary:** Sarf ki **gharaz** (purpose) = **taalib-e-ilm ke zehn ko Arabic kalam mein sigha ki ghalti se bachana** — taake har lafz sahi tareeqe se padha jaye.

---

**Status:** PDF-VERIFIED 2026-05-28 (post back-validation iteration 2) — opening sentence + numbered list + Mauzu + Gharaz definitions PDF verbatim ✅. Tareef body text mostly PDF-verbatim BUT Arabic morphology example chain in middle is **small-font / unresolved** — marked `[?]` standalone (Rule 11). Nazir physical book se exact tasreef chain verify kare.

---

#### Slide 4 — Waadi (4 aqwaal) + Ahmiyat (PDF p-019)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.1 | تعریف، موضوع، غرض، واضع | Slide 4 | اصطلاحات | Topic 1.0**
- Body do hisson mein:
  - **واضع** — 4 aqwaal (opinions on who first established Sarf)
  - **اہمیت** — ek Arabic مقولہ + uska explanation

---

##### (۴) واضع — 4 aqwaal (PDF verbatim)

> **"واضع:** علم الصرف کے واضع کے متعلق مختلف اقوال ہیں:۔"

| # | Qaul (verbatim from PDF) |
|---|---|
| **پہلا قول** | یہ ہے کہ علم الصرف کے واضع اول **حضرت علی المرتضیٰ رضی اللہ عنہ** ہیں۔ |
| **دوسرا قول** | یہ ہے کہ علم الصرف کے واضع اول **حضرت معاذ بن مسلم ہراوی رحمۃ اللہ علیہ** ہیں۔ |
| **تیسرا قول** | یہ ہے کہ علم الصرف کے واضع اول **حضرت امام ابو حنیفہ رحمۃ اللہ علیہ** ہیں۔ |
| **چوتھا قول** | یہ ہے کہ علم الصرف کے واضع اول **حضرت ابو عثمان بکر مازنی رحمۃ اللہ علیہ** ہیں۔ |

**Roman summary:** Sarf ki bunyaad kis ne dali — yeh 4 mukhtalif aqwaal hain. Kitab khud kisi ek ko tarjeeh nahi deti, sirf 4 opinions present karti hai.

**Note:** Naam aur RA/RH ki attribution **PDF se verbatim** uthai gayi hai — memory se NAHI.

---

##### (۵) اہمیت — مقولہ (PDF verbatim)

> **"اہمیت:** عربی کا مقولہ ہے کہ
>
> **﴿اَلصَّرْفُ اُمُّ الْعُلُومِ وَالنَّحْوُ اَبُوهَا﴾**
>
> ترجمہ: صرف علوم کی ماں ہے اور نحو علوم کا باپ ہے۔"

**Mohim baat:** Yeh **hadith nahi** — kitab ne saaf likha hai *"عربی کا مقولہ"* (Arabic ka muhawra / saying). Koi specific shakhsiyat ko attribute nahi kiya gaya. Hum bhi attribution add NAHI karenge.

**Phir kitab samjhati hai (PDF verbatim):**

> "جس طرح شریعت نے عزیز و قارب میں ماں کے حقوق کو مقدم رکھا ہے، اسی طرح طالب علم کے لیے تمام علوم میں سے علم صرف کو مقدم رکھا گیا ہے۔ اس میں کوئی شک نہیں کہ جب تک علم صرف و نحو کی کامیابی `[?]` (exact phrase verify karein — PDF par 2 plausible readings: *"نہیں مل سکتی"* ya *"حاصل نہیں ہو سکتی"*) اس وقت تک علوم عربیہ میں کامیابی حاصل نہیں ہو سکتی، کیونکہ صرف و نحو کے بغیر قرآن و حدیث اور فقہ کا سمجھنا محال ہے۔"

**Roman summary:** Jaise Islam mein maa ka haq baap se pehle hai, wese Sarf ka ilm baqi tamam Arabic uloom se pehle aata hai. Sarf-o-Nahw ke baghair Quran, Hadith aur Fiqh samajhna **محال** (na-mumkin) hai.

**Status:** PDF-VERIFIED 2026-05-28 — Arabic مقولہ verbatim, names verbatim. `[?]` sirf akhri 2 lines ke wording mein.

---

#### Slide 5 — Exercise / review bar `[?]` (PDF p-019)

**PDF par jo hai:**
- Ek thin bar slide ke beech mein
- Bar text (post back-validation iteration 2): **"متعلقہ سب ٹاپک کے سوالات | Slide 5 | [workbook name `[?]`] میں حل کریں"** — same pattern as Slide 14
- Body koi nahi — sirf bar header hai

**Roman:** Yeh bar instruction hai — "Slide 5 — **متعلقہ سب ٹاپک** کے سوالات [workbook] میں حل کریں" — student ko **متعلقہ Sub Topic** ke سوالات workbook mein hal karne ka kaha gaya hai. Workbook ka exact naam `[?]` (chhote/decorative font).

**Status:** PDF-VERIFIED 2026-05-28 (post back-validation iteration 2) — bar text "متعلقہ سب ٹاپک کے سوالات" confirmed (matches Slide 14 same pattern). Sirf workbook naam `[?]`.

---

### Sub Topic 1.2 — Kalimah ki تعریف aur aqsam

> *Note:* Slides 6-7 = Kalimah + Ism/Fi'l. Slides 8-9 = Fi'l ki sub-divisions. **Slide 10** = Harf ki tareef. **Slide 11** = Huroof Tahajji + Sahih/Illat. **Slide 12** = Huroof ki harakat-based taqseem + 4 buniyadi vocab (Harakah/Fath/Kasra/Damma). **Slide 13** = reference table of ~30 common Arabic particles. **Slide 14** = exercise bar. **Sub Topic 1.2 = 9 slides ka span (6-14)** — Kalimah ki tareef se le kar comprehensive huroof + buniyadi vocab tak.

---

#### Slide 6 — Sub Topic 1.2 cover (PDF p-019)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 6 | اصطلاحات | Topic 1.0**
- Body khaali — sirf cover slide

Sirf cover slide hai — Sub Topic 1.2 ka aaghaaz. Asal teaching Slide 7 par.

**Status:** PDF-VERIFIED 2026-05-28 — Sub Topic title middle word back-validation par confirmed = **تعریف** (NOT پہچان).

---

#### Slide 7 — Kalimah ki tareef + Ism + Fi'l (PDF p-019)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 7**
- Body:
  - Bara styled title: **کلمہ**
  - Kalimah ki tareef
  - 3 aqsam ki list (Ism, Fi'l, Harf)
  - Ism ki tareef + misaal
  - Fi'l ki tareef + misaal
  - Nota: 3 zamane (Maazi, Haal, Mustaqbil)
- **Harf ki tareef Slide 7 par nahi** — agle slide (probably Slide 8, p-020) par hogi

---

##### Kalimah ki tareef (PDF verbatim)

> **"کلمہ وہ لفظ ہے جو ایک معنیٰ کے لیے بنایا گیا ہو۔"**

**Roman summary:** **Kalimah** = woh lafz jiska **ek ma'na** ho. Yaani har woh lafz jiska koi matlab hai = kalimah.

##### Kalimah ki 3 aqsam (PDF verbatim)

> **"عربی زبان کے کلمات تین قسم پر ہیں: (۱) اسم (۲) فعل (۳) حرف"**

| # | Qism | Aasan matlab |
|---|---|---|
| 1 | **اسم (Ism)** | naam |
| 2 | **فعل (Fi'l)** | kaam |
| 3 | **حرف (Harf)** | tareef Slide 10 par — wo kalimah jo doosre ke saath milaaye baghair samjh nahi aata |

##### Ism ki tareef (PDF verbatim)

> **"اسم:** اسم نام کو کہتے ہیں اور اصطلاح صرف میں اسم وہ کلمہ ہے جو مستقل معنیٰ بتائے اور اس میں کوئی زمانہ نہ پایا جائے، جیسے: **زَیْدٌ، خَالِدٌ** وغیرہ۔"

**Roman summary:** **Ism** = naam. Sarf ki istilah mein, ism wo kalimah hai jo (a) apna **mustaqil ma'na** rakhta hai aur (b) uske andar **koi zamana** (past/present/future) nahi paya jata. Misaal: **زَیْدٌ** (Zayd — ek aadmi ka naam), **خَالِدٌ** (Khalid — naam).

##### Fi'l ki tareef (PDF verbatim)

> **"فعل:** فعل کام کو کہتے ہیں اور اصطلاح صرف میں فعل وہ کلمہ ہے جو مستقل معنیٰ بتائے اور اس میں کوئی زمانہ بھی پایا جائے، جیسے: **نَصَرَ** (مدد کی اس ایک مرد نے گزرے ہوئے زمانے میں)۔"

**Roman summary:** **Fi'l** = kaam. Sarf ki istilah mein, fi'l wo kalimah hai jo (a) apna **mustaqil ma'na** rakhta hai (Ism ki tarah) AUR (b) uske andar **zamana bhi paya jaye** (past/present/future). Misaal: **نَصَرَ** = "madad ki (kisi ek mard ne, guzray hue zamane mein)" — yaani **ek lafz mein** kaun ne kya kiya, kab kiya — sab moujood hai.

##### Zamane (PDF verbatim)

> **"نوٹ:** زمانے تین ہیں: (۱) ماضی (گزرا ہوا) (۲) حال (موجودہ) (۳) مستقبل (آنے والا)"

| # | Zamana | Matlab |
|---|---|---|
| 1 | **ماضی (Maazi)** | guzra hua waqt (past) |
| 2 | **حال (Haal)** | abhi ka waqt (present) |
| 3 | **مستقبل (Mustaqbil)** | aane wala waqt (future) |

---

**Mohim baat:** **Ism vs Fi'l ka asli farq** = *zamana hai ya nahi*. Ism mein zamana nahi (naam to har waqt naam rehta hai), Fi'l mein zamana hai (kaam kab hua, ho raha hai, hoga).

**Status:** PDF-VERIFIED 2026-05-28 — Kalimah, Ism, Fi'l ki definitions PDF verbatim. **Harf ki tareef ab Slide 10 (p-021) par aa gayi hai** — Sub Topic 1.2 ke 3 aqsam definitionally complete.

**Chart reference:** Kalimah → 3 aqsam wala taxonomy `charts.md` mein **Chart 1** ke roop mein add hua hai (2026-05-28).

---

#### Slide 8 — Fi'l ki taqseem: Ithbat/Nafi + Muarrab/Mabni (PDF p-020)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 8 | اصطلاحات | Topic 1.0**
- Body 2 hisson mein + ek note:
  - **اثبات اور نفی** ke aitebar se Fi'l ki 2 qismein
  - **عامل ke badalne** se Fi'l ki 2 qismein
  - Note about kaun-se forms hamesha مبنی hain

---

##### Hissa 1: اِثبات اور نَفِی ke aitebar se Fi'l ki taqseem (PDF verbatim)

> **"اِثبات اور نَفِی کے اعتبار سے فعل کی تقسیم"** (red heading)
>
> "اثبات اور نفی کے اعتبار سے فعل کی دو قسمیں ہیں: (۱) **فعل ثبت** (۲) **فعل منفی**"

- **فعل ثبت (Fi'l Subut):** "وہ فعل ہے جس سے کسی کام کا کرنا یا ہونا معلوم ہو، جیسے: **نَصَرَ** (مدد کی اس ایک مرد نے)"
- **فعل منفی (Fi'l Manfi):** "وہ فعل ہے جس سے کسی کام کا نہ کرنا یا نہ ہونا معلوم ہو، جیسے: **مَا نَصَرَ** (نہیں مدد کی اس ایک مرد نے)"

**Roman summary:** Fi'l ki **pehli taqseem** — kaam **hua** (ithbat = positive) ya kaam **NAHI hua** (nafi = negative). Nafi banane ke liye **مَا** lagaya jata hai. Misaal: **نَصَرَ** = "madad ki" → **مَا نَصَرَ** = "nahi madad ki".

---

##### Hissa 2: عامل ke badalne se Fi'l ki taqseem (PDF verbatim)

> **"عامل کے بدلنے سے فعل کی تقسیم"** (red heading)

**عامل ki tareef (PDF verbatim):**
> "عامل وہ ہے جس کے اثر سے بعد والے کلمے میں اعراب کی تبدیلی آ جائے۔"

**Roman:** **عامل (Aamil)** = wo lafz jiska asar uske **baad waale kalimah** ke **اعراب** (zer/zabar/pesh — ending vowel) ko **badal de**.

> "عامل کا اثر قبول کرنے اور نہ کرنے کے اعتبار سے فعل کی دو قسمیں ہیں: (۱) **فعل معرب** (۲) **فعل مبنی**"

- **فعل معرب (Fi'l Mu'arrab):** "وہ فعل ہے جس کا آخر عامل کے بدلنے سے بدل جائے، جیسے: **یَعْلَمُ، اَنْ یَعْلَمَ، لَنْ یَعْلَمَ، لَمْ یَعْلَمْ** ۔"
- **فعل مبنی (Fi'l Mabni):** "وہ فعل ہے جس کا آخر عامل کے بدلنے سے نہ بدلے، جیسے: **یَعْلَمْنَ، لَنْ یَعْلَمْنَ، لَمْ یَعْلَمْنَ** ۔" *(feminine plural — مؤنث جمع — exactly woh siyaghe jo neeche Note mein "mabni" listed hain. Back-validation 2026-05-28 par PDF se confirmed.)*

**Roman summary:** Fi'l ki **doosri taqseem** — kya Fi'l ka **aakhri harkat** عامل ke saath **badalti hai** ya **NAHI**.
- **Mu'arrab:** YES — اعراب change hota hai (e.g., یَعْلَمُ ka pesh → اَنْ ke baad zabar → یَعْلَمَ)
- **Mabni:** NO — aakhri ending **fixed** rehti hai (chahe koi bhi عامل aaye)

---

##### Note: kaun-se forms hamesha مبنی hain (PDF verbatim attempt)

> **"نوٹ:** فعل ماضی معلوم و مجہول، فعل مضارع کے دو صیغے فعل غائب مؤنث جمع، فعل حاضر مؤنث جمع، فعل امر حاضر، فعل امر معلوم و تمام حروف مبنی ہیں۔"

**Roman summary (kitab kya keh rahi hai):** **Hamesha mabni hain:**
- Har **فعل ماضی** (Maazi — Ma'lum aur Majhul dono)
- **فعل مضارع ke 2 specific siyaghe:**
  1. **فعل غائب مؤنث جمع** (third-person feminine plural — e.g., یَعْلَمْنَ)
  2. **فعل حاضر مؤنث جمع** (second-person feminine plural)
- **فعل امر حاضر** + **فعل امر معلوم**
- **Tamam حروف** (all particles) bhi mabni hain

(Abhi sirf zehn mein rakho: Most Muzaari' = mu'arrab; sirf 2 mu'annath jam' siyaghe mabni hain. Tafseel jab gardaan shuru hoga.)

**Self-consistency check (Rule 12):** Mabni examples (یَعْلَمْنَ، لَنْ یَعْلَمْنَ، لَمْ یَعْلَمْنَ) = **feminine plural** — match karte hain Note ke "مؤنث جمع" rule se. ✅

**Status:** PDF-VERIFIED 2026-05-28 (post back-validation) — Mabni examples + Note text dono PDF verbatim. Earlier memory-fill (masculine plural یعلمون) corrected.

**Cross-reference:** Slide 8 ke **مُعرَب examples** (یَعْلَمُ، اَنْ یَعْلَمَ، لَنْ یَعْلَمَ، لَمْ یَعْلَمْ) `gardaan-tables.md` mein **Table 1** ke roop mein arrange ho gaye hain (starter paradigm — aakhri harakah ki tabdeeli عامل ke saath).

---

#### Slide 9 — Fi'l ki taqseem: Ma'lum/Majhul + Fa'il/Maf'ul fa'ida (PDF p-020)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 9 | اصطلاحات | Topic 1.0**
- Body:
  - **فاعل ke aitebar se** Fi'l ki 2 qismein (Ma'lum/Majhul) — har ek ke saath jumla misaal
  - **فائدہ** box: Fi'l, Fa'il, Maf'ul ki short definitions

---

##### فاعِل ke aitebar se Fi'l ki taqseem (PDF verbatim)

> **"فاعِل کے اعتبار سے فعل کی تقسیم"** (red heading)
>
> "فاعل کے اعتبار سے فعل کی دو قسمیں ہیں: (۱) **فعل معلوم** (۲) **فعل مجہول**"

- **فعل معلوم (Fi'l Ma'lum):** "وہ فعل ہے جس کا فاعل معلوم ہو اور اس فعل کی نسبت فاعل کی طرف ہو، جیسے: **شَرِبَ حَامِدٌ مَاءً** (پیا حامد نے پانی) اس مثال میں فاعل **حامد** معلوم ہے اور فعل کی نسبت فاعل کی طرف ہے۔"
- **فعل مجہول (Fi'l Majhul):** "وہ فعل ہے جس کا فاعل معلوم نہ ہو اور اس کی نسبت مفعول کی طرف ہو، جیسے: **شُرِبَ مَاءٌ** (پیا گیا پانی) اس مثال میں فاعل مذکور نہیں اور فعل کی نسبت مفعول کی طرف ہے۔"

**Roman summary:** Fi'l ki **teesri taqseem** — **kaam kis ne kiya** woh saaf hai ya nahi:

| Qism | Kya hai | Misaal (PDF) | Tarjuma |
|---|---|---|---|
| **معلوم** | فاعل maaloom — saaf hai | شَرِبَ حَامِدٌ مَاءً | Hamid ne paani piya |
| **مجہول** | فاعل maaloom nahi — chhupa hua | شُرِبَ مَاءٌ | paani piya gaya |

(English: ma'lum ≈ active voice, majhul ≈ passive voice.)

---

##### فائدہ — Fi'l, Fa'il, Maf'ul ki short definitions (PDF verbatim)

> **"فائدہ:**
>
> **فعل:** کام کو کہتے ہیں۔
>
> **فاعل:** کام کرنے والے کو کہتے ہیں۔
>
> **مفعول:** وہ ہے جس پر فاعل کا فعل (کام) واقع ہو۔"

| Istilah | Tareef (PDF) | Slide 9 ke jumlay se misaal |
|---|---|---|
| **فعل (Fi'l)** | kaam (action) | شَرِبَ (piya) |
| **فاعل (Faa'il)** | kaam karne wala (doer) | حامد (Hamid) |
| **مفعول (Maf'ul)** | جس par فاعل ka kaam waqi' ho (object) | مَاءً (paani) |

**Mohim baat:** Yeh 3 istilahaat — **Fi'l + Fa'il + Maf'ul** — pure Sarf-o-Nahw mein bunyaadi hain. Inhein achhi tarah zehn mein bithaayein.

**Status:** PDF-VERIFIED 2026-05-28 — Slide 9 PDF verbatim. Sirf harakaat ka chhota chance Nazir verify kare.

**Cross-reference:** **Fi'l ki 3 taqseemein** (Slides 8 + 9 combined) ka comprehensive overview `charts.md` mein **Chart 2** ke roop mein hai (10 nodes — Ithbat/Nafi + Muarrab/Mabni + Ma'lum/Majhul saare ek tree mein).

---

#### Slide 10 — Harf ki tareef + 6-misaal table + sample jumla (PDF p-021)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 10 | اصطلاحات | Topic 1.0**
- Body:
  - Red heading: **حرف کی تعریف**
  - 1-paragraph Harf definition (lafzi + istilahi)
  - **"غور کیجیے!"** sub-heading
  - 6-cell table: 6 Harf + Urdu ma'na pairs
  - Sample jumla showing مِنْ and اِلٰی in real usage

---

##### Harf ki tareef (PDF verbatim) — **akhirkar aa gayi!**

> **"حرف:** حرف کنارے کو کہتے ہیں اور اصطلاح صرف میں حرف وہ کلمہ ہے جس کے معنیٰ دوسرے کلمے کو ملائے بغیر سمجھ میں نہ آ سکیں۔"

**Roman summary:**
- **حرف ka lafzi matlab** = **"kinara"** (edge/side) — Arabic mein یہ rozmarrah ka lafz hai
- **Sarf ki istilah mein** = **Harf wo kalimah hai jiska ma'na DOOSRE kalimah ke saath milaaye baghair samjh mein NAHI aata**

Yaani Harf akele khada nahi rehta — kisi Ism ya Fi'l ke saath milkar uska matlab clear hota hai. Jaise English "from", "to", "in", "on" — yeh akele meaningless lagte hain; kisi noun/verb ke saath jud kar matlab dete hain.

> **Note (builder gloss, NOT PDF):** Ism / Fi'l / Harf ke buniyadi farq (zamana / mustaqil ma'na) ki cross-page summary chaahiye? — wo "Yaad rakho" section mein dekhein. Yahaan Slide 10 ka PDF anchor sirf Harf ki tareef + 6-misaal table + sample jumla hai.

---

##### غور کیجیے! — 6 Harf ki misaal table (PDF verbatim)

| Harf (Arabic) | Ma'na (Urdu) | English |
|---|---|---|
| **مِنْ** | سے | from |
| **اِلٰی** | تک | to / till |
| **فِيْ** | میں | in |
| **اِنَّ** | بیشک | verily / surely |
| **لَمْ** | نہیں | not (past negation) |
| **عَلٰی** | پر | on |

---

##### Sample jumla — Harf akele kuch nahi, kalimah ke saath milkar ma'na deta hai (PDF verbatim)

> "جب تک ان کے ساتھ کسی اسم یا فعل نہیں ملائیں گے، اس وقت تک ان کے معنیٰ سمجھ نہیں آئیں گے، جیسے:
>
> **سَفَرْتُ مِنَ الْمَدِيْنَةِ اِلَی الْکُوْفَةِ**
>
> (سفر کیا میں نے مدینہ سے کوفہ تک)
>
> اب مِنْ اور اِلٰی کے معنیٰ سمجھ میں آ گئے کہ سفر کی ابتداء مدینہ سے ہوئی اور انتہا کوفہ تک ہوئی۔"

**Roman:** Akela **"مِنْ"** boldo — kuch matlab nahi. Lekin pure jumlay mein **"سَفَرْتُ مِنَ الْمَدِيْنَةِ اِلَی الْکُوْفَةِ"** = "Maine **Madinah se** **Kufa tak** safar kiya". Ab:
- **مِنْ** ka matlab clear = "safar ki **ابتداء**" (starting point)
- **اِلٰی** ka matlab clear = "safar ki **انتہا**" (ending point)

**Status:** PDF-VERIFIED 2026-05-28 — Harf definition, 6-misaal table, sample jumla sab PDF verbatim.

---

#### Slide 11 — Huroof Tahajji (alphabet) + 2 qismein (Sahih / Illat) + Alif/Hamza note (PDF p-021)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 11 | اصطلاحات | Topic 1.0**
- Body:
  - Red heading: **حُروف تَہَجِّی**
  - Tahajji ki tareef + kalimah se ta'alluq
  - **حروف کی دو قسمیں** — Sahih (25) aur Illat (3 = و، ا، ی)
  - Bottom note about **Alif vs Hamza**

---

##### حُروف تَہَجِّی ki tareef (PDF verbatim)

> "الف سے لے کر یا تک تمام حروف، حروف تہجی کہلاتے ہیں اور یہ عربی زبان کی بنیاد ہیں۔ ان مختلف حروف کو آپس میں ملانے سے کلمہ (اسم، فعل، حرف) بنتا ہے۔"

**Roman summary:**
- **حروف تہجی (Huroof Tahajji)** = Arabic **alphabet** (ا se لے kar ی tak — sab huroof)
- Yeh Arabic zubaan ki **بنیاد** (foundation) hain
- In huroof ko **aapas mein milane** se **kalimah** (Ism / Fi'l / Harf) banta hai

**Mohim distinction — "حرف" lafz ke 2 meaning** (builder gloss — cross-slide comparison, dono examples PDF p-021 se trace karte hain):

| Sense | Matlab | Slide |
|---|---|---|
| **Harf (kalimah ki qism)** | Slide 10 wala — مِنْ، اِلٰی، فِيْ | 10 |
| **Harf (alphabet ka letter)** | Slide 11 wala — ا، ب، ت | 11 |

Donon "حرف" hote hain, lekin **alag-alag senses mein**! Yeh confuse hone wala hai — yaad rakho ke "Sub Topic 1.2 mein 'Harf' ke 2 alag chashma hai".

---

##### Huroof ki 2 qismein (PDF verbatim)

> "حروف کی دو قسمیں ہیں: (۱) **حروف صحیح** (۲) **حروف علت**"

- **حروف صحیح (Huroof Sahih):** "وہ حروف ہیں جو اکثر ایک شکل میں موجود رہتے ہیں اور وہ پچیس (۲۵) ہیں۔"
- **حروف علت (Huroof Illat):** "وہ حروف ہیں جو اکثر ایک شکل میں نہیں رہتے، یعنی ایک کلمے سے دوسرا کلمہ بناتے ہوئے تبدیل ہوتے رہتے ہیں، اور وہ تین حروف **و، ا، ی** ہیں۔ یاد رکھنے کے لیے ان کو **'وَائِی'** کہتے ہیں اور اہل عرب ان کو بیماری کہہ کر ادا کرتے ہیں، نیز جس طرح بیمار کا حال بدلتا رہتا ہے، اسی طرح ان میں بھی تبدیلی ہوتی رہتی ہے۔"

**Table summary:**

| Qism | Tadaad | Khasiyat | Misaal |
|---|---|---|---|
| **حروف صحیح** | **25** | ek shakal mein rehte (fixed form) | ب، ت، ج، س، م waghaira |
| **حروف علت** | **3** | shakal **badalti hai** kalimah banate waqt | **و، ا، ی** (mnemonic: **"وَائِی"** / Waa'i) |

**Mohim baat (Sarf ke liye CRUCIAL):**

> **حروف علت = "Bimaar" huroof.** Jaise bimaar ka **حال** (state) badalta rehta hai, **وَائِی** huroof bhi conjugation/tasreef ke dauran **shakal badalte hain**.

Aage Sarf mein jab gardaan shuru hoga, **Illat-walay verbs** (jin mein و، ا، ی hain) "irregular" lagein ge. **Yeh isi wajah se** — kyunke yeh "bimaari" huroof shakal badalte hain. Yeh foundational concept hai.

---

##### نوٹ — Alif vs Hamza (PDF verbatim)

> "**نوٹ:** الف ہمیشہ ساکن ہوتا ہے، لیکن جب متحرک نظر آئے تو جان لیجیے کہ دراصل وہ ہمزہ ہے، بعض کے نزدیک یہ دونوں الگ الگ حرف ہیں۔"

**Roman summary:**
- **الف (Alif)** **hamesha ساکن** (no vowel harakah) hota hai
- Agar Alif **متحرک** (zer/zabar/pesh wala) dikhe — to woh **dar-asal Alif NAHI**, **ہَمزہ (Hamza)** hai
- **Kuch ulema** ke nazdeek **Alif aur Hamza alag-alag** huroof hain (2 separate huroof count hote)

(Yeh distinction Sarf-o-Nahw mein bohat jagah aati hai. Abhi sirf zehn mein rakho — tafseel jab Hamza-walay misaal aaye.)

**Status:** PDF-VERIFIED 2026-05-28 (validator-corrected). Tahajji tareef + 2 qismein + Note Alif/Hamza sab PDF verbatim. Previously fabricated "Visual misaal" block (اَحْمَدُ) deleted — PDF par koi misaal nahi.

**Cross-reference:** Slide 11 ka **Huroof Tahajji → Sahih/Illat** taxonomy `charts.md` mein **Chart 4** ke roop mein visualize hua hai (5 nodes — Sahih 25 vs Illat 3, Waa'i mnemonic, بیماری analogy).

---

#### Slide 12 — Huroof ki taqseem: Harkat aur 'adam-e-harkat ke aitebar se (PDF p-022)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 12 | اصطلاحات | Topic 1.0**
- Body: red heading + 4-column comparison table + 4 buniyadi vocabulary definitions in centre area

---

##### Heading (PDF verbatim)

> **"حرکت اور عدم حرکت کے اعتبار سے حروف کی تقسیم"**

**Roman:** **Harkat** (movement = zer/zabar/pesh) aur **عدم** (absence of) Harkat ke aitebar se **huroof ki 4 qismein** hain.

---

##### Huroof ki 4 qismein — main table (PDF verbatim)

| # | Qism | Tareef (PDF) | Misaal (PDF) |
|---|---|---|---|
| 1 | **مُتَحَرِّک (Mutaharrik)** | جس پر کوئی حرکت ہو | **ضَرَبَ** |
| 2 | **ساکِن (Saakin)** | جس پر کوئی حرکت نہ ہو | جیسے لفظ **خَالِدْ** میں دال |
| 3 | **مُشَدَّد (Mushaddad)** | جس پر شد ہو، یعنی پہلا حرف ساکن، دوسرا متحرک ہو | **(دَقَّ، رَبَّ)** |
| 4 | **مُنَوَّن (Munawwan)** | جس پر تنوین ہو | **ضَرْبًا** |

---

##### مُتَحَرِّک ki 3 sub-qismein (PDF verbatim)

| Sub-qism | Tareef | Misaal |
|---|---|---|
| **مفتوح (Maftuh)** | جس پر زبر ہو | **کَتَبَ** |
| **مکسور (Maksur)** | جس کے نیچے زیر ہو | **اِبْلِی** |
| **مضموم (Madmum)** | جس پر پیش ہو | **اُذُنْ** |

---

##### مُنَوَّن ki 3 sub-qismein (PDF verbatim)

| Sub-qism | Matlab | Misaal |
|---|---|---|
| **فتحتان (Fathatayn)** | **دو زبر** | **کِتَابًا** |
| **کسرتان (Kasratayn)** | **دو زیر** | **کِتَابٍ** |
| **ضمتان (Dammatayn)** | **دو پیش** | **کِتَابٌ** |

---

##### 4 buniyadi vocabulary definitions (PDF verbatim — slide ke beech mein)

> "حرکت: زبر، زیر اور پیش کو کہتے ہیں۔
>
> فتح: زبر کو کہتے ہیں۔
>
> کسرہ: زیر کو کہتے ہیں۔
>
> ضمہ: پیش کو کہتے ہیں۔"

| Istilah | Matlab | English ko |
|---|---|---|
| **حَرَکَت (Harakah)** | zabar + zer + pesh ko mil kar | "vowel marks" collectively |
| **فَتْح (Fath)** | zabar | "a" (fatha) |
| **کَسْرَہ (Kasra)** | zer | "i" (kasra) |
| **ضَمَّہ (Damma)** | pesh | "u" (damma) |

**MOHIM:** Yeh **buniyadi Sarf vocabulary** hai — har Sarf page par yeh alfaaz aate hain. Yaad rakho.

**Status:** PDF-VERIFIED 2026-05-28 (validator-corrected). 4 qismein, sub-types, vocab sab PDF verbatim. Previous `[?]` markers + bracket guesses on Saakin (خَالِدْ) aur Maksur (اِبْلِی, not اِبْلٰی) hata diye — Rule 11 fix.

**Cross-reference:** Slide 12 ka **Huroof harkat taxonomy** `charts.md` mein **Chart 3** ke roop mein visualize hua hai (11 nodes — Mutaharrik aur Munawwan ki sub-types ke saath complete tree).

---

#### Slide 13 — Reference table: Arabic ibarat ke ~30 aam huroof (PDF p-022)

**PDF par jo hai:**
- Header bar: **Sub Topic 1.2 | کلمہ کی تعریف اور اقسام | Slide 13 | اصطلاحات | Topic 1.0**
- Body: red heading + ek bara dense table (~30 cells) Arabic particles + Urdu meanings ka

---

##### Heading (PDF verbatim)

> **"عربی عبارت میں استعمال ہونے والے چند حروف"**

**Roman:** Yeh ek **reference table** hai — Arabic kitabein parhne mein **bohat aam particles** aur unke Urdu meanings. Yaad karne ka core vocabulary list.

---

##### 6 single-letter prefix particles (top row — PDF verbatim)

| Harf | Matlab (Urdu) | English |
|---|---|---|
| **ب** | ساتھ | with |
| **ت** | قسم کیلیے | for oath |
| **و** | اور | and |
| **ف** | پس | then / so |
| **ک** | جیسے | like / as |
| **ل** | کیلیے | for |

Yeh 6 single-letter **prefix** particles hain — kalimah ke aage juda kar lagte hain (e.g., **ب**ِ + اِسْمِ = بِسْمِ).

---

##### Multi-letter particles — PDF table (validator-corrected + 2026-05-29 PDF re-read cleanup, post-validator-Round-2)

> **HONEST NOTE:** PDF par yeh table **7 rows × 6 columns = 42 total cells** ka layout hai — Row 1 = 6 single-letter prefix particle header (ب/ت/و/ف/ک/ل), Rows 2-7 = **36 multi-letter particle cells (6 rows × 6 cols)**. 2026-05-29 PDF re-read + validator Round 2 + Round 3 audit se 3 pichle `[?]` markers resolve hue (مِنْ present / فِيْ absent / لَا absent — neeche detail). Validator ne 2026-05-28 ko 5 memory-fill instances pakari thi (اِذَا/جب fabricated, اِذْنْ wrong harakat, هَیَّا meaning wrong, مُنْذُ meaning wrong, لَیْتَ meaning truncated) — sab corrected. Validator Round 3 ne مَا (نہیں) aur لَنْ (ہرگز نہیں) ko canonically confirm kiya (Round 2 ki visual ambiguity flags retracted via semantic gloss matching). Currently **~28 multi-letter cells transcribed** + ~8 cells **abhi unconfirmed** (PDF par dikhayi to dete hain magar small-font + dense layout ki wajah se confident reading nahi ho saki). Nazir physical book khol kar baqi cells complete kare.

| Harf (PDF verbatim) | Urdu matlab (PDF) | English (builder gloss) |
|---|---|---|
| **قَدْ** | تحقیق | "verily / already" |
| **مَا** | نہیں | "not" (Slide 10 mein bhi tha) |
| **اِنْ** | اگر | "if" |
| **اَنْ** | کہ | "that" (subjunctive marker) |
| **تَا** | کہ | "so that" (purpose) |
| **لَنْ** | ہرگز نہیں | "never" (future negation) |
| **مِنْ** | `[?]` | "from / since" (2026-05-29 PDF re-read: multi-letter table mein **mojood**; exact row/col position aur exact Urdu meaning Nazir physical book se verify kare. Commentary: particle مِنْ canonically معنیٰ "سے" deti hai, but is specific PDF cell ka exact gloss small-font hone ki wajah se confidently nahi parha — Nazir physical book confirm kare.) |
| **مُذْ** | وقت کیلیے | "since / for (time)" |
| **مُنْذُ** | وقت کیلیے | "since / for (time)" |
| **اَنَّ** | بیشک | "verily / that" |
| **اِنَّ** | بیشک | "verily" (Slide 10 mein tha) |
| **اَیَا** | اے | "O" (vocative) |
| **هَیَّا** | اے | "O" (vocative; same gloss as اَیَا on PDF) |
| **سَوْفَ** | عنقریب | "soon / shall" (future) |
| **اِذَنْ** | جس وقت | "at that time" |
| **خَلَا** | سوائے | "except" |
| **عَدَا** | سوائے | "except" |
| **حَاشَا** | سوائے | "except" |
| **حَتّٰی** | یہاں تک | "until / up to" |
| **لَیْتَ** | کاش کہ | "if only / would that" |
| **لَعَلَّ** | شاید | "perhaps / maybe" |
| **ثُمَّ** | پھر | "then" |
| **رُبَّ** | اکثر | "often / many a" |
| **لَمَّا** | جب | "when" |
| **لٰکِنَّ** | لیکن | "but" |
| **کَأَنَّ** | گویا کہ | "as if" |
| **اِلٰی** | تک | "to / till" (Slide 10) |
| **عَلٰی** | پر | "on" (Slide 10) |

**2026-05-29 PDF re-read + validator Round 2 + Round 3 audit se 3 `[?]` resolved:**
- **مِنْ** ✅ → Multi-letter table mein **mojood**. Upar table mein add ho gaya `[?]` standalone meaning ke saath. Validator Round 2 ne builder ka original positional claim ("Row 2 position 1 rightmost") reject kar diya (woh cell actually قَدْ hai); exact row/col + exact PDF Urdu gloss Nazir physical book se verify kare.
- **فِيْ** ❌ → Multi-letter table mein **alag cell NAHI mili** (Round 2 + Round 3 verified). Sirf column header **ف** (پس) hai jo single-letter prefix hai (different particle se فِيْ). فِيْ ki content Slide 10 ki Harf-misaal mein hai (with meaning میں).
- **لَا** ❌ → Multi-letter table mein **alag cell NAHI mili** (Round 2 + Round 3 verified). Negation ka particle table mein **مَا** ( نہیں ) Row 1 par hai (لَا alag se PDF table mein listed nahi).

**Round 3 validator audit ne Round 2 ki 2 visual-ambiguity flags ko canonically resolve kar diya:**
- **مَا (نہیں)** Row 1 position 2 — Round 3 PDF re-read ne builder ka reading **مَا confirm** kiya (canonical 2-letter م-ا shape match). Round 2 ka لَمْ suggestion retracted.
- **لَنْ (ہرگز نہیں)** Row 1 position 6 — Round 3 ne builder ka reading **لَنْ confirm** kiya via semantic gloss matching (Urdu gloss ہرگز نہیں canonically = لَنْ; اَنْ ka matlab کہ hai jo position 4 par already hai). Round 2 ka اَنْ suggestion retracted.

**Validator-removed (memory-fill or harakat-wrong, ab corrected — 2026-05-28):**
- **اِذْنْ** ❌ → corrected to **اِذَنْ** ✅ (harakat: dhāl pe fatha hai, sukoon nahi)
- **اِذَا** ❌ → actually PDF par **لَمَّا** hai us (جب) cell mein. اِذَا training-knowledge fill thi.
- **هَیَّا (آؤ)** ❌ → PDF Urdu gloss **اے** hai (NOT "آؤ" — woh training-knowledge meaning thi)
- **مُنْذُ (جس وقت سے)** ❌ → PDF par sirf **وقت کیلیے** likha hai
- **لَیْتَ (کاش)** ❌ → PDF par **کاش کہ** hai (کہ chhoot gayi thi)

**Remaining gaps:** Multi-letter table **36 cells (6 rows × 6 cols)** ka grid hai. Abhi **~28 cells transcribed** + ~8 cells exact harf+meaning unconfirmed. Cells PDF par dikhayi to dete hain magar small-font + dense layout ki wajah se confident position+content reading nahi ho saki. Nazir physical book se cell-by-cell verify aur complete kare.

**Mohim baat:** Yeh table aage Quran/Hadith/Adab/Tafseer parhne mein **roz** aane wale particles sikhati hai. **Memorize karna foundational hai** — yeh kitabi vocabulary ka core hai. Lekin **incomplete state mein memorize NA karein** — pehle Nazir physical book khol kar baqi ~8 cells verify aur complete kare.

**Status:** PARTIAL (2026-05-28 validator Round 1 corrected; 2026-05-29 PDF re-read cleanup + validator Round 2 + Round 3 audit complete). 6 single-letter prefix particles confident. Multi-letter table: **36 cells total grid** (6 rows × 6 cols); ~28 cells transcribed + ~8 cells exact-content-unconfirmed. 3 pichle `[?]` markers all resolved (1 confirmed present-but-position-unknown, 2 confirmed absent). **Nazir ko: (a) remaining ~8 cells PDF/physical book se complete karna hai, (b) مِنْ ka exact cell position + exact Urdu gloss confirm karna hai.**

---

#### Slide 14 — Exercise bar `[?]` (PDF p-022)

**PDF par jo hai:**
- Header bar: **متعلقہ سب ٹاپک کے سوالات `[?]` | Slide 14 | میں حل کریں**
  - "متعلقہ سب ٹاپک کے سوالات" — confirmed PDF verbatim (NOT "سبق" — Slide 5 parallel ke saath match)
  - Middle workbook name slot `[?]` — Slide 5 jaisa hi pattern; Nazir physical book se workbook ka exact naam fill kare
- Body koi nahi — sirf bar header

**Roman:** Slide 5 ki tarah, yeh bhi **review/exercise instruction bar** hai — "متعلقہ سب ٹاپک کے سوالات [workbook naam `[?]`] میں حل کریں" — yaani student ko Sub Topic 1.2 ke متعلقہ سوالات workbook mein hal karna hai. Body content NAHI hai. Yeh **Sub Topic 1.2 ka khatima** suggest karta hai.

**Status:** PDF-VERIFIED 2026-05-28 (validator-confirmed). Slide 5 parallel structure cross-verified ("سب ٹاپک" both slides). Sirf workbook name `[?]` standalone — Nazir physical book se fill kare.

---

### Sub Topic 1.3 — جامد، مصدر، مشتق (Ism ki derivational morphology)

> **Yeh asal Sarf ka aaghaaz hai.** Sub Topic 1.1 = meta-intro (5 cheezein). Sub Topic 1.2 = bunyaadi taxonomy (Kalimah, 3 aqsam, Huroof harkat). **Sub Topic 1.3 = Ism ki teen qismein based on derivation** (kahaan se bana / aage kya banta hai) — yeh hi **morphological engine** hai jis se aage 12 cheezein (6 ism + 6 fi'l) nikalti hain.

#### Slide 15 — Sub Topic 1.3 cover (PDF p-023)

**PDF par jo hai:**
- Header bar (RTL reading order): **Sub Topic 1.3 | جامد، مصدر، مشتق | Slide 15 | اصطلاحات | Topic 1.0**
- Body koi visible content nahi — Slide 15 bar ke turant neeche Slide 16 ka header bar shuru ho jata hai (do bars stacked tight). Slide 2 aur Slide 6 jaisa cover pattern.

**Roman:** Slide 15 ek **cover/transition bar** hai — Sub Topic 1.3 ka aaghaaz declare karta hai. Content Slide 16 se shuru hota hai. Sub Topic 1.3 ka title (header bar mein PDF par): **جامد، مصدر، مشتق**.

**Status:** PDF-VERIFIED 2026-05-28 — Slide 15 par body content NAHI hai (PDF render se confirmed, validator-confirmed). Sirf cover bar.

---

#### Slide 16 — اسم کی اقسام (Ism ki 3 qismein) (PDF p-023)

**PDF par jo hai:**
- Title (red Nastaliq, slide ke aupar): **اسم کی اقسام**
- Sub-line: *"اسم کی تین قسمیں ہیں:"*
- Numbered list (pink/red): **(۱) اسم جامد (۲) اسم مصدر (۳) اسم مشتق**
- 3 tareef paragraphs (ek har qism par), har ek mein PDF se misaal
- Closing **نوٹ:** ahl-e-Arab + 12 mushtaq cheezein
- Transition line: *"آئیے! اسم مصدر سے بننے والے افعال اور اسماء کو پڑھتے ہیں:۔"*

##### (۱) اسم جامد ki tareef (PDF verbatim)

> **اسم جامد:** وہ اسم ہے جو نہ تو خود سے بنے اور نہ ہی اس سے کوئی کلمہ بنایا جائے، جیسے: **فَرَسٌ، اِبْرَاهِیْمُ، اَبَابِیْلُ، بَرْزَخٌ** وغیرہ۔

**Roman:** *Jamid wo ism hai jo (a) khud kisi aur cheez se nahi banta, aur (b) is se bhi koi doosra kalimah nahi banta.* Yeh **morphologically "frozen"** isms hain — derivational chain ke andar nahi.

**PDF ke 4 misaal:**

| Arabic | Roman | Matlab (meri taraf se gloss; book mein nahi) |
|---|---|---|
| **فَرَسٌ** | farasun | ghoda |
| **اِبْرَاهِیْمُ** | Ibrāhīmu | Hazrat Ibrahim AS ka naam (ghair munsarif — isiliye akhri harakah ضمہ bina tanween) |
| **اَبَابِیْلُ** | abābīlu | abābīl (woh chiriyaan jo Surah Fil mein zikar hain — ghair munsarif) |
| **بَرْزَخٌ** | barzakhun | barzakh (parda; do cheezon ke darmiyan separator) |

**Nokta:** Yeh chaaron — ghoda, naam, chiriya, barzakh — sab **mahsoos cheezein ya khaas naam** hain. Inhein "banaya" nahi gaya kisi aur lafz se, aur in se aur kuch banta nahi (derivation ke aitebar se).

---

##### (۲) اسم مصدر ki tareef (PDF verbatim)

> **اسم مصدر:** وہ اسم ہے جو خود تو کسی سے نہ بنے لیکن اس سے کلمے بنتے ہوں، جیسے: **عِلْمًا، ضَرْبًا، نَصْرًا** وغیرہ۔

**Roman:** *Masdar wo ism hai jo (a) khud kisi se nahi banta, lekin (b) is se aage doosre kalmay bante hain.*

**PDF ke 3 misaal:**

| Arabic | Roman | Asal (dictionary form) | Matlab (meri taraf se gloss; book mein nahi) |
|---|---|---|---|
| **عِلْمًا** | ʿilman | عِلْم | jaan'na, ilm (action ka naam) |
| **ضَرْبًا** | ḍarban | ضَرْب | maarna (action ka naam) |
| **نَصْرًا** | naṣran | نَصْر | madad karna (action ka naam) |

**Nokta — mansoob form:** Teeno PDF examples **اً** (fathatayn / تنوین نصب) ke saath khatm hote hain — yeh **case ending** hai. Kitab ne mansoob form di hai. Pure dictionary form (raf'): عِلْم/ضَرْب/نَصْر.

**Bunyaadi pehchaan:** Masdar = **action ka naam** (verbal noun). Yeh **derivation engine** hai — Slide 16 Note ke mutabiq is se ek hi waqt mein 6 ism + 6 fi'l mushtaq hote hain.

---

##### (۳) اسم مشتق ki tareef (PDF verbatim)

> **اسم مشتق:** وہ اسم ہے جو خود بھی کسی سے بنے اور اس سے بھی کئی کلمے بنتے ہوں، جیسے: **عَالِمٌ، عَالِمَانِ، عَالِمُوْنَ** وغیرہ۔

**Roman:** *Mushtaq wo ism hai jo (a) khud bhi kisi aur cheez (asal = masdar) se bana ho, aur (b) is se aage bhi kalmay bante hon.*

**PDF ke 3 misaal:**

| Arabic | Roman | Form |
|---|---|---|
| **عَالِمٌ** | ʿālimun | mufrad marfu' (singular, raf' tanween) |
| **عَالِمَانِ** | ʿālimāni | tathniyya marfu' (dual, اَنِ ending) |
| **عَالِمُوْنَ** | ʿālimūna | jam' mudhakkar salim marfu' (sound masc. plural, وْنَ ending) |

**Nokta — derivation chain (meri taraf se observation; book ne explicit chain nahi banayi):**
- Asal masdar: **عِلْم** (knowledge)
- Is se bana ism mushtaq: **عَالِم** (knower / scholar)
- Phir is se aage forms: **عَالِمَانِ** (do scholars), **عَالِمُوْنَ** (kayi scholars), aur others (عَالِمَۃ feminine, etc.)

**Yaani:** مشتق lafz **chain ke beech mein** baithta hai — ek taraf se "bana" (masdar se), doosri taraf "banta hai" (aage forms).

---

##### Closing Note (PDF verbatim)

> **نوٹ:** اہل عرب اسم مصدر سے `[?]` بارہ چیزیں مشتق کرتے ہیں، وہ چھ اسم اور چھ فعل ہیں۔

**Roman:** *Ahl-e-Arab ism masdar se `[?]` **12 cheezein** mushtaq karte hain: **6 ism + 6 fi'l**.*

> **`[?]` ka maamla:** PDF par "سے" aur "بارہ" ke darmiyan ek chhota lafz (~3-4 letters) hai jo small font + render limitations ki wajah se confidently nahi parha ja sakta. **Spelling aur meaning dono Nazir physical book se daale** — yahaan na koi spelling, na koi translation commit ki ja rahi (Rule 11 strict: no guess, no "likely X").

**Yeh poori Sub Topic 1.3 ka root statement hai:** ek masdar → 12 derivatives (6 + 6). Aage ke slides isi tree ko expand karenge.

##### Transition line (PDF verbatim)

> *"آئیے! اسم مصدر سے بننے والے افعال اور اسماء کو پڑھتے ہیں:۔"*

**Roman:** Aaiye! Pehle **6 af'aal** (Slide 17) parhte hain, phir **6 asma'** (Slide 18+ — expected p-024).

**Status:** PRE-BUILD (2026-05-28) — Nazir ko PDF ke saath verify karna hai. Khaas tor par:
- (a) Note mein **`[?]` standalone** ek chhota lafz — Nazir physical book se exact spelling daale (no guess committed per Rule 11);
- (b) Jamid examples **اِبْرَاهِیْمُ** aur **اَبَابِیْلُ** ki **final harakah** (ضمہ bina tanween — ghair munsarif marker) — physical book par yeh harakah saaf dikhe to confirm;
- (c) Mushtaq examples ke teeno forms ki **internal harakaat** — خاص tor par عَالِمَانِ ka noon kasrah aur عَالِمُوْنَ ka noon fatha (yeh tathniyya/jam' ki standard endings hain).

---

#### Slide 17 — اسم مصدر سے بننے والے ۶ فعل (PDF p-023)

**PDF par jo hai:**
- Title (red Nastaliq): **اسم مصدر سے بننے والے چھ فعل**
- Numbered list (pink/red): **(۱) فعل ماضی (۲) فعل مضارع (۳) فعل جحد (۴) فعل نفی (۵) فعل امر (۶) فعل نہی**
- 6 tareef + misaal blocks — har ek mein PDF Arabic example + Urdu tarjuma in parentheses

##### 6 fi'l qismein — PDF verbatim table

Har row PDF se direct uthayi gayi hai. Sab examples **standard root نصر (madad karna)** ke saath hain — yeh classical Sarf book pattern hai:

| # | Fi'l ki qism | Tareef (PDF Urdu verbatim) | Misaal (Arabic) | Urdu tarjuma (PDF verbatim — parentheses mein) |
|---|---|---|---|---|
| ۱ | **فعل ماضی** | وہ فعل ہے جو گزرے ہوئے زمانے کے متعلق بتائے | **نَصَرَ** | (مدد کی اس نے ایک مرد نے) |
| ۲ | **فعل مضارع** | وہ فعل ہے جو موجودہ یا آئندہ زمانے کے متعلق بتائے | **یَنْصُرُ** | (مدد کرتا ہے یا کرے گا وہ ایک مرد) |
| ۳ | **فعل جحد** | وہ فعل ہے جس میں کسی کام کا انکار، ماضی میں سمجھا جائے | **لَمْ یَنْصُرْ** | (نہیں مدد کی اس نے ایک مرد نے) |
| ۴ | **فعل نفی** | وہ فعل ہے جس میں کسی کام کا انکار، حال یا مستقبل میں سمجھا جائے | **لَا یَنْصُرُ** | (نہیں مدد کرتا یا نہیں کرے گا وہ ایک مرد) |
| ۵ | **فعل امر** | وہ فعل ہے جس میں کسی کام کا حکم دیا جائے | **اُنْصُرْ** | (مدد کر تو ایک مرد) |
| ۶ | **فعل نہی** | وہ فعل ہے جس میں کسی کام سے روکا جائے | **لَا تَنْصُرْ** | (نہ مدد کر تو ایک مرد) |

##### Cross-slide observation (builder gloss; book ne yeh tabseera nahi diya)

- **Pichli Slide 7 mein** Kalimah ki taxonomy ke waqt Fi'l ke **3 zamane** taught the (Maazi/Haal/Mustaqbil) — yeh **time-axis** par the.
- **Yahaan Slide 17 mein** Fi'l ki **6 qismein** = **functional categories**: zamane (Maazi/Mudaari') + negation (Jahd past, Nafi present/future) + command (Amr) + prohibition (Nahi).
- **Aage ke Sub Topics mein** "اقسام فعل" ka tafseeli bayan aayega (Slide 1 table ke baqi rows ka content abhi `[?]` markers ke saath pending) — yahaan sirf **masdar-derivation** context mein 6 qismein introduce hui hain (Note ke 6 fi'l = ye hi 6).

##### Pattern observation (meri taraf se; book ne yeh explicit nahi kaha)

PDF examples se yeh pattern saaf nazar aata hai (Nazir verify kare):

| Functional pair | Particle + sigha |
|---|---|
| **Past affirmative vs negation** | نَصَرَ (madhi) vs **لَمْ + mudaari' majzoom** (jahd) → لَمْ یَنْصُرْ |
| **Present/future affirmative vs negation** | یَنْصُرُ (mudaari' marfu') vs **لَا + mudaari' marfu'** (nafi) → لَا یَنْصُرُ |
| **Command vs prohibition** | اُنْصُرْ (amr) vs **لَا + mudaari' majzoom** (nahi) → لَا تَنْصُرْ |

**Status:** PRE-BUILD (2026-05-28) — Nazir verify kare. **6 rows ki tareef-text + 6 Arabic misaal + 6 Urdu parentheses translations** — sab character-by-character physical book se match karna chahiye. Chhote Urdu particles (کا، کے، میں، تو، نے, etc.) PDF render mein easy to mis-copy hote hain. Khaas tor par:
- (a) **Har row ki tareef** — 6 rows, har ek mein 8-12 Urdu words; word-by-word match;
- (b) **6 Arabic misaal** (نَصَرَ، یَنْصُرُ، لَمْ یَنْصُرْ، لَا یَنْصُرُ، اُنْصُرْ، لَا تَنْصُرْ) — harakaat aur sukoon-marks pe khaas dhyaan;
- (c) **6 Urdu parentheses translations** — "(مدد کی اس نے ایک مرد نے)" wagairah — har particle aur lafz check;
- (d) **اُنْصُرْ** ki **damma on alif** (ا par ضمہ marker, hamzat-ul-wasl) — PDF par chhota dikha, physical book mein saaf hoga.

---

#### Slide 18 — اسم مصدر سے بننے والے ۶ اسم (part 1 of 2) (PDF p-024)

**PDF par jo hai:**
- Header bar (RTL reading order): **Sub Topic 1.3 | جامد، مصدر، مشتق | Slide 18 | اصطلاحات | Topic 1.0**
- Title (red Nastaliq): **اسم مصدر سے بننے والے چھ اسم**
- Numbered list (pink/red): **(۱) اسم فاعل (۲) اسم مفعول (۳) اسم تفضیل (۴) اسم ظرف (۵) اسم آلہ (۶) صفت مشبہ**
- 4 tareef + misaal blocks on this slide (Fa'il, Maf'ul, Tafzeel, Zarf — last 2 ism qismein Slide 19 par)
- اسم ظرف ke andar **2 sub-types** ki tafseel (Zarf Zaman + Zarf Makan), har ek ka tareef + misaal

##### Title intro + 6-naam list (PDF verbatim)

> **اسم مصدر سے بننے والے چھ اسم**
> (۱) اسم فاعل (۲) اسم مفعول (۳) اسم تفضیل (۴) اسم ظرف (۵) اسم آلہ (۶) صفت مشبہ

**Roman:** Slide 16 ke Note ne kaha tha: *"ek masdar → 12 cheezein = 6 ism + 6 fi'l"*. Slide 17 par **6 fi'l** mil gaye (Madhi/Mudaari'/Jahd/Nafi/Amr/Nahi). Ab Slide 18-19 par **6 ism** aate hain. **Yeh masdar→tree ka doosra haalf hai.**

##### 6 ism qismein — 4 tareef blocks (Slide 18 par; PDF verbatim)

| # | Ism ki qism | Tareef (PDF Urdu verbatim) | Misaal (Arabic) | Urdu tarjuma (PDF verbatim — parentheses) |
|---|---|---|---|---|
| ۱ | **اسم فاعل** | وہ اسم ہے جو کام کرنے والے کی ذات کے متعلق بتائے | **نَاصِرٌ** | (مدد کرنے والا ایک مرد) |
| ۲ | **اسم مفعول** | وہ اسم ہے جو ایسی ذات کے متعلق بتائے جس پر فاعل کا فعل واقع ہو | **مَنْصُوْرٌ** | (مدد کیا ہوا ایک مرد) |
| ۳ | **اسم تفضیل** | وہ اسم ہے جو کسی ذات میں دوسروں کی نسبت صفت کی زیادتی ظاہر کرے | **اَنْصَرُ** | (زیادہ مدد کرنے والا) |
| ۴ | **اسم ظرف** | وہ اسم ہے جس میں وقت یا جگہ کے معنی پائے جائیں | (2 sub-types — neeche) | (sub-type wise) |

##### اسم ظرف ki 2 sub-types (PDF verbatim)

> اسم ظرف کی دو قسمیں ہیں: **(۱) ظرف زمان (۲) ظرف مکان**

| Sub-type | Tareef (PDF verbatim) | Misaal (Arabic) | Urdu tarjuma |
|---|---|---|---|
| **ظرف زمان** | کام کرنے کے وقت کو کہتے ہیں | **مَنْصَرٌ** | (مدد کرنے کا وقت) |
| **ظرف مکان** | کام کرنے کی جگہ کو کہتے ہیں | **مَجْلِسٌ** | (بیٹھنے کی جگہ) |

##### Pattern observation (meri taraf se; book ne yeh tabseera nahi diya)

PDF examples se yeh pattern saaf hai (Nazir verify kare):

| Ism qism | Pattern (wazn) | Misaal |
|---|---|---|
| اسم فاعل | فَاعِل | نَاصِر |
| اسم مفعول | مَفْعُوْل | مَنْصُوْر |
| اسم تفضیل | اَفْعَل | اَنْصَر |
| ظرف زمان | مَفْعَل | مَنْصَر |
| ظرف مکان | مَفْعِل | مَجْلِس |

Yeh **wazn / morphological patterns** Sarf ki bunyaadi mehnat ka khaaka hain — har ism qism ek mukhtalif wazn par bani hoti hai. (Yeh observation builder gloss hai; book ne abhi tak wazn ko explicit naam se nahi sikhaya — Sub Topic 1.4/1.5 mein expected.)

**Status:** PDF-VERIFIED 2026-05-28 (validator Round 1 confirmed):
- (a) Har tareef + Urdu parenthetical Round 1 PDF re-read se confirmed (one fix applied: Maf'ul tareef "واقع ہوا" → "واقع ہو" — validator caught extra alif);
- (b) اَنْصَرُ ki sad par **fatha** confirmed (afʿal pattern); مَنْصَرٌ (no wāw) vs مَنْصُوْرٌ (wāw-saakin) farq confirmed; مَجْلِسٌ par ل ki kasrah confirmed (مَفْعِل pattern);
- (c) "تفضیل" mein ض (dad) ki diacritical dot confirmed (not ص).

---

#### Slide 19 — اسم qismein (part 2 of 2) + matching exercise table (PDF p-024)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.3 | جامد، مصدر، مشتق | Slide 19 | اصطلاحات | Topic 1.0**
- Last 2 of 6 ism qismein ke tareef + misaal blocks (Aalah + Sifat-e-Mushabbaha)
- Red title: **اسماء مشتقہ آپس میں ملائیں** (matching exercise heading)
- 5-row matching exercise table — left column "اسمائے مشتقہ" + right column "اسمائے مشتقہ" + نمبر column

##### Last 2 ism qismein — tareef + misaal (PDF verbatim)

| # | Ism ki qism | Tareef (PDF Urdu verbatim) | Misaal (Arabic) | Urdu tarjuma (PDF verbatim) |
|---|---|---|---|---|
| ۵ | **اسم آلہ** | وہ اسم ہے جو کسی کام کے آلے (ذریعے) یا واسطے کے متعلق بتائے | **مِصْبَاحٌ** | (چراغ، روشنی کا آلہ) |
| ۵ continued | (same row, 2nd PDF misaal) | — | **مِیْزَانٌ** | (ترازو، وزن کرنے کا آلہ) |
| ۶ | **صفت مشبہ** | وہ اسم ہے جو ایسی ذات کے متعلق بتائے کہ جس میں یہ صفت ہمیشہ سے موجود ہو | **سَمِیْعٌ** | (ہمیشہ سننے والا) |

##### Pattern observation expansion (continued from Slide 18; builder gloss)

| Ism qism | Pattern (wazn) | Misaal |
|---|---|---|
| اسم آلہ | مِفْعَال | مِصْبَاح، مِیْزَان |
| صفت مشبہ | فَعِیْل (ek common pattern; aur patterns bhi) | سَمِیْع |

**Note:** Sifat-e-Mushabbaha ke kayi waznein hote hain (فَعِیْل، فَعْل، فَعَل، waghaira) — book ne sirf سَمِیْع misaal di hai. Yeh observation builder gloss hai.

##### Matching exercise table — اسماء مشتقہ آپس میں ملائیں (PDF verbatim)

> **اسماء مشتقہ آپس میں ملائیں** (Derived nouns ko aapas mein match karein)

PDF par 5-row table; left + right columns dono "اسمائے مشتقہ":

| نمبر | اسمائے مشتقہ (R column — PDF right) | اسمائے مشتقہ (L column — PDF left) |
|---|---|---|
| ۱ | **نَاصِرٌ** (مدد کرنے والا ایک مرد) | **اَعْلَمُ** (زیادہ جاننے والا ایک مرد) |
| ۲ | **مَنْصُوْرٌ** (مدد کیا ہوا ایک مرد) | **عَالِمٌ** (جاننے والا ایک مرد) |
| ۳ | **اَنْصَرُ** (زیادہ مدد کرنے والا) | **مَضْرُوْبٌ** (مارا ہوا ایک مرد) |
| ۴ | **مَنْصَرٌ** (مدد کرنے کا وقت یا جگہ) | **عَلِیْمٌ** (ہمیشہ جاننے والا) |
| ۵ | **سَمِیْعٌ** (ہمیشہ سننے والا) | **مَدْخَلٌ** (داخل ہونے کا وقت یا جگہ) |

**Exercise ka maqsad (builder gloss; book ne yeh explicit nahi kaha):** har row mein R-column ka form + L-column ka form **same morphological qism** ke hone chahiye (cross-root pattern recognition). Solution (meri taraf se — Nazir confirm kare):
- R1 نَاصِرٌ (faail) ↔ L2 عَالِمٌ (faail) — dono فَاعِل wazn
- R2 مَنْصُوْرٌ (maf'ul) ↔ L3 مَضْرُوْبٌ (maf'ul) — dono مَفْعُوْل wazn
- R3 اَنْصَرُ (tafzeel) ↔ L1 اَعْلَمُ (tafzeel) — dono اَفْعَل wazn
- R4 مَنْصَرٌ (zarf) ↔ L5 مَدْخَلٌ (zarf) — dono مَفْعَل wazn
- R5 سَمِیْعٌ (sif-e-mush) ↔ L4 عَلِیْمٌ (sif-e-mush) — dono فَعِیْل wazn

**Note:** Exercise mein **اسم آلہ** included NAHI (5 rows = 5 ism qismein only) — book ne 6 mein se 5 chuna.

**Status:** PDF-VERIFIED 2026-05-28 (validator Round 1 confirmed):
- (a) مِصْبَاحٌ + مِیْزَانٌ ki compound parentheticals ("چراغ، روشنی کا آلہ" + "ترازو، وزن کرنے کا آلہ") confirmed PDF-verbatim;
- (b) Matching table L column row 3 = **مَضْرُوْبٌ** confirmed (PDF Urdu tarjuma "مارا ہوا ایک مرد" = maf'ul of ضرب; agar root ضرر hota to "مضرر" hota aur "harm" matlab hota — match nahi);
- (c) Matching table L column row 1 = **اَعْلَمُ** confirmed (ع+ل+م letters; ism tafzeel of علم matching "زیادہ جاننے والا");
- (d) (Slide 18 par cover ho gaya.)

---

#### Slide 20 — Exercise bar `[?]` (PDF p-024) — Sub Topic 1.3 ka khatima

**PDF par jo hai:**
- Header bar: **متعلقہ سب ٹاپک کے سوالات | Slide 20 | `[?]` میں حل کریں**
  - Slides 5 + 14 jaisa hi exercise bar pattern (`[?]` workbook name slot "میں حل کریں" ke saath)
  - Bar layout: "متعلقہ سب ٹاپک کے سوالات" (right) | "Slide 20" (middle) | "`[?]` میں حل کریں" (left)
- Body koi nahi — sirf bar header

**Roman:** Slide 5 (Sub Topic 1.1 khatima) aur Slide 14 (Sub Topic 1.2 khatima) ki tarah, Slide 20 bhi **Sub Topic 1.3 ka khatima** suggest karta hai — student ko متعلقہ workbook mein Sub Topic 1.3 ke sawalat hal karne hain. Body content NAHI.

**Yeh confirm karta hai:** Slide 16 Note ka "1 masdar → 12 cheezein" formula ab fully delivered — 6 fi'l (Slide 17) + 6 ism (Slides 18-19) = **12 mushtaq cheezein** + matching exercise. Sub Topic 1.3 mukammal.

**Status:** PDF-VERIFIED 2026-05-28 — Slide 5 + Slide 14 parallel structure cross-verified ("متعلقہ سب ٹاپک کے سوالات" pattern); sirf workbook name `[?]` standalone — Nazir physical book se fill kare.

---

### Sub Topic 1.4 — حروف اصلی کی پہچان (Huroof Asli ki pehchaan — wazn ka formal taaruf)

> **Yeh Sub Topic 1.3 ka natural extension hai** — Sub Topic 1.3 ne sikhaya ke ek masdar se 12 mushtaq hoti hain; Sub Topic 1.4 ab sikhata hai ke **kaisey identify karein konsa harf root ka hai aur konsa zaa'idah (extra)**. Yeh kaam **وزن (wazn)** ke zariye hota hai — Arabic morphology ka core tool. **Yeh asal Sarf ka technical engine hai** — abhi tak jo "Pattern observation" tables thi notes.md mein wo ab PDF-formal nomenclature hai.

#### Slide 21 — Sub Topic 1.4 cover (PDF p-025)

**PDF par jo hai:**
- Header bar (RTL reading order): **Sub Topic 1.4 | حروف اصلی کی پہچان | Slide 21 | اصطلاحات | Topic 1.0**
- Body koi visible content nahi — sirf cover bar (Slide 15 + Slide 6 + Slide 2 jaisa cover pattern)

**Roman:** Slide 21 ek **cover/transition bar** hai — Sub Topic 1.4 ka aaghaaz declare karta hai. Title: **حروف اصلی کی پہچان** (Identification of root letters). Content Slide 22 se shuru hota hai.

**Status:** PDF-VERIFIED 2026-05-28 — Slide 21 par body content NAHI (cover bar pattern, Slides 2/6/15 ke parallel).

---

#### Slide 22 — وزن نکالنے کا طریقہ (Method for extracting wazn) (PDF p-025)

**PDF par jo hai:**
- Header bar (compressed/4-cell variant): **Sub Topic 1.4 | Slide 22 | وزن کے ذریعے حروف اصلی کی پہچان** — yahaan standard اصطلاحات + Topic 1.0 cells slide-specific sub-heading se replace ho gaye. Slides 21 + 23 standard 5-cell layout use karte hain.
- Red title 1: **وزن نکالنے کا طریقہ**
- 3 tareef paragraphs: **موزون**, **میزان**, **وزن** — har ek mein definition
- Red title 2: **اسماء کے وزن نکالنے کا طریقہ**
- Method paragraph + example (ضَرْبٌ → فَعْلٌ)
- 6-column table (3 موزون-وزن pairs) with PDF examples

##### 3 bunyaadi tareefein (PDF verbatim)

> **موزون:** وہ لفظ ہے جس کا وزن نکالا جائے۔

**Roman:** *Mauzun = wo lafz jis ka wazn nikalna ho.* (The word being measured.)

> **میزان:** ان حروف کو کہتے ہیں جن کے ذریعے وزن نکالا جائے اور وہ حروف یہ ہیں: **فا، عین، لام**، ان کا مجموعہ **فَعَلَ** ہے۔

**Roman:** *Meezan = wo huroof jin ke zariye wazn nikala jaye. Yeh huroof = **فا، عین، لام**. Inka combined form = **فَعَلَ**.* (The yardstick/template letters.)

> **وزن:** کسی بھی لفظ میں پائے جانے والے حروف کی مرتب شکل اور خاص حرکات و سکنات جو میزان کے ذریعے واضح ہو، اُس کو وزن کہتے ہیں۔

**Roman:** *Wazn = kisi bhi lafz mein paaye jaane wale huroof ki **murattab shakal** + khaas **harakaat-o-sukoonaat**, jo meezan ke zariye waazeh ho — wo wazn hai.* (The pattern: ordered letter structure + harakaat/sukoonaat made explicit via meezan.)

##### Method (PDF verbatim)

> **اسماء کے وزن نکالنے کا طریقہ:** عربی زبان کے کلمات کا **'ف، ع، ل'** کے ذریعے وزن نکالا جاتا ہے، اور وزن نکالنے کا طریقہ یہ ہے کہ موزون کی شکل دیکھ کر میزان کو منتخب کریں یعنی جو حرکات و سکنات موزون پر ہیں، وہی میزان پر لگا دیں، جیسے: **ضَرْبٌ وزن فَعْلٌ**۔

**Roman:** Method ke 3 steps:
1. **Mauzun ki shakal dekho** (e.g., ضَرْبٌ — 3 huroof, fatha-sukoon-damma+tanween).
2. **Meezan select karo** matching length (yahaan 3-letter root so use ف-ع-ل).
3. **Same harakaat-sukoonaat** meezan par lagao — har position se: ض(fatha)→ف(fatha), ر(sukoon)→ع(sukoon), ب(damma+tanween)→ل(damma+tanween) → **فَعْلٌ**.

##### 3-pair example table (PDF verbatim)

| موزون | وزن |
|---|---|
| **فَتْحٌ** | **فَعْلٌ** |
| **عِلْمٌ** | **فِعْلٌ** |
| **بَعْدٌ** | **فَعْلٌ** |

(PDF par yeh table 6-column single-row layout mein hai — 3 paired columns. Roman Urdu reading: pehla pair فَتْحٌ→فَعْلٌ, doosra عِلْمٌ→فِعْلٌ, teesra بَعْدٌ→فَعْلٌ.)

**Pattern (builder gloss; book ne in 3 examples ka explicit pattern-comparison nahi diya):**
- فَتْح aur بَعْد dono **fatha-sukoon** pattern par → wazn **فَعْل** (fatha-sukoon).
- عِلْم alag pattern par — **kasrah-sukoon** → wazn **فِعْل** (kasrah-sukoon).
- **Sabaq:** Mauzun ki harakaat hi wazn ka shakal decide karti hain. Same harakaat-pattern = same wazn.

**Status:** PDF-VERIFIED 2026-05-28 (validator Round 1 confirmed):
- (a) Bar layout = compressed/4-cell variant confirmed against PDF;
- (b) 3 tareefein (Mauzun/Meezan/Wazn) — full dense Urdu PDF-verbatim, every word matches;
- (c) Meezan ke 3 huroof spelled out as "فا، عین، لام" confirmed;
- (d) Combined form **فَعَلَ** (3 fathas) confirmed;
- (e) **Table rightmost cell = فَتْحٌ** confirmed via validator's PDF re-read (first letter ف dot above, middle letter ت 2 dots above, final letter ح no dot). NOT ضَرْبٌ. Table 3 pairs = فَتْحٌ→فَعْلٌ / عِلْمٌ→فِعْلٌ / بَعْدٌ→فَعْلٌ.

---

#### Slide 23 — حروف اصلی ki pehchaan via wazn — فا کلمہ / عین کلمہ / لام کلمہ (PDF p-025)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.4 | حروف اصلی کی پہچان | Slide 23 | اصطلاحات | Topic 1.0**
- Body text: 3 paragraphs explaining root-letter identification via wazn + terminology
- Closing **نوٹ** at bottom

##### Hissa 1: حروف اصلی ki pehchaan (PDF verbatim)

> صرفیوں نے حروف اصلی کی پہچان کے لیے **'ف، ع، ل'** کلمہ کو **میزان** اور **کسوٹی** مقرر کیا ہے، یعنی جو حرف 'ف، ع، ل' کلمہ کے مقابلے میں آئے، وہ **اصلی** ہوگا اور جو 'ف، ع، ل' کلمہ کے مقابلے میں نہ ہو، وہ **زائدہ** یا **علامات یا کلام** میں سے ہوگا، جیسے: **عِلْمٌ** کا وزن **فِعْلٌ** ہے۔ اس مثال میں **تمام حروف اصلی** ہیں اور **عَالِمٌ** کا وزن **فَاعِلٌ** ہے۔ اس مثال میں **الف زائد** ہے اور **اسم فاعل کی علامت** ہے۔

**Roman:** Sarfiyon (Sarf experts) ne 'ف، ع، ل' kalimah ko **meezan + kasoti** (touchstone/yardstick) muqarrar kiya:
- Jo harf 'ف، ع، ل' ke **muqaabile mein aaye** = **اصلی** (root).
- Jo na aaye = **زائدہ** (extra) ya **علامات** (sign) ya **کلام میں سے** (part of the case ending).

**Misaal 1:** عِلْمٌ → فِعْلٌ. Saare 3 huroof (ع، ل، م) → root (3 letters all align with ف، ع، ل).

**Misaal 2:** عَالِمٌ → فَاعِلٌ. Yahaan **الف زائد** hai — meezan ke ف، ع، ل ka extension (فَاعِل = wazn with alif between ف aur ع). Alif **اسم فاعل ki علامت** (sign of ism faail).

##### Hissa 2: فا کلمہ، عین کلمہ، لام کلمہ — root letter labels (PDF verbatim)

> موزون میں جو حرف میزان کے **'فا'** کلمہ کے مقابلے میں ہو، اس کو **'فا کلمہ'** کہیں گے، اور جو حرف **'عین'** کلمہ کے مقابلے میں ہو، اس کو **'عین کلمہ'** کہیں گے اور جو حرف **'لام'** کلمہ کے مقابلے میں ہو، اس کو **'لام کلمہ'** کہیں گے۔ جیسے: **ضَرْبٌ** کا وزن **فَعْلٌ** ہے، اس مثال میں **'ض'** کو **'فا کلمہ'** اور **'ر'** کو **'عین کلمہ'** اور **'ب'** کو **'لام کلمہ'** کہیں گے۔

**Roman:** **3 naye terms** root ke 3 letters ke liye:
- 1st root letter (jo ف ke muqaabile mein) = **فا کلمہ** (Fa Kalimah)
- 2nd root letter (jo ع ke muqaabile mein) = **عین کلمہ** (Ain Kalimah)
- 3rd root letter (jo ل ke muqaabile mein) = **لام کلمہ** (Lam Kalimah)

**Misaal:** ضَرْبٌ → فَعْلٌ:
- ض = **فا کلمہ**
- ر = **عین کلمہ**
- ب = **لام کلمہ**

##### Hissa 3 — Note (PDF verbatim)

> **نوٹ:** جو حرف موزون میں زیادہ ہوگا، وہی حرف میزان میں بھی زیادہ کیا جائے گا۔

**Roman:** *Jo harf mauzun mein "ziyada" (extra beyond root) hoga, wahi harf meezan mein bhi "ziyada" kiya jaye ga.* — Yaani agar mauzun mein extra alif hai (jaise عَالِم mein), to meezan mein bhi corresponding extra alif lagega (فَاعِل mein). **Yeh isi liye derived forms ke waznein lambay hote** (مَفْعُوْل، مِفْعَال، اَفْعَل waghaira).

##### Cross-page connection (builder gloss; book ne yeh tabseera nahi diya)

- **p-024 Slides 18-19** mein 6 ism qismein ke saath "Pattern observation" tables thi jin mein waznein listed thi as **builder gloss**. Sub Topic 1.4 ne ab wazn ko **PDF-formally introduce** kar diya — toh woh wazn knowledge ab "memory-fill" nahi raha, balki **PDF-attested** ho gaya (kam-az-kam فَاعِل for ism faail).
- **Chart 5** se wazn labels validator ne hatwaye the (Round 1 FAIL Rule 7) kyunke us waqt wazn introduced nahi tha. Ab Sub Topic 1.4 mukammal hone ke baad Chart 5 mein wazn labels add karne ka case-by-case consideration kar sakte (separate sub-decision).

**Status:** PDF-VERIFIED 2026-05-28 (validator Round 1 confirmed; 1 MED fix applied):
- (a) Hissa 1 dense Urdu paragraph PDF-verbatim (میزان+کسوٹی, 3-cheez listing زائدہ/علامات/کلام, عَالِمٌ→فَاعِلٌ alif zaa'idah);
- (b) عَالِمٌ ka فَاعِلٌ wazn confirmed PDF-formally introduced — Sub Topic 1.3 ke builder gloss observations ab PDF-attested;
- (c) Hissa 2 — Round 1 fix applied: middle clause "اور جو حرف 'عین' کلمہ کے مقابلے میں ہو، اس کو 'عین کلمہ' کہیں گے" restore kiya (previously elided/abbreviated builder shortening tha); ضَرْبٌ assignment ض/ر/ب → فا/عین/لام کلمہ PDF-verbatim confirmed;
- (d) Note "ہوگا" / "جائے گا" verb forms confirmed.

---

#### Slide 24 — حروف اصلی (مادہ) کی پہچان — 7-misaal table (PDF p-026)

**PDF par jo hai:**
- Header bar (RTL reading order): **Sub Topic 1.4 | حروف اصلی کی پہچان | Slide 24 | اصطلاحات | Topic 1.0**
- Red title: **حروف اصلی (مادہ) کی پہچان**
- 4-column × 7-row table demonstrating wazn-extraction method on 7 examples
- Table columns (RTL): **لفظ | وزن | حروف اصلیہ | حروف زائدہ/علامات**
- (Note: Column 3 header **حروف اصلیہ** (ہ-ending, feminine plural agreement with حروف) — validator-confirmed via PDF re-read 2026-05-29. Slide 23 ne "حروف اصلی" (masculine form) use kiya tha — yahaan plural feminine form *حروف اصلیہ* — dono synonymous hain "root letters" ke liye.)

##### New term taaruf: مادہ (Maddah) — synonym for حروف اصلی

PDF title bracket mein "مادہ" lafz add hua — yeh **synonym** hai حروف اصلی ka. **مادہ ka literal matlab:** "matter" / "substance" — yaani lafz ka **asal jauhar / sarchashma**. Sarf mein **روٹ letters** ko hi "مادہ" kehte. Aaj se aap **حروف اصلی** aur **مادہ** dono interchangeably use kar sakte.

##### 7-misaal table (PDF verbatim — RTL column order: لفظ | وزن | حروف اصلیہ | حروف زائدہ/علامات)

| لفظ (mauzun) | وزن | حروف اصلیہ (root) | حروف زائدہ/علامات (extras) |
|---|---|---|---|
| **نَصْرٌ** | **فَعْلٌ** | ن، ص، ر | **×** (koi zaa'idah nahi) |
| **عَابِدٌ** | **فَاعِلٌ** | ع، ب، د | ا |
| **کَاتِبُوْنَ** | **فَاعِلُوْنَ** | ک، ت، ب | ا، و، ن |
| **کَرِیْمٌ** | **فَعِیْلٌ** | ک، ر، م | ی |
| **کَاتِبٌ** | **فَاعِلٌ** | ک، ت، ب | ا |
| **عَالِمَانِ** | **فَاعِلَانِ** | ع، ل، م | ا، ا، ن |
| **شَرِیْفٌ** | **فَعِیْلٌ** | ش، ر، ف | ی |

##### Row-by-row analysis (PDF table ka apna pattern — builder commentary explicitly marked)

**Row 1 — نَصْرٌ → فَعْلٌ:**
- 3 root letters (ن، ص، ر) match 3 meezan letters (ف، ع، ل) ek-ek karke.
- Koi zaa'idah letter nahi (× column).
- **Builder observation (meri taraf se):** Yeh **simplest case** hai — pure root only, no morphological additions. Yeh **اسم مصدر** (verbal noun) ki shape hai jisko Sub Topic 1.3 mein dekh chuke (Slide 16 ka "نَصْرًا" reference).

**Row 2 — عَابِدٌ → فَاعِلٌ:**
- Root: ع، ب، د (worship-related). Extra: ا (between ع aur ب).
- Wazn فَاعِلٌ — Slide 23 par ye wazn formally introduce hua tha (عَالِمٌ ke saath).
- **Builder observation (meri taraf se):** ا = **اسم فاعل ki علامت** (Slide 23 statement). To عَابِدٌ = "ibadat karne wala" — اسم فاعل of عَبَدَ.

**Row 3 — کَاتِبُوْنَ → فَاعِلُوْنَ:**
- Root: ک، ت، ب (write-related). Extras: ا، و، ن (3 zaa'idah letters).
- Wazn فَاعِلُوْنَ — yeh **masculine plural** ki form hai.
- **Builder observation (meri taraf se):** Asal اسم فاعل of "kataba" = **کَاتِبٌ** (singular, Row 5). Plural ke liye **و + ن** add kar diye — یہ **علامتِ جمع مذکر سالم** (sound masculine plural marker, Sarf detail aage Sub Topics mein). Toh **ا = ism faail ki علامت + و، ن = jamع ki علامت** = 3 zaa'idah letters total.

**Row 4 — کَرِیْمٌ → فَعِیْلٌ:**
- Root: ک، ر، م (generosity-related). Extra: ی (between ر aur م).
- Wazn فَعِیْلٌ — yeh wazn Sub Topic 1.3 Slide 19 par "Pattern observation" mein **صفت مشبہ** ke saath associate kiya tha (سَمِیْعٌ ki wajah se).
- **Builder observation (meri taraf se):** کَرِیْمٌ = "permanently generous" = **صفت مشبہ** (jis mein sifat hamesha mojood ho — Slide 19 tareef). Yeh Sub Topic 1.3 + 1.4 ka cross-link hai.

**Row 5 — کَاتِبٌ → فَاعِلٌ:**
- Same root as Row 3 (ک، ت، ب). Extra: ا only.
- Wazn فَاعِلٌ — singular form. Row 3 ka **singular bhai**.
- **Builder observation (meri taraf se):** کَاتِبٌ = "ek likhne wala" (singular). Row 3 ka کَاتِبُوْنَ = "kayi likhne wale" (plural). **Same root, different morphological additions = different wazn = different form.**

**Row 6 — عَالِمَانِ → فَاعِلَانِ:**
- Root: ع، ل، م (know-related). Extras: ا (after ع) + ا (after م) + ن.
- Wazn فَاعِلَانِ — yeh **dual** (تثنیہ) form hai.
- **Builder observation (meri taraf se):** عَالِم singular hota hai "ek jaanne wala". Dual ke liye **ا + ن** add ho jaata hai = "do jaanne wale". Toh **pehla ا = ism faail ki علامت** (Slide 23 ka statement) + **doosra ا + ن = علامتِ تثنیہ** (dual marker, Sarf detail aage). Yeh Sub Topic 1.4 mein **pehli baar تثنیہ** ka wazn formally dikhaya gaya — Sub Topics aage tafseel denge.

**Row 7 — شَرِیْفٌ → فَعِیْلٌ:**
- Root: ش، ر، ف (honor-related). Extra: ی.
- Wazn فَعِیْلٌ — same wazn as Row 4 (کَرِیْمٌ).
- **Builder observation (meri taraf se):** Cross-root same-wazn — کَرِیْمٌ aur شَرِیْفٌ dono **فَعِیْلٌ** wazn par hain. Yeh Slide 19 ka **cross-root pattern recognition** concept ka practical demonstration hai (sifat-e-mushabbaha qism).

##### Sub Topic 1.4 ka practical application (builder gloss; book ne yeh tabseera nahi diya)

- Slide 22 mein **method** sikhayi gayi (مثال: ضَرْبٌ → فَعْلٌ).
- Slide 23 mein **terminology** + **علامات** ka concept (عَالِمٌ → فَاعِلٌ; ا = ism faail ki علامت).
- Slide 24 ka table **method ko 7 alag examples par apply karke** dikhata hai. Yahi **practical training** hai.
- **Sub Topic 1.3** ke builder gloss observations (Slides 18-19 "Pattern observation" tables) ab Sub Topic 1.4 ke saath **PDF-attested ho gaye** — فَاعِلٌ, فَعِیْلٌ formally dikha diye gaye Slide 24 mein.

**Status:** PRE-BUILD (2026-05-29) + validator Round 1 (1 HIGH + 3 MED) corrected — Slide 24 ka 7-row table + column headers PDF-verbatim copy kiye. Following items Nazir physical book se verify kare:
- (a) Column 3 header **حروف اصلیہ** (ہ-ending) — validator Round 1 PDF re-read se confirmed; physical book par bhi confirm kare;
- (b) Row 6 (عَالِمَانِ) extras column "ا، ا، ن" — validator Round 1 confirmed (3 extras in order: pehla ا after ع, doosra ا after م, phir ن with kasrah);
- (c) All 7 mauzun + wazn columns ki harakaat validator Round 1 confirmed PDF-verbatim;
- (d) Builder commentary blocks (Row-by-row analysis + Sub Topic 1.4 ka practical application) sab `(meri taraf se)` markers ke saath fenced — book ka khaalis content (table + title) se alag. Validator Round 1 ne flag kiya ke individual mauzun words ki English semantic glosses ("worship-related", "honor-related", etc.) memory-fill hain — yeh general etymological hints hain (canonical Arabic roots se), specific PDF-attestation nahi.

---

#### Slide 25 — اسم کے اوزان — 3 / 4 / 5 harfi taqseem (PDF p-026)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.4 | حروف اصلی کی پہچان | Slide 25 | اصطلاحات | Topic 1.0**
- Red title: **اسم کے اوزان**
- 3-section side-by-side table (RTL): **اسم تین حرفی | اسم چار حرفی | اسم پانچ حرفی**
- Har section mein 2 sub-columns: **مثال | وزن** (RTL: مثال right, وزن left within section)
- 2 data rows per section (total 6 examples)
- Niche ek **paragraph rule** + **نوٹ** with forward-ref

##### 3 sub-tables (PDF verbatim)

###### اسم تین حرفی (3-letter ism)

| مثال | وزن |
|---|---|
| **نَصْرٌ** | **فَعْلٌ** |
| **ضَرْبٌ** | **فَعْلٌ** |

###### اسم چار حرفی (4-letter ism)

| مثال | وزن |
|---|---|
| **بَرْزَخٌ** | **فَعْلَلٌ** |
| **جَعْفَرٌ** | **فَعْلَلٌ** |

###### اسم پانچ حرفی (5-letter ism)

| مثال | وزن |
|---|---|
| **جَحْمَرَشٌ** | **فَعْلَلِلٌ** |
| **سَفَرْجَلٌ** | **فَعْلَلِلٌ** |

##### Paragraph rule (PDF verbatim)

> **"اسم کے اوزان کثیر تعداد میں ہیں، خواہ اسم جامد، مصدر یا مشتق ہو۔ اسم جامد کے اوزان تین، چار اور پانچ حرفی ہوتے ہیں لیکن اسم مصدر اور اسم مشتق کے اوزان صرف تین اور چار حرفی ہوتے ہیں۔"**

**Roman tarjuma + breakdown:**
- *Ism ke اوزان bohat ziyada hain* — chahe **اسم جامد**, **اسم مصدر**, ya **اسم مشتق** ho (yeh Sub Topic 1.3 Slide 16 ki 3 ism qismein hain).
- *Ism jamid* ke اوزان **3, 4, ya 5 harfi** ho sakte (yaani اسم جامد ki sub-classification 3/4/5-letter mein).
- *Ism masdar aur Ism mushtaq* ke اوزان **sirf 3 ya 4 harfi** hote (yaani inka 5-letter version nahi hota).

##### نوٹ (PDF verbatim — forward-ref note)

> **"نوٹ: اسم کے اوزان کی مکمل تفصیل معلم الابواب والخاصیات میں پڑھیں گے ان شاء اللہ۔"**

**Roman:** *Ism ke اوزان ki **مکمل تفصیل** future kitab **"معلم الابواب والخاصیات"** mein parhenge insha'allah.* — Yaani aaj jo sikhaaya gaya woh **introduction** hai, full taxonomy aage hai. **Book ka apna self-flag — abhi memory-fill nahi karna.**

##### Cross-link to Sub Topic 1.3 (builder gloss; book ne yeh explicit comparison nahi diya)

- **Slide 16** (Sub Topic 1.3) mein Ism ki 3 qismein PDF-attested hui thi: **Jamid** + **Masdar** + **Mushtaq**.
- Ab Slide 25 ne in 3 qismon ki **wazn-based sub-classification** kar di:
  - **Jamid** → 3, 4, ya 5 harfi (sab se zyada variety)
  - **Masdar** → sirf 3 ya 4 harfi
  - **Mushtaq** → sirf 3 ya 4 harfi
- **Builder observation (meri taraf se):** Yeh **kyun**? Probable wajah — Jamid mein non-derived loanwords aur foreign-origin nouns shamil hote (جَحْمَرَش، سَفَرْجَل = unusual native + loanwords) — yahi 5-harfi forms produce karte. Masdar aur Mushtaq derivational system ke andar hain — uniform 3/4-harfi rules. **Book ne yeh tafseel "معلم الابواب والخاصیات" tak defer ki — aaj sirf naam-anchor mil gaya.**

##### 6 examples ka inferred ism-qism (builder gloss — book ne categorization explicit nahi ki)

> **⚠️ Memory-fill banner:** Following ism-qism classifications builder gloss hain — PDF Slide 25 NE 6 examples ki جامد/مصدر/مشتق classification explicit NAHI ki. Sirf wazn + 3/4/5 harfi taqseem di hai. Builder ne **PDF Slide 25 ke paragraph rule** (Jamid 3/4/5; Masdar+Mushtaq 3/4) + **Slide 16 ki Ism qismein definitions** se inference ki hai. **Individual word meanings** (English translations, etymological hints) bilkul PDF par nahi hain — woh canonical Arabic dictionary knowledge se hain; Nazir physical book + Shaykh se confirm kare jab in alfaaz ka istemaal future Sub Topics mein ho.

| مثال | Wazn | Inferred ism qism (builder gloss) |
|---|---|---|
| **نَصْرٌ** | فَعْلٌ | Likely اسم مصدر — Slide 16 ne نَصْرًا masdar example diya tha (same lexeme) |
| **ضَرْبٌ** | فَعْلٌ | Likely اسم مصدر — Slide 16 ne ضَرْبًا masdar example diya tha (same lexeme) |
| **بَرْزَخٌ** | فَعْلَلٌ | Likely اسم جامد — Slide 25 rule: 4-harfi sirf Jamid ya Mushtaq ho sakta; Mushtaq pattern fit nahi |
| **جَعْفَرٌ** | فَعْلَلٌ | Likely اسم جامد — same reasoning as بَرْزَخٌ |
| **جَحْمَرَشٌ** | فَعْلَلِلٌ | **PDF rule-confirmed**: 5-harfi sirf اسم جامد ho sakta (Slide 25 paragraph) |
| **سَفَرْجَلٌ** | فَعْلَلِلٌ | **PDF rule-confirmed**: 5-harfi sirf اسم جامد ho sakta (Slide 25 paragraph) |

**Status:** PRE-BUILD (2026-05-29) — Slide 25 ka content (title + 3 sub-tables + paragraph + Note) PDF-verbatim. Following items Nazir physical book se verify kare:
- (a) 3 sub-table headers — exact spellings of **اسم تین حرفی** / **اسم چار حرفی** / **اسم پانچ حرفی**;
- (b) Sub-column header order within each section — **مثال** vs **وزن** ki positioning;
- (c) 6 examples ki harakaat (specially جَحْمَرَش aur سَفَرْجَل — rare 5-letter words);
- (d) Paragraph aur Note ka exact wording;
- (e) Forward-ref kitab name **"معلم الابواب والخاصیات"** ki spelling — small font.
- (f) Builder gloss blocks (Cross-link + Categorical breakdown table) sab `(meri taraf se)` markers ke saath fenced.

---

#### Slide 26 — Exercise bar `[?]` (PDF p-026) — Sub Topic 1.4 ka khatima

**PDF par jo hai:**
- Header bar (compressed): **متعلقہ سب ٹاپک کے سوالات | Slide 26 | `[?]` میں حل کریں**
  - Slides 5 + 14 + 20 jaisa hi exercise bar pattern (`[?]` workbook name slot "میں حل کریں" ke saath)
  - Bar layout: "متعلقہ سب ٹاپک کے سوالات" (right) | "Slide 26" (middle) | "`[?]` میں حل کریں" (left)
- Body koi nahi — sirf bar header

**Roman:** Slides 5/14/20 ki tarah, Slide 26 bhi **Sub Topic 1.4 ka khatima** suggest karta hai — student ko متعلقہ workbook mein Sub Topic 1.4 ke sawalat hal karne hain. Body content NAHI.

**Yeh confirm karta hai:** **Sub Topic 1.4 MUKAMMAL ho gaya** — Slides 21-26 ka complete arc:
- **Slide 21** = Sub Topic 1.4 ka cover
- **Slides 22-23** = wazn ki tareef + method + terminology (Mauzun/Meezan/Wazn + Fa/Ain/Lam Kalimah)
- **Slide 24** = wazn-extraction method ki **7 examples** par application
- **Slide 25** = **اسم ke اوزان** ki taqseem (3/4/5 harfi) + Ism qismein ke saath connection
- **Slide 26** = exercise/khatima bar

**Status:** PDF-VERIFIED 2026-05-29 — Slides 5/14/20 parallel structure cross-verified ("متعلقہ سب ٹاپک کے سوالات" pattern); sirf workbook name `[?]` standalone — Nazir physical book se fill kare.

---

### Sub Topic 1.5 — فعل کے چھ ابواب (Fi'l ke 6 abwaab — **major Sarf milestone**)

> **Yeh classical Sarf ki ASAL bunyaad hai.** Saara conjugation system (har baab ki paradigms, har baab ke saare 14-sigha tables) is concept par khari hai: **عین کلمہ ki harakah ke اعتبار se فعل ke 6 ابواب**. Sub Topic 1.5 ka aaghaaz p-027 par hota hai — wazn-extraction method **فعل par bhi apply** karna + ماضی aur مضارع ke 3+3 waznein dekh kar 6 used pairings (= 6 ابواب) identify karna.

#### Slide 27 — Sub Topic 1.5 cover (PDF p-027)

**PDF par jo hai:**
- Header bar (RTL reading order): **Sub Topic 1.5 | فعل کے چھ ابواب | Slide 27 | اصطلاحات | Topic 1.0**
- Body koi visible content nahi — sirf cover bar (Slides 21/15/6/2 jaisa cover pattern)

**Roman:** Slide 27 ek **cover/transition bar** hai — Sub Topic 1.5 ka aaghaaz declare karta hai. Title: **فعل کے چھ ابواب** ("fi'l ke 6 chapters/categories"). Content Slide 28 se shuru hota hai. **Note**: Slide 1 row 1.5 par title `[?]` tha tentatively "وزن کے اعتبار سے فعل کا باب" — actual PDF title yahaan "فعل کے چھ ابواب" hai (Slide 1 row 1.5 ka resolve hua maybe — Nazir physical book confirm kare).

**Status:** PDF-VERIFIED 2026-05-29 — Slide 27 par body content NAHI (cover bar pattern). Title بار-text se verify kiya.

---

#### Slide 28 — افعال کے وزن نکالنے کا طریقہ + فعل ماضی/مضارع کے اوزان (PDF p-027)

**PDF par jo hai:**
- Header bar (compressed/4-cell variant — slide-specific sub-heading): **Sub Topic 1.5 | Slide 28 | وزن کے اعتبار سے فعل کے چھ ابواب** (standard اصطلاحات + Topic 1.0 cells replaced — Slide 22 jaisa compressed pattern)
- Red title 1: **افعال کے وزن نکالنے کا طریقہ**
- Method paragraph
- Red title 2: **فعل ماضی کے اوزان:**
- 3 side-by-side sub-tables for ماضی (each with مَوْزون | وزن sub-columns; total 6 examples, 3 distinct waznein)
- Red title 3: **فعل مضارع کے اوزان:**
- 3 side-by-side sub-tables for مضارع (each with مَوْزون | وزن sub-columns; total 6 examples, 3 distinct waznein)

##### Method paragraph (PDF verbatim)

> **"فعل کا وزن نکالنے کا وہی طریقہ ہے جو اسم کا وزن نکالنے کا طریقہ ہے، یعنی موزون کی شکل دیکھ کر میزان کو منتخب کریں اور جو حرکات و سکنات موزون پر ہیں، وہی میزان پر لگا دیں۔"**

**Roman:** **Fi'l ka wazn nikalne ka tareeqa wahi hai jo اسم ka tha** (Sub Topic 1.4 Slide 22 mein dekha tha). Yaani:
1. Mauzun (fi'l) ki shakal dekho.
2. Meezan (ف، ع، ل) select karo same length ka.
3. Mauzun par jo harakaat aur sukoonaat hain, **wohi** meezan par lagao.

**Builder observation (meri taraf se — Sub Topic 1.4 cross-link):** Sub Topic 1.4 ne method اسم par sikhayi (Slide 22 paragraph: "اسماء کے وزن نکالنے کا طریقہ"). Ab Sub Topic 1.5 ne **wahi method فعل par bhi apply** kar di — **universal wazn-extraction algorithm** confirmed. Fi'l aur Ism dono ke liye **same method**.

##### فعل ماضی کے اوزان — 3 sub-tables (PDF verbatim, RTL order)

PDF par 3 sub-tables side-by-side hain. Har ek sub-table mein 2 rows × 2 columns (مَوْزون | وزن). Total 6 ماضی examples, **3 distinct waznein** mein distributed.

###### Sub-table 1 (rightmost — PDF visual position 1)

| موزون | وزن |
|---|---|
| **ضَرَبَ** | **فَعَلَ** |
| **حَسِبَ** | **فَعِلَ** |

###### Sub-table 2 (middle — PDF visual position 2)

| موزون | وزن |
|---|---|
| **نَصَرَ** | **فَعَلَ** |
| **سَمِعَ** | **فَعِلَ** |

###### Sub-table 3 (leftmost — PDF visual position 3)

| موزون | وزن |
|---|---|
| **فَتَحَ** | **فَعَلَ** |
| **شَرُفَ** | **فَعُلَ** |

##### فعل مضارع کے اوزان — 3 sub-tables (PDF verbatim, RTL order)

###### Sub-table 1 (rightmost)

| موزون | وزن |
|---|---|
| **یَضْرِبُ** | **یَفْعِلُ** |
| **یَحْسِبُ** | **یَفْعِلُ** |

###### Sub-table 2 (middle)

| موزون | وزن |
|---|---|
| **یَنْصُرُ** | **یَفْعُلُ** |
| **یَسْمَعُ** | **یَفْعَلُ** |

###### Sub-table 3 (leftmost)

| موزون | وزن |
|---|---|
| **یَفْتَحُ** | **یَفْعَلُ** |
| **یَشْرُفُ** | **یَفْعُلُ** |

##### Slide 28 ka structural decoding (builder gloss — book ne is overview ko explicit nahi diya, Slide 29 mein concept zaroor diya hai)

**3 distinct ماضی waznein** (عین کلمہ ki harakah ke اعتبار se):
- **فَعَلَ** — عین par **fatha** (e.g., ضَرَبَ, نَصَرَ, فَتَحَ — 3 examples)
- **فَعِلَ** — عین par **kasrah** (e.g., حَسِبَ, سَمِعَ — 2 examples)
- **فَعُلَ** — عین par **damma** (e.g., شَرُفَ — 1 example)

**3 distinct مضارع waznein** (عین کلمہ ki harakah ke اعتبار se):
- **یَفْعَلُ** — عین par **fatha** (e.g., یَفْتَحُ, یَسْمَعُ — 2 examples)
- **یَفْعِلُ** — عین par **kasrah** (e.g., یَضْرِبُ, یَحْسِبُ — 2 examples)
- **یَفْعُلُ** — عین par **damma** (e.g., یَنْصُرُ, یَشْرُفُ — 2 examples)

**6 ماضی-مضارع pairings (PDF examples ko jod kar)** — yeh **6 ابواب** hain jin ki taraf Slide 29 ka اشارہ hai:

| # | Mauzun pair (ماضی + مضارع) | Wazn pair |
|---|---|---|
| 1 | ضَرَبَ + یَضْرِبُ | فَعَلَ + یَفْعِلُ |
| 2 | نَصَرَ + یَنْصُرُ | فَعَلَ + یَفْعُلُ |
| 3 | فَتَحَ + یَفْتَحُ | فَعَلَ + یَفْعَلُ |
| 4 | حَسِبَ + یَحْسِبُ | فَعِلَ + یَفْعِلُ |
| 5 | سَمِعَ + یَسْمَعُ | فَعِلَ + یَفْعَلُ |
| 6 | شَرُفَ + یَشْرُفُ | فَعُلَ + یَفْعُلُ |

(Yeh 6-pairings table **builder gloss** hai — book ne Slide 28 par sirf 3 sub-tables alag-alag dikhai hain ماضی aur مضارع ke liye. Pairing logic Slide 29 paragraph se derive hoti hai *"ماضی اور مضارع کو جمع کر کے پڑھیں"*. Saath-saath sub-tables par ek-doosre ka mapping (sub-table 1 ka ماضی Row 1 + sub-table 1 ka مضارع Row 1 = first pairing) implicit hai.)

**Status:** PRE-BUILD (2026-05-29) — Slide 28 ka content (method paragraph + 2 main tables ke 12 mauzun-wazn pairs) PDF-verbatim. Nazir physical book se verify kare:
- (a) Method paragraph ka exact wording — long Urdu prose;
- (b) Sub-table 1 (rightmost) ki 2 mazi pairs (ضَرَبَ/فَعَلَ، حَسِبَ/فَعِلَ) ki harakaat;
- (c) Sub-table 1 ki 2 mudaari' pairs (یَضْرِبُ/یَفْعِلُ، یَحْسِبُ/یَفْعِلُ) ki harakaat;
- (d) Sub-table 3 (leftmost) Row 2 mazi: **شَرُفَ → فَعُلَ** — 6th بَاب ka example (rare wazn فَعُلَ);
- (e) Sub-table 3 (leftmost) Row 2 mudaari': **یَشْرُفُ → یَفْعُلُ** — corresponding 6th بَاب mudaari'.
- (f) Builder commentary blocks (Structural decoding + 6-pairings table) `(builder gloss)` markers ke saath fenced.

---

#### Slide 29 — عین کلمہ پر مختلف حرکات کی وجہ سے بننے والے ابواب (PDF p-027)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.5 | فعل کے چھ ابواب | Slide 29 | اصطلاحات | Topic 1.0**
- Red title: **عین کلمہ پر مختلف حرکات کی وجہ سے بننے والے ابواب**
- Paragraph 1 (concept intro)
- Sub-heading 1 + 3 cells (ماضی waznein)
- Sub-heading 2 + 3 cells (مضارع waznein)
- Paragraph 2 (the 9 → 6 rule)

##### Paragraph 1 (PDF verbatim — concept intro)

> **"فعل ماضی اور مضارع کے اوزان کو آپس میں ملانے سے مختلف باب بنتے ہیں یعنی اگر فعل ماضی اور فعل مضارع کو جمع کر کے پڑھیں تو عین کلمہ کی مختلف حرکت کی وجہ سے جو اوزان مستعمل ہیں، وہ چھ ہیں اور ان کو علم الصرف کی اصطلاح میں چھ ابواب کہتے ہیں۔ آئیے! چھ ابواب کی وضاحت پڑھتے ہیں:"**

**Roman tarjuma + breakdown:**
- *Fi'l ماضی aur مضارع ke اوزان ko **آپس mein milane** se mukhtalif **باب** bante hain.* — Yaani اگر mazi-mudaari' ek-saath padhe jayein, to **عین کلمہ ki mukhtalif harakah** ki wajah se jo **مستعمل** (used in practice) اوزان hain woh **چھ** hain.
- *In ko **علم الصرف ki اصطلاح** mein **"چھ ابواب"** kehte hain.* — Yeh **بَاب** ek bilkul naya istilahi term hai is page par formally introduce hua.
- *"آئیے! چھ ابواب ki **وضاحت** padhte hain"* — book aage in 6 ابواب ki tafseel dene wali hai (subsequent pages).

##### ماضی wazn 3 طرح (PDF verbatim)

> **"ماضی کا وزن تین طرح استعمال ہوا ہے، جیسے:"**

3 cells (PDF visible order, RTL):

| فَعَلَ | فَعِلَ | فَعُلَ |
|---|---|---|

##### مضارع wazn 3 طرح (PDF verbatim)

> **"اسی طرح مضارع کا وزن بھی تین طرح استعمال ہوا ہے، جیسے:"**

3 cells (PDF visible order, RTL):

| یَفْعَلُ | یَفْعِلُ | یَفْعُلُ |
|---|---|---|

##### Paragraph 2 — 9 → 6 rule (PDF verbatim — MASTER RULE)

> **"ماضی اور مضارع میں صرف عین کلمہ کی حرکت تبدیل ہو رہی ہے، جب ماضی اور مضارع کا پہلا صیغہ ملا کر بولا جائے تو عین کلمہ مختلف ہونے کے باعث نو (سیٹ) باب بننے چاہیئیں مگر صرف چھ مستعمل ہیں، ان کو چھ باب کہتے ہیں۔"**

**Roman + structural decoding:**
- *Mazi aur mudaari' mein **sirf عین کلمہ ki harakah tabdeel** ho rahi hai* — yaani فا اور لام کلمہ same hain, change sirf middle letter (ع) par hai.
- *Jab ماضی + مضارع ka **پہلا صیغہ** mila kar bola jaye* — yeh pehli baar **صیغہ** (PDF-attested) lafz appear hua. **پہلا صیغہ** ka exact tafseel (kaunsi shakal hai morphologically) PDF p-027 par NAHI di — future Sub Topics mein expected. PDF ne sirf yeh kaha ke "pehla sayghah ko mila kar bola jaye" — yaani mazi + mudaari' ke "pehle form" ka combination.
- *عین کلمہ mukhtalif hone ke baais **نَو (سیٹ) باب** banne chahiyein* — yaani **3 ماضی waznein × 3 مضارع waznein = 9 logical possibilities (سیٹ)**.
- *Magar sirf **چھ مستعمل** hain, in ko **چھ باب** kehte hain* — sirf 6 actually use hote Arabic mein.

**Mohim baat:** **Yeh classical Sarf ka master decoding hai.** Saara conjugation system 6 ابواب par khara hai. **3 missing pairings** (jo logically possible the magar مستعمل nahi):
- (Yeh 3 missing pairings PDF par **explicitly nahi** likhe hain — book sirf "6 مستعمل" kehti hai. Future pages mein possibly tafseel ho.)

##### Cross-link to Slide 28 (builder gloss; book ne yeh explicit comparison nahi diya)

- **Slide 28** mein 6 ماضی examples + 6 مضارع examples dikhaye gaye, kuch corresponding pairings ke saath.
- **Slide 29** ne theoretical framework diya: **3×3 = 9 logical, 6 مستعمل**.
- **Connecting Slide 28's 6 pairings to Slide 29's "چھ ابواب":** Slide 28 par jo 6 mauzun pairs the (ضَرَبَ+یَضْرِبُ, نَصَرَ+یَنْصُرُ, فَتَحَ+یَفْتَحُ, حَسِبَ+یَحْسِبُ, سَمِعَ+یَسْمَعُ, شَرُفَ+یَشْرُفُ), **woh hi 6 ابواب hain jin ka Slide 29 zikr karta hai** — book ne examples pehle diye (Slide 28), conceptual frame baad mein (Slide 29).
- **6 ابواب ke canonical Sarf naam** (e.g., "باب نَصَرَ", "باب ضَرَبَ", etc.) **PDF p-027 par formally NAHI** diye gaye — future pages (p-028+) mein expected. **Builder memory-fill NAHI karta** — sirf jo examples PDF par hain woh quote kiye.

**Status:** PRE-BUILD (2026-05-29) — Slide 29 ka content (long Urdu paragraphs + 6 wazn cells) PDF-verbatim. Nazir physical book se verify kare:
- (a) Paragraph 1 ka exact wording (long Urdu — letter-by-letter);
- (b) Mazi 3 cells (فَعَلَ، فَعِلَ، فَعُلَ) ki harakaat + PDF visible order (rightmost to leftmost);
- (c) Mudaari' 3 cells (یَفْعَلُ، یَفْعِلُ، یَفْعُلُ) ki harakaat + order;
- (d) Paragraph 2 ka exact wording specially **"نَو (سیٹ) باب"** mein "سیٹ" lafz — yeh asal Urdu mein hai ya English borrowing — Nazir verify kare. Aur **"صیغہ"** PDF-attested confirmation;
- (e) Builder commentary blocks `(builder gloss)` markers ke saath fenced.

---

#### Slide 30 — فَعَلَ / فَعِلَ / فَعُلَ se 3 + 2 + 1 = 6 سیٹ ka algebraic derivation (PDF p-028)

**PDF par jo hai:**
- Header bar (RTL reading order): **Sub Topic 1.5 | فعل کے چھ ابواب | Slide 30 | اصطلاحات | Topic 1.0**
- **3 paragraphs + 3 sub-tables** structure — har paragraph ek ماضی wazn ko unpack karta hai aur usse bante hue مضارع waznein ginata hai (پہلا paragraph 3 waznein, doosra 2, teesra 1)
- Closing line — explicit **3+2+1 = 6** master rule: *"یہ کل چھ سیٹ ہیں، ان کو چھ باب کہتے ہیں۔"*

---

**Paragraph 1 (PDF verbatim) — فَعَلَ se 3 ابواب:**

> اب فَعَلَ فعل ماضی سے مضارع کے تین وزن ہیں: (۱) عین کلمہ کے فتح کے ساتھ، جیسے: فَعَلَ یَفْعَلُ (۲) عین کلمہ کے کسرہ کے ساتھ، جیسے: فَعَلَ یَفْعِلُ (۳) عین کلمہ کے ضمہ کے ساتھ، جیسے: فَعَلَ یَفْعُلُ۔ لہذا فَعَلَ فعل ماضی سے مضارع کے تین سیٹ بنتے ہیں، ان کو تین باب کہتے ہیں۔

**Roman gloss:** فَعَلَ (ماضی) se مضارع ke 3 waznein bante hain — عین par fatha, kasrah, damma teeno harakaat possible. Yeh **3 سیٹ = 3 ابواب** hain.

**Table 1 (PDF — 3 cells with RTL numbering ۱-۲-۳):**

| # | Wazn pair (ماضی + مضارع) | عین par harakah |
|---|---|---|
| (۱) | فَعَلَ یَفْعَلُ | fatha (zabar) |
| (۲) | فَعَلَ یَفْعِلُ | kasrah (zer) |
| (۳) | فَعَلَ یَفْعُلُ | damma (pesh) |

---

**Paragraph 2 (PDF verbatim) — فَعِلَ se 2 ابواب:**

> اسی طرح فَعِلَ فعل ماضی سے مضارع کے دو وزن ہیں: (۱) عین کلمہ کے فتح کے ساتھ، جیسے: فَعِلَ یَفْعَلُ (۲) عین کلمہ کے کسرہ کے ساتھ، جیسے: فَعِلَ یَفْعِلُ۔ لہذا فَعِلَ فعل ماضی سے مضارع کے دو سیٹ بنتے ہیں، ان کو دو باب کہتے ہیں۔

**Roman gloss:** فَعِلَ (ماضی) se مضارع ke 2 waznein — sirf عین par fatha aur kasrah possible. **Damma wala pairing** (فَعِلَ + یَفْعُلُ) **missing hai** — book ne is paragraph mein explicit nahi kaha, structurally clear hai. Yeh **2 سیٹ = 2 ابواب**.

**Table 2 (PDF — 2 cells with RTL numbering ۴-۵):**

| # | Wazn pair (ماضی + مضارع) | عین par harakah |
|---|---|---|
| (۴) | فَعِلَ یَفْعَلُ | fatha |
| (۵) | فَعِلَ یَفْعِلُ | kasrah |

---

**Paragraph 3 (PDF verbatim) — فَعُلَ se 1 باب:**

> اسی طرح فَعُلَ فعل ماضی سے مضارع کا ایک وزن ہے ضمہ کے ساتھ، یعنی عین کلمہ کے ضمہ کے ساتھ، جیسے: فَعُلَ یَفْعُلُ۔ لہذا فَعُلَ فعل ماضی سے مضارع کا ایک سیٹ ہے، اس کو ایک باب کہتے ہیں۔

**Roman gloss:** فَعُلَ (ماضی) se مضارع ka sirf 1 wazn — sirf عین par damma. **Fatha aur kasrah wale pairings dono missing** (فَعُلَ + یَفْعَلُ aur فَعُلَ + یَفْعِلُ). Yeh **1 سیٹ = 1 باب**.

**Table 3 (PDF — 1 cell, numbered ۶):**

| # | Wazn pair (ماضی + مضارع) | عین par harakah |
|---|---|---|
| (۶) | فَعُلَ یَفْعُلُ | damma |

---

**Closing line (PDF verbatim — Slide 30 ka master rule:**

> یہ کل چھ سیٹ ہیں، ان کو چھ باب کہتے ہیں۔

**Roman:** "Yeh kul **6 سیٹ** hain, in ko **چھ باب** kehte hain" — yaani **3 + 2 + 1 = 6** ka explicit algebraic master rule.

##### Slide 30 ka core insight (book-derivable structural commentary; partially builder gloss)

Slide 30 ne **kyun sirf 6 ابواب banti hain, 9 nahi** ka structural answer dia — Slide 29 ke "9 → 6" master rule ka algebraic proof:

| ماضی wazn | مضارع possibilities (book ne diye) | Pairings count |
|---|---|---|
| **فَعَلَ** | یَفْعَلُ، یَفْعِلُ، یَفْعُلُ (sab 3 harakaat) | **3** |
| **فَعِلَ** | یَفْعَلُ، یَفْعِلُ (sirf 2; damma missing) | **2** |
| **فَعُلَ** | یَفْعُلُ (sirf 1; fatha aur kasrah dono missing) | **1** |
| | **Total** | **3 + 2 + 1 = 6** ✓ |

**Slide 30 se structurally inferable 3 missing pairings** (builder gloss — book ne explicitly list NAHI kiya is page par, structurally derive hota hai paragraphs 2 aur 3 ke "missing harakaat" se):

1. فَعِلَ + یَفْعُلُ (ماضی kasrah → مضارع damma)
2. فَعُلَ + یَفْعَلُ (ماضی damma → مضارع fatha)
3. فَعُلَ + یَفْعِلُ (ماضی damma → مضارع kasrah)

(Yeh ٹھیک **wahi 3 missing pairings** hain jo Slide 29 paragraph 2 ke "9 - 6 = 3 logical-but-not-musta'mal" se predict hote the. Slide 30 ne ab unko derivationally identify kar diya — Slide 29 ka rule + Slide 30 ki derivation = complete picture. **Yeh enumeration builder gloss hai — book ne 3 missing pairings ko named list mein nahi diya, magar Slide 30 ke 3-2-1 structure se directly infer hota hai.**)

**Status:** PRE-BUILD (2026-05-30) — Slide 30 ka content (3 paragraphs + 3 tables + closing line) PDF-verbatim. Nazir physical book se verify kare:
- (a) 3 paragraphs ka exact wording (long Urdu — letter-by-letter spelling; specifically "کسرہ" vs "کسرَۃ" vs "کسرا" ki consistency, aur "لہذا" vs "لہٰذا")
- (b) 3 tables ke wazn cells ki harakaat — specifically فَعَلَ ke teeno letters par fatha, فَعِلَ ka فا fatha + عین kasrah + لام fatha, فَعُلَ ka فا fatha + عین damma + لام fatha; aur مضارع ke یَفْعَلُ/یَفْعِلُ/یَفْعُلُ ka یا par fatha, فا par sukoon, عین par specific harakah, لام par damma
- (c) Tables ka **RTL numbering** order: PDF mein cells RTL hain — sab se daahini taraf ۱ aur sab se baayin taraf ۳ (Table 1), ۴/۵ (Table 2), ۶ (Table 3). Yeh order verify
- (d) Closing line ki exact wording — "یہ کل چھ سیٹ ہیں" vs "یہ کل چھ سیٹس ہیں" (Urdu vs Urdu-plural style)
- (e) "3 missing pairings" enumeration **builder gloss hai** — Slide 30 ke explicit paragraph text mein 3 specific missing pairings ko **name nahi kiya**, sirf "do/aik" se imply hua. Yeh builder structural inference hai (Slide 29 ke 9→6 rule + Slide 30 ke 3-2-1 derivation se).

---

#### Slide 31 — مذکورہ چھ ابواب کے اوزان اور مثالیں — **CANONICAL 6 ابواب formally PDF-introduced** (PDF p-028)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.5 | فعل کے چھ ابواب | Slide 31 | اصطلاحات | Topic 1.0**
- **Slide title (red color)**: **مذکورہ چھ (۶) ابواب کے اوزان اور مثالیں**
- **2×3 table (6 cells total)** — har cell mein 2 lines: wazn-pair (upar) + canonical misaal (neeche). RTL numbering: top row ۱-۲-۳, bottom row ۴-۵-۶
- **نوٹ at bottom**: alternate misaalein doosri kitabon mein

**Slide 31 = milestone slide** — yahan 6 ابواب ke **canonical Sarf naam** (ضَرَبَ، فَتَحَ، نَصَرَ، حَسِبَ، سَمِعَ، شَرُفَ) **pehli baar PDF par formally introduce** hue. Sub Topic 1.5 ka core reference point yeh slide hai.

---

**Slide title (PDF verbatim):**

> مذکورہ چھ (۶) ابواب کے اوزان اور مثالیں

**Roman:** "Mazkurah (i.e., upar batae gaye) chhe (۶) abwaab ke **awzaan** (waznein) **aur misaalein**" — yaani Slide 30 mein jin 6 سیٹ ki bath hui, un ki **waznein + naamzad misaalein**.

---

**Slide 31 canonical 2×3 table (PDF verbatim — yahi 6 ابواب ke canonical naam hain):**

| # | Wazn pair | Canonical misaal (PDF — Slide 31) |
|---|---|---|
| **(۱)** | فَعَلَ یَفْعِلُ | **ضَرَبَ یَضْرِبُ** |
| **(۲)** | فَعَلَ یَفْعَلُ | **فَتَحَ یَفْتَحُ** |
| **(۳)** | فَعَلَ یَفْعُلُ | **نَصَرَ یَنْصُرُ** |
| **(۴)** | فَعِلَ یَفْعِلُ | **حَسِبَ یَحْسِبُ** |
| **(۵)** | فَعِلَ یَفْعَلُ | **سَمِعَ یَسْمَعُ** |
| **(۶)** | فَعُلَ یَفْعُلُ | **شَرُفَ یَشْرُفُ** |

**Canonical baab naam (PDF Slide 31 se):**
1. **باب ضَرَبَ** — wazn فَعَلَ یَفْعِلُ (mazi fatha → mudaari' kasrah)
2. **باب فَتَحَ** — wazn فَعَلَ یَفْعَلُ (mazi fatha → mudaari' fatha)
3. **باب نَصَرَ** — wazn فَعَلَ یَفْعُلُ (mazi fatha → mudaari' damma)
4. **باب حَسِبَ** — wazn فَعِلَ یَفْعِلُ (mazi kasrah → mudaari' kasrah)
5. **باب سَمِعَ** — wazn فَعِلَ یَفْعَلُ (mazi kasrah → mudaari' fatha)
6. **باب شَرُفَ** — wazn فَعُلَ یَفْعُلُ (mazi damma → mudaari' damma)

(NOTE: "باب ضَرَبَ" style naming convention book ne is page par strictly establish nahi kiya — Slide 31 par cells mein sirf "wazn-pair + misaal" likha hai, "باب X" formal label nahi tha. Lekin classical Sarf ki rasm hai ke baabs ko canonical misaal ke naam se pukara jata hai. Yeh naming pattern future Sub Topics mein expected — builder gloss as forward-pointer.)

---

##### نوٹ — alternate misaalein doosri kitabon mein (PDF verbatim — Slide 31 footer)

> نوٹ: مذکورہ ابواب کیلیے بعض کتب میں اس سے کچھ مختلف الفاظ مستعمل ہیں، یعنی فَتَحَ یَفْتَحُ کی جگہ مَنَعَ یَمْنَعُ مستعمل ہے، نَصَرَ یَنْصُرُ کی جگہ دَخَلَ یَدْخُلُ اور طَلَبَ یَطْلُبُ مستعمل ہیں، سَمِعَ یَسْمَعُ کی جگہ عَلِمَ یَعْلَمُ مستعمل ہے اور شَرُفَ یَشْرُفُ کی جگہ کَرُمَ یَکْرُمُ مستعمل ہے۔

**Roman:** "Mazkurah ابواب ke liye **بعض کتب** (some other Sarf books) mein in se kuch **مختلف الفاظ** (different misaalein) **مستعمل** (in use) hain..."

**Alternate vocabulary mapping (PDF verbatim — Slide 31 Note se table-form mein):**

| باب # | Primary misaal (yeh kitab) | Alternate misaal (doosri kitabon mein — PDF Note se) |
|---|---|---|
| (۱) | ضَرَبَ یَضْرِبُ | *(yahi naam — Note mein alternate mention NAHI hua)* |
| (۲) | فَتَحَ یَفْتَحُ | **مَنَعَ یَمْنَعُ** |
| (۳) | نَصَرَ یَنْصُرُ | **دَخَلَ یَدْخُلُ** *aur* **طَلَبَ یَطْلُبُ** (do alternates) |
| (۴) | حَسِبَ یَحْسِبُ | *(yahi naam — Note mein alternate mention NAHI hua)* |
| (۵) | سَمِعَ یَسْمَعُ | **عَلِمَ یَعْلَمُ** |
| (۶) | شَرُفَ یَشْرُفُ | **کَرُمَ یَکْرُمُ** |

---

##### Khaas ahmiyat ki cheez — book ka canonical set vs deegar Sarf kitabon ka standard (builder commentary, fenced)

(**Yeh observation builder gloss hai — book ne yeh comparison khud explicitly nahi ki**. Lekin Slide 31 Note ke alternate-list se yeh yaad-dasht ke liye kar`am useful hai.)

- **Yeh kitab ka primary 6th baab = شَرُفَ یَشْرُفُ** (NOT کَرُمَ یَکْرُمُ).
- Slide 31 ke **Note** ne explicitly bataya ke "بعض کتب میں" (some other books mein) **کَرُمَ یَکْرُمُ** use hota hai is باب ke liye. Yaani کَرُمَ یَکْرُمُ is kitab ki primary list mein nahi, lekin doosri Sarf kitabon mein attested misaal hai.
- Agar tum kabhi doosri Sarf kitab dekho aur **"باب کَرُمَ"** zikr ho — samjh jaana ke **woh yahi باب شَرُفَ hai is kitab ka** (same wazn فَعُلَ یَفْعُلُ).
- **Saare 6 abwaab structurally same hi hain** — sirf misaal-lafz badal jata hai, **wazn-pair (mazi-mudaari' harakaat ka pattern) wahi rehta hai**. Pattern fixed, misaal flexible.

---

##### Slide 28 ke prior builder-gloss "6 pairings" table ka reconciliation (Slide 31 canonical numbering)

(Builder commentary — Slide 28 ke prior builder gloss aur Slide 31 ke canonical numbering ke darmiyan ka order ka farq notice karna zaroori.)

Sub Topic 1.5 ke pehle build mein (p-027, Slide 28 ke builder-gloss "6 pairings" table) jo positional numbering thi, woh **tentative** thi (uss waqt canonical numbering PDF par formally nahi tha). **Slide 31 ne ab canonical 1-6 establish kar di hai**:

| # | Slide 28 builder-gloss (prior, p-027 notes) | **Slide 31 canonical (PDF, p-028)** |
|---|---|---|
| 1 | ضَرَبَ یَضْرِبُ | **ضَرَبَ یَضْرِبُ** ✓ same |
| 2 | نَصَرَ یَنْصُرُ | **فَتَحَ یَفْتَحُ** ← swap |
| 3 | فَتَحَ یَفْتَحُ | **نَصَرَ یَنْصُرُ** ← swap |
| 4 | حَسِبَ یَحْسِبُ | حَسِبَ یَحْسِبُ ✓ same |
| 5 | سَمِعَ یَسْمَعُ | سَمِعَ یَسْمَعُ ✓ same |
| 6 | شَرُفَ یَشْرُفُ | شَرُفَ یَشْرُفُ ✓ same |

**Positions ۲ aur ۳ swap** hue. Slide 31 ka **canonical order authoritative** hai. (Slide 28 ke builder-gloss table par koi destructive overwrite nahi karta — yeh reconciliation cross-reference rakh dia, future fix-up cycle mein cleanup possible.)

**Forward reference**: Slide 28 ke 6-pairings table mein bhi later "Slide 31 canonical numbering ka cross-ref" footnote add ho sakta hai (deferred fix-up).

---

**Status:** PRE-BUILD (2026-05-30) — Slide 31 ka content PDF-verbatim. Nazir physical book se verify kare:
- (a) Slide title ka exact wording (مذکورہ چھ (۶) ابواب کے اوزان اور مثالیں — red color, parentheses around ۶, "اور" vs "و")
- (b) 6 cells mein har wazn ki harakaat — khaas: فَعَلَ یَفْعِلُ ka یَفْعِلُ par exact harakaat (یا fatha + فا sukoon + عین kasrah + لام damma); فَعِلَ یَفْعَلُ ka فَعِلَ ka عین kasrah; فَعُلَ یَفْعُلُ ka فا fatha + عین damma
- (c) **6 canonical misaalein ki har harakat ki tasdeeq** (yeh sab se zaroori check):
  - **ضَرَبَ یَضْرِبُ** — ضَرَبَ ke ضاد/را/با sab par fatha; یَضْرِبُ ka یا fatha, ضاد sukoon, را kasrah, با damma
  - **فَتَحَ یَفْتَحُ** — فَتَحَ ke فا fatha, تا fatha, حا fatha; یَفْتَحُ ka یا fatha, فا sukoon, تا fatha, حا damma
  - **نَصَرَ یَنْصُرُ** — نَصَرَ ke nuon fatha, sad fatha, ra fatha; یَنْصُرُ ka یا fatha, nuon sukoon, sad damma, ra damma
  - **حَسِبَ یَحْسِبُ** — **حَسِبَ ka ح fatha + س kasrah + ب fatha** (yeh baab ۴ ka definitional check); یَحْسِبُ ka یا fatha, ح sukoon, س kasrah, ب damma
  - **سَمِعَ یَسْمَعُ** — سَمِعَ ka س fatha + م kasrah + ع fatha; یَسْمَعُ ka یا fatha, س sukoon, م fatha, ع damma
  - **شَرُفَ یَشْرُفُ** — **شَرُفَ ka ش fatha + ر damma + ف fatha** (yeh baab ۶ ka definitional check — ر par damma critical, kyunki yeh عین کلمہ ki position hai); یَشْرُفُ ka یا fatha, ش sukoon, ر damma, ف damma
- (d) Cells ka 2×3 layout: top row RTL (۱ → ۲ → ۳), bottom row RTL (۴ → ۵ → ۶) — confirm order
- (e) Note ka exact text — **alternate misaalein ki har harakah**:
  - **مَنَعَ یَمْنَعُ** (م fatha, ن fatha, ع fatha; مضارع: یَمْنَعُ — یا fatha, م sukoon, ن fatha, ع damma)
  - **دَخَلَ یَدْخُلُ** (د fatha, خ fatha, ل fatha; مضارع: یَدْخُلُ — د sukoon, خ damma)
  - **طَلَبَ یَطْلُبُ** (طا fatha, لام fatha, با fatha; مضارع: یَطْلُبُ — طا sukoon, لام damma)
  - **عَلِمَ یَعْلَمُ** (ع fatha, ل kasrah, م fatha; مضارع: یَعْلَمُ — ع sukoon, ل fatha)
  - **کَرُمَ یَکْرُمُ** (ک fatha, ر damma, م fatha; مضارع: یَکْرُمُ — ک sukoon, ر damma)
- (f) "بعض کتب میں" ka exact phrasing aur "مستعمل" lafz kitni dafa repeat hua Note mein (PDF reading mein 4-5 baar dikha)
- (g) "Khaas ahmiyat" wala builder commentary block fairly state karta hai — Nazir confirm kare ke aap classical Sarf ki rasm se waqif ho ke 6th baab ka common misaal کَرُمَ hota hai (general knowledge confirmation, builder gloss hi rahega varna).

---

#### Slide 32 — حرکات کے اعتبار سے ابواب کے گروپ + مجہول forms universal (PDF p-029)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.5 | فعل کے چھ ابواب | Slide 32 | اصطلاحات | Topic 1.0**
- **Slide title (red)**: **حرکات کے اعتبار سے ابواب کے گروپ**
- **Sub-title 1 (red)**: **فعل ماضی معلوم کے تین گروپ ہیں:**
- **Table 1 (ماضی groupings)** — 3 columns (RTL: پہلا/دوسرا/تیسرا گروپ), 1 data row distributing the 6 ماضی misaalein
- **Sub-title 2 (red)**: **فعل مضارع معلوم کے تین گروپ ہیں:**
- **Table 2 (مضارع groupings)** — 3 columns same RTL ordering, 1 data row distributing the 6 مضارع misaalein
- **فائدہ box at bottom**: ماضی مجہول aur مضارع مجہول ka universal wazn

---

**Slide title (PDF verbatim):**
> حرکات کے اعتبار سے ابواب کے گروپ

**Roman:** "Harakaat ke اعتبار se ابواب ke **گروپ**" — yaani harakaat ke base par 6 ابواب ko groups mein arrange karna. **Naya term: گروپ** (Urdu/English borrowing for "group").

---

##### Table 1 — فعل ماضی معلوم ke 3 گروپ

**PDF sub-title (verbatim):**
> فعل ماضی معلوم کے تین گروپ ہیں:

**PDF reading (re-verified 2026-05-30 — corrected after initial Rule 14 misread):**

| گروپ # | عین کلمہ ki harakaat | ماضی misaalein | Wazn | Count |
|---|---|---|---|---|
| **پہلا گروپ** | damma (pesh) | **شَرُفَ** | فَعُلَ | 1 |
| **دوسرا گروپ** | kasrah (zer) | **حَسِبَ، سَمِعَ** | فَعِلَ | 2 |
| **تیسرا گروپ** | fatha (zabar) | **ضَرَبَ، فَتَحَ، نَصَرَ** | فَعَلَ | 3 |

**Structural cross-check**: 1 + 2 + 3 = 6 ✓ — same 6 ابواب as Slide 30, but **opposite indexing** (Slide 30 paragraphs went فَعَلَ→فَعِلَ→فَعُلَ; Slide 32 Table 1 goes damma→kasrah→fatha = پہلا → تیسرا).

---

##### Table 2 — فعل مضارع معلوم ke 3 گروپ

**PDF sub-title (verbatim):**
> فعل مضارع معلوم کے تین گروپ ہیں:

**Mera reading (builder transcription — Nazir physical book se confirm kare):**

| گروپ # | عین کلمہ ki harakaat | مضارع misaalein | Wazn |
|---|---|---|---|
| **پہلا گروپ** | fatha (zabar) | **یَفْتَحُ، یَسْمَعُ** | یَفْعَلُ |
| **دوسرا گروپ** | kasrah (zer) | **یَضْرِبُ، یَحْسِبُ** | یَفْعِلُ |
| **تیسرا گروپ** | damma (pesh) | **یَنْصُرُ، یَشْرُفُ** | یَفْعُلُ |

**Structural cross-check**: 2 + 2 + 2 = 6 ✓ — yaani har مضارع wazn par exactly 2 verbs distribute hote. Yeh asymmetric pattern hai vs ماضی side (3+2+1 vs 2+2+2).

---

##### Slide 30 vs Slide 32 — same 6 ابواب, **alternate framing** (builder structural commentary)

(Yeh observation **builder gloss hai** — book ne explicit comparison nahi diya, magar yeh samajhne ke liye important hai.)

| Slide | Framing | ماضی side group sizes | مضارع side group sizes | Indexing direction (پہلا → تیسرا) |
|---|---|---|---|---|
| **Slide 30** | "Mazi se mudaari' derive" framing | 3 + 2 + 1 = 6 (paragraphs-driven) | (combined with mazi rows) | fatha → kasrah → damma |
| **Slide 32 Table 1** (ماضی) | "Independent groupings by عین harakah" | 1 + 2 + 3 = 6 | — | **damma → kasrah → fatha** |
| **Slide 32 Table 2** (مضارع) | "Independent groupings by عین harakah" | — | 2 + 2 + 2 = 6 | **fatha → kasrah → damma** |

**Mohim baat**: dono framings same 6 ابواب ko describe karte. Slide 30 ne **algebraic derivation** dikhaayi (why 6 not 9, fatha→damma ordering). Slide 32 Table 1 (ماضی) ka indexing **opposite direction** (damma→fatha) — kitab ne is table ko "smallest group first" arrange kiya (1 verb → 2 verbs → 3 verbs). Slide 32 Table 2 (مضارع) ka indexing fatha→damma (Slide 30 ke jaisa). **Inter-table asymmetry book ki choice hai** — Nazir physical book confirm kare.

---

##### فائدہ box (PDF verbatim — Slide 32 bottom)

> **فائدہ**: مذکورہ چھ (۶) ابواب میں ماضی مجہول ہمیشہ **فُعِلَ** کے وزن پر ہوتا ہے اور مضارع مجہول ہمیشہ **یُفْعَلُ** کے وزن پر ہوتا ہے۔

**Roman:** "Mazkurah 6 ابواب mein **ماضی مجہول** hamesha **فُعِلَ** ke wazn par hota hai aur **مضارع مجہول** hamesha **یُفْعَلُ** ke wazn par hota hai."

**Universal rule (PDF-attested):**
- **ماضی مجہول universal wazn**: **فُعِلَ** (ف damma + ع kasrah + ل fatha)
- **مضارع مجہول universal wazn**: **یُفْعَلُ** (یا damma + ف sukoon + ع fatha + ل damma)
- Yaani jo bhi باب ho (1-6 mein se), uska **مجہول** form **hamesha فُعِلَ / یُفْعَلُ** par hota — **6 alag-alag مجہول waznein NAHI**.

**Cross-link to Sub Topic 1.2 (Slide 9)** (builder structural commentary):
- Sub Topic 1.2 Slide 9 mein Ma'lum/Majhul distinction concept-level introduce hua tha — **شَرِبَ حَامِدٌ مَاءً** (ma'lum) vs **شُرِبَ مَاءٌ** (majhul) — pattern observation tha lekin formal wazn nahi diya gaya tha.
- Slide 32 fa'ida ne ab **majhul ka formal wazn PDF-attest** kiya — concept-to-wazn-formalization complete.

---

**Status:** PRE-BUILD (2026-05-30) — Slide 32 ka content PDF-verbatim. **NOTE**: Slide 32 Table 1 ka cell-to-column mapping initial-pass mein Rule 14 default ki wajah se inverted likha gaya tha (پہلا = "structurally-expected largest cluster"); validator + PDF re-read ne correct mapping confirm ki — **پہلا گروپ = rightmost = شَرُفَ (1 verb, damma)**. Fix applied 2026-05-30. Nazir physical book se yeh items verify kare:
- (a) Slide title "حرکات کے اعتبار سے ابواب کے گروپ" exact wording
- (b) **Table 1 (ماضی) cell-to-column mapping** (post-correction): پہلا = شَرُفَ (rightmost, damma), دوسرا = حَسِبَ، سَمِعَ (middle, kasrah), تیسرا = ضَرَبَ، فَتَحَ، نَصَرَ (leftmost, fatha). **Iss inverted indexing ko book ne kyun chuna woh book ka design choice hai** — Slide 30 ke "fatha→damma" ordering se opposite.
- (c) **Table 2 (مضارع) cell-to-column mapping**: پہلا = یَفْتَحُ، یَسْمَعُ (rightmost, fatha), دوسرا = یَضْرِبُ، یَحْسِبُ (middle, kasrah), تیسرا = یَنْصُرُ، یَشْرُفُ (leftmost, damma). **Note**: Table 2 ka indexing Table 1 se opposite hai (fatha-first vs damma-first) — book ki internal asymmetry.
- (d) Table 1 ke har verb ki harakaat letter-by-letter (especially حَسِبَ ka س-kasrah aur شَرُفَ ka ر-damma)
- (e) Table 2 ke har مضارع verb ki harakaat (یَنْصُرُ vs یَنْصِرُ check)
- (f) فائدہ box ka exact wording — **فُعِلَ** ki harakaat (ف-damma، ع-kasrah، ل-fatha) PDF par confirm; **یُفْعَلُ** ki harakaat (یا-damma، ف-sukoon، ع-fatha، ل-damma) PDF par confirm
- (g) "Slide 30 vs Slide 32 alternate framing" wala comparison **builder gloss** hai — kitab ne yeh tabseera explicit nahi diya
- (h) Cross-link to Sub Topic 1.2 Slide 9 (Ma'lum/Majhul) **builder structural commentary** hai

---

#### Slide 33 — مذکورہ ابواب کی علامات (PDF p-029)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.5 | فعل کے چھ ابواب | Slide 33 | اصطلاحات | Topic 1.0**
- **Slide title (red)**: **مذکورہ ابواب کی علامات**
- **3-column table** (RTL header order: نمبر | ابواب | علامات), 6 rows
- Har row mein: number + verb (mazi+mudaari') + harakaat signature in Urdu prose

---

**Slide title (PDF verbatim):**
> مذکورہ ابواب کی علامات

**Roman:** "Mazkurah ابواب ki **علامات**" — yaani upar batae gaye 6 ابواب ke **signatures / identifying markers** (har باب ki unique harakaat-fingerprint).

**Naya term: علامت** (Arabic) — "identification mark / signature". Plural: **علامات**.

---

**Table — 6 ابواب ki علامات (PDF verbatim):**

| نمبر | ابواب | علامات (Urdu prose signature) |
|---|---|---|
| **۱** | **ضَرَبَ یَضْرِبُ** | ماضی مفتوح العین اور مضارع مکسور العین ہے |
| **۲** | **فَتَحَ یَفْتَحُ** | ماضی مفتوح العین اور مضارع **بھی** مفتوح العین ہے |
| **۳** | **نَصَرَ یَنْصُرُ** | ماضی مفتوح العین اور مضارع مضموم العین ہے |
| **۴** | **سَمِعَ یَسْمَعُ** | ماضی مکسور العین اور مضارع مفتوح العین ہے |
| **۵** | **حَسِبَ یَحْسِبُ** | ماضی مکسور العین اور مضارع **بھی** مکسور العین ہے |
| **۶** | **شَرُفَ یَشْرُفُ** | ماضی مضموم العین اور مضارع **بھی** مضموم العین ہے |

**Roman gloss of علامات column:**
- Row ۱: ماضی par عین mein fatha + مضارع par عین mein kasrah → unique signature of باب ۱
- Row ۲: dono par عین mein fatha ("**بھی** مفتوح" = "**also** fatha") → unique signature of باب ۲
- Row ۳: ماضی par fatha + مضارع par damma → unique signature of باب ۳
- Row ۴: ماضی par kasrah + مضارع par fatha → unique signature
- Row ۵: dono par kasrah ("**بھی** مکسور") → unique signature
- Row ۶: dono par damma ("**بھی** مضموم") → unique signature

**Linguistic note (builder commentary, fenced):** Urdu prose mein "بھی" lafz ka kaam = "also/same" — har row mein **بھی** appear hota hai jab ماضی aur مضارع par عین کلمہ ki harakah **same** hoti (rows ۲، ۵، ۶). Rows ۱، ۳، ۴ mein **بھی NAHI** kyunki dono harakaat **different** hain.

---

##### ⚠️ Critical inter-slide numbering inconsistency (Slide 31 vs Slide 33) — Nazir physical book se resolve kare

**Slide 31 (p-028)** ne canonical 1-6 numbering establish ki thi:
- ۴ = **حَسِبَ یَحْسِبُ** (wazn فَعِلَ یَفْعِلُ — kasrah/kasrah)
- ۵ = **سَمِعَ یَسْمَعُ** (wazn فَعِلَ یَفْعَلُ — kasrah/fatha)

**Slide 33 (p-029)** mein mera reading hai (signature-column ke base par definitive):
- ۴ = **سَمِعَ یَسْمَعُ** (kyunki signature "ماضی مکسور + مضارع مفتوح" = kasrah/fatha = فَعِلَ یَفْعَلُ = سَمِعَ ka pattern)
- ۵ = **حَسِبَ یَحْسِبُ** (kyunki signature "ماضی مکسور + مضارع بھی مکسور" = kasrah/kasrah = فَعِلَ یَفْعِلُ = حَسِبَ ka pattern)

**Yaani Slide 33 ka order Slide 31 se opposite hai (rows ۴ aur ۵ swap)**. Yeh ho sakta hai:
- (a) **Kitab ki own inconsistency** — Slide 31 aur Slide 33 alag numbering use karte hain (book typo)
- (b) **Mera reading galat** — image rendering ne mujhe ulta padhwa diya hai
- (c) **Different ordering principle** — Slide 31 wazn-pair pattern follow karti (kasrah-kasrah, kasrah-fatha), Slide 33 signature column logic follow karti

**Nazir physical book** se row ۴ aur row ۵ ke ابواب column mein **kya likha hai** confirm kare. Agar mismatch hai, dono slides ke signatures align karne ka tareeqa decide karna padega.

**Row ۴ aur ۵ ka PDF reading definitive hai** (signature column unambiguously matches): ۴=سَمِعَ، ۵=حَسِبَ. `[?]` markers verbs ke aage **HATA diye** (Rule 11 — `[?]` standalone ke siwa kuch nahi). **Inter-slide swap** (Slide 31 ↔ Slide 33) bhi PDF-attested hai (book ki own choice) — neeche cross-slide table mein resolved framing dekho.

---

**Status:** PRE-BUILD (2026-05-30) — Slide 33 ka content PDF-verbatim transcription kiya. Nazir physical book se verify kare:
- (a) Slide title "مذکورہ ابواب کی علامات" exact wording
- (b) **6 rows ka exact verb-to-row mapping** — khaaskar row ۴ aur ۵ (Slide 31 se inconsistency suspected)
- (c) Har row ki علامات column ki Urdu prose verbatim — خاص kar "**بھی**" lafz ka use rows ۲، ۵، ۶ par (same harakaat indicator)
- (d) "مفتوح / مکسور / مضموم العین" terminology PDF-exact (yeh shayad pehli baar Sarf mein appear ho rahe — "_ال_عین" naming convention)
- (e) Row order top-to-bottom (rows ۱-۶) numbering visually clear
- (f) "بھی" word ka kaam (signature-matching indicator) **builder commentary** hai — kitab ne yeh explicit nahi kaha
- (g) Slide 31 ↔ Slide 33 numbering swap ka final resolution Nazir ke physical book se aayegi

---

#### Slide 34 — Sub Topic 1.5 ka exercise bar (PDF p-029) — **SUB TOPIC 1.5 KHATIMA**

**PDF par jo hai:**
- **Bar (RTL — 3-cell compressed exercise pattern)**: **متعلقہ سب ٹاپک کے سوالات | Slide 34 | میں حل کریں**
- Pattern **Slide 5 + Slide 14 + Slide 20 + Slide 26 jaisa** — 3-cell exercise bar (compressed compared to standard 5-cell header bars on Slides 32-33)
- **Yeh Sub Topic 1.5 ka khatima signal karta hai**

**Roman:** "Mutalliqah Sub Topic ke sawalat ... mein hal karein" — "Related Sub Topic ke sawalat [workbook] mein hal karein". Workbook ka exact naam PDF par saaf nahi (other exercise bars mein bhi same `[?]` tha — Slide 5/14/20/26 mein bhi).

**Status:** PRE-BUILD (2026-05-30) — Slide 34 = exercise bar Sub Topic 1.5 ke khatime ka indicator. Workbook ka naam `[?]` (Slide 5/14/20/26 pattern same — uniform `[?]` cluster).

---

### Sub Topic 1.5 — CLOSURE block (Slides 27-34 = **MUKAMMAL**)

> **Sub Topic 1.5 MUKAMMAL** ho gaya — total **8 slides ka span (27-34)** + 3 PDF pages (p-027, p-028, p-029).

**Sub Topic 1.5 ka core content rollup (Slide-by-slide):**

| Slide | PDF page | Content milestone |
|---|---|---|
| 27 | p-027 | Cover bar — "فعل کے چھ ابواب" |
| 28 | p-027 | افعال ka wazn nikalne ka method + 3+3 waznein (ماضی + مضارع) |
| 29 | p-027 | "**چھ ابواب**" concept formally introduced — 3×3=9 logical, 6 مستعمل master rule + naya term **صیغہ** |
| 30 | p-028 | **3 + 2 + 1 = 6** algebraic derivation (Slide 29 ka structural proof) + 3 missing pairings structurally inferable |
| 31 | p-028 | **CANONICAL 6 ابواب formally PDF-introduced** (ضَرَبَ، فَتَحَ، نَصَرَ، حَسِبَ، سَمِعَ، شَرُفَ) + Note ke 4 alternates |
| 32 | p-029 | Harakaat-based groupings (ماضی 3+2+1, مضارع 2+2+2) + **مجہول universal forms** (فُعِلَ / یُفْعَلُ) |
| 33 | p-029 | **علامات** (signatures) — har باب ka harakaat-fingerprint Urdu prose mein |
| 34 | p-029 | Exercise bar — **Sub Topic 1.5 ka khatima** |

**3 alag presentations of same 6 ابواب** (book ki teaching scaffolding):

1. **Slide 28-29 = numerical foundation** — 9 logical pairings, 6 مستعمل reality
2. **Slide 30-31 = canonical reference** — 3+2+1 algebraic derivation + canonical 6 misaalein
3. **Slide 32-33 = pattern recognition** — alternate harakaat-based groupings + علامات signatures

Yeh **redundancy by design** — concept ko 3 alag angles se introduce karke reinforce karta. Real-world Sarf learning mein student ko har باب ki علامات (Slide 33) yaad rakhna sab se asli skill hai — yahin se future conjugation paradigms (14-sigha tables) build hote.

**Major terms PDF-attested in Sub Topic 1.5:**

| Term | Source slide | Meaning |
|---|---|---|
| **باب** | Slide 29 | Conjugation category |
| **ابواب** | Slide 29 | Plural of باب |
| **مستعمل** | Slide 29 | Used in practice |
| **صیغہ** | Slide 29 | Form / morphological variant |
| **گروپ** | Slide 32 | Grouping (Urdu/English) |
| **علامت** / **علامات** | Slide 33 | Signature / identifying mark |
| **فُعِلَ** | Slide 32 fa'ida | Universal ماضی مجہول wazn |
| **یُفْعَلُ** | Slide 32 fa'ida | Universal مضارع مجہول wazn |
| **مفتوح العین** | Slide 33 | "Fatha on ع" (signature shorthand) |
| **مکسور العین** | Slide 33 | "Kasrah on ع" |
| **مضموم العین** | Slide 33 | "Damma on ع" |

**Sub Topic 1.5 ke 6 canonical ابواب — final reference (Slide 31 authoritative numbering + Slide 33 signatures):**

| باب # | Canonical misaal | Wazn-pair | علامت (Slide 33 signature) |
|---|---|---|---|
| ۱ | ضَرَبَ یَضْرِبُ | فَعَلَ یَفْعِلُ | ماضی مفتوح + مضارع مکسور العین |
| ۲ | فَتَحَ یَفْتَحُ | فَعَلَ یَفْعَلُ | ماضی مفتوح + مضارع بھی مفتوح |
| ۳ | نَصَرَ یَنْصُرُ | فَعَلَ یَفْعُلُ | ماضی مفتوح + مضارع مضموم |
| ۴ | **حَسِبَ یَحْسِبُ** | فَعِلَ یَفْعِلُ | ماضی مکسور + مضارع بھی مکسور |
| ۵ | **سَمِعَ یَسْمَعُ** | فَعِلَ یَفْعَلُ | ماضی مکسور + مضارع مفتوح |
| ۶ | شَرُفَ یَشْرُفُ | فَعُلَ یَفْعُلُ | ماضی مضموم + مضارع بھی مضموم |

**Note — inter-slide numbering swap (book-internal)**: Slide 31 (p-028) ne canonical 1-6 establish ki yeh order; **Slide 33 (p-029) ne rows ۴ aur ۵ swap kar diye** (Slide 33 row ۴=سَمِعَ, row ۵=حَسِبَ). Yeh book ki own inconsistency hai (typo ya intentional alternate ordering — physical book confirm karega). **Yahaan canonical reference Slide 31 ke order ko follow karta hai** (per builder's earlier "Slide 31 authoritative" call out p-028 par).

---

#### Sub Topic 1.5 ke charts roadmap (post-mukammal)

- **Chart 7 candidate (high priority — ab buildable, Rule 16 unlocked):** "6 ابواب master overview" — combining Slide 31 ke canonical wazn-pairs + Slide 33 ke علامات. 10-15 nodes. Source: PDF p-028 Slide 31 + p-029 Slide 33.
- **Chart 8 candidate**: "Sub Topic 1.5 conceptual journey" — Slide 28 (waznein) → Slide 29 (9→6 rule) → Slide 30 (3+2+1 derivation) → Slide 31 (canonical names) → Slide 32 (groupings + مجہول) → Slide 33 (علامات). Topic-overview style.
- **Chart 9 candidate**: "Mujhole forms universal" — Slide 32 fa'ida visualization (small 4-node chart). Low priority.

**Forward pointer:** **Aglay session p-030 = Slide 35+, Sub Topic 1.6 ka aaghaaz** — per Slide 1 (p-018) row 1.6, title likely "تعداد حروف کے اعتبار سے فعل کی اقسام" (letter-count-based فعل classification — ثلاثی / رباعی / etc.). **PDF kholo aur dekho — Rule 16 strict**: لازم / متعدی categorization OR 14-sigha enumeration plant nahi karna agar PDF formally introduce na kare.

---

#### Slide 35 — Sub Topic 1.6 cover (PDF p-030)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.6 | ششش اقسام | Slide 35 | اصطلاحات | Topic 1.0**
  - **Note (verified 2026-05-30)**: PDF mein **header bars + body text + closing statements** SAB jagah consistently **ششش** (3 ش letters) likha hai — Slide 36 transition, Slide 37 title, Slide 37 closing — sab "ششش اقسام". **Standard Persian/Urdu mein "شش" (= 6, 2 ش letters) hota hai** — yeh kitab ki **specific spelling variant** hai (likely stylistic or author's idiosyncratic choice). Notes mein PDF spelling "ششش" verbatim preserve ki gayi hai. Nazir physical book se confirm kare.
- **Body content**: NAHI — Slide 35 sirf **cover/transition bar** hai (pattern Sub Topic 1.5 Slide 27 jaisa). Sub Topic 1.6 ka declaration karta hai.

**Roman:** Slide 35 ek **cover/transition bar** hai. Sub Topic 1.6 ka unwaan "**ششش اقسام**" (= "6 categories" — Persian شش = 6). Content Slide 36 se shuru hota hai.

**Status:** PRE-BUILD (2026-05-30) — Slide 35 par body content nahi. Header bar text Nazir physical book confirm kare (specifically "ششش" vs "شش" rendering).

---

#### Slide 36 — حروف اصلی (مادہ) کے اعتبار سے اسم کی اقسام (PDF p-030)

**PDF par jo hai:**
- Header bar (compressed RTL — Slide 22/28 jaisa multi-line pattern): **Sub Topic 1.6 | تعداد اور حروف کے اعتبار سے اسم اور فعل کی اقسام (ششش اقسام) | Slide 36**
  - Yeh compressed header pattern (standard 5-cell **اصطلاحات + Topic 1.0** cells replaced) Sub Topic 1.6 ka **dou-level scope** declare karta — **اسم اور فعل dono**.
- **Slide title (red)**: **حروف اصلی (مادہ) کے اعتبار سے اسم کی اقسام**
- Body: 1 introductory paragraph + 3 definition paragraphs (with misaalein) + transition statement + 3×4 table

**Slide title (PDF verbatim):**
> حروف اصلی (مادہ) کے اعتبار سے اسم کی اقسام

**Roman:** "Huroof asli (**مادہ**) ke اعتبار se اسم ki aqsam" — root letters/material ke base par اسم ki classification.

**Naya term PDF-attested**: **مادہ** (matter/root material) — explicitly bracketed in title as synonym of "حروف اصلی". Yeh Sub Topic 1.4 mein "حروف اصلی" tha; ab "مادہ" parallel naam introduce hua.

---

##### Paragraph 1 — 3 main qismein declaration (PDF verbatim)

> حروف اصلی (مادہ) کے اعتبار سے اسم تین قسم پر ہے: (۱) ثلاثی (۲) رباعی (۳) خماسی

**Roman:** "Huroof asli (مادہ) ke اعتبار se اسم 3 qism par **ہے** (PDF singular verb — verbatim preserved despite grammatical "ہیں" expectation): (1) **ثلاثی** (2) **رباعی** (3) **خماسی**".

| # | Qism | Naam ka matlab |
|---|---|---|
| ۱ | **ثلاثی** | "Tri-" — 3-letter root |
| ۲ | **رباعی** | "Quadri-" — 4-letter root |
| ۳ | **خماسی** | "Quinque-" — 5-letter root |

(Naam derivation builder gloss: ثلاثة=3, اربعة=4, خمسة=5 in Arabic — yeh general Sarf knowledge hai but standard etymology.)

---

##### Paragraph 2 — 3 qismein ki tareefein + misaalein (PDF verbatim)

> **اسم ثلاثی**: وہ اسم ہے جس میں تین حرف اصلی ہوں، جیسے: **زَیْدٌ**
>
> **اسم رباعی**: وہ اسم ہے جس میں چار حرف اصلی ہوں، جیسے: **جَعْفَرٌ**
>
> **اسم خماسی**: وہ اسم ہے جس میں پانچ حرف اصلی ہوں، جیسے: **جَحْمَرَشٌ** (بوڑھی عورت)

**Roman tareefein + misaalein:**

| Qism | Tareef | PDF misaal | Tarjuma |
|---|---|---|---|
| **اسم ثلاثی** | 3 حروف اصلی hon | **زَیْدٌ** | Zayd (proper noun) |
| **اسم رباعی** | 4 حروف اصلی hon | **جَعْفَرٌ** | Ja'far (proper noun) |
| **اسم خماسی** | 5 حروف اصلی hon | **جَحْمَرَشٌ** | بوڑھی عورت (old woman) |

**Cross-link to Sub Topic 1.4 (Slide 25)** (builder structural commentary):
- Sub Topic 1.4 Slide 25 ne **informal taxonomy** introduce ki thi — "**جَحْمَرَش aur سَفَرْجَل** — yeh kis qism ke ism ho sakte" (rhetorical question, structural rule-derivation).
- Sub Topic 1.6 Slide 36 ne **formal classification + naming** kar di hai — جَحْمَرَش (5-harfi) ab **خماسی مجرد** ke under aaya.
- Sub Topic 1.4 = taxonomy introduction; Sub Topic 1.6 = formal naming + complete breakdown.

---

##### Paragraph 3 — Transition + 3×2 = 6 master rule (PDF verbatim)

> ان میں سے ہر ایک کی دو دو قسمیں ہیں، صرف والے کو ششش اقسام کہتے ہیں۔

**Roman:** "In mein se har ek ki **2-2 qismein** hain, **Sarf wale ko ششش اقسام kehte hain**" → yaani **3 × 2 = 6 sub-categories** = **ششش اقسام**.

**Naya term PDF-attested**: **ششش اقسام** (Persian شش = 6) — Sarf ki istilah for the 6-way breakdown.

---

##### Table — 6 sub-categories named (PDF — 3 rows × 4 alternating num+name columns)

**RTL reading**: rightmost cell of each row starts with the lower number; numbers go 1→6 across rows.

| # | Qism | # | Qism |
|---|---|---|---|
| ۱ | **ثلاثی مجرد** | ۲ | **ثلاثی مزید فیہ** |
| ۳ | **رباعی مجرد** | ۴ | **رباعی مزید فیہ** |
| ۵ | **خماسی مجرد** | ۶ | **خماسی مزید فیہ** |

**Naye terms PDF-attested**:
- **مجرد** — "pure / stripped" → koi extra letter NAHI
- **مزید فیہ** — "added-in" → koi extra letter PRESENT (mazid = added, فیہ = in it)

**Pehchaan rule**: Har root-letter-count (3/4/5) ki **2-2 qismein** = mujarrad (pure) + mazid fih (with addition). 3 × 2 = 6.

**Status:** PRE-BUILD (2026-05-30) — Slide 36 ka content PDF-verbatim. Nazir physical book se verify kare:
- (a) Slide title "حروف اصلی (مادہ) کے اعتبار سے اسم کی اقسام" exact wording + "(مادہ)" bracket placement
- (b) Compressed header bar (Sub Topic 1.6 cell + long sub-heading + Slide 36) — Sub Topic 1.6 ka **اسم AUR فعل** dou-level scope verify
- (c) 3 main qismein ki spellings — ثلاثی، رباعی، خماسی (sab final یا par tanwin nahi, simple یا)
- (d) **خماسی misaal "جَحْمَرَشٌ"** ki exact harakaat — mera reading: ج-fatha + ح-sukoon + م-fatha + ر-fatha + ش-damma+tanwin
- (e) "(بوڑھی عورت)" parenthetical Urdu translation PDF par confirm
- (f) Transition statement "صرف والے کو ششش اقسام کہتے ہیں" — exact wording
- (g) **3×4 table cell-to-column mapping** — Slide 32 Table 1 ki Rule 14 failure ke baad **EXTRA caution**: pakka kare ke rightmost column = ۱/۳/۵ numbers (odd), aur leftmost column = ۲/۴/۶ qism names. **Visual reading wins over expectation.**
- (h) "مادہ" lafz Slide 36 par confirm (synonym for حروف اصلی)
- (i) "شش" lafz Slide 36 body par confirm (Persian "six")
- (j) "Naam derivation" wala builder gloss (ثلاثة/اربعة/خمسة) **builder commentary** hai — kitab ne yeh etymology explicit nahi di

---

#### Slide 37 — ششش اقسام کی وضاحت (PDF p-030)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.6 | ششش اقسام | Slide 37 | اصطلاحات | Topic 1.0**
- **Slide title (red)**: **ششش اقسام کی وضاحت**
- Body: 6 numbered definitions (each = tareef + misaal + wazn + zaayid letter identification) + closing statement + closing نوٹ

**Slide title (PDF verbatim):**
> ششش اقسام کی وضاحت

**Roman:** "**ششش اقسام** ki وضاحت" — explanation/elaboration of the 6 categories.

---

##### 6 numbered definitions (PDF verbatim)

| # | Qism | Tareef | Misaal (PDF) | Wazn | Zaayid letter(s) |
|---|---|---|---|---|---|
| 1 | **ثلاثی مجرد** | 3 حروف اصلی se koi harf zaa'idah na ho | **عَرْفٌ** | **فَعْلٌ** | — (none) |
| 2 | **ثلاثی مزید فیہ** | 3 حروف اصلی se koi harf zaa'idah ho | **اِغْرَافٌ** (validator-confirmed غ, harakaat Nazir final-verify) | **اِفْعَالٌ** | **ہمزہ** + **الف** (2 letters) |
| 3 | **رباعی مجرد** | 4 حروف اصلی se koi harf zaa'idah na ho | **جَعْفَرٌ** | **فَعْلَلٌ** | — (none) |
| 4 | **رباعی مزید فیہ** | 4 حروف اصلی se koi harf zaa'idah ho | **تَخَدْرُجٌ** (validator-confirmed ت + zaayid callout ت) | **تَفَعْلُلٌ** | **ت** (validator-confirmed) |
| 5 | **خماسی مجرد** | 5 حروف اصلی se koi harf zaa'idah na ho | **جَحْمَرَشٌ** | **فَعْلَلَلٌ** | — (none) |
| 6 | **خماسی مزید فیہ** | 5 حروف اصلی se koi harf zaa'idah ho | **خَنْدَرِیْسٌ** | **فَعْلَلِیْلٌ** | *[?]* — PDF callout par exact letter "ی" / "نی" / "یا" mein se ambiguous; Nazir physical book se resolve kare |

**PDF verbatim definitions (long-form):**

> **ثلاثی مجرد**: وہ اسم ہے جس میں تین حروف اصلی سے کوئی حرف زائدہ نہ ہو، جیسے: عَرْفٌ وزن فَعْلٌ۔
>
> **ثلاثی مزید فیہ**: وہ اسم ہے جس میں تین حروف اصلی سے کوئی حرف زائدہ ہو، جیسے: اِغْرَافٌ وزن اِفْعَالٌ، اس میں 'ہمزہ' اور 'الف' زائد ہیں۔
>
> **رباعی مجرد**: وہ اسم ہے جس میں چار حروف اصلی سے کوئی حرف زائدہ نہ ہو، جیسے: جَعْفَرٌ وزن فَعْلَلٌ۔
>
> **رباعی مزید فیہ**: وہ اسم ہے جس میں چار حروف اصلی سے کوئی حرف زائدہ ہو، جیسے: تَخَدْرُجٌ وزن تَفَعْلُلٌ، اس میں 'ت' زائد ہے۔
>
> **خماسی مجرد**: وہ اسم ہے جس میں پانچ حروف اصلی سے کوئی حرف زائدہ ہو، جیسے: جَحْمَرَشٌ وزن فَعْلَلَلٌ۔
>
> **خماسی مزید فیہ**: وہ اسم ہے جس میں پانچ حروف اصلی سے کوئی حرف زائدہ ہو، جیسے: خَنْدَرِیْسٌ وزن فَعْلَلِیْلٌ، اس میں '[?]' (PDF callout par exact letter ambiguous — "ی"، "نی"، ya "یا" mein se ek) زائد ہے۔

---

##### Closing statement + closing نوٹ (PDF verbatim)

**Closing statement:**
> یہ کل چھ قسمیں ہیں، ان کو ششش اقسام کہا جاتا ہے۔

**Roman:** "Yeh kul **6 qismein** hain, in ko **ششش اقسام** kaha jaata hai" — same master rule as Slide 36 ka transition, ab final reiteration ke saath.

**Closing نوٹ:**
> نوٹ: اسم ثلاثی، رباعی اور خماسی کی مکمل اوزان اور ان کی وضاحت معلم الابواب والخصائص میں پڑھیں گے اِنْ شَاءَ اللهُ۔

**Roman:** "Note: Asli/mazid wazn aur **un ki** (= aur in waznein ki) tafseel **معلم الابواب والخصائص** mein parhenge in shaa Allah."

**Forward-reference book PDF-attested**: **معلم الابواب والخصائص** — likely Sarf series ki **doosri kitab** (current book = معلم الصرف). Detailed wazn coverage wahaan deferred.

---

##### Slide 37 ka structural insight (builder commentary, fenced)

(Builder gloss — kitab ne yeh sub-pattern explicit nahi diya, lekin teaching ke liye useful pattern hai.)

**Mujarrad vs Mazid fih ka pattern (PDF examples ko jod kar):**
- **Mujarrad waznein** sab simple/short hain: فَعْلٌ (3), فَعْلَلٌ (4), فَعْلَلَلٌ (5) — exactly root-letter count + tanwin.
- **Mazid fih waznein** sab longer hain (1+ zaayid letters add): اِفْعَالٌ (3+2 zaayid), تَفَعْلُلٌ (4+1 zaayid), فَعْلَلِیْلٌ (5+1 zaayid).
- **Zaayid letters** har case mein **specific** hain: ہمزہ+الف (ثلاثی), ت (رباعی), یا (خماسی). Yeh **future Sub Topics mein systematic taxonomy** ki taraf indicate karte (lekin **abhi NAHI** — Rule 16 strict).

**Status:** PRE-BUILD (2026-05-30) — Slide 37 ka content PDF-verbatim. Nazir physical book se verify kare:
- (a) Slide title "ششش اقسام کی وضاحت" exact wording
- (b) **ثلاثی مجرد misaal "عَرْفٌ"** — harakaat ع-fatha + ر-sukoon + ف-damma+tanwin (= "scent/fragrance" meaning)
- (c) **ثلاثی مزید fih misaal "اِغْرَافٌ"** — validator-confirmed غ; harakaat Nazir final-verify: اِ-kasrah + غ-sukoon + ر-fatha + ا-sukoon + ف-damma+tanwin
- (d) **رباعی مزید fih misaal "تَخَدْرُجٌ"** — validator-confirmed ت + zaayid callout ت; exact harakaat Nazir final-verify
- (e) **خماسی مجرد misaal "جَحْمَرَشٌ"** — Slide 36 same example confirm
- (f) **خماسی مزید fih misaal "خَنْدَرِیْسٌ"** — harakaat خ-fatha + ن-sukoon + د-fatha + ر-kasrah + یا-sukoon + س-damma+tanwin (= "old wine" — classical Arabic)
- (g) 6 wazn forms ki exact harakaat: فَعْلٌ، اِفْعَالٌ، فَعْلَلٌ، تَفَعْلُلٌ، فَعْلَلَلٌ، فَعْلَلِیْلٌ — letter-by-letter
- (h) Closing نوٹ ka kitab name **"معلم الابواب والخصائص"** — exact spelling + harakaat (specifically خصائص ka خ-damma + ص-fatha + ا + ء + ص)
- (i) "اِنْ شَاءَ اللهُ" tashkeel PDF par saaf vs not — formal Islamic verbatim transcription
- (j) "Mujarrad vs Mazid pattern" builder commentary — kitab ne yeh tabseera nahi diya, structural inference hai

---

#### Slide 38 — حروف اصلی (مادہ) کے اعتبار سے فعل کی اقسام (PDF p-031)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.6 | ششش اقسام | Slide 38 | اصطلاحات | Topic 1.0**
- **Slide title (red)**: **حروف اصلی (مادہ) کے اعتبار سے فعل کی اقسام** (Slide 36 ka فعل-side parallel)
- Body: 1 introductory paragraph + 2 definition paragraphs (with misaalein) + transition statement + 2×2 table (4 cells) + closing transition

**Slide title (PDF verbatim):**
> حروف اصلی (مادہ) کے اعتبار سے فعل کی اقسام

**Roman:** "Huroof asli (مادہ) ke اعتبار se **فعل** ki aqsam" — root letters ke base par **فعل** ki classification (Slide 36 ne yahi ism ke liye kiya tha).

---

##### Paragraph 1 — 2 main qismein declaration (PDF verbatim)

> حروف اصلی (مادہ) کے اعتبار سے فعل دو قسم پر ہے: (۱) ثلاثی (۲) رباعی

**Roman:** "Huroof asli ke اعتبار se **فعل do (2) qism par hai**: (۱) **ثلاثی** (۲) **رباعی**۔"

**PDF-attested**: فعل ki sirf **2** main qismein hain (ثلاثی، رباعی) — yeh **PDF Slide 38 "دو قسم پر ہے" wording ka direct claim** hai. Ism ki 3 main qismein thi (ثلاثی، رباعی، خماسی per Slide 36); فعل ki sirf 2.

**Builder inference (fenced, NOT PDF claim)**: *"خماسی فعل NAHI hota" / "Arabic فعل ka maximum 4 root letters hota" — yeh builder ka structural reading hai PDF ke "دو قسم پر ہے" wording se. **Book ne yeh explicitly nahi kaha** ke khumaasi NAHI hota — sirf 2 qismein listed ki hain. Reader inference banata hai.* (Fence consistent with Yaad rakho 70 + Status item (i) + Slide 38-39 structural insight section.)

---

##### Paragraph 2-3 — فعل ثلاثی + فعل رباعی tareef (PDF verbatim)

> **فعل ثلاثی**: وہ فعل ہے جس میں تین حرف اصلی ہوں، جیسے: عَلِمَ وزن فَعِلَ۔
>
> **فعل رباعی**: وہ فعل ہے جس میں چار حرف اصلی ہوں، جیسے: دَحْرَجَ وزن فَعْلَلَ۔

**Roman:**
- **فعل ثلاثی** = wo فعل jis mein 3 حرف اصلی hon, jaise: **عَلِمَ** (wazn **فَعِلَ**)
- **فعل رباعی** = wo فعل jis mein 4 حرف اصلی hon, jaise: **دَحْرَجَ** (wazn **فَعْلَلَ**)

**Verification:**
- عَلِمَ ke 3 letters: ع، ل، م — all root letters, no zaayid → ثلاثی ✓ → wazn فَعِلَ (ع→ف fatha, ل→ع kasra, م→ل fatha)
- دَحْرَجَ ke 4 letters: د، ح، ر، ج — all root letters, no zaayid → رباعی ✓ → wazn فَعْلَلَ (د→ف fatha, ح→ع sukoon, ر→ل fatha, ج→ل fatha)

---

##### Transition statement (PDF verbatim)

> ان میں سے ہر ایک کی دو دو قسمیں ہیں:

**Roman:** "In mein se **har ek ki do-do qismein** hain:" — yani ثلاثی aur رباعی dono ki **2-2 sub-qismein**. Total = **2 × 2 = 4 sub-qismein** (ism side ki 6 ke against 4).

---

##### Slide 38 ka 3-col × 2-row table (RTL, PDF verbatim)

| نمبر | اقسام | نمبر | اقسام |
|---|---|---|---|
| ۱ | ثلاثی مجرد | ۲ | ثلاثی مزید فیہ |
| ۳ | رباعی مجرد | ۴ | رباعی مزید فیہ |

**Cell-by-cell verification (Rule 14 — RTL cell mapping):**
- Right pair (rightmost in RTL reading): نمبر ۱ / اقسام **ثلاثی مجرد** ; نمبر ۳ / اقسام **رباعی مجرد**
- Left pair: نمبر ۲ / اقسام **ثلاثی مزید فیہ** ; نمبر ۴ / اقسام **رباعی مزید فیہ**

**Pattern parallel to Slide 36 table:** Same exact column structure (نمبر + اقسام × 2 pairs), but **2 rows** instead of 3 (no خماسی فعل row). Sub-categorization pattern identical: **مجرد + مزید فیہ** for each main qism.

---

##### Closing transition (PDF verbatim)

> آئیے! ان کی وضاحت پڑھتے ہیں۔

**Roman:** "Aaiye! In ki وضاحت parhte hain" — Slide 39 par 4 detailed definitions aati hain.

**Status:** PRE-BUILD (2026-05-30) — Slide 38 ka content PDF-verbatim transcribed. Nazir physical book se verify kare:
- (a) Slide title "حروف اصلی (مادہ) کے اعتبار سے فعل کی اقسام" exact wording
- (b) Paragraph 1 (PDF verbatim) — confirm "دو قسم پر ہے" wording (Slide 36 ne "تین قسم پر ہے" kiya tha — parallel)
- (c) **فعل ثلاثی tareef** — confirm "تین حرف اصلی ہوں" + misaal **عَلِمَ** wazn **فَعِلَ**
- (d) **فعل رباعی tareef** — confirm "چار حرف اصلی ہوں" + misaal **دَحْرَجَ** wazn **فَعْلَلَ**
- (e) **Transition** "ان میں سے ہر ایک کی دو دو قسمیں ہیں" — exact wording + colon
- (f) **Table 4 cells**: ۱ ثلاثی مجرد / ۲ ثلاثی مزید فیہ / ۳ رباعی مجرد / ۴ رباعی مزید فیہ — RTL cell-mapping confirm (Rule 14 lesson from p-029)
- (g) **Closing transition** "آئیے! ان کی وضاحت پڑھتے ہیں۔" exact wording
- (h) Harakaat verify: **عَلِمَ** (ع-fatha + ل-kasra + م-fatha), **فَعِلَ** (ف-fatha + ع-kasra + ل-fatha), **دَحْرَجَ** (د-fatha + ح-sukoon + ر-fatha + ج-fatha), **فَعْلَلَ** (ف-fatha + ع-sukoon + ل-fatha + ل-fatha)
- (i) "**خماسی فعل NAHI hota**" — builder gloss; book ne yeh explicit nahi kaha, **derivable from "دو قسم پر ہے"** structural constraint (yahi sirf 2 qismein mention ki)

---

#### Slide 39 — فعل side کی 4 qismein ki وضاحت (PDF p-031)

**PDF par jo hai:**
- Header bar (RTL): **Sub Topic 1.6 | ششش اقسام | Slide 39 | اصطلاحات | Topic 1.0**
- **No separate red title** — header bar ke baad seedha 4 definition paragraphs shuru hote (Slide 37 ka pattern different tha — wahaan "ششش اقسام کی وضاحت" red title thi; Slide 39 par koi separate title nahi)
- Body: 4 numbered tareef paragraphs (each = qism name + tareef + misaal + wazn + [zaayid letter callout for مزید فیہ cases])

---

##### 4 fi'l qismein ki وضاحت (PDF verbatim, long-form)

> **ثلاثی مجرد**: وہ فعل ہے جس کے ماضی کے پہلے صیغے میں تین حرف اصلی سے کوئی حرف زائدہ نہ ہو، جیسے: عَرَفَ وزن فَعَلَ۔
>
> **ثلاثی مزید فیہ**: وہ فعل ہے جس کے ماضی کے پہلے صیغے میں تین حرف اصلی سے کوئی حرف زائدہ ہو، جیسے: اَعْرَفَ وزن اَفْعَلَ۔ اس میں ہمزہ زائدہ ہے۔
>
> **رباعی مجرد**: وہ فعل ہے جس کے ماضی کے پہلے صیغے میں چار حرف اصلی سے کوئی حرف زائدہ نہ ہو، جیسے: دَحْرَجَ وزن فَعْلَلَ۔
>
> **رباعی مزید فیہ**: وہ فعل ہے جس کے ماضی کے پہلے صیغے میں چار حرف اصلی سے کوئی حرف زائدہ ہو، جیسے: تَدَحْرَجَ وزن تَفَعْلَلَ۔ اس میں 'ت' زائدہ ہے۔

---

##### 4 fi'l qismein consolidated table (Slide 39)

| # | Qism | Tareef (precis) | Misaal (PDF) | Wazn | Zaayid letter(s) |
|---|---|---|---|---|---|
| 1 | **ثلاثی مجرد** | ماضی pehle صیغہ mein 3 حروف اصلی se koi harf zaa'idah na ho | **عَرَفَ** | **فَعَلَ** | — (none) |
| 2 | **ثلاثی مزید فیہ** | ماضی pehle صیغہ mein 3 حروف اصلی se koi harf zaa'idah ho | **اَعْرَفَ** | **اَفْعَلَ** | **ہمزہ** (PDF callout) |
| 3 | **رباعی مجرد** | ماضی pehle صیغہ mein 4 حروف اصلی se koi harf zaa'idah na ho | **دَحْرَجَ** | **فَعْلَلَ** | — (none) |
| 4 | **رباعی مزید فیہ** | ماضی pehle صیغہ mein 4 حروف اصلی se koi harf zaa'idah ho | **تَدَحْرَجَ** | **تَفَعْلَلَ** | **'ت'** (PDF callout) |

**Roman summary:**
- **ثلاثی مجرد** = 3 root letters, no extras → wazn فَعَلَ (e.g., عَرَفَ)
- **ثلاثی مزید فیہ** = 3 root + ہمزہ added (Slide 39 ne sirf **یeh ek wazn** dikhayi) → wazn اَفْعَلَ (e.g., اَعْرَفَ)
- **رباعی مجرد** = 4 root letters, no extras → wazn فَعْلَلَ (e.g., دَحْرَجَ)
- **رباعی مزید فیہ** = 4 root + ت added (Slide 39 ne sirf yeh ek wazn dikhayi) → wazn تَفَعْلَلَ (e.g., تَدَحْرَجَ)

**Verification:**
- عَرَفَ ke 3 letters: ع، ر، ف — all root, no zaayid → ثلاثی مجرد ✓
- اَعْرَفَ ke 4 letters: ا (=ہمزہ)، ع، ر، ف — ہمزہ zaayid, root = ع/ر/ف → ثلاثی مزید فیہ ✓
- دَحْرَجَ ke 4 letters: د، ح، ر، ج — all root, no zaayid → رباعی مجرد ✓
- تَدَحْرَجَ ke 5 letters: ت، د، ح، ر، ج — ت zaayid (prefix), root = د/ح/ر/ج → رباعی مزید فیہ ✓

**Rule 16 strict observation**: Slide 39 ne ثلاثی مزید فیہ ki **sirf ek** wazn (اَفْعَلَ) dikhayi + رباعی مزید فیہ ki **sirf ek** wazn (تَفَعْلَلَ). Classical Sarf mein ثلاثی مزید فیہ ki kai aur waznein hoti hain — **lekin book ne yeh ek hi exemplar di hai**, isliye notes mein bhi sirf yeh ek hi PDF-attest hai. **Doosri waznein abhi NAHI naam** (Rule 16: forward-defer; ye الباب الخصائص-type forward-ref hai per Slide 37 closing نوٹ).

**Status:** PRE-BUILD (2026-05-30) — Slide 39 ke 4 paragraphs PDF-verbatim. Nazir physical book se verify kare:
- (a) **No separate red title** on Slide 39 (header bar ke baad seedha 4 paragraphs) — confirm
- (b) **ثلاثی مجرد tareef** — exact wording "ماضی کے پہلے صیغے میں تین حرف اصلی سے کوئی حرف زائدہ نہ ہو"
- (c) **ثلاثی مزید فیہ tareef** — exact wording + misaal **اَعْرَفَ** + wazn **اَفْعَلَ** + zaayid callout "**ہمزہ زائدہ ہے**"
- (d) **رباعی مجرد tareef** — exact + misaal **دَحْرَجَ** + wazn **فَعْلَلَ**
- (e) **رباعی مزید فیہ tareef** — exact + misaal **تَدَحْرَجَ** + wazn **تَفَعْلَلَ** + zaayid callout "**'ت' زائدہ ہے**" (single quotes around ت preserved verbatim per S8 spelling-fidelity)
- (f) Harakaat verify letter-by-letter:
  - **عَرَفَ** (ع-fatha + ر-fatha + ف-fatha) + **فَعَلَ** (ف-fatha + ع-fatha + ل-fatha)
  - **اَعْرَفَ** (ا-fatha + ع-sukoon + ر-fatha + ف-fatha) + **اَفْعَلَ** (ا-fatha + ف-sukoon + ع-fatha + ل-fatha)
  - **دَحْرَجَ** (د-fatha + ح-sukoon + ر-fatha + ج-fatha) + **فَعْلَلَ** (ف-fatha + ع-sukoon + ل-fatha + ل-fatha)
  - **تَدَحْرَجَ** (ت-fatha + د-fatha + ح-sukoon + ر-fatha + ج-fatha) + **تَفَعْلَلَ** (ت-fatha + ف-fatha + ع-sukoon + ل-fatha + ل-fatha)
- (g) **"ماضی کے پہلے صیغے میں"** phrase — Slide 39 mein 4-baar consistent appearance verify (yeh Slide 37 ke ism tareefs se slight phrasing difference; ism mein sirf "اسم ہے جس میں" tha)

---

#### Slide 40 — Exercise bar — Sub Topic 1.6 ka khatima (PDF p-031)

**PDF par jo hai:**
- Closing bar (RTL, 3-cell pattern): **متعلقہ سب ٹاپک کے سوالات | Slide 40 | میں حل کریں**
- Footer: tawwabeen.org | **14** | almuallim.org (printed page 14 confirms PDF page 31 mapping)
- **No body content** — Slide 40 sirf exercise bar hai (pattern Slides 5, 14, 20, 26, 34 jaisa)

**Bar text (PDF verbatim, RTL natural reading):**
> متعلقہ سب ٹاپک کے سوالات Slide 40 میں حل کریں

**Roman:** "Related Sub Topic ke sawaalat **Slide 40 mein** hal karein" — i.e., is Sub Topic ke sawaalat is slide par solve karne hain (workbook reference).

**Sub Topic 1.6 closure signal:** Slide 40 ne Sub Topic 1.6 ko formally band kiya — exactly Slide 34 (Sub Topic 1.5 closure) ka pattern. **Aglay Sub Topic 1.7 Slide 41 par shuru** expected (per Slide 1 list — Sub Topic 1.7 starts at Slide 41).

**Status:** PRE-BUILD (2026-05-30) — Slide 40 bar text PDF-verbatim. Nazir physical book se verify kare:
- (a) Bar 3-cell structure confirm (Slides 5/14/20/26/34 ke patterns ki tarah)
- (b) Cell text exact: "متعلقہ سب ٹاپک کے سوالات" + "Slide 40" + "میں حل کریں" — confirm spelling + harakaat (yahaan koi harakaat nahi expected, Urdu prose hai)
- (c) Page footer "14" confirms PDF p-031 = printed page 14 mapping

---

#### Slide 38-39 ka structural insight (builder commentary, fenced)

(Builder gloss — kitab ne in cross-links ko explicit nahi kiya, lekin teaching ke liye useful pattern hai.)

**Asymmetry (ism vs fi'l)**:
- **Ism** ki 3 main qismein → 6 sub-qismein (3×2). PDF-attested.
- **Fi'l** ki 2 main qismein → 4 sub-qismein (2×2). PDF-attested.
- **Total combined**: 6 + 4 = **10 actual qismein**, lekin Sub Topic ka naam "**ششش اقسام**" (= 6) hai — naam ism-side count se aaya. Slide 38/39 headers sab "ششش اقسام" hi rakhte hain even fi'l side mein (book Sub Topic-level branding maintain karta).
- **خماسی فعل NAHI hota** — yeh foundational asymmetry hai. (Ism mein جَحْمَرَش 5-letter possible; فعل mein max 4 letters.)

**Slide 38 vs Slide 39 wazn observation (cross-link to Sub Topic 1.5 Slide 30)**:
- **Slide 38** ne ثلاثی misaal **عَلِمَ** di wazn **فَعِلَ** (ع-fatha + ل-kasra + م-fatha) — yeh **kasra ماضی** pattern hai.
- **Slide 39** ne ثلاثی مجرد misaal **عَرَفَ** di wazn **فَعَلَ** (ع-fatha + ر-fatha + ف-fatha) — yeh **fatha ماضی** pattern hai.
- **Dono ثلاثی مجرد hain** (3 root letters, no zaayid) — phir bhi wazn alag. **Kyun**? Kyun ki "ثلاثی مجرد" sirf letter-count category hai; ماضی ki wazn (فَعَلَ / فَعِلَ / فَعُلَ) **Sub Topic 1.5 Slide 30** mein already establish ho chuki thi — **3 ماضی waznein** possible hain. Book ne is page par yeh cross-link explicit nahi kiya, lekin observant student dekh sakta ke ثلاثی مجرد ke andar **multiple ماضی patterns** chal sakte (jo Sub Topic 1.5 ke 6 ابواب ke foundation hai).

**Cross-link to 6 ابواب (Sub Topic 1.5 Slide 31)**: Sub Topic 1.5 ke 6 canonical ابواب (ضَرَبَ، فَتَحَ، نَصَرَ، حَسِبَ، سَمِعَ، شَرُفَ) sab **3-letter, no zaayid** hain — yani structurally **sab ثلاثی مجرد hain**. Book ne yeh cross-link explicit nahi kiya, lekin Sub Topic 1.6 + 1.5 ke material ko jod kar yeh inference banta hai. (**Builder gloss only** — wait for explicit PDF attribution if it comes later.)

**Mujarrad vs Mazid fih ka pattern (fi'l side, parallel to ism)**:
- **مجرد waznein** sab simple/short: فَعَلَ (3), فَعْلَلَ (4) — exactly root-letter count.
- **مزید فیہ waznein** longer (1+ zaayid letters): اَفْعَلَ (3+1 zaayid = ہمزہ), تَفَعْلَلَ (4+1 zaayid = ت).
- Pattern ism side se identical (Slide 37 ki taraf cross-link), bas **zaayid letters specific** hain har case ke liye.

---

### Sub Topic 1.6 (Slides 35-40 done, p-030 + p-031 — **MUKAMMAL**) — Naye terms (rolling)

> **Sub Topic 1.6 MUKAMMAL** — اسم side (Slides 36-37) + فعل side (Slides 38-39) + exercise bar closure (Slide 40). Total 6-slide span (35-40), 2 PDF pages (p-030 + p-031).

#### مادہ / Maaddah (PDF Slide 36)

- **Urdu**: حروف اصلی کا متبادل نام
- **Roman Urdu**: "Material / root substance" — synonym for **حروف اصلی** (root letters). Slide 36 title mein bracketed.
- **Pehchaan**: Mauzun ke andar wo letters jo basic stem banate hain (jaise نصر mein ن، ص، ر).
- **Source**: Sarf p-030, Slide 36 title

---

#### اسم ثلاثی / Ism Thulaathi (PDF Slide 36)

- **Urdu**: وہ اسم ہے جس میں تین حرف اصلی ہوں
- **Roman Urdu**: An ism with **3 root letters**.
- **PDF misaal**: **زَیْدٌ** (Zayd — proper noun)
- **2 sub-qismein** (Slide 36 table + Slide 37 وضاحت):
  - **ثلاثی مجرد** (no extras) — wazn فَعْلٌ — misaal عَرْفٌ
  - **ثلاثی مزید فیہ** (with extras) — wazn اِفْعَالٌ — misaal اِغْرَافٌ
- **Source**: Sarf p-030, Slides 36-37

---

#### اسم رباعی / Ism Rubaa'i (PDF Slide 36)

- **Urdu**: وہ اسم ہے جس میں چار حرف اصلی ہوں
- **Roman Urdu**: An ism with **4 root letters**.
- **PDF misaal**: **جَعْفَرٌ** (Ja'far — proper noun)
- **2 sub-qismein** (Slide 36 table + Slide 37 وضاحت):
  - **رباعی مجرد** (no extras) — wazn فَعْلَلٌ — misaal جَعْفَرٌ
  - **رباعی مزید فیہ** (with extras) — wazn تَفَعْلُلٌ — misaal تَخَدْرُجٌ
- **Source**: Sarf p-030, Slides 36-37

---

#### اسم خماسی / Ism Khumaasi (PDF Slide 36)

- **Urdu**: وہ اسم ہے جس میں پانچ حرف اصلی ہوں
- **Roman Urdu**: An ism with **5 root letters**.
- **PDF misaal**: **جَحْمَرَشٌ** (= "boorhi aurat" / old woman per PDF parenthetical)
- **2 sub-qismein**:
  - **خماسی مجرد** (no extras) — wazn فَعْلَلَلٌ — misaal جَحْمَرَشٌ
  - **خماسی مزید فیہ** (with extras) — wazn فَعْلَلِیْلٌ — misaal خَنْدَرِیْسٌ (= "old wine" — classical Arabic); zaayid letter PDF callout `[?]` (Nazir resolve)
- **Source**: Sarf p-030, Slides 36-37

---

#### مجرد / Mujarrad (PDF Slide 36)

- **Urdu**: خالص — جس میں کوئی حرف زائدہ نہ ہو
- **Roman Urdu**: "**Pure / stripped**" — ism jisme **koi zaayid letter NAHI**. Sab letters root ke hain.
- **Pehchaan**: Mujarrad ka wazn root-letter count exact match karta (3 root → فَعْلٌ 3-shape; 4 root → فَعْلَلٌ 4-shape; 5 root → فَعْلَلَلٌ 5-shape — sab plus tanwin).
- **Source**: Sarf p-030, Slides 36-37

---

#### مزید فیہ / Mazid Fih (PDF Slide 36)

- **Urdu**: جس میں کوئی حرف زائدہ ہو
- **Roman Urdu**: "**Added-in**" — ism jisme **kuch zaayid letters present hain** (added on top of root letters).
- **Etymology**: مزید (added) + فیہ (in it).
- **Pehchaan**: Mazid fih ka wazn longer hai (root letters + zaayid letters): اِفْعَالٌ (3+2), تَفَعْلُلٌ (4+1), فَعْلَلِیْلٌ (5+1).
- **Source**: Sarf p-030, Slides 36-37

---

#### ششش اقسام / Shashsh Aqsam (PDF Slides 35, 36, 37, 38, 39 — Sub Topic 1.6 ka **Sub Topic-level branding**)

- **Urdu**: چھ قسمیں (kitab "**ششش**" likhti hai — 3 ش letters; standard Persian/Urdu "شش" = 6 mein 2 ش hain)
- **Roman Urdu**: "**Six categories**" — Sarf ki istilah for the **3×2=6** breakdown of اسم by root-letter count + mujarrad/mazid status.
- **6 ke naam (ism side)**: ثلاثی مجرد، ثلاثی مزید فیہ، رباعی مجرد، رباعی مزید فیہ، خماسی مجرد، خماسی مزید فیہ
- **Spelling variant (S8 pattern)**: Standard Persian/Urdu **شش** (= 6) ki jagah is kitab mein consistently **ششش** (3 ش) likha gaya hai — PDF Slides 35, 36, 37, **38, 39** sab par. Likely book ki **stylistic choice** ya author's specific spelling. Nazir physical book final verify kare.
- **Sub Topic-level branding (cross-slide observation)**: "**ششش اقسام**" header bar Sub Topic 1.6 ke **saare slides (35-39)** par appear hota — even fi'l side slides (38-39) jahan actual count **4 hai (NOT 6)**. Yeh book ka **Sub Topic-level branding** hai: "ششش" naam ism breakdown se aaya (6), aur Sub Topic ki **identity label** ke taur par use hota raha. **Actual combined qism count = 6 ism + 4 fi'l = 10 qismein** (lekin Sub Topic ka identity naam "ششش اقسام" hi rehta).
- **Source**: Sarf p-030 (Slides 35, 36, 37) + p-031 (Slides 38, 39) — Sub Topic 1.6 branding consistent across both PDF pages

---

#### فعل ثلاثی / Fi'l Thulaathi (PDF Slide 38)

- **Urdu**: وہ فعل ہے جس میں تین حرف اصلی ہوں
- **Roman Urdu**: A فعل with **3 root letters**.
- **PDF misaal**: **عَلِمَ** (wazn فَعِلَ — Slide 38) AND **عَرَفَ** (wazn فَعَلَ — Slide 39 ثلاثی مجرد reference)
- **2 sub-qismein** (Slide 38 table + Slide 39 وضاحت):
  - **ثلاثی مجرد** (no extras) — wazn **فَعَلَ** — misaal **عَرَفَ**
  - **ثلاثی مزید فیہ** (with extras) — wazn **اَفْعَلَ** — misaal **اَعْرَفَ** (zaayid = ہمزہ)
- **Source**: Sarf p-031, Slides 38-39

---

#### فعل رباعی / Fi'l Rubaa'i (PDF Slide 38)

- **Urdu**: وہ فعل ہے جس میں چار حرف اصلی ہوں
- **Roman Urdu**: A فعل with **4 root letters**.
- **PDF misaal**: **دَحْرَجَ** (wazn فَعْلَلَ — Slide 38 AND Slide 39 رباعی مجرد reference — same example reused)
- **2 sub-qismein** (Slide 38 table + Slide 39 وضاحت):
  - **رباعی مجرد** (no extras) — wazn **فَعْلَلَ** — misaal **دَحْرَجَ**
  - **رباعی مزید فیہ** (with extras) — wazn **تَفَعْلَلَ** — misaal **تَدَحْرَجَ** (zaayid = 'ت')
- **No خماسی فعل**: Structural fact — ism ki 3 main qismein (ثلاثی، رباعی، خماسی), فعل ki sirf 2 (ثلاثی، رباعی). Arabic فعل ka maximum 4 root letters hota. (PDF-derivable from Slide 38 "دو قسم پر ہے" wording.)
- **Source**: Sarf p-031, Slides 38-39

---

#### 6 ism waznein PDF-attested — Sub Topic 1.6 (Slide 37)

| # | Qism | Wazn | PDF misaal | Zaayid letters |
|---|---|---|---|---|
| 1 | ثلاثی مجرد | **فَعْلٌ** | عَرْفٌ | — |
| 2 | ثلاثی مزید فیہ | **اِفْعَالٌ** | اِغْرَافٌ | ہمزہ + الف |
| 3 | رباعی مجرد | **فَعْلَلٌ** | جَعْفَرٌ | — |
| 4 | رباعی مزید فیہ | **تَفَعْلُلٌ** | تَخَدْرُجٌ | ت |
| 5 | خماسی مجرد | **فَعْلَلَلٌ** | جَحْمَرَشٌ | — |
| 6 | خماسی مزید فیہ | **فَعْلَلِیْلٌ** | خَنْدَرِیْسٌ | *[?]* — "ی"/"نی"/"یا" mein se ek (Nazir resolve) |

**Source**: Sarf p-030, Slide 37 — formal 6-wazn introduction.

---

#### 4 fi'l waznein PDF-attested — Sub Topic 1.6 (Slide 39)

| # | Qism | Wazn | PDF misaal | Zaayid letter(s) |
|---|---|---|---|---|
| 1 | ثلاثی مجرد | **فَعَلَ** | عَرَفَ | — |
| 2 | ثلاثی مزید فیہ | **اَفْعَلَ** | اَعْرَفَ | ہمزہ |
| 3 | رباعی مجرد | **فَعْلَلَ** | دَحْرَجَ | — |
| 4 | رباعی مزید فیہ | **تَفَعْلَلَ** | تَدَحْرَجَ | 'ت' |

**Source**: Sarf p-031, Slide 39 — formal 4-fi'l-wazn introduction.

**Note on book exemplar selection (Rule 16 strict)**: Slide 39 ne **ثلاثی مزید فیہ** ki sirf **ایک wazn (اَفْعَلَ)** dikhayi + **رباعی مزید فیہ** ki sirf **ایک wazn (تَفَعْلَلَ)**. Classical Sarf mein mazid fih ki **bahut si waznein** hoti hain — but book ne **sirf yeh exemplars di hain** is foundational page par. Detailed wazn coverage Slide 37 ke closing نوٹ per **معلم الابواب والخصائص** mein deferred (forward-reference). **Notes mein sirf yeh PDF-attested waznein** — baqi NAHI naam (Rule 16: training-data forward-defer).

**Cross-link (builder gloss, fenced) — ism vs fi'l waznein parallel:**
- **ثلاثی مجرد**: ism = فَعْلٌ (with tanwin); fi'l = فَعَلَ (no tanwin)
- **رباعی مجرد**: ism = فَعْلَلٌ (with tanwin); fi'l = فَعْلَلَ (no tanwin)
- **Pattern**: ism waznein **tanwin** (ٌ) lagati hain (kyun ki nominal form); fi'l waznein tanwin-less hain (ماضی form). Yeh book ne explicit nahi kaha lekin PDF examples se inferable.

---

#### معلم الابواب والخصائص / Mu'allim al-Abwaab wal-Khasaa'is (PDF Slide 37 — forward-reference)

- **Urdu**: علم الصرف کی اگلی کتاب جس میں اوزان کی مکمل تفصیل ہو گی
- **Roman Urdu**: Sarf series ki **next textbook** — current "معلم الصرف" ke baad. Complete wazn coverage wahan tafseel se aayegi.
- **Pehchaan**: Slide 37 ke closing نوٹ mein forward-reference. Tells reader: detailed wazn knowledge is deferred to a more advanced text.
- **Source**: Sarf p-030, Slide 37 closing نوٹ

---

### Sub Topic 1.6 — Yaad rakho (Slides 35-40 — **MUKAMMAL**)

63. **Roman:** **Sub Topic 1.6 ka scope** — **اسم AUR فعل** dono ki classification by tadaad-e-huroof (letter count). Slide 36 ke compressed header ne "اسم اور فعل کی اقسام" diya. p-030 ne **اسم side** cover ki (Slides 36-37); p-031 ne **فعل side** cover ki (Slides 38-39); Slide 40 par closure.

64. **Roman:** **اسم ki 3 main qismein** (per حروف اصلی count, Slide 36):
   - **ثلاثی** — 3-letter root (misaal: زَیْدٌ)
   - **رباعی** — 4-letter root (misaal: جَعْفَرٌ)
   - **خماسی** — 5-letter root (misaal: جَحْمَرَشٌ — "بوڑھی عورت")

65. **Roman:** **Master rule (Slide 36 transition statement):** Har main qism ki **2-2 sub-qismein** (mujarrad + mazid fih) = **3 × 2 = 6** = **ششش اقسام** (ism side).

66. **Roman:** **مجرد vs مزید فیہ ka core distinction:**
   - **مجرد** = "pure" → **koi extra letter NAHI** → wazn root-count exact (فَعْلٌ / فَعْلَلٌ / فَعْلَلَلٌ for ism; فَعَلَ / فَعْلَلَ for fi'l)
   - **مزید فیہ** = "added-in" → **kuch extra letters present** → wazn longer (اِفْعَالٌ / تَفَعْلُلٌ / فَعْلَلِیْلٌ for ism; اَفْعَلَ / تَفَعْلَلَ for fi'l)

67. **Roman:** **6 ism waznein PDF-attested (Slide 37):**
   - ثلاثی مجرد → **فَعْلٌ** (e.g., عَرْفٌ)
   - ثلاثی مزید فیہ → **اِفْعَالٌ** (ہمزہ + الف zaayid; e.g., اِغْرَافٌ)
   - رباعی مجرد → **فَعْلَلٌ** (e.g., جَعْفَرٌ)
   - رباعی مزید فیہ → **تَفَعْلُلٌ** (ت zaayid; e.g., تَخَدْرُجٌ)
   - خماسی مجرد → **فَعْلَلَلٌ** (e.g., جَحْمَرَشٌ)
   - خماسی مزید فیہ → **فَعْلَلِیْلٌ** (zaayid letter `[?]` — PDF callout ambiguous; e.g., خَنْدَرِیْسٌ)

68. **Roman:** **Cross-link to Sub Topic 1.4 (Slide 25):** Sub Topic 1.4 ne **informal taxonomy** introduce ki thi (3-harfi/4-harfi/5-harfi + جَحْمَرَش aur سَفَرْجَل ke rhetorical examples). Sub Topic 1.6 ab **formal naming** kar di hai — جَحْمَرَش ab **خماسی مجرد** ke under named.

69. **Roman:** **Forward-reference book (Slide 37 closing نوٹ):** Detailed wazn knowledge ki tafseel **معلم الابواب والخصائص** mein milegi — yeh **Sarf series ki agli kitab** hai. Current book sirf foundational classification deti hai.

70. **Roman:** **فعل ki sirf 2 main qismein** (Slide 38, per حروف اصلی count):
   - **ثلاثی** — 3-letter root (misaal: عَلِمَ wazn فَعِلَ)
   - **رباعی** — 4-letter root (misaal: دَحْرَجَ wazn فَعْلَلَ)
   - **"خماسی فعل NAHI hota"** — *(builder inference from Slide 38 ki "دو قسم پر ہے" wording; book ne yeh explicitly nahi kaha — sirf 2 qismein mention ki hain. Yeh structural reading inference hai, PDF claim NAHI.)*

71. **Roman:** **فعل ki 4 sub-qismein** (Slide 38 table — 2 × 2):
   - ۱ **ثلاثی مجرد** (no zaayid)
   - ۲ **ثلاثی مزید فیہ** (zaayid present)
   - ۳ **رباعی مجرد** (no zaayid)
   - ۴ **رباعی مزید فیہ** (zaayid present)

72. **Roman:** **4 fi'l waznein PDF-attested (Slide 39):**
   - ثلاثی مجرد → **فَعَلَ** (e.g., عَرَفَ)
   - ثلاثی مزید فیہ → **اَفْعَلَ** (ہمزہ zaayid; e.g., اَعْرَفَ)
   - رباعی مجرد → **فَعْلَلَ** (e.g., دَحْرَجَ)
   - رباعی مزید فیہ → **تَفَعْلَلَ** ('ت' zaayid; e.g., تَدَحْرَجَ)

73. **Roman:** **Slide 38 vs Slide 39 wazn observation (builder cross-link, fenced):** Slide 38 ne general ثلاثی misaal **عَلِمَ** (wazn **فَعِلَ**) di; Slide 39 ne ثلاثی مجرد ki misaal **عَرَفَ** (wazn **فَعَلَ**) di. **Dono ثلاثی مجرد hain** (3 root, no zaayid) — phir bhi **wazn alag**. Wajah: "ثلاثی مجرد" sirf **letter-count category** hai; ماضی ki wazn (فَعَلَ / فَعِلَ / فَعُلَ) **Sub Topic 1.5 Slide 30** mein already establish ho chuki thi — 3 ماضی waznein possible hain. (Book ne yeh cross-link explicit nahi kiya — builder gloss.)

74. **Roman:** **Sub Topic 1.6 ka NAMING note (Sub Topic-level branding):** "**ششش اقسام**" label Sub Topic 1.6 ke saare slides (35, 36, 37, 38, 39) ke header bars par appear hota — even fi'l side jahan actual count **4 hai (NOT 6)**. Yeh book ka **Sub Topic-level branding** hai: ism breakdown ke 6 count se naam aaya, aur fi'l side mein bhi same label rakha gaya. **Combined actual count = 6 + 4 = 10 qismein**.

75. **Roman:** **Rule 16 strict observation (Sub Topic 1.6 fi'l side):** Slide 39 ne ثلاثی مزید فیہ ki sirf **ek wazn (اَفْعَلَ)** + رباعی مزید فیہ ki sirf **ek wazn (تَفَعْلَلَ)** dikhayi. Classical Sarf mein **bahut si** mazid fih waznein hoti hain — lekin book ne sirf yeh exemplars di hain. **Notes mein bhi sirf yeh PDF-attested waznein** — baqi NAHI naam. Detailed coverage **معلم الابواب والخصائص** mein deferred (per Slide 37 closing نوٹ).

76. **Roman:** **Sub Topic 1.6 MUKAMMAL** (Slide 40 exercise bar par closure) — Slides 35-40 total 6-slide span, 2 PDF pages (p-030 + p-031). Aglay Sub Topic **1.7** Slide 41+ par expected (per Slide 1 list — Sub Topic 1.7 starts at Slide 41, likely "صحت کے اعتبار سے فعل کی اقسام" — صحیح / معتل classification).

---

### Sub Topic 1.6 — Sabak sawal (khud test karein — Slides 35-40 — **MUKAMMAL**)

88. **Sub Topic 1.6 ka scope kya hai** (Slide 36 ke compressed header se)? Sirf اسم cover hota hai ya اسم + فعل dono?
89. **حروف اصلی** ka doosra naam kya PDF Slide 36 par diya? (Hint: bracket mein hai)
90. **اسم ki 3 main qismein** (per root-letter count) kya hain? Har ek ki PDF misaal kya hai?
91. **Khumaasi ki PDF misaal** kya hai? Uska Urdu tarjuma kya hai?
92. **ششش اقسام** ka literal matlab kya hai? Yeh kis Persian word se aaya?
93. **مجرد vs مزید فیہ** mein bunyaadi farq kya hai? Wazn structure mein kya difference?
94. **Slide 37 ke 6 ism waznein** mein se kam-az-kam 3 yaad karwao — wazn + qism + misaal + zaayid letter (agar koi).
95. **خنْدَرِیسٌ** kis qism ka misaal hai? Iska zaayid letter kya hai (Slide 37 explanation)?
96. **Closing نوٹ ka forward-reference book** kya hai (kitab ka naam)?
97. **Cross-link**: Sub Topic 1.4 Slide 25 mein **جَحْمَرَش** kis rhetorical context mein appear hua tha? Ab Sub Topic 1.6 ne usko kis formal category mein placed kiya?
98. **Slide 38 ka master rule:** فعل ki kitni **main** qismein (per حروف اصلی count)? **Aur خماسی فعل kyun NAHI hota** — yeh structural fact yaad rakhne wala hai.
99. **فعل ثلاثی** + **فعل رباعی** ki tareef batao + Slide 38 ki PDF misaal + wazn donon ke liye (عَلِمَ + دَحْرَجَ).
100. **Slide 38 ka 4-cell table** — 4 qismein ke naam + numbering yaad karwao (۱=ثلاثی مجرد، ... ۴=رباعی مزید فیہ).
101. **4 fi'l waznein** (Slide 39) PDF se yaad karwao — wazn + qism + misaal + zaayid letter (agar koi).
102. **اَعْرَفَ vs اَفْعَلَ** — zaayid letter kya hai? **تَدَحْرَجَ vs تَفَعْلَلَ** — zaayid letter kya hai? (PDF callout exact wording quote karo.)
103. **Cross-link (builder gloss check):** Slide 38 mein **عَلِمَ** ka wazn **فَعِلَ**, lekin Slide 39 mein **عَرَفَ** ka wazn **فَعَلَ**. **Dono ثلاثی مجرد hain** — phir bhi wazn alag kyun? (Hint: Sub Topic 1.5 Slide 30 ka recall — ماضی mein 3 waznein possible.)
104. **Sub Topic 1.6 MUKAMMAL** — total kitne slides span (35-40)? "**ششش اقسام**" naming ka fi'l side se relationship kya — fi'l side ki actual count kya thi (4) phir bhi label **ششش** kyun (Sub Topic-level branding)?
105. **Total Sub Topic 1.6 mein kitne qismein cover hui** (ism + fi'l combined)? Yeh "ششش" label se kaise different hai?

---

### Sub Topic 1.6 (Slides 35-40 done; **MUKAMMAL** — p-030 + p-031) — Charts roadmap + forward pointer

**Sub Topic 1.6 ki visual coverage candidates (Sub Topic MUKAMMAL — ab buildable):**
- **Chart 7 candidate** (Sub Topic 1.5 ka 6 ابواب overview waiting — see Sub Topic 1.5 CLOSURE block): still highest priority.
- **Chart 10 candidate (Sub Topic 1.6 ism side)**: "**ششش اقسام master overview (ism)**" — root tree: اسم → ثلاثی/رباعی/خماسی → 6 leaves (مجرد + مزید فیہ per). With 6 PDF waznein + 6 PDF misaalein. **Ab buildable** (fi'l side bhi attest ho chuki — chart focused on ism side).
- **Chart 11 candidate (Sub Topic 1.6 combined)**: "**Sub Topic 1.6 master overview — اسم + فعل**" — root tree: Sub Topic 1.6 → اسم (3 main → 6 sub) + فعل (2 main → 4 sub) → total 10 leaves. Density: ~12-15 nodes (acceptable for topic-overview). **Highly recommended** — captures the full ism-vs-fi'l asymmetry visually.
- **Chart 12 candidate (Sub Topic 1.7 forward — post-build)**: "Fi'l ki sehat taxonomy (صحیح/معتل)" — wait till Sub Topic 1.7 mukammal.

**Aglay session p-032 = Slide 41+, Sub Topic 1.7 ka aaghaaz expected** — per Slide 1 list (p-018) row 1.7, title (per Slide 1 entry) ka direction "**صحت کے اعتبار سے فعل کی اقسام**" hai. **Rule 16 ULTRA-strict reset**: Sub Topic 1.7 par jo bhi sub-categorization names book introduce kare — **un ke alawa kuch plant NAHI karna**. Classical Sarf training data se aane wale category names (whatever they are) ko **disclaimer mein bhi list NAHI karna** (yahi Rule 16 ka canonical anti-pattern hai — disclaimer khud naam plant kar deta hai). **Sub Topic 1.5 ka multi-session strict-defer success (شَرُفَ canonical PDF-attest hua, NOT کَرُمَ jo memory default tha) — wohi discipline yahaan repeat karna hai.** Page kholo → jo PDF ne diya wahi notes mein, baqi book ka next slide khud reveal karega.

---

### Sub Topic 1.6 — CLOSURE block (Slides 35-40 = **MUKAMMAL**)

> **Sub Topic 1.6 MUKAMMAL** ho gaya — total **6 slides ka span (35-40)** + 2 PDF pages (p-030 + p-031).

**Sub Topic 1.6 ka core content rollup (Slide-by-slide):**

| Slide | PDF page | Content milestone |
|---|---|---|
| 35 | p-030 | Cover bar — "ششش اقسام" |
| 36 | p-030 | **اسم side ka aaghaaz** — اسم ki 3 main qismein (ثلاثی/رباعی/خماسی) + 3×2=6 sub-categories table |
| 37 | p-030 | **6 ism waznein wuzaaht** — فَعْلٌ / اِفْعَالٌ / فَعْلَلٌ / تَفَعْلُلٌ / فَعْلَلَلٌ / فَعْلَلِیْلٌ + misaalein + zaayid letters + forward-ref to **معلم الابواب والخصائص** |
| 38 | p-031 | **فعل side ka aaghaaz** — فعل ki 2 main qismein (ثلاثی/رباعی — **NO خماسی**) + 2×2=4 sub-categories table |
| 39 | p-031 | **4 fi'l waznein wuzaaht** — فَعَلَ / اَفْعَلَ / فَعْلَلَ / تَفَعْلَلَ + misaalein + zaayid letters (ہمزہ / 'ت') |
| 40 | p-031 | Exercise bar — **Sub Topic 1.6 ka khatima** |

**Sub Topic 1.6 ki dou-side teaching architecture (book ka structural choice):**

1. **Slides 35 = cover** — Sub Topic ka identity declaration ("ششش اقسام")
2. **Slides 36-37 = ism side** — 3-main → 6-sub + 6 waznein
3. **Slides 38-39 = fi'l side** — 2-main → 4-sub + 4 waznein
4. **Slide 40 = closure** — exercise bar

Book ne **ism side pehle kiya** kyun ki ism ki **3 main qismein zyada hain** (including خماسی); fi'l side baad mein **simpler structure** (sirf 2 main, NO خماسی) — pedagogically natural sequence.

**Total qismein consolidated (combined ism + fi'l):**
- **Ism**: 6 qismein × 6 waznein × 6 PDF misaalein
- **Fi'l**: 4 qismein × 4 waznein × 4 PDF misaalein
- **Combined**: **10 qismein, 10 waznein, 10 misaalein**
- **Sub Topic naam**: "**ششش اقسام**" (= 6) — refers to ism breakdown; applied as Sub Topic-level branding even on fi'l slides

**Major terms PDF-attested in Sub Topic 1.6:**

| Term | Source slide | Meaning |
|---|---|---|
| **مادہ** | Slide 36 (bracketed in title) | Root material / حروف اصلی synonym |
| **ششش** | Slides 35-39 (header bar consistent) | Six (book's spelling variant — 3 ش vs standard 2 ش) |
| **ثلاثی** | Slides 36, 38 | 3-letter (root letter count) |
| **رباعی** | Slides 36, 38 | 4-letter (root letter count) |
| **خماسی** | Slide 36 (ism only — NOT fi'l) | 5-letter (root letter count) |
| **مجرد** | Slides 36, 37, 38, 39 | Pure / no zaayid letters |
| **مزید فیہ** | Slides 36, 37, 38, 39 | Added-in / with zaayid letters |
| **معلم الابواب والخصائص** | Slide 37 closing نوٹ | Forward-reference: next book in Sarf series for detailed wazn coverage |

**Sub Topic 1.6 ke 10 PDF-attested waznein — final reference:**

| Side | Qism | Wazn | PDF misaal | Zaayid letter(s) |
|---|---|---|---|---|
| Ism | ثلاثی مجرد | فَعْلٌ | عَرْفٌ | — |
| Ism | ثلاثی مزید فیہ | اِفْعَالٌ | اِغْرَافٌ | ہمزہ + الف |
| Ism | رباعی مجرد | فَعْلَلٌ | جَعْفَرٌ | — |
| Ism | رباعی مزید فیہ | تَفَعْلُلٌ | تَخَدْرُجٌ | ت |
| Ism | خماسی مجرد | فَعْلَلَلٌ | جَحْمَرَشٌ | — |
| Ism | خماسی مزید فیہ | فَعْلَلِیْلٌ | خَنْدَرِیْسٌ | `[?]` (Nazir resolve) |
| Fi'l | ثلاثی مجرد | فَعَلَ | عَرَفَ | — |
| Fi'l | ثلاثی مزید فیہ | اَفْعَلَ | اَعْرَفَ | ہمزہ |
| Fi'l | رباعی مجرد | فَعْلَلَ | دَحْرَجَ | — |
| Fi'l | رباعی مزید فیہ | تَفَعْلَلَ | تَدَحْرَجَ | 'ت' |

**Cross-link bridges to other Sub Topics:**
- **Sub Topic 1.4 (Slide 25) → Sub Topic 1.6**: جَحْمَرَش + سَفَرْجَل rhetorical examples → ab formally **خماسی مجرد** + **رباعی مجرد** ke under categorized.
- **Sub Topic 1.5 (Slide 30) → Sub Topic 1.6**: 3 ماضی waznein (فَعَلَ / فَعِلَ / فَعُلَ) ka structural foundation Sub Topic 1.6 ke فعل ثلاثی misaalein (عَلِمَ-فَعِلَ, عَرَفَ-فَعَلَ) ko explain karta — sab ثلاثی مجرد phir bhi different waznein.
- **Sub Topic 1.5 ke 6 ابواب (Slide 31) ↔ Sub Topic 1.6 ثلاثی مجرد فعل**: All 6 canonical ابواب structurally **ثلاثی مجرد فعل** hain (3 root, no zaayid). Book ne yeh cross-link explicit nahi kiya — **builder gloss only**.

**Forward pointer:** **Aglay session p-032 = Slide 41+, Sub Topic 1.7 ka aaghaaz** — per Slide 1 (p-018) row 1.7, Sub Topic 1.7 ki direction "**صحت کے اعتبار سے فعل کی اقسام**" hai. **Rule 16 ULTRA-strict**: Sub Topic 1.7 par jo bhi sub-categorization book introduce kare — **un ke alawa kuch plant NAHI karna**. Classical training-data se aane wale category names ko **disclaimer mein bhi list NAHI karna** (Rule 16 canonical anti-pattern — disclaimer khud naam plant kar deta hai). **Sub Topic 1.5 ka multi-session strict-defer success (شَرُفَ PDF-attest hua, NOT کَرُمَ jo memory default tha) — wohi discipline yahaan repeat karna hai.**

---

### Sub Topic 1.7 — MIGRATED to topic-1/sub-topic-1.7.md (2026-05-30 Phase 1)

> Sub Topic 1.7 content (Slides 41-48, PDF p-032 → p-034) lives at [topic-1/sub-topic-1.7.md](topic-1/sub-topic-1.7.md). This stub remains here until Phase 2 backfill moves remaining Sub Topics. See `_planning/architecture-v2.md`.

---

### Sub Topic 1.1 + 1.2 — Naye terms (rolling glossary)

> Yeh def-cards Slides 1-13 ke based hain (Slides 5 aur 14 exercise bars hain — un mein naye terms nahi).

#### اصطلاحات / Istilahaat

- **Urdu**: کسی فن کے خاص فنی الفاظ
- **Roman Urdu**: kisi fan ke khaas fanni alfaaz
- **Rule**: Har ilm ki apni "istilahaat" hoti hain
- **Misaal**: "Fi'l", "Ism", "Harf", "Wazn", "Baab" — yeh sab Sarf ki istilahaat hain
- **Source**: Sarf p-018, Slide 1

#### علم الصرف / Ilm-us-Sarf (PDF Slide 3)

- **Urdu**: علم صرف ایسے علم کا نام ہے جس کے ذریعے ایک کلمے کو دوسرے کلمے سے بنانے کا طریقہ معلوم ہو، یعنی لفظی تبدیلی کا نام علم الصرف ہے۔
- **Roman Urdu**: Woh ilm jis ke zariye ek kalimah se doosra kalimah, ek sigha se doosra sigha banana aata hai — yaani **alfaazi tabdeeli** ka ilm.
- **Source**: Sarf p-018, Slide 3 (Tareef definition)

#### تعریف، موضوع، غرض، واضع، اہمیت — Sarf ke liye summary

| Istilah | Sarf mein iska jawab (PDF) |
|---|---|
| **تعریف** | Ilm jo alfaaz/sigha ki tabdeeli sikhata hai |
| **موضوع** | کلمہ (kalimah — lafz) |
| **غرض** | Arabic kalam mein sigha ki ghalti se bachana |
| **واضع** | 4 aqwaal: Hazrat Ali RA / Mu'aadh bin Muslim Harawi RH / Imam Abu Hanifa RH / Abu Uthman Bakr Maazni RH |
| **اہمیت** | "الصرف ام العلوم والنحو ابوها" — Sarf علوم ki maa, Nahw علوم ka baap |

#### کلمہ / Kalimah (PDF Slide 7)

- **Urdu**: وہ لفظ جو ایک معنیٰ کے لیے بنایا گیا ہو
- **Roman Urdu**: Wo lafz jiska **ek ma'na** ho
- **Aqsam**: 3 — Ism, Fi'l, Harf
- **Source**: Sarf p-019, Slide 7

#### اسم / Ism (PDF Slide 7)

- **Urdu**: وہ کلمہ جو مستقل معنیٰ بتائے اور اس میں کوئی زمانہ نہ پایا جائے
- **Roman Urdu**: Wo kalimah jo (a) mustaqil ma'na rakhta ho (b) jisme zamana NAHI ho
- **Misaal**: زَیْدٌ، خَالِدٌ (Zayd, Khalid)
- **Source**: Sarf p-019, Slide 7

#### فعل / Fi'l (PDF Slide 7)

- **Urdu**: وہ کلمہ جو مستقل معنیٰ بتائے اور اس میں کوئی زمانہ بھی پایا جائے
- **Roman Urdu**: Wo kalimah jo (a) mustaqil ma'na rakhta ho AUR (b) jisme zamana **paya** jata ho
- **Misaal**: نَصَرَ (madad ki — guzray zamane mein)
- **Source**: Sarf p-019, Slide 7

#### زمانے / Zamane (PDF Slide 7 note)

- 3: ماضی (Maazi = guzra hua), حال (Haal = moujooda), مستقبل (Mustaqbil = aane wala)
- **Source**: Sarf p-019, Slide 7 note

#### فعل ثبت / Fi'l Subut (PDF Slide 8)

- **Urdu**: وہ فعل ہے جس سے کسی کام کا کرنا یا ہونا معلوم ہو
- **Roman**: Wo Fi'l jisme kaam ka **hona** ya **karna** maaloom ho (positive verb)
- **Misaal**: نَصَرَ (madad ki)
- **Source**: Sarf p-020, Slide 8

#### فعل منفی / Fi'l Manfi (PDF Slide 8)

- **Urdu**: وہ فعل ہے جس سے کسی کام کا نہ کرنا یا نہ ہونا معلوم ہو
- **Roman**: Wo Fi'l jisme kaam ka **NA hona** ya **NA karna** maaloom ho (negative verb)
- **Misaal**: مَا نَصَرَ (nahi madad ki)
- **Source**: Sarf p-020, Slide 8

#### عامل / Aamil (PDF Slide 8)

- **Urdu**: وہ ہے جس کے اثر سے بعد والے کلمے میں اعراب کی تبدیلی آ جائے
- **Roman**: Wo lafz jiska **asar** uske baad waale kalimah ke **اعراب** ko **badal de**
- **Misaal**: اَنْ، لَنْ، لَمْ (yeh sab Fi'l Muzaari' ke اعراب badalte hain)
- **Source**: Sarf p-020, Slide 8

#### فعل معرب / Fi'l Mu'arrab (PDF Slide 8)

- **Urdu**: وہ فعل ہے جس کا آخر عامل کے بدلنے سے بدل جائے
- **Roman**: Wo Fi'l jiska aakhir عامل ke aane se **badle** (ending changes with amil)
- **Misaal**: یَعْلَمُ، اَنْ یَعْلَمَ، لَنْ یَعْلَمَ، لَمْ یَعْلَمْ
- **Source**: Sarf p-020, Slide 8

#### فعل مبنی / Fi'l Mabni (PDF Slide 8)

- **Urdu**: وہ فعل ہے جس کا آخر عامل کے بدلنے سے نہ بدلے
- **Roman**: Wo Fi'l jiska aakhir عامل ke aane se **NA badle** (fixed ending)
- **Misaal (PDF verbatim — feminine plural)**: یَعْلَمْنَ، لَنْ یَعْلَمْنَ، لَمْ یَعْلَمْنَ
- **Source**: Sarf p-020, Slide 8

#### فعل معلوم / Fi'l Ma'lum (PDF Slide 9)

- **Urdu**: وہ فعل ہے جس کا فاعل معلوم ہو اور اس فعل کی نسبت فاعل کی طرف ہو
- **Roman**: Wo Fi'l jiska **fa'il (kaam karne wala) maaloom** ho — active voice
- **Misaal**: شَرِبَ حَامِدٌ مَاءً (Hamid ne paani piya)
- **Source**: Sarf p-020, Slide 9

#### فعل مجہول / Fi'l Majhul (PDF Slide 9)

- **Urdu**: وہ فعل ہے جس کا فاعل معلوم نہ ہو اور اس کی نسبت مفعول کی طرف ہو
- **Roman**: Wo Fi'l jiska **fa'il maaloom NAHI** — passive voice
- **Misaal**: شُرِبَ مَاءٌ (paani piya gaya)
- **Source**: Sarf p-020, Slide 9

#### فاعل / Faa'il (PDF Slide 9 fa'ida)

- **Urdu**: کام کرنے والے کو کہتے ہیں
- **Roman**: Kaam karne wala (the doer / subject)
- **Misaal**: حامد (Hamid) — *شَرِبَ حَامِدٌ مَاءً* jumlay mein
- **Source**: Sarf p-020, Slide 9

#### مفعول / Maf'ul (PDF Slide 9 fa'ida)

- **Urdu**: وہ ہے جس پر فاعل کا فعل (کام) واقع ہو
- **Roman**: Wo cheez jis par **fa'il ka kaam** waqi' ho (the object)
- **Misaal**: مَاءً (paani) — *شَرِبَ حَامِدٌ مَاءً* jumlay mein paani par kaam hua
- **Source**: Sarf p-020, Slide 9

#### حرف / Harf (PDF Slide 10) — Kalimah ki teesri qism

- **Urdu**: وہ کلمہ جس کے معنیٰ دوسرے کلمے کو ملائے بغیر سمجھ میں نہ آ سکیں (لفظی: کنارہ)
- **Roman**: Wo kalimah jiska ma'na DOOSRE kalimah ke saath milaaye baghair samjh mein NAHI aata
- **Misaal**: مِنْ (سے), اِلٰی (تک), فِيْ (میں), اِنَّ (بیشک), لَمْ (نہیں), عَلٰی (پر)
- **Sample jumla**: سَفَرْتُ مِنَ الْمَدِيْنَةِ اِلَی الْکُوْفَةِ
- **Source**: Sarf p-021, Slide 10

#### حروف تہجی / Huroof Tahajji (PDF Slide 11)

- **Urdu**: الف سے لے کر یا تک تمام حروف — یہ عربی زبان کی بنیاد ہیں
- **Roman**: Alif se Ya tak tamam huroof = Arabic **alphabet**. In ko milane se **kalimah** banta hai.
- **Aqsam**: 2 — Huroof Sahih (25) + Huroof Illat (3)
- **Source**: Sarf p-021, Slide 11

#### حروف صحیح / Huroof Sahih (PDF Slide 11)

- **Urdu**: وہ حروف جو اکثر ایک شکل میں موجود رہتے ہیں
- **Roman**: Wo huroof jo **ek shakal mein rehte hain** (fixed, change nahi hote)
- **Tadaad**: **25**
- **Source**: Sarf p-021, Slide 11

#### حروف علت / Huroof Illat (PDF Slide 11)

- **Urdu**: وہ حروف جو اکثر ایک شکل میں نہیں رہتے، یعنی کلمے بناتے وقت تبدیل ہوتے ہیں — Arab "بیماری" کہہ کر ادا کرتے ہیں
- **Roman**: Wo huroof jo **shakal badalte** hain kalimah banate waqt — Arab "bimaari" kehte hain
- **Tadaad**: **3** — **و، ا، ی** (mnemonic: **وَائِی / Waa'i**)
- **Importance**: Sarf gardaan mein "irregular" verbs ka asal sabab — Illat-walay verbs (jin mein و، ا، ی) shakal badalte hain
- **Source**: Sarf p-021, Slide 11

#### ہمزہ / Hamza (PDF Slide 11 note)

- **Urdu**: الف ہمیشہ ساکن ہوتا ہے، لیکن جب متحرک نظر آئے تو دراصل وہ ہمزہ ہے
- **Roman**: Alif hamesha **saakin**. Agar Alif **mutaharrik** (harakah wala) dikhe — to woh asal mein **Hamza** hai (na ke Alif). Kuch ulema dono ko separate huroof maante hain.
- **Source**: Sarf p-021, Slide 11 (نوٹ)

#### حَرَکَت / Harakah (PDF Slide 12 — bunyaadi vocab)

- **Urdu**: زبر، زیر اور پیش کو کہتے ہیں
- **Roman**: **Harakah** = zabar, zer, pesh — teeno ko mil kar (Arabic ki vowel marks)
- **Source**: Sarf p-022, Slide 12

#### فَتْح / Fath (PDF Slide 12)

- **Urdu**: زبر کو کہتے ہیں
- **Roman**: **Fath** = zabar (a sound)
- **Source**: Sarf p-022, Slide 12

#### کَسْرَہ / Kasra (PDF Slide 12)

- **Urdu**: زیر کو کہتے ہیں
- **Roman**: **Kasra** = zer (i sound)
- **Source**: Sarf p-022, Slide 12

#### ضَمَّہ / Damma (PDF Slide 12)

- **Urdu**: پیش کو کہتے ہیں
- **Roman**: **Damma** = pesh (u sound)
- **Source**: Sarf p-022, Slide 12

#### مُتَحَرِّک / Mutaharrik (PDF Slide 12)

- **Urdu**: وہ حرف جس پر کوئی حرکت ہو
- **Roman**: Wo harf jis par **koi harakah** ho (zer/zabar/pesh)
- **Misaal**: ضَرَبَ (saare huroof par harakah)
- **3 sub-qismein**: Maftuh (zabar) / Maksur (zer) / Madmum (pesh)
- **Source**: Sarf p-022, Slide 12

#### ساکِن / Saakin (PDF Slide 12) — harf-level (NOT verb-level Mabni)

- **Urdu**: وہ حرف جس پر کوئی حرکت نہ ہو
- **Roman**: Wo harf jis par **koi harakah NAHI** (no vowel mark)
- **Misaal**: "خَالِدْ" mein آخر ka د saakin hai `[?]`
- **Source**: Sarf p-022, Slide 12

#### مُشَدَّد / Mushaddad (PDF Slide 12)

- **Urdu**: وہ حرف جس پر شد ہو، یعنی پہلا حرف ساکن، دوسرا متحرک ہو
- **Roman**: Wo harf jis par **شد** (shadda) ho — yaani ek hi harf ki **2 baar awaz** — pehla saakin, doosra mutaharrik
- **Misaal**: **دَقَّ، رَبَّ** (PDF par 2 misaal hain; ba par shadda + final fatha — رَبَّ yaani رَبْبَ)
- **Source**: Sarf p-022, Slide 12

#### مُنَوَّن / Munawwan (PDF Slide 12)

- **Urdu**: وہ حرف جس پر تنوین ہو
- **Roman**: Wo harf jis par **تنوین** (double harakah) ho
- **Misaal**: ضَرْبًا
- **3 sub-qismein**: Fathatayn (2 zabar) / Kasratayn (2 zer) / Dammatayn (2 pesh)
- **Source**: Sarf p-022, Slide 12

#### مفتوح، مکسور، مضموم / Maftuh, Maksur, Madmum (PDF Slide 12) — Mutaharrik ki 3 sub-qismein

- **مفتوح**: zabar wala (e.g., کَتَبَ)
- **مکسور**: zer wala (e.g., اِبْلِی)
- **مضموم**: pesh wala (e.g., اُذُنْ)
- **Source**: Sarf p-022, Slide 12

#### فتحتان، کسرتان، ضمتان / Fathatayn, Kasratayn, Dammatayn (PDF Slide 12) — Munawwan ki 3 sub-qismein

- **فتحتان** = 2 zabar tanwin (e.g., کِتَابًا)
- **کسرتان** = 2 zer tanwin (e.g., کِتَابٍ)
- **ضمتان** = 2 pesh tanwin (e.g., کِتَابٌ)
- **Source**: Sarf p-022, Slide 12

#### Slide 13 ka particle reference — partial preview

Top 6 single-letter particles: **ب** (ساتھ), **ت** (قسم), **و** (اور), **ف** (پس), **ک** (جیسے), **ل** (کیلیے).

Full multi-letter table Slide 13 par hai (~25 particles). Yahan glossary mein har particle ki def-card NAHI banai — sirf Slide 13 mein table form mein listed hain.

---

### Sub Topic 1.1 — Yaad rakho (Slides 1-4)

1. **Roman:** Har naya ilm parhne se pehle **5 cheezein** jaano: Tareef, Mauzu, Gharaz, Wadi, Ahmiyat.
   **Urdu:** ہر نیا علم پڑھنے سے پہلے ۵ چیزیں جانو۔

2. **Roman:** **Sarf** = ilm-e-tabdeeli-e-alfaaz. Ek lafz se doosra lafz, ek sigha se doosra sigha banana.
   **Urdu:** صرف لفظی تبدیلی کا علم ہے۔

3. **Roman:** **Sarf ka mauzu** = **kalimah**. Sarf bahas karta hai kalimah ki shakal aur banaawat par.
   **Urdu:** صرف کا موضوع کلمہ ہے۔

4. **Roman:** **Sarf ki gharaz** = student ke zehn ko Arabic kalam mein sigha ki ghalti se bachana.

5. **Roman:** **Waadi** ke baare mein **4 aqwaal** hain — kitab kisi ek ko tarjeeh nahi deti.

6. **Roman:** **Ahmiyat** ka مقولہ: *"الصرف ام العلوم والنحو ابوها"* — Sarf علوم ki maa, Nahw علوم ka baap.
   **Urdu:** صرف علوم کی ماں ہے، نحو علوم کا باپ ہے۔

---

### Sub Topic 1.2 — Yaad rakho (Slides 6-14)

1. **Roman:** **Kalimah** = wo lafz jiska **ek ma'na** ho.
   **Urdu:** کلمہ وہ لفظ ہے جس کا ایک معنیٰ ہو۔

2. **Roman:** Arabic kalimat ki **3 aqsam**: Ism, Fi'l, Harf.
   **Urdu:** عربی کلمات کی تین قسمیں ہیں۔

3. **Roman:** **Ism vs Fi'l ka asli farq = zamana**.
   - Ism: mustaqil ma'na + zamana NAHI
   - Fi'l: mustaqil ma'na + zamana HAI
   **Urdu:** اسم میں زمانہ نہیں، فعل میں زمانہ ہوتا ہے۔

4. **Roman:** **3 zamane** — Maazi (past), Haal (present), Mustaqbil (future).

5. **Roman:** Fi'l ki **3 taqseemein** Slides 8-9 par aati hain:
   - **اثبات/نفی** — kaam **hua** ya **NAHI hua** (Nafi banane ke liye مَا)
   - **معرب/مبنی** — اعراب عامل se **badalta hai** ya **fixed hai**
   - **معلوم/مجہول** — fa'il **saaf hai** (active) ya **chhupa hai** (passive)

6. **Roman:** **عامل** = wo lafz jo apne baad waale kalimah ke اعراب ko badal de (misaal: اَنْ، لَنْ، لَمْ).

7. **Roman:** **Hamesha mabni hain:** sab فعل ماضی (Ma'lum/Majhul), sab فعل امر, **2 specific Muzaari' siyaghe** (غائب مؤنث جمع + حاضر مؤنث جمع — جیسے یَعْلَمْنَ), aur **tamam حروف**. Baqi Muzaari' siyaghe = muarrab.

8. **Roman:** **3 buniyadi istilahaat** Sarf-o-Nahw ki: **Fi'l** (kaam), **Faa'il** (kaam karne wala), **Maf'ul** (jis par kaam waqi' ho).
   **Urdu:** فعل، فاعل، مفعول۔

9. **Roman:** **Harf** = wo kalimah jiska ma'na DOOSRE kalimah ke saath milaaye baghair samjh nahi aata (Slide 10).
   **Urdu:** حرف وہ کلمہ ہے جس کا معنیٰ دوسرے کے بغیر سمجھ میں نہ آئے۔
   **Misaal**: مِنْ، اِلٰی، فِيْ، اِنَّ، لَمْ، عَلٰی

10. **Roman:** **3 aqsam ka asal farq** ab fully clear:
    - **Ism + Fi'l** = mustaqil ma'na (akele samjh)
    - **Harf** = ghair-mustaqil ma'na (akele NAHI samjh)
    - Phir **Ism vs Fi'l** ka farq = zamana (Ism mein nahi, Fi'l mein hai)

11. **Roman:** **حروف تہجی** = Arabic alphabet (Alif se Ya). Yeh **kalimah ki bunyaad** hain.

12. **Roman:** Huroof ki **2 qismein**:
    - **حروف صحیح** = **25**, ek shakal mein rehte (fixed)
    - **حروف علت** = **3** (**و، ا، ی** = mnemonic **"وَائِی"**), shakal **badalte** hain — Arab "bimaari" kehte
    - Yeh future Sarf gardaan mein "irregular" verbs ki asal wajah hai.

13. **Roman:** **Alif vs Hamza** — Alif hamesha saakin; mutaharrik dikhe to dar-asal Hamza hai.
   **Urdu:** الف ساکن، ہمزہ متحرک۔

14. **Roman:** **4 buniyadi Sarf vocab** (Slide 12):
    - **حَرَکَت** = zer + zabar + pesh sab
    - **فَتْح** = zabar
    - **کَسْرَہ** = zer
    - **ضَمَّہ** = pesh
    Yeh **har page** par aane wale alfaaz hain. Memorize karo.

15. **Roman:** Huroof ki **4 qismein** (harkat ke aitebar se, Slide 12):
    - **مُتَحَرِّک** = harakah HAI (ضَرَبَ)
    - **ساکِن** = harakah NAHI (خَالِدْ ka د)
    - **مُشَدَّد** = shadda hai (دَقَّ، رَبَّ — ek harf 2 baar)
    - **مُنَوَّن** = tanwin hai (ضَرْبًا — double harakah)

16. **Roman:** **Mutaharrik ki 3 sub-types** = Maftuh (zabar) / Maksur (zer) / Madmum (pesh).
   **Munawwan ki 3 sub-types** = Fathatayn (دو زبر) / Kasratayn (دو زیر) / Dammatayn (دو پیش).

17. **Roman:** **Slide 13** ek **reference table** hai (~30 common Arabic particles ke). 6 single-letter "prefix" particles top par: **ب ت و ف ک ل**. Baqi multi-letter particles (e.g., قَدْ، سَوْفَ، حَتّٰی، لَیْتَ، لَعَلَّ، رُبَّ، waghaira). **Yeh table memorize karna foundational vocabulary hai.**

---

### Sub Topic 1.1 + 1.2 — Sabak sawal (khud test karein)

Book band kar ke jawab dene ki koshish karein:

1. Koi bhi naya ilm parhne se pehle koun se **5 cheezein** zaroor jaani chahiyein? (sirf naam)
2. **علم صرف** ki kitab wali tareef apne lafzon mein batao.
3. **Sarf ka mauzu** kya hai?
4. **Sarf ki gharaz** kya hai?
5. **Waadi** ke baare mein kitne aqwaal hain? Pehla qaul kaun ka hai?
6. *"الصرف ام العلوم والنحو ابوها"* — is مقولہ ka **tarjuma** kya hai aur is se kya samjh aati hai?
7. **Kalimah** ki tareef? Arabic kalimat ki kitni aqsam hain?
8. **Ism** aur **Fi'l** mein asal **farq** kya hai? (1 lafz mein jawab)
9. **3 zamane** koun se hain? (Arabic naam + Urdu)
10. *Misaal:* یہ batao — **زَیْدٌ** ism hai ya fi'l? Kyun? Aur **نَصَرَ** ism hai ya fi'l? Kyun?
11. Fi'l ki **3 taqseemein** koun si hain? (Slides 8-9 par)
12. **فعل ثبت** aur **فعل منفی** mein farq kya hai? Misaal ke saath.
13. **عامل** ki tareef? Aur **معرب** vs **مبنی** mein farq?
14. **Hamesha mabni** koun-se hain? (kam-az-kam 3 cheezein batao)
15. **معلوم** aur **مجہول** mein farq? Misaal jumla ke saath.
16. **Faa'il** aur **Maf'ul** mein farq? *"شَرِبَ حَامِدٌ مَاءً"* jumlay mein kaun fa'il hai aur kaun maf'ul?
17. **Harf** ki tareef (Slide 10)? **Harf** aur **Ism/Fi'l** mein **bunyaadi farq** kya hai?
18. **6 Hurūf** ke naam batao + un ka Urdu ma'na (Slide 10 table se — at least 4).
19. *"سَفَرْتُ مِنَ الْمَدِيْنَةِ اِلَی الْکُوْفَةِ"* — is jumlay mein **مِنْ** aur **اِلٰی** kya kaam kar rahe hain? (mat akela meaning — full sense mein)
20. **حروف تہجی** kya hain aur in ko milane se kya banta hai?
21. **حروف صحیح** kitne hain? **حروف علت** koun se hain (3 huroof) aur **mnemonic** kya hai?
22. **Huroof Illat** ko Arab **"بیماری"** kyun kehte hain? Aage Sarf mein iska kya asar hoga?
23. **Alif** aur **Hamza** mein farq kya hai? (Slide 11 note ke mutabiq)
24. **حَرَکَت، فَتْح، کَسْرَہ، ضَمَّہ** — chaar alfaaz aur unka exact matlab batao.
25. Huroof ki **4 qismein** (harkat ke aitebar se) batao + har ek ka **misaal** (Slide 12 se).
26. **مُتَحَرِّک** ki 3 sub-types? **مُنَوَّن** ki 3 sub-types?
27. **مُشَدَّد** mein hota kya hai? "**رَبَّ**" lafz mein shadda kaise samjhaayi jaaye? (PDF par doosra misaal بھی hai: **دَقَّ**)
28. Slide 13 table se: **ب، ت، و، ف، ک، ل** — har ek ka Urdu matlab batao.
29. Slide 13 se kam-az-kam **5 multi-letter particles** ke naam + matlab batao (e.g., قَدْ، سَوْفَ، حَتّٰی، waghaira).
30. **اِنَّ** vs **اَنْ** vs **اِنْ** — teen alag particles, kya farq hai? (Slide 13 table se)

---

### Sub Topic 1.3 — Naye terms (Slides 16-17)

#### اسم جامد / Ism Jamid (PDF Slide 16)

- **Urdu**: وہ اسم ہے جو نہ تو خود سے بنے اور نہ ہی اس سے کوئی کلمہ بنایا جائے
- **Roman Urdu**: Wo ism jo na khud (kisi se) banta hai, na is se aage kuch banta hai
- **Misaal (PDF verbatim)**: فَرَسٌ، اِبْرَاهِیْمُ، اَبَابِیْلُ، بَرْزَخٌ
- **Pehchaan**: morphologically "frozen" — proper nouns, mahsoos cheezon ke naam, etc. Derivational chain ke andar nahi.
- **Source**: Sarf p-023, Slide 16

#### اسم مصدر / Ism Masdar (PDF Slide 16)

- **Urdu**: وہ اسم ہے جو خود تو کسی سے نہ بنے لیکن اس سے کلمے بنتے ہوں
- **Roman Urdu**: Wo ism jo khud kisi se nahi banta, lekin is se aage kalmay (ism + fi'l dono) bante hain
- **Misaal (PDF verbatim, mansoob form)**: عِلْمًا، ضَرْبًا، نَصْرًا (asal: عِلْم، ضَرْب، نَصْر)
- **Pehchaan**: **action ka naam** (verbal noun) — derivation ka asli sarchashma / root.
- **Source**: Sarf p-023, Slide 16

#### اسم مشتق / Ism Mushtaq (PDF Slide 16)

- **Urdu**: وہ اسم ہے جو خود بھی کسی سے بنے اور اس سے بھی کئی کلمے بنتے ہوں
- **Roman Urdu**: Wo ism jo khud bhi (masdar se) bana hai, aur is se aage bhi kalmay bante hain
- **Misaal (PDF verbatim)**: عَالِمٌ، عَالِمَانِ، عَالِمُوْنَ (asal masdar: عِلْم)
- **Pehchaan**: **derived form** — chain ke beech mein. Ek taraf se "bana", doosri taraf "banta hai".
- **Source**: Sarf p-023, Slide 16

#### فعل ماضی / Fi'l Maadhi (PDF Slide 17)

- **Urdu**: وہ فعل ہے جو گزرے ہوئے زمانے کے متعلق بتائے
- **Roman Urdu**: Wo fi'l jo guzre hue zamane ke baare mein batae (past tense)
- **Misaal (PDF)**: **نَصَرَ** — "مدد کی اس نے ایک مرد نے"
- **Source**: Sarf p-023, Slide 17

#### فعل مضارع / Fi'l Mudaari' (PDF Slide 17)

- **Urdu**: وہ فعل ہے جو موجودہ یا آئندہ زمانے کے متعلق بتائے
- **Roman Urdu**: Wo fi'l jo maujooda ya aainda zamane ke baare mein batae (present or future)
- **Misaal (PDF)**: **یَنْصُرُ** — "مدد کرتا ہے یا کرے گا وہ ایک مرد"
- **Source**: Sarf p-023, Slide 17

#### فعل جحد / Fi'l Jahd (PDF Slide 17)

- **Urdu**: وہ فعل ہے جس میں کسی کام کا انکار، ماضی میں سمجھا جائے
- **Roman Urdu**: Wo fi'l jis mein kisi kaam ka **inkaar** (negation) **maazi** (past) mein samjha jaae
- **Misaal (PDF)**: **لَمْ یَنْصُرْ** — "نہیں مدد کی اس نے ایک مرد نے"
- **Pehchaan (meri taraf se observation)**: **لَمْ + mudaari'** ka pattern — sigha mudaari' hai magar matlab maazi ka inkaar.
- **Source**: Sarf p-023, Slide 17

#### فعل نفی / Fi'l Nafi (PDF Slide 17)

- **Urdu**: وہ فعل ہے جس میں کسی کام کا انکار، حال یا مستقبل میں سمجھا جائے
- **Roman Urdu**: Wo fi'l jis mein kisi kaam ka inkaar **haal ya mustaqbil** (present or future) mein samjha jaae
- **Misaal (PDF)**: **لَا یَنْصُرُ** — "نہیں مدد کرتا یا نہیں کرے گا وہ ایک مرد"
- **Pehchaan (meri taraf se observation)**: **لَا + mudaari'** ka pattern.
- **Source**: Sarf p-023, Slide 17

#### فعل امر / Fi'l Amr (PDF Slide 17)

- **Urdu**: وہ فعل ہے جس میں کسی کام کا حکم دیا جائے
- **Roman Urdu**: Wo fi'l jis mein kisi kaam ka **hukm** (command) diya jaae
- **Misaal (PDF)**: **اُنْصُرْ** — "مدد کر تو ایک مرد"
- **Source**: Sarf p-023, Slide 17

#### فعل نہی / Fi'l Nahi (PDF Slide 17)

- **Urdu**: وہ فعل ہے جس میں کسی کام سے روکا جائے
- **Roman Urdu**: Wo fi'l jis mein kisi kaam se **roakna** (prohibition) ho
- **Misaal (PDF)**: **لَا تَنْصُرْ** — "نہ مدد کر تو ایک مرد"
- **Pehchaan (meri taraf se observation)**: **لَا + tu-sigha** — Nafi se farq sirf yeh ke addressee "tu" hai (تَ-) aur matlab "na karo".
- **Source**: Sarf p-023, Slide 17

#### اسم فاعل / Ism Faail (PDF Slide 18)

- **Urdu**: وہ اسم ہے جو کام کرنے والے کی ذات کے متعلق بتائے
- **Roman Urdu**: Wo ism jo **kaam karne wale** (doer) ki zaat ke baare mein batae
- **Misaal (PDF)**: **نَاصِرٌ** — "مدد کرنے والا ایک مرد"
- **Wazn (meri taraf se observation)**: **فَاعِل** (fa-alif-i-l pattern)
- **Source**: Sarf p-024, Slide 18

#### اسم مفعول / Ism Maf'ul (PDF Slide 18)

- **Urdu**: وہ اسم ہے جو ایسی ذات کے متعلق بتائے جس پر فاعل کا فعل واقع ہو
- **Roman Urdu**: Wo ism jo us zaat ke baare mein batae **jis par fa'il ka fi'l waqi' ho** (the one acted upon — passive recipient)
- **Misaal (PDF)**: **مَنْصُوْرٌ** — "مدد کیا ہوا ایک مرد"
- **Wazn (meri taraf se observation)**: **مَفْعُوْل**
- **Source**: Sarf p-024, Slide 18

#### اسم تفضیل / Ism Tafzeel (PDF Slide 18)

- **Urdu**: وہ اسم ہے جو کسی ذات میں دوسروں کی نسبت صفت کی زیادتی ظاہر کرے
- **Roman Urdu**: Wo ism jo kisi zaat mein **doosron ki nisbat sifat ki ziyadati** (comparative/superlative degree) zaahir kare
- **Misaal (PDF)**: **اَنْصَرُ** — "زیادہ مدد کرنے والا"
- **Wazn (meri taraf se observation)**: **اَفْعَل**
- **Source**: Sarf p-024, Slide 18

#### اسم ظرف / Ism Zarf (PDF Slide 18)

- **Urdu**: وہ اسم ہے جس میں وقت یا جگہ کے معنی پائے جائیں
- **Roman Urdu**: Wo ism jis mein **waqt ya jagah** (time or place) ke ma'na paye jayein
- **2 sub-types (PDF Slide 18)**:
  - **ظرف زمان** = کام کرنے کے وقت کو کہتے ہیں — misaal: **مَنْصَرٌ** (مدد کرنے کا وقت). Wazn: **مَفْعَل**
  - **ظرف مکان** = کام کرنے کی جگہ کو کہتے ہیں — misaal: **مَجْلِسٌ** (بیٹھنے کی جگہ). Wazn: **مَفْعِل**
- **Source**: Sarf p-024, Slide 18

#### اسم آلہ / Ism Aalah (PDF Slide 19)

- **Urdu**: وہ اسم ہے جو کسی کام کے آلے (ذریعے) یا واسطے کے متعلق بتائے
- **Roman Urdu**: Wo ism jo kisi kaam ke **aalah** (instrument / tool / medium) ke baare mein batae
- **Misaal (PDF — 2 examples)**:
  - **مِصْبَاحٌ** (چراغ، روشنی کا آلہ)
  - **مِیْزَانٌ** (ترازو، وزن کرنے کا آلہ)
- **Wazn (meri taraf se observation)**: **مِفْعَال** (donon examples isi wazn par)
- **Source**: Sarf p-024, Slide 19

#### صفت مشبہ / Sifat-e-Mushabbaha (PDF Slide 19)

- **Urdu**: وہ اسم ہے جو ایسی ذات کے متعلق بتائے کہ جس میں یہ صفت ہمیشہ سے موجود ہو
- **Roman Urdu**: Wo ism jo us zaat ke baare mein batae **jis mein yeh sifat hamesha se maujood** (permanent / inherent quality) ho
- **Misaal (PDF)**: **سَمِیْعٌ** — "ہمیشہ سننے والا"
- **Wazn (meri taraf se observation)**: **فَعِیْل** (yeh ek common wazn hai; sif-e-mush ke aur waznein bhi hote hain — book ne sirf yeh ek misaal di)
- **Source**: Sarf p-024, Slide 19

#### Asma-e-Mushtaqqa matching exercise — bonus terms (PDF Slide 19 table)

Matching exercise table mein 5 naye examples PDF par aaye hain (notes mein definitions ke taur par track nahi karte; reference ke liye yahaan list):

- **اَعْلَمُ** (زیادہ جاننے والا ایک مرد) — ism tafzeel of علم, wazn اَفْعَل
- **عَالِمٌ** (جاننے والا ایک مرد) — ism faail of علم, wazn فَاعِل
- **مَضْرُوْبٌ** (مارا ہوا ایک مرد) — ism maf'ul of ضرب, wazn مَفْعُوْل (final letter ب/ر distinction Slide 19 Status mein flagged hai)
- **عَلِیْمٌ** (ہمیشہ جاننے والا) — sif-e-mush of علم, wazn فَعِیْل
- **مَدْخَلٌ** (داخل ہونے کا وقت یا جگہ) — ism zarf of دخل, wazn مَفْعَل

---

### Sub Topic 1.3 — Yaad rakho (Slides 15-20 — Sub Topic 1.3 MUKAMMAL)

> **Yeh asal Sarf ka aaghaaz tha** — Ism ki derivational morphology. Sub Topic 1.3 ab mukammal (Slides 15-20 = p-023 + p-024).

18. **Roman:** Ism ki **3 qismein** hain (derivation ke aitebar se): **جامد، مصدر، مشتق**.
   **Urdu/script:** اسم کی تین قسمیں ہیں: جامد، مصدر، مشتق۔

19. **Roman:** **جامد** = na khud banta hai, na is se kuch banta hai (proper nouns, mahsoos cheezein). **Misaal (PDF):** فَرَسٌ (ghoda), اِبْرَاهِیْمُ (naam), اَبَابِیْلُ، بَرْزَخٌ.

20. **Roman:** **مصدر** = khud nahi banta, **lekin is se aage bohot kuch banta hai** — *action ka naam* (verbal noun). **Misaal (PDF):** عِلْم، ضَرْب، نَصْر. **Yeh derivation ka root hai.**

21. **Roman:** **مشتق** = khud bhi (masdar se) bana, aur is se aage bhi banta hai — *derived form*. **Misaal (PDF):** عَالِم، عَالِمَانِ، عَالِمُوْنَ — sab masdar **عِلْم** ki derivation.

22. **Roman:** **Bunyaadi formula (PDF Slide 16 Note):** **ek masdar → kam-az-kam 12 cheezein mushtaq hoti hain → 6 ism + 6 fi'l**. Yeh Sub Topic 1.3 ka root statement hai. Aage saare slides isi tree ko expand karenge.

23. **Roman:** **6 fi'l qismein (Slide 17)** — root نصر ke saath:
   - **ماضی** → **نَصَرَ** (madad ki — past)
   - **مضارع** → **یَنْصُرُ** (madad karta/kare ga — present/future)
   - **جحد** → **لَمْ یَنْصُرْ** (nahi ki — past inkaar)
   - **نفی** → **لَا یَنْصُرُ** (nahi karta/kare ga — haal/mustaqbil inkaar)
   - **امر** → **اُنْصُرْ** (madad kar — hukm)
   - **نہی** → **لَا تَنْصُرْ** (na madad kar — roakna)

24. **Roman:** **Jahd vs Nafi** farq = **zamane** ka (Jahd = past inkaar, Nafi = present/future inkaar). **Amr vs Nahi** farq = **direction** ka (Amr = "karo", Nahi = "na karo").

25. **Roman:** **Pichli Slide 7 ke 3 zamane** (Maazi/Haal/Mustaqbil) = bunyaadi **time-axis**. **Yahaan Slide 17 ke 6 qismein** = **functional categories** (zamane + negation + command + prohibition). Aage ke Sub Topics mein Fi'l ki aqsaam ka tafseeli bayan aayega (Slide 1 table ke baaqi rows ka content abhi `[?]` markers ke saath pending hai).

26. **Roman:** **6 ism qismein** (Slide 18-19) — sab masdar **نصر** ke saath:
   - **اسم فاعل** → **نَاصِرٌ** (kaam karne wala / madad karne wala) — wazn **فَاعِل**
   - **اسم مفعول** → **مَنْصُوْرٌ** (jis par kaam waqi' hua / madad kiya gaya) — wazn **مَفْعُوْل**
   - **اسم تفضیل** → **اَنْصَرُ** (ziyada madad karne wala — comparative/superlative) — wazn **اَفْعَل**
   - **اسم ظرف** → **مَنْصَرٌ** (madad ka waqt) ya **مَجْلِسٌ** (baithne ki jagah) — wazn **مَفْعَل / مَفْعِل**
   - **اسم آلہ** → **مِصْبَاحٌ** (chiraagh) ya **مِیْزَانٌ** (taraazu) — wazn **مِفْعَال**
   - **صفت مشبہ** → **سَمِیْعٌ** (hamesha sun'ne wala) — wazn **فَعِیْل**

27. **Roman:** **اسم ظرف ki 2 sub-types** (Slide 18): **ظرف زمان** (waqt — مَفْعَل wazn par، misaal مَنْصَر) aur **ظرف مکان** (jagah — مَفْعِل wazn par، misaal مَجْلِس). Wazn ka chhota farq (zer vs zabar on middle harf) hi waqt-vs-jagah ka faisla karta.

28. **Roman:** **Slide 16 Note ka formula ab complete hua:** 1 masdar → **12 mushtaq** = **6 fi'l (Slide 17) + 6 ism (Slides 18-19)** ✓. Sub Topic 1.3 ka pura tree:
   - **Masdar** (root, e.g., نَصْر)
     - **6 fi'l**: نَصَرَ / یَنْصُرُ / لَمْ یَنْصُرْ / لَا یَنْصُرُ / اُنْصُرْ / لَا تَنْصُرْ
     - **6 ism**: نَاصِرٌ / مَنْصُوْرٌ / اَنْصَرُ / مَنْصَرٌ / (اسم آلہ — نصر mein natural nahi) / (سَمِیْعٌ pattern — sif-e-mush book ne different root se diya)

29. **Roman:** **Aham concept — wazn (morphological pattern):** har ism qism apne **alag wazn** par bani hoti hai. Yeh CLAUDE.md per "asal Sarf" hai — book ne wazn ka explicit naam abhi nahi sikhaya (Sub Topic 1.4/1.5 mein expected) magar 6 ism qismein dekh kar pattern (فَاعِل، مَفْعُوْل، اَفْعَل، مَفْعَل/مَفْعِل، مِفْعَال، فَعِیْل) khud zaahir ho jata. **Wazn samjh aaya to har lafz ki shakal pehchaani jaa sakti.**

30. **Roman:** **Cross-root pattern recognition** (Slide 19 matching exercise) — alag-alag roots se same wazn par bane hue ism aapas mein "saga" hote hain: نَاصِر-عَالِم (dono فَاعِل), مَنْصُوْر-مَضْرُوْب (dono مَفْعُوْل), waghaira. **Yeh Sarf ki asal training hai** — wazn pehchaan kar root + qism dono nikaalna.

---

### Sub Topic 1.3 — Sabak sawal (khud test karein)

Book band kar ke jawab dene ki koshish karein:

31. Ism ki **3 qismein** (derivation ke aitebar se) konsi hain? Sirf naam batao.
32. **اسم جامد** ki tareef apne lafzon mein batao. PDF ke kam-az-kam **2 misaal** yaad hain?
33. **اسم مصدر** ki tareef? Yeh **derivation chain mein** kahaan baithta hai — root, middle, ya end? Kyun?
34. **اسم مشتق** kya hai? **عَالِمٌ، عَالِمَانِ، عَالِمُوْنَ** — yeh teen forms PDF ne kis qism ke ism ke misaal ke taur par diye hain?
35. PDF Slide 16 ka **Note** kya kehta hai? Ek masdar se kitni cheezein mushtaq hoti hain aur kis kis qism mein?
36. Fi'l ki **6 qismein** Slide 17 par konsi hain? Sirf naam.
37. **فعل ماضی** vs **فعل مضارع** mein farq kya hai? Misaal "نصر" ke saath.
38. **فعل جحد** aur **فعل نفی** dono "انکار" wale hain — **farq** kya hai? Misaal ke saath.
39. **فعل امر** aur **فعل نہی** mein farq? Misaal "نصر" ke saath.
40. لَمْ یَنْصُرْ، لَا یَنْصُرُ، لَا تَنْصُرْ — teen forms hain. **Har ek** kis qism ka fi'l hai aur kis particle se shuru hota hai?

41. **6 ism qismein** (Slide 18-19) — sirf naam batao. Plus: **اسم ظرف** ki **2 sub-types** kon si hain?
42. **اسم فاعل** vs **اسم مفعول** — bunyaadi farq kya hai? Misaal "نصر" ke saath (نَاصِر vs مَنْصُوْر).
43. **اسم تفضیل** kya zaahir karta hai? نصر ke liye iska misaal kya hai (Slide 18)?
44. **ظرف زمان** aur **ظرف مکان** — donon kya batate hain? Wazn ka kya chhota farq hai? Misaal: مَنْصَر vs مَجْلِس.
45. **اسم آلہ** ki 2 misaalein PDF se yaad hain? Donon ka kya matlab hai (chiraagh / taraazu)?
46. **صفت مشبہ** mein "ہمیشہ" lafz kyun aata hai tareef mein? سَمِیْعٌ ki tareef apne lafzon mein batao.
47. **Wazn (morphological pattern)** kya hai? **فَاعِل، مَفْعُوْل، اَفْعَل، مَفْعَل، مِفْعَال، فَعِیْل** — yeh 6 waznein kin ism qismein ke hain?
48. Slide 19 matching exercise table se: **نَاصِرٌ** ka match L column mein kya hoga? **مَنْصُوْرٌ** ka? **اَنْصَرُ** ka? (Same wazn → same qism rule).
49. **Sub Topic 1.3 mukammal ho gaya** — apni samajh se 2-3 lines mein batao: ek masdar se kya kya banta hai aur kyun? (Slide 16 Note + Slide 17 + Slides 18-19 ka roll-up).

---

### Sub Topic 1.4 — Naye terms (Slides 22-26 — Sub Topic 1.4 MUKAMMAL)

#### موزون / Mauzun (PDF Slide 22)

- **Urdu**: وہ لفظ ہے جس کا وزن نکالا جائے
- **Roman Urdu**: Wo lafz jis ka **wazn nikalna** ho — yaani jis lafz ka morphological pattern decode karna hai
- **Misaal (PDF)**: ضَرْبٌ، عِلْمٌ، عَالِمٌ — yeh sab "moozun" hain
- **Source**: Sarf p-025, Slide 22

#### میزان / Meezan (PDF Slide 22)

- **Urdu**: ان حروف کو کہتے ہیں جن کے ذریعے وزن نکالا جائے
- **Roman Urdu**: Wo huroof jin ke zariye wazn nikala jata hai — **yardstick/template letters**
- **Yeh huroof (PDF)**: **فا، عین، لام** (ف، ع، ل)
- **Combined form**: **فَعَلَ** (Sub Topic 1.3 ke fi'l Maazi ka standard form)
- **Source**: Sarf p-025, Slide 22

#### وزن / Wazn (PDF Slide 22)

- **Urdu**: کسی بھی لفظ میں پائے جانے والے حروف کی مرتب شکل اور خاص حرکات و سکنات جو میزان کے ذریعے واضح ہو، اُس کو وزن کہتے ہیں
- **Roman Urdu**: Lafz ki **murattab shakal** (ordered letter structure) + **harakaat-o-sukoonaat** (vowel marks pattern), jo meezan ke zariye waazeh ho — wo wazn hai
- **Misaal (PDF)**: ضَرْبٌ → wazn **فَعْلٌ**; عِلْمٌ → wazn **فِعْلٌ**; عَالِمٌ → wazn **فَاعِلٌ**
- **Pehchaan**: wazn = **pattern/mould** jis par koi bhi lafz dhala hua hai
- **Source**: Sarf p-025, Slide 22

#### حروف اصلی / Huroof Asli (PDF Slide 23)

- **Urdu**: وہ حروف جو 'ف، ع، ل' کلمہ کے مقابلے میں آئیں
- **Roman Urdu**: Wo huroof jo meezan (ف، ع، ل) ke **muqaabile mein aate** hain — **root letters**, lafz ki bunyaadi structure
- **Misaal (PDF)**: عِلْمٌ mein ع، ل، م sab asli (saare meezan ke muqaabile mein); ضَرْبٌ mein ض، ر، ب sab asli
- **Source**: Sarf p-025, Slide 23

#### زائدہ / Zaa'idah (PDF Slide 23)

- **Urdu**: وہ حروف جو 'ف، ع، ل' کلمہ کے مقابلے میں نہ ہوں
- **Roman Urdu**: Wo huroof jo meezan ke muqaabile mein **NA** hon — **extra letters** (zaa'idah means "extra/added"), lafz ki derivation ke liye add hue
- **Misaal (PDF)**: عَالِمٌ mein **الف** zaa'idah hai (ism faail ki علامت ke taur par)
- **Pehchaan**: zaa'idah huroof aksar **علامت** (sign of a specific qism) ya **کلام ka hissa** hote hain
- **Source**: Sarf p-025, Slide 23

#### فا کلمہ / Fa Kalimah (PDF Slide 23)

- **Urdu**: موزون میں جو حرف میزان کے 'فا' کلمہ کے مقابلے میں ہو
- **Roman Urdu**: Mauzun ka **pehla root letter** — jo meezan ke ف ke muqaabile mein hai
- **Misaal (PDF)**: ضَرْبٌ → فَعْلٌ; yahaan **ض = فا کلمہ**
- **Source**: Sarf p-025, Slide 23

#### عین کلمہ / Ain Kalimah (PDF Slide 23)

- **Urdu**: موزون میں جو حرف میزان کے 'عین' کلمہ کے مقابلے میں ہو
- **Roman Urdu**: Mauzun ka **doosra root letter** — jo meezan ke ع ke muqaabile mein hai
- **Misaal (PDF)**: ضَرْبٌ → فَعْلٌ; yahaan **ر = عین کلمہ**
- **Source**: Sarf p-025, Slide 23

#### لام کلمہ / Lam Kalimah (PDF Slide 23)

- **Urdu**: موزون میں جو حرف میزان کے 'لام' کلمہ کے مقابلے میں ہو
- **Roman Urdu**: Mauzun ka **teesra root letter** — jo meezan ke ل ke muqaabile mein hai
- **Misaal (PDF)**: ضَرْبٌ → فَعْلٌ; yahaan **ب = لام کلمہ**
- **Source**: Sarf p-025, Slide 23

#### کسوٹی / Kasoti (PDF Slide 23)

- **Urdu**: 'ف، ع، ل' کلمہ کو میزان اور **کسوٹی** مقرر کیا گیا
- **Roman Urdu**: **Touchstone / yardstick** — Urdu/Persian-origin word meaning the standard against which something is tested
- **Pehchaan**: Slide 23 ne meezan ko "کسوٹی" bhi kaha hai — yaani jis se moozun ko test kar ke root vs zaa'idah identify karte hain
- **Source**: Sarf p-025, Slide 23

#### علامت / Alaamat (PDF Slide 23)

- **Urdu**: نشانی، چِیْز جو کسی بات کا اشارہ ہو
- **Roman Urdu**: **Sign / marker** — extra letter jo kisi specific qism ki علامت ho. **Misaal (PDF)**: عَالِم mein extra الف "اسم فاعل ki علامت" hai
- **Source**: Sarf p-025, Slide 23

#### مادہ / Maddah (PDF Slide 24)

- **Urdu**: حروف اصلی کا دوسرا نام (Slide 24 title ke bracket mein: "حروف اصلی (مادہ) کی پہچان")
- **Roman Urdu**: **Synonym** for حروف اصلی — yaani lafz ka **asal jauhar / root substance**. Literal meaning: "matter/substance".
- **Pehchaan**: Aaj se aap **حروف اصلی** aur **مادہ** dono interchangeably use kar sakte. Sarf textbooks aur classical Arabic grammar mein **مادہ** ka use bohat aam hai.
- **Source**: Sarf p-026, Slide 24

#### فَعْلٌ wazn (PDF Slides 22 + 24 + 25)

- **Pattern**: 3 root letters (ف، ع، ل) with **fatha-sukoon-damma+tanween** harakaat
- **PDF misaalein**: ضَرْبٌ، فَتْحٌ، بَعْدٌ (Slide 22), نَصْرٌ (Slide 24 Row 1 + Slide 25), ضَرْبٌ (Slide 25)
- **Likely qism (builder gloss)**: اسم مصدر (verbal noun) — Slide 16 ke masdar examples (ضَرْبًا، نَصْرًا) ki base form ka wazn
- **Source**: Sarf p-025, Slide 22 + p-026, Slides 24-25

#### فَاعِلٌ wazn (PDF Slides 23 + 24)

- **Pattern**: 3 root letters with extra **ا** (alif) between root letter 1 aur 2 — fatha-alif-kasrah-damma+tanween
- **PDF misaalein**: عَالِمٌ (Slide 23), عَابِدٌ (Slide 24 Row 2), کَاتِبٌ (Slide 24 Row 5)
- **Qism (PDF-attested)**: **اسم فاعل** — Slide 23 ka explicit statement *"عَالِمٌ ka wazn فَاعِلٌ hai; الف زائد hai aur اسم فاعل ki علامت hai"*
- **Sub Topic 1.3 connection**: Slides 18-19 ke "Pattern observation" tables mein faail=فَاعِل tha builder gloss — Slide 23 + 24 ne PDF-formally attest kar diya
- **Source**: Sarf p-025, Slide 23 + p-026, Slide 24

#### فَعِیْلٌ wazn (PDF Slide 24)

- **Pattern**: 3 root letters with extra **ی** (ya) between root letters 2 aur 3 — fatha-kasrah-ya-damma+tanween
- **PDF misaalein**: کَرِیْمٌ (Slide 24 Row 4), شَرِیْفٌ (Slide 24 Row 7), سَمِیْعٌ (Slide 19 — Sub Topic 1.3)
- **Likely qism (builder gloss — PDF Slide 24 ne classification nahi di)**: **صفت مشبہ** — Slide 19's builder gloss observation jab سَمِیْعٌ ko sifat-e-mushabbaha qism mein dikhaya gaya tha; Slide 24 ne sirf wazn فَعِیْلٌ formally introduce kiya (کَرِیْم + شَرِیْف ke saath). **صفت مشبہ classification** in specific words ki abhi PDF-attested NAHI — yeh inference hai pichle Slide 19 observation se.
- **Source**: Sarf p-026, Slide 24 (cross-ref Slide 19)

#### فَاعِلَانِ wazn (PDF Slide 24)

- **Pattern**: فَاعِل wazn + dual ending **ا + ن** (alif-noon-kasrah) — total 6 letters
- **PDF misaal**: عَالِمَانِ (Slide 24 Row 6)
- **Builder observation (meri taraf se — PDF Slide 24 par yeh terminology nahi)**: Yeh **تثنیہ** (dual — "do") form hai. **Pehla ا** = ism faail ki علامت (Slide 23 statement — PDF-attested). **Doosra ا + ن** = علامتِ تثنیہ (dual marker — yeh concept aur naam *تثنیہ* PDF p-026 tak abhi formally introduce NAHI hue; future Sub Topics mein expected).
- **Source**: Sarf p-026, Slide 24

#### فَاعِلُوْنَ wazn (PDF Slide 24)

- **Pattern**: فَاعِل wazn + masculine plural ending **و + ن** (waw-noon-fatha) — total 6 letters
- **PDF misaal**: کَاتِبُوْنَ (Slide 24 Row 3)
- **Builder observation (meri taraf se — PDF Slide 24 par yeh terminology nahi)**: Yeh **masculine plural** form hai. **ا** = ism faail ki علامت (Slide 23 statement — PDF-attested). **و، ن** = علامتِ جمع (plural marker — yeh concept aur naam *جمع مذکر سالم* PDF p-026 tak abhi formally introduce NAHI hue; future Sub Topics mein expected).
- **Source**: Sarf p-026, Slide 24

#### فَعْلَلٌ wazn (PDF Slide 25)

- **Pattern**: 4 root letters mapped to 4 meezan letters (ف، ع، ل، ل) — fatha-sukoon-fatha-damma+tanween
- **PDF misaalein**: بَرْزَخٌ، جَعْفَرٌ (Slide 25 — اسم چار حرفی section)
- **Qism**: **اسم چار حرفی** (4-letter ism) — Slide 25 ki sub-table header
- **Builder gloss**: Slide 25 paragraph rule kehta hai 4-harfi ism **Jamid ya Mushtaq** ho sakte (Masdar bhi 4-harfi ho sakta). **بَرْزَخ ya جَعْفَر** ki specific qism PDF par attest nahi — yeh canonical Arabic dictionary knowledge se Jamid lagte (specific dictionary lookups Shaykh se confirm karein).
- **Source**: Sarf p-026, Slide 25

#### فَعْلَلِلٌ wazn (PDF Slide 25)

- **Pattern**: 5 root letters mapped to 5 meezan letters (ف، ع، ل، ل، ل) — fatha-sukoon-fatha-kasrah-damma+tanween
- **PDF misaalein**: جَحْمَرَشٌ، سَفَرْجَلٌ (Slide 25 — اسم پانچ حرفی section)
- **Qism**: **اسم پانچ حرفی** (5-letter ism) — Slide 25 sub-table header
- **PDF rule (Slide 25 paragraph)**: 5-harfi ism **sirf اسم جامد** hote — اسم مصدر aur اسم مشتق sirf 3 ya 4 harfi. **Yeh PDF-attested rule hai** (paragraph verbatim). Individual word meanings (e.g., "Old woman", "Quince") PDF par nahi — woh canonical Arabic dictionary se, Shaykh se confirm karein.
- **Source**: Sarf p-026, Slide 25

#### اسم تین حرفی / اسم چار حرفی / اسم پانچ حرفی (PDF Slide 25)

- **Urdu (paragraph rule)**: اسم جامد کے اوزان تین، چار اور پانچ حرفی ہوتے ہیں لیکن اسم مصدر اور اسم مشتق کے اوزان صرف تین اور چار حرفی ہوتے ہیں
- **Roman Urdu**: Ism ki **letter-count-based taqseem**:
  - **اسم تین حرفی** = 3 root letters wala ism (e.g., نَصْر، ضَرْب — اسم مصدر / مشتق / جامد teeno)
  - **اسم چار حرفی** = 4 root letters wala ism (e.g., بَرْزَخ، جَعْفَر — اسم مصدر / مشتق / جامد teeno)
  - **اسم پانچ حرفی** = 5 root letters wala ism (e.g., جَحْمَرَش، سَفَرْجَل — **sirf اسم جامد**)
- **Rule (PDF Slide 25 paragraph verbatim)**: Jamid → 3/4/5 harfi possible. Masdar + Mushtaq → sirf 3/4 harfi.
- **Source**: Sarf p-026, Slide 25

#### معلم الابواب والخاصیات / Mu'allim al-Abwab wal-Khasiyaat (PDF Slide 25 — forward-ref kitab)

- **Pehchaan**: Future Sarf textbook ka naam — Slide 25 ke نوٹ mein reference: *"اسم کے اوزان کی مکمل تفصیل معلم الابواب والخاصیات میں پڑھیں گے ان شاء اللہ۔"*
- **Status**: Forward-ref — abhi sirf naam-anchor (book ne self-flag kiya). Tafseel future kitab mein.
- **Builder discipline**: Yeh kitab ke baare mein **memory-fill nahi karna** — sirf naam preserve karna jaisa PDF par hai.
- **Source**: Sarf p-026, Slide 25 (Note)

---

### Sub Topic 1.4 — Yaad rakho (Slides 21-26 — Sub Topic 1.4 MUKAMMAL)

> **Yeh Sarf ka technical engine hai** — wazn samjh aaya to har lafz ki shakal pehchaani jaa sakti.

31. **Roman:** **3 bunyaadi terms** (Slide 22):
   - **موزون** = wo lafz jis ka wazn nikalna ho (e.g., ضَرْب، علم)
   - **میزان** = wo huroof jin se wazn nikalta — **ف، ع، ل** — combined: **فَعَلَ**
   - **وزن** = mauzun ki murattab shakal + harakaat/sukoonaat, jo meezan par lagaae jaayein

32. **Roman:** **Method (Slide 22):** Mauzun ki shakal dekho → meezan select karo → same harakaat/sukoonaat meezan par lagao. **Misaal:** ضَرْبٌ (fatha-sukoon-damma+tanween) → فَعْلٌ (same harakaat on ف-ع-ل).

33. **Roman:** **Pattern observation (PDF table Slide 22):**
   - فَتْحٌ (fatha-sukoon) → **فَعْلٌ**
   - عِلْمٌ (kasrah-sukoon) → **فِعْلٌ**
   - بَعْدٌ (fatha-sukoon) → **فَعْلٌ**
   - **Same harakaat-pattern = same wazn**, regardless of root letters.

34. **Roman:** **Hroof Asli vs Zaa'idah (Slide 23):** Jo harf میزان (ف، ع، ل) ke **muqaabile mein aaye** = **اصلی** (root). Jo na aaye = **زائدہ** (extra). Misaal: عِلْمٌ → فِعْلٌ (saare 3 asli). **عَالِمٌ → فَاعِلٌ** (الف zaa'idah, اسم فاعل ki علامت).

35. **Roman:** **3 naye terms — root letter labels (Slide 23):**
   - **فا کلمہ** = 1st root letter (ف ke muqaabile mein)
   - **عین کلمہ** = 2nd root letter (ع ke muqaabile mein)
   - **لام کلمہ** = 3rd root letter (ل ke muqaabile mein)
   - **Misaal:** ضَرْب → ض(فا) / ر(عین) / ب(لام)

36. **Roman:** **Note (Slide 23):** *"Jo harf mauzun mein ziyada hoga, wahi harf meezan mein bhi ziyada kiya jaye ga."* — Yaani agar mauzun mein extra alif hai, to meezan mein bhi corresponding extra alif lagega. **Isi liye derived forms ke waznein lambay hote** (مَفْعُوْل، مِفْعَال، اَفْعَل).

37. **Roman (cross-Sub-Topic connection):** **p-024 Slides 18-19** mein 6 ism qismein ke waznein (فَاعِل، مَفْعُوْل، اَفْعَل، مَفْعَل، مِفْعَال، فَعِیْل) **builder gloss** ke taur par observe ki gayi thin. Sub Topic 1.4 ne ab wazn ka concept formally introduce kar diya — toh wo gloss observations ab PDF-attested foundation par khari hain (kam-az-kam فَاعِل = ism faail explicitly Slide 23 mein PDF-verbatim hai; aur فَعِیْل ka pattern Slide 24 ke کَرِیْم + شَرِیْف mein bhi dikhaya gaya — Slide 19's sifat-e-mushabbaha observation reinforce hua).

38. **Roman:** **Slide 24 ki 7-misaal table — wazn extraction practical demonstration:**
   - **Row 1:** نَصْرٌ → فَعْلٌ → root ن، ص، ر — **koi zaa'idah letter nahi** (× column). Simplest case.
   - **Row 2 + Row 5:** عَابِدٌ + کَاتِبٌ → dono **فَاعِلٌ** — different roots, same wazn — **اسم فاعل** (ا = ism faail ki علامت).
   - **Row 3:** کَاتِبُوْنَ → فَاعِلُوْنَ → **جمع مذکر سالم** form (ا + و + ن = 3 zaa'idah).
   - **Row 4 + Row 7:** کَرِیْمٌ + شَرِیْفٌ → dono **فَعِیْلٌ** — different roots, same wazn — **صفت مشبہ** likely pattern (Slide 19's sifat-e-mushabbaha cross-link).
   - **Row 6:** عَالِمَانِ → فَاعِلَانِ → **تثنیہ** (dual) form (ا + ا + ن = 3 zaa'idah).

39. **Roman:** **مادہ = حروف اصلی ka synonym (Slide 24).** Slide 24 ka title bracket explicitly states: *"حروف اصلی (مادہ) کی پہچان"*. **مادہ** ka literal matlab = "matter/substance" = lafz ka **asal jauhar** = root letters.

40. **Roman:** **Slide 25 — اسم ki letter-count-based taqseem:**
   - **اسم تین حرفی** = 3 root letters (e.g., نَصْر، ضَرْب). Examples wazn: فَعْلٌ.
   - **اسم چار حرفی** = 4 root letters (e.g., بَرْزَخ، جَعْفَر). Examples wazn: فَعْلَلٌ.
   - **اسم پانچ حرفی** = 5 root letters (e.g., جَحْمَرَش، سَفَرْجَل). Examples wazn: فَعْلَلِلٌ.

41. **Roman:** **Slide 25 paragraph ka master rule (cross-Sub-Topic 1.3 connection):**
   - **اسم جامد** ke اوزان: 3, 4, **YA 5** harfi (3 options).
   - **اسم مصدر** + **اسم مشتق** ke اوزان: **SIRF** 3 ya 4 harfi (2 options).
   - **Pattern:** Jamid sab se zyada varied (foreign-origin/rare native nouns 5-harfi tak ja sakte). Masdar/Mushtaq derivational system rules 3-4 letters tak hi rakhte hain.

42. **Roman:** **Slide 25 نوٹ — forward-ref kitab:** *"اسم کے اوزان کی مکمل تفصیل **معلم الابواب والخاصیات** میں پڑھیں گے ان شاء اللہ۔"* — Ism ke اوزان ki **مکمل تفصیل** future kitab mein milegi. Aaj jo sikhaaya hai woh **introduction** hai. **Memory-fill nahi karna** — sirf naam-anchor preserve kar liya.

43. **Roman:** **Slide 26 = Sub Topic 1.4 ka khatima exercise bar** (Slides 5/14/20 ka 4th instance). متعلقہ سب ٹاپک کے سوالات workbook mein hal karne hain. **Pattern confirm:** Har Sub Topic ka khatima exercise bar se hota hai.

44. **Roman:** **Sub Topic 1.4 ka mukammal arc (Slides 21-26):**
   - **Slide 21** = cover
   - **Slides 22-23** = wazn ki tareef + method + terminology
   - **Slide 24** = method ka 7-example application + مادہ ka synonym
   - **Slide 25** = اسم ke اوزان ki taqseem + cross-Sub-Topic 1.3 rule
   - **Slide 26** = khatima exercise bar
   - **Net result:** Aaj se aap kisi bhi lafz ka wazn nikal sakte; اسم ke 3/4/5-harfi categories pehchaan sakte.

---

### Sub Topic 1.4 — Sabak sawal (khud test karein — Slides 21-26 MUKAMMAL)

Book band kar ke jawab dene ki koshish karein:

50. **3 bunyaadi terms** Slide 22 par: موزون / میزان / وزن — har ek ki tareef apne lafzon mein batao.
51. **Meezan** ke 3 huroof konse hain? Combined form kya hai (full harakaat)?
52. **Method:** ضَرْبٌ ka wazn kaisey nikaalein ge step by step? Final wazn kya hoga?
53. PDF Slide 22 table ke **3 examples** yaad hain? Har ek ka wazn kya?
54. **حروف اصلی** vs **زائدہ** mein farq kya hai? Misaal "عَالِمٌ" mein konsa harf زائدہ hai aur kis cheez ki علامت hai?
55. **فا کلمہ / عین کلمہ / لام کلمہ** kya hain? ضَرْبٌ mein kaunsa harf konsa kalimah hai?
56. Slide 23 ka **Note** apne lafzon mein batao — moozun mein ziyada harf ho to meezan mein kya hoga?
57. عِلْمٌ ka wazn **فِعْلٌ** kyun hua aur عَالِمٌ ka **فَاعِلٌ** kyun? Farq samjhaao.

58. **Slide 24 Row 1:** نَصْرٌ ka wazn nikaalo step by step. Root letters kaunse? Zaa'idah letters? (Hint: column "حروف زائدہ" mein × ka kya matlab?)

59. **Slide 24 Rows 3 + 5:** کَاتِبٌ aur کَاتِبُوْنَ — dono same root (ک، ت، ب) se hain. Magar wazn alag — کیوں? Konsa "ek" hai aur konsa "kayi"?

60. **Slide 24 Row 6:** عَالِمَانِ ka wazn فَاعِلَانِ kya batata hai — singular, dual ya plural? 3 zaa'idah letters (ا، ا، ن) mein se kaunsa ism faail ki علامت hai aur kaunsa تثنیہ ki?

61. **Slide 24 Rows 4 + 7:** کَرِیْمٌ aur شَرِیْفٌ — wazn dono ka **فَعِیْلٌ**. Likely qism kya hai (builder gloss)? Sub Topic 1.3 Slide 19 se konsi qism cross-match hoti hai?

62. **مادہ** kya hai? (Slide 24 ka title bracket)

63. **Slide 25 ka master rule:** Ism jamid ke اوزان kitne harfi ho sakte? Ism masdar aur mushtaq ke kitne? **Farq batao + wajah** (builder gloss).

64. **Slide 25 examples:** 3-harfi / 4-harfi / 5-harfi mein se ek-ek misaal + wazn batao (PDF se).

65. **Slide 25 نوٹ:** Ism ke اوزان ki مکمل تفصیل kis kitab mein milegi? (forward-ref kitab name)

---

### Sub Topic 1.4 closure block (Sub Topic MUKAMMAL — Slides 21-26)

p-025 + p-026 par total **6 slides** cover hue:
- **Slide 21 (p-025)** = cover
- **Slide 22 (p-025)** = Mauzun/Meezan/Wazn tareefein + method + 3-pair example table
- **Slide 23 (p-025)** = حروف اصلی pehchaan + Fa/Ain/Lam Kalimah terminology + Note
- **Slide 24 (p-026)** = 7-misaal table (wazn-extraction practical application) + مادہ ka taaruf
- **Slide 25 (p-026)** = اسم ke اوزان (3/4/5 harfi taqseem) + paragraph rule + Note (forward-ref to معلم الابواب والخاصیات)
- **Slide 26 (p-026)** = khatima exercise bar

**Sub Topic 1.4 ne kya diya:**
- **Wazn ka concept formally introduce kiya** (Mauzun/Meezan/Wazn = 3 buniyadi terms).
- **Method** practical hai (mauzun ka shakal → meezan select → same harakaat lagao).
- **Root vs Zaa'idah pehchaan** ki kasoti = meezan ke huroof ke muqaabile.
- **3 root letter labels** (فا/عین/لام کلمہ).
- **مادہ** = synonym for حروف اصلی.
- **Aur 4 naye waznein PDF-attested:** فَعِیْلٌ (kareem-style), فَاعِلَانِ (dual), فَاعِلُوْنَ (m. plural), فَعْلَلٌ (4-letter), فَعْلَلِلٌ (5-letter) — plus pehle se introduced فَعْلٌ, فَاعِلٌ, فِعْلٌ.
- **اسم ki letter-count taxonomy** + Ism qism × harfi count ka cross-rule.

**Sub Topic 1.3 ke builder gloss observations validated:**
- p-024 Slides 18-19 ki "Pattern observation" wala observation ke aage waznein hote hain (فَاعِل for faail, مَفْعُوْل for maf'ul, etc.) — Slide 23 ne **فَاعِل** ko explicitly attest kiya; Slide 24 ne **فَعِیْلٌ** ko bhi attest kar diya (Slide 19 ki سَمِیْعٌ ki sifat-e-mushabbaha observation).
- Baqi 4 waznein (مَفْعُوْل، اَفْعَل، مَفْعَل، مَفْعِل، مِفْعَال) **abhi PDF-formally introduce NAHI hui** — Sub Topics 1.5+ mein expected.

**Chart consideration (current status as of p-027 + 2026-05-29 chart audit):**
- **Chart 5 (deferred):** 2 of 6 ism-qism waznein (فَاعِل, فَعِیْل) PDF-attested; baqi 4 abhi nahi. Sub Topic 1.5 ka focus فعل ke waznein hai (not ism), so ism-qism wazn-label re-addition still pending future Sub Topics jab مَفْعُوْل، اَفْعَل، مَفْعَل، مِفْعَال PDF-attest hojayein.
- **Chart 6 BUILT 2026-05-29 — Wazn extraction system** (Sub Topic 1.4 topic-overview): Mauzun ↔ Meezan ↔ Wazn + 3 kalimah labels + Asli/Zaa'idah + 2 anchor examples (عِلْمٌ → فِعْلٌ all-asli case; عَالِمٌ → فَاعِلٌ with-zaa'idah case). 11 nodes, Source: PDF p-025 Slides 22-23. See `charts.md`.
- **Chart candidate (Sub Topic 1.5 — ab buildable hai, Slide 31 ne canonical names PDF-attest kar diye):** "6 ابواب master overview chart" — 6 baab nodes (ضَرَبَ، فَتَحَ، نَصَرَ، حَسِبَ، سَمِعَ، شَرُفَ) + wazn-pair labels + عین harakah (mazi→mudaari'). Source: PDF p-028 Slide 31. Rule 16 ab unlocked.
- **Chart candidate (alternate framing):** "9 → 6 ابواب derivation tree" — 3 mazi waznein × 3 mudaari' waznein grid, 6 cells filled (مستعمل) + 3 cells empty (Slide 30 ke 3 missing pairings). Slides 29 + 30 combine karta hai.
- **Chart candidate (low priority):** "Ism qism × harfi count" cross-grid (Slide 25's master rule). Master rule already clear in notes table.

**Aglay session p-030 = Slide 35+, Sub Topic 1.6 ka aaghaaz** — **Sub Topic 1.5 MUKAMMAL ho gayi p-029 ke saath** (Slides 27-34 cover hue). Per Slide 1 (p-018) ka TOC row 1.6 title — likely **"تعداد حروف کے اعتبار سے فعل کی اقسام"** (letter-count-based فعل classification — ثلاثی / رباعی + mujarrad/mazid breakdown expected). **PDF kholo aur dekho — Rule 16 strict**: لازم/متعدی, 14-sigha tables, ya specific باب-wise conjugation paradigms plant NAHI karna jab tak PDF formally introduce na kare.

---

### Sub Topic 1.5 — Naye terms (Slides 28-33)

#### باب / Baab (PDF Slide 29)

- **Urdu**: ماضی اور مضارع کے اوزان کو آپس میں ملانے سے بننے والی قسم (علم الصرف کی اصطلاح)
- **Roman Urdu**: Ek **conjugation category** — ماضی wazn + مضارع wazn ka combination jo verb ki قِسم decide karta hai. (Builder gloss — PDF p-027 par lughwi meaning nahi di: "chapter / door" yaad rakhne ke liye background help, formal definition future kitab mein.)
- **Quantity**: **6 ابواب** Arabic mein مستعمل hote (PDF Slide 29 ka master rule).
- **Pehchaan**: Baab ka core = **عین کلمہ ki harakah** ka mazi-mudaari' combination. E.g., ضَرَبَ + یَضْرِبُ ek alag baab; نَصَرَ + یَنْصُرُ doosra baab.
- **Source**: Sarf p-027, Slide 29

#### ابواب / Abwaab (PDF Slide 29)

- **Urdu**: باب کی جمع — "chapters"
- **Roman Urdu**: Plural of باب — yaani **multiple baabs**. Sub Topic 1.5 ka unwaan "فعل کے چھ ابواب" mein bhi yahi plural hai.
- **Source**: Sarf p-027, Slide 29

#### مستعمل / Musta'mal (PDF Slide 29)

- **Urdu**: استعمال میں آنے والا، رائج
- **Roman Urdu**: **Used / employed in practice** — Arabic mein actually use hone wala wazn-pairing.
- **Pehchaan**: Slide 29 ka master rule: "جو اوزان **مستعمل** ہیں، وہ چھ ہیں" — yaani 9 logical possibilities mein se sirf 6 Arabic-speakers actually use karte. Baqi 3 theoretically possible the magar مستعمل nahi.
- **Source**: Sarf p-027, Slide 29

#### صیغہ / Sayghah (PDF Slide 29 — formal first appearance)

- **Urdu**: فعل کی شکل (مثلاً پہلا صیغہ = third-person masculine singular form)
- **Roman Urdu**: A **form** / specific morphological variant of fi'l. Slide 29 mein PDF-attested: *"ماضی اور مضارع کا **پہلا صیغہ** ملا کر بولا جائے"*.
- **Pehchaan (builder gloss — PDF par yeh tafseel nahi)**: Aage conjugation tables mein **14-sigha** dekhenge — har sayghah ek alag form (3rd person, 2nd person, 1st person × singular/dual/plural × masculine/feminine, etc.). **پہلا صیغہ** ka exact morphological tafseel PDF p-027 par NAHI; future Sub Topics mein expected. Yeh classical Sarf ka core conjugation term hai.
- **Forward-defer**: 14-sigha tafseel + "pehla sayghah" ki specific identity future Sub Topics mein.
- **Source**: Sarf p-027, Slide 29 (term first PDF-attested yahaan).

#### عین کلمہ ki 3 harakaat → 3 ماضی waznein (PDF Slide 28 + 29)

| ماضی wazn | عین کلمہ par harakah | PDF examples (Slide 28) |
|---|---|---|
| **فَعَلَ** | fatha (zabar) | ضَرَبَ، نَصَرَ، فَتَحَ |
| **فَعِلَ** | kasrah (zer) | حَسِبَ، سَمِعَ |
| **فَعُلَ** | damma (pesh) | شَرُفَ |

**Source**: Sarf p-027, Slides 28 + 29

#### عین کلمہ ki 3 harakaat → 3 مضارع waznein (PDF Slide 28 + 29)

| مضارع wazn | عین کلمہ par harakah | PDF examples (Slide 28) |
|---|---|---|
| **یَفْعَلُ** | fatha | یَفْتَحُ، یَسْمَعُ |
| **یَفْعِلُ** | kasrah | یَضْرِبُ، یَحْسِبُ |
| **یَفْعُلُ** | damma | یَنْصُرُ، یَشْرُفُ |

**Source**: Sarf p-027, Slides 28 + 29

#### 6 PDF-shown باب pairings (PDF Slide 28 — builder gloss aggregates Slide 28's 6 mauzun pairs)

| # | ماضی pair | مضارع pair | Wazn pair |
|---|---|---|---|
| 1 | ضَرَبَ | یَضْرِبُ | فَعَلَ + یَفْعِلُ |
| 2 | نَصَرَ | یَنْصُرُ | فَعَلَ + یَفْعُلُ |
| 3 | فَتَحَ | یَفْتَحُ | فَعَلَ + یَفْعَلُ |
| 4 | حَسِبَ | یَحْسِبُ | فَعِلَ + یَفْعِلُ |
| 5 | سَمِعَ | یَسْمَعُ | فَعِلَ + یَفْعَلُ |
| 6 | شَرُفَ | یَشْرُفُ | فَعُلَ + یَفْعُلُ |

**Note**: PDF Slide 28 mein **6 ماضی + 6 مضارع examples** alag dikhaye gaye 3+3 sub-tables mein. **Pairing** (sub-table position-wise) **builder gloss** hai — Slide 29 paragraph *"ماضی اور مضارع کو جمع کر کے پڑھیں"* se derive hoti hai. Canonical Sarf baab naam (jaise "باب نَصَرَ", "باب ضَرَبَ") **PDF p-027 par formally NAHI** introduce hue — **p-028 Slide 31 par formally PDF-attest ho gaye**.

**Source**: Sarf p-027, Slide 28 (PDF examples) + Slide 29 (pairing logic). **Canonical 1-6 numbering Slide 31 (p-028) se** — positions ۲ aur ۳ (نَصَرَ ↔ فَتَحَ) Slide 28 builder-gloss aur Slide 31 canonical mein swap hain; **Slide 31 authoritative**.

---

#### 6 canonical ابواب — PDF Slide 31 (p-028) se formally introduced

Yeh **classical Sarf ki canonical 6 ابواب** hain — Slide 31 ne formally PDF-attest kiye:

> ⚠️ **Builder forward-pointer fence (Rule 16):** PDF Slide 31 ke cells mein sirf **wazn-pair + misaal** likhe hain — **"باب ۱" / "باب ضَرَبَ" style formal label PDF par NAHI tha**. Cells ka numbering (۱-۶) PDF par hai, aur misaalein (ضَرَبَ، فَتَحَ، ...) bhi PDF par hain. **"باب X" naming convention classical Sarf ki rasm hai jo builder ne PDF-attested misaalein ke saath couple ki — future Sub Topics mein expected jab kitab khud "باب X" labels formally use kare. Pehle uss waqt tak yeh fence yaad rakho** ke "باب ضَرَبَ" likhna = "wo wazn-pair jiska canonical misaal ضَرَبَ یَضْرِبُ hai".

| باب # | Wazn pair (ماضی + مضارع) | Canonical misaal | عین کلمہ ki harakaat (ماضی → مضارع) |
|---|---|---|---|
| **باب ۱** | فَعَلَ یَفْعِلُ | **ضَرَبَ یَضْرِبُ** | fatha → kasrah |
| **باب ۲** | فَعَلَ یَفْعَلُ | **فَتَحَ یَفْتَحُ** | fatha → fatha |
| **باب ۳** | فَعَلَ یَفْعُلُ | **نَصَرَ یَنْصُرُ** | fatha → damma |
| **باب ۴** | فَعِلَ یَفْعِلُ | **حَسِبَ یَحْسِبُ** | kasrah → kasrah |
| **باب ۵** | فَعِلَ یَفْعَلُ | **سَمِعَ یَسْمَعُ** | kasrah → fatha |
| **باب ۶** | فَعُلَ یَفْعُلُ | **شَرُفَ یَشْرُفُ** | damma → damma |

**Source**: Sarf p-028, Slide 31

---

#### Alternate misaalein — doosri Sarf kitabon mein (PDF Slide 31 Note se)

Slide 31 ka **نوٹ** ne 4 ابواب ke liye alternate canonical misaalein diye (jo doosri Sarf kitabon mein use hote hain):

| باب | Yeh kitab (primary) | Doosri kitabon mein (alternate) |
|---|---|---|
| (۱) | ضَرَبَ یَضْرِبُ | *(Note mein alternate nahi diya — apparently same)* |
| (۲) | فَتَحَ یَفْتَحُ | **مَنَعَ یَمْنَعُ** |
| (۳) | نَصَرَ یَنْصُرُ | **دَخَلَ یَدْخُلُ** *aur* **طَلَبَ یَطْلُبُ** (do alternates) |
| (۴) | حَسِبَ یَحْسِبُ | *(Note mein alternate nahi diya — apparently same)* |
| (۵) | سَمِعَ یَسْمَعُ | **عَلِمَ یَعْلَمُ** |
| (۶) | شَرُفَ یَشْرُفُ | **کَرُمَ یَکْرُمُ** |

**Pehchaan ka rule**: Saare 6 abwaab structurally same hi hain — **sirf misaal-lafz badal jata hai, wazn-pair (mazi-mudaari' harakaat ka pattern) wahi rehta hai**. E.g., agar doosri kitab mein "باب کَرُمَ یَکْرُمُ" mile, samjh jana ke woh **yeh kitab ka باب شَرُفَ** hi hai (same wazn فَعُلَ یَفْعُلُ).

**Source**: Sarf p-028, Slide 31 Note

---

#### گروپ / Group (PDF Slide 32 — Urdu/English borrowing)

- **Urdu**: گروپ — "group" ka Urdu form (English borrowing, kitab ne directly use kiya)
- **Roman Urdu**: A **classification group / cluster** based on shared property. Sub Topic 1.5 mein Slide 32 ne 6 ابواب ko **harakaat ki bunyaad par 3 groups** mein arrange kiya — ماضی side aur مضارع side dono.
- **Pehchaan**: Group = abwaab ka same-harakah-on-عین cluster. **ماضی 3 groups** (fatha-3, kasrah-2, damma-1) aur **مضارع 3 groups** (fatha-2, kasrah-2, damma-2).
- **Source**: Sarf p-029, Slide 32

---

#### علامت / علامات / Alaamat (PDF Slide 33)

- **Urdu**: نشانی، پہچان کا ذریعہ
- **Roman Urdu**: **Signature / identifying mark / fingerprint** — har باب ki **unique harakaat-based identification**.
- **Pehchaan**: Slide 33 ne har باب ki علامت Urdu prose mein di — e.g., باب ۱ ki علامت = "ماضی مفتوح العین اور مضارع مکسور العین". Yeh signature unique hai (koi doosra باب same signature nahi rakhta).
- **Plural**: علامات (signatures, identifying marks)
- **Naye sub-terms (Slide 33 par PDF-attested)**:
  - **مفتوح العین** = ع par fatha
  - **مکسور العین** = ع par kasrah
  - **مضموم العین** = ع par damma
- **Source**: Sarf p-029, Slide 33

---

#### فُعِلَ / Fu'ila (PDF Slide 32 fa'ida — **ماضی مجہول universal wazn**)

- **Urdu**: ماضی مجہول کا عمومی وزن — "ف پر ضمہ، ع پر کسرہ، ل پر فتحہ"
- **Roman Urdu**: **Universal ماضی مجہول wazn** — sare 6 ابواب ke liye **same**.
- **Harakaat**: ف-damma + ع-kasrah + ل-fatha → **فُعِلَ**
- **Misaal (builder gloss — PDF par individual mujhol examples nahi diye gaye is page par)**: agar نَصَرَ ka مجہول form bane to **نُصِرَ** (universal فُعِلَ pattern par).
- **Cross-link**: Sub Topic 1.2 Slide 9 mein **Ma'lum/Majhul** ka concept aaya tha (شَرِبَ vs شُرِبَ). Slide 32 ne ab **formal wazn** dia.
- **Pehchaan rule**: **Har باب** ke liye yahi wazn — separate 6 majhol waznein nahi.
- **Source**: Sarf p-029, Slide 32 fa'ida

---

#### یُفْعَلُ / Yuf'alu (PDF Slide 32 fa'ida — **مضارع مجہول universal wazn**)

- **Urdu**: مضارع مجہول کا عمومی وزن — "ی پر ضمہ، ف پر سکون، ع پر فتحہ، ل پر ضمہ"
- **Roman Urdu**: **Universal مضارع مجہول wazn** — sare 6 ابواب ke liye **same**.
- **Harakaat**: یا-damma + ف-sukoon + ع-fatha + ل-damma → **یُفْعَلُ**
- **Misaal (builder gloss)**: agar یَنْصُرُ ka مجہول form bane to **یُنْصَرُ** (universal یُفْعَلُ pattern par).
- **Pehchaan rule**: **Har باب** ke liye yahi wazn — separate 6 mudaari'-majhol waznein nahi.
- **Source**: Sarf p-029, Slide 32 fa'ida

---

### Sub Topic 1.5 — Yaad rakho (Slides 27-34 — **MUKAMMAL**)

> **Sub Topic 1.5 = classical Sarf ka conjugation engine ka aaghaaz** — yeh foundation hai jis par saare future paradigms (14-sigha tables, abwaab-wise conjugation) khare hote.

45. **Roman:** **Sub Topic 1.5 ka core concept (Slide 29):**
   - فعل ki har shakal ki **پہچان** = uska **بَاب**.
   - Baab decide karne ka tareeqa = **ماضی wazn + مضارع wazn ka combination** dekho.
   - Decisive factor = **عین کلمہ ki harakah** (fa aur lam kalimah ki harakah same rehti, sirf middle change hoti).

46. **Roman:** **Fi'l ka wazn nikalne ka method (Slide 28):** Bilkul wahi method jo اسم par tha (Sub Topic 1.4 Slide 22) — mauzun ki shakal dekho → meezan select karo → same harakaat lagao. **Method universal hai** ism aur fi'l dono ke liye.

47. **Roman:** **3 ماضی waznein** (Slide 28 + 29):
   - **فَعَلَ** (عین par fatha) — e.g., ضَرَبَ، نَصَرَ، فَتَحَ
   - **فَعِلَ** (عین par kasrah) — e.g., حَسِبَ، سَمِعَ
   - **فَعُلَ** (عین par damma) — e.g., شَرُفَ

48. **Roman:** **3 مضارع waznein** (Slide 28 + 29):
   - **یَفْعَلُ** (عین par fatha) — e.g., یَفْتَحُ، یَسْمَعُ
   - **یَفْعِلُ** (عین par kasrah) — e.g., یَضْرِبُ، یَحْسِبُ
   - **یَفْعُلُ** (عین par damma) — e.g., یَنْصُرُ، یَشْرُفُ

49. **Roman:** **MASTER RULE — 9 vs 6 ابواب (Slide 29 ka paragraph 2):**
   - 3 ماضی × 3 مضارع = **9 logical possibilities** (سیٹ).
   - Magar sirf **6 مستعمل** (used in practice) Arabic mein.
   - In 6 ko **"چھ ابواب"** kehte = علم الصرف ki اصطلاح.
   - **3 missing pairings** PDF par named-list nahi — magar **Slide 30 ke 3 + 2 + 1 structure se structurally derive ho jaate hain** (point 54 dekho).

50. **Roman:** **6 PDF-shown pairings (Slide 28 ka 6-pairs table — builder gloss):** ضَرَبَ+یَضْرِبُ (فَعَلَ+یَفْعِلُ) / نَصَرَ+یَنْصُرُ (فَعَلَ+یَفْعُلُ) / فَتَحَ+یَفْتَحُ (فَعَلَ+یَفْعَلُ) / حَسِبَ+یَحْسِبُ (فَعِلَ+یَفْعِلُ) / سَمِعَ+یَسْمَعُ (فَعِلَ+یَفْعَلُ) / شَرُفَ+یَشْرُفُ (فَعُلَ+یَفْعُلُ). **Yeh 6 ابواب hain jin ki tafseel aage aati hai.**

51. **Roman:** **Naya term "صیغہ" PDF-attested (Slide 29):** "Pehla sayghah" — exact morphological identity PDF par NAHI di (future Sub Topics mein expected). Yeh classical Sarf ka core conjugation term hai — saare 14-sigha tables aage isi se develop honge (builder gloss — 14-sigha bhi forward-ref).

52. **Roman (cross-Sub-Topic 1.4 connection):** Sub Topic 1.4 mein method اسم par sikhayi (Slide 22). Sub Topic 1.5 ne wahi method فعل par bhi apply ki — **universal wazn-extraction algorithm** confirmed. Sub Topic 1.4 mein "حروف اصلیہ vs زائدہ" pehchaan; Sub Topic 1.5 mein "عین کلمہ ki harakah" decisive factor ban gayi باب identification ke liye.

53. **Roman:** **Slide 30 ka algebraic master rule — 3 + 2 + 1 = 6:**
   - **فَعَلَ** (mazi fatha) → **3 mudaari' waznein** (fatha, kasrah, damma) → **3 سیٹ**
   - **فَعِلَ** (mazi kasrah) → **2 mudaari' waznein** (fatha, kasrah; damma missing) → **2 سیٹ**
   - **فَعُلَ** (mazi damma) → **1 mudaari' wazn** (sirf damma; fatha aur kasrah missing) → **1 سیٹ**
   - **Total: 3 + 2 + 1 = 6 سیٹ = 6 ابواب** ✓ (Slide 29 ka 9→6 master rule ka algebraic proof yeh slide hai)

54. **Roman:** **3 missing pairings structurally identified (Slide 30 se infer)** — builder gloss enumeration:
   - **فَعِلَ + یَفْعُلُ** (mazi kasrah → mudaari' damma)
   - **فَعُلَ + یَفْعَلُ** (mazi damma → mudaari' fatha)
   - **فَعُلَ + یَفْعِلُ** (mazi damma → mudaari' kasrah)

   (Yeh wahi 3 hain jo Slide 29 ke "9-6=3 musta'mal nahi" se hint hue the. Slide 30 ka 3+2+1 structure ne unko derivationally identify kar diya.)

55. **Roman:** **CANONICAL 6 ابواب — Slide 31 ne 6 wazn-pairs + 6 misaalein PDF-introduce kiye** *(builder forward-pointer: "باب X" prefix naming convention classical Sarf ki rasm hai, Slide 31 cells par formal "باب X" label nahi tha — sirf wazn-pair + misaal)*:
   1. **باب ضَرَبَ** (= wazn-pair jiska misaal ضَرَبَ یَضْرِبُ) — فَعَلَ یَفْعِلُ (fatha → kasrah)
   2. **باب فَتَحَ** — فَعَلَ یَفْعَلُ (fatha → fatha)
   3. **باب نَصَرَ** — فَعَلَ یَفْعُلُ (fatha → damma)
   4. **باب حَسِبَ** — فَعِلَ یَفْعِلُ (kasrah → kasrah)
   5. **باب سَمِعَ** — فَعِلَ یَفْعَلُ (kasrah → fatha)
   6. **باب شَرُفَ** — فَعُلَ یَفْعُلُ (damma → damma)

56. **Roman:** **Alternate misaalein doosri Sarf kitabon mein (Slide 31 Note):**
   - باب فَتَحَ ki jagah → **مَنَعَ یَمْنَعُ**
   - باب نَصَرَ ki jagah → **دَخَلَ یَدْخُلُ** *aur* **طَلَبَ یَطْلُبُ** (do alternates)
   - باب سَمِعَ ki jagah → **عَلِمَ یَعْلَمُ**
   - باب شَرُفَ ki jagah → **کَرُمَ یَکْرُمُ**
   - باب ضَرَبَ aur باب حَسِبَ — Note mein alternate nahi diya.
   - **Rule**: Misaal-lafz badle, **wazn-pair pattern wahi rehta**. کَرُمَ mile to samjho woh isi باب شَرُفَ hi hai.

57. **Roman:** **Slide 28 builder-gloss numbering vs Slide 31 canonical numbering** — positions ۲ aur ۳ swap hue:
   - Slide 28 builder-gloss tha: ۱ ضَرَبَ، ۲ نَصَرَ، ۳ فَتَحَ، ۴-۶ same.
   - Slide 31 canonical hai: ۱ ضَرَبَ، **۲ فَتَحَ**، **۳ نَصَرَ**، ۴-۶ same.
   - **Slide 31 authoritative** — canonical 1-6 ke liye Slide 31 reference rakho.

58. **Roman:** **Slide 32 ka naya framing — harakaat-based groupings (independent of Slide 30):**
   - **ماضی side**: 3 groups by عین کلمہ harakah — fatha (3 verbs: ضَرَبَ، فَتَحَ، نَصَرَ), kasrah (2 verbs: حَسِبَ، سَمِعَ), damma (1 verb: شَرُفَ) = **3+2+1=6** ✓
   - **مضارع side**: 3 groups — fatha (2 verbs), kasrah (2 verbs), damma (2 verbs) = **2+2+2=6** ✓
   - Asymmetric distribution: ماضی side mein 3+2+1, مضارع side mein 2+2+2. Same 6 ابواب, alag-alag perspectives se group ho rahe.

59. **Roman:** **Slide 32 fa'ida — مجہول universal forms** (PDF-attested):
   - **ماضی مجہول universal wazn: فُعِلَ** (ف-damma, ع-kasrah, ل-fatha)
   - **مضارع مجہول universal wazn: یُفْعَلُ** (یا-damma, ف-sukoon, ع-fatha, ل-damma)
   - **Saare 6 ابواب** ke liye yahi wazn — alag majhol waznein NAHI hain.
   - Sub Topic 1.2 Slide 9 mein Ma'lum/Majhul concept tha, ab formal wazn confirmed.

60. **Roman:** **Slide 33 — har باب ki علامت (signature):**
   - **علامت** = unique harakaat-based fingerprint of a باب.
   - Format: "ماضی [X] العین اور مضارع [Y] العین" — where X aur Y mein se ek hi value ho to "**بھی**" lafz add hota.
   - 6 unique علامات = 6 distinct ابواب ki definitive identification.
   - **Naye terminology terms**: مفتوح العین (fatha-on-ع), مکسور العین (kasrah-on-ع), مضموم العین (damma-on-ع).

61. **Roman:** **3 alag presentations of same 6 ابواب** (Sub Topic 1.5 ka teaching scaffolding):
   - **Numerical foundation** (Slides 28-29): 9 logical → 6 مستعمل
   - **Canonical reference** (Slides 30-31): 3+2+1 algebraic + canonical names
   - **Pattern recognition** (Slides 32-33): harakaat groupings + علامات signatures
   - **Mukammal Sub Topic 1.5** — Slide 34 = exercise bar khatima.

62. **Roman (Sub Topic 1.5 ka core takeaway):** Agar koi nayi فعل dekho aur uska باب identify karna ho — Slide 33 ki علامات follow karo:
   - **ماضی ke عین ki harakah** dekho (fatha/kasrah/damma)
   - **مضارع ke عین ki harakah** dekho (fatha/kasrah/damma)
   - Dono ko combine karke 6 mein se ek signature match karo → باب identified ✓

---

### Sub Topic 1.5 — Sabak sawal (khud test karein — Slides 27-34 — **MUKAMMAL**)

Book band kar ke jawab dene ki koshish karein:

66. **Sub Topic 1.5 ka unwaan** kya hai (Arabic)? Aur uska Urdu/English meaning?
67. **Fi'l ka wazn nikalne ka method** (Slide 28) — yeh اسم ke method (Sub Topic 1.4 Slide 22) se kitna different hai?
68. **3 ماضی waznein** + un par عین کلمہ ki harakah batao. Har wazn ka **kam-az-kam ek PDF misaal** do.
69. **3 مضارع waznein** + un par عین کلمہ ki harakah batao. Har wazn ka kam-az-kam ek PDF misaal do.
70. **Slide 29 paragraph 2 ka master rule:** 3 ماضی × 3 مضارع = kitne logical combinations? Kitne مستعمل? Logical-but-not-used = kitne?
71. **6 PDF-shown pairings** yaad karwao (builder gloss table se): mazi pair + mudaari' pair + wazn pair. Ek complete pairing batao.
72. **بَاب** ka tareef kya hai (PDF Slide 29 ka concept)? اس کا decisive factor kya hai (mazi-mudaari' combination mein)?
73. **مستعمل** ka literal matlab kya hai? Slide 29 ke context mein iska kya kaam hai?
74. **صیغہ** lafz PDF par pehli baar Slide 29 par appear hua — uska context kya tha?
75. **Slide 30 ka algebraic master rule** — فَعَلَ se kitne mudaari' waznein? فَعِلَ se kitne? فَعُلَ se kitne? Total kitne? (3 + 2 + 1 = ?)
76. **Slide 30 se structurally inferable 3 missing pairings** kaun se hain (mazi + mudaari' harakaat combinations)?
77. **Slide 31 ke 6 canonical canonical baab naam** yaad karwao — har baab ka misaal + wazn-pair + عین کلمہ ki harakaat (mazi → mudaari').
78. **Slide 31 Note** ke alternate misaalein — kin 4 ابواب ke liye alternates diye gaye hain doosri kitabon se? (Tip: 2 ابواب ke liye Note mein alternate mention NAHI hua.)
79. **باب نَصَرَ** (= wo wazn-pair jiska canonical misaal Slide 31 par نَصَرَ یَنْصُرُ hai — *yaad rakho: "باب X" naming builder convention hai*) ka wazn-pair kya hai? Uska doosri kitabon mein alternate misaal kya hai (Slide 31 Note se — Tip: 2 alternates hain)?
80. **شَرُفَ یَشْرُفُ vs کَرُمَ یَکْرُمُ** — yeh dono different ابواب hain ya same? Wazn-pair check karke samjhao.
81. **Slide 32 ka naya framing** — ماضی side ka 3+2+1 grouping batao + مضارع side ka 2+2+2 grouping. Yeh Slide 30 ke 3+2+1 se kis tareeqe se different perspective deta hai?
82. **Slide 32 fa'ida — مجہول universal forms**: ماضی مجہول ka wazn? مضارع مجہول ka wazn? **Saare 6 ابواب** ke liye yahi waznein hain ya har باب ka apna majhol wazn hai?
83. **عَلَامَت** (Slide 33 par naya term) ka matlab batao. **6 ابواب ki علامات** mein se kam-az-kam 3 yaad karwao — format: "ماضی X العین + مضارع Y العین".
84. Naye terminology — **مفتوح العین**، **مکسور العین**، **مضموم العین** — har ek ka exact matlab batao. Yeh kis context mein use hota?
85. **"بھی" lafz ka role** Slide 33 ki علامات mein — kab use hota aur kab nahi? (Hint: 3 rows mein use hua, 3 mein nahi — kyun?)
86. **Sub Topic 1.5 MUKAMMAL** — Slides 27-34 ka 1-line khulasa batao. Slide 28-29 vs 30-31 vs 32-33 ka teaching purpose different kya tha?
87. **Practical scenario**: Agar koi nayi فعل dekho jiska ماضی **عین par kasrah** aur مضارع **عین par fatha** ho — yeh konsa باب hai (canonical misaal + number Slide 31 se)?

---

#### Sub Topic 1.3 closure block (preserved for reference)

p-024 par 3 slides cover hue (18 + 19 + 20). **Sub Topic 1.3 MUKAMMAL** ho gaya — total **6 slides ka span (15-20)**. **Slide 20 = exercise bar** (Slide 5 + Slide 14 jaisa pattern), Sub Topic 1.3 ka khatima confirm karta hai. **Slide 16 Note ka formula fully delivered:** 1 masdar → 12 mushtaq cheezein (6 fi'l + 6 ism) ✓ + matching exercise (Slide 19). **Chart 5 BUILT 2026-05-28** — Masdar derivation tree topic-overview, 15 nodes, clean PASS after 2 fix cycles.
