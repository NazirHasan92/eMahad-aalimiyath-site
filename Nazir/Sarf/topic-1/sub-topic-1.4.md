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

# Sub Topic 1.4 — حروف اصلی کی پہچان (Huroof Asli ki pehchaan — wazn ka formal taaruf)

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

