<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');
  @font-face {
    font-family: 'UrduArabicScript';
    src: local('Noori Nastaliq'), local('Jameel Noori Nastaleeq'), local('Alvi Nastaleeq'),
         local('Faiz Lahori Nastaleeq'), local('Noto Nastaliq Urdu');
    unicode-range: U+0600-06FF, U+0750-077F, U+FB50-FDFF, U+FE70-FEFF;
    size-adjust: 135%;
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
  th, td { padding: 0.75em 1em; border: 1px solid #ccc; line-height: 1.95; vertical-align: top; }
  th { background: #e8f4f4; font-weight: 700; color: #064e3b; }
  blockquote { border-left: 5px solid #064e3b; padding: 0.7em 1.3em; background: #f3faf6; margin: 1.3em 0; }
  code { background: #f4f4f4; padding: 0.18em 0.45em; border-radius: 3px; color: #be123c; font-size: 0.9em; }
  pre { background: #f7f7f7; padding: 1em 1.2em; border-radius: 6px; border: 1px solid #eee; }
</style>

# Nahw — Concept Charts (Mermaid)

> **One chart = one concept. Built during teaching when a concept genuinely needs visual representation.**
>
> Rules (full version in CLAUDE.md → Charts discipline):
> - Beginner charts: max 6-8 nodes, 2-3 color roles, NO subgraphs
> - Topic-overview charts (built AFTER all sub-concepts taught): max 16 nodes, one level of subgraph max
> - **Never use comprehensive overview chart to OPEN a topic for a beginner**
> - **I'rab tables → `irab-tables.md`, NOT here.** Mermaid is for trees, processes, dependency parses, concept maps.

---

## Standard `classDef` palette (paste into every chart)

> Niche sample tree palette aur shapes demo karta hai:

```mermaid
flowchart TD
  R["Root<br/>topic node"]:::root
  M["Main<br/>concept"]:::main
  S["Sub<br/>rule/detail"]:::sub
  L["Leaf<br/>terminal"]:::leaf
  E["Example<br/>misaal"]:::ex

  R --> M
  R --> E
  M --> S
  M --> L

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
  classDef ex   fill:#ffe4e6,stroke:#be123c,color:#881337;
```

Apne charts mein sirf wahi `classDef` lines paste karein jo zaroori hain.

Semantics (never deviate):
- **root** = topic node
- **main** = main concept
- **sub** = rule / detail
- **leaf** = terminal leaf
- **ex** = example

---

## Chart index

| # | Chart | Source pages | Added |
|---|-------|---------------|-------|
| 1 | Kalimah → 3 qismein (Mufrad taxonomy) | PDF p-06, p-07 | 2026-05-28 |
| 2 | Lafz → Mauzu'/Muhmal → Mufrad/Murakkab (parent context) | PDF p-06, p-07 | 2026-05-28 |
| 3 | Jumla Khabariya → Ismiya / Fi'liya (with elements) | PDF p-08 | 2026-05-28 |
| 4 | Jumla Insha'iya → 10 qismein (with one example each) | PDF p-09, p-10 | 2026-05-28 |
| 5 | Murakkab Ghair Mufid → 3 qismein (Idafi/Bina'i/Mana' Sarf) | PDF p-10, p-11 | 2026-05-28 |
| 6 | Mu'arrab-Mabni concrete demo (Zayd 3 forms + Hadha 3 forms) | PDF p-16 | 2026-05-28 |
| 7 | Alamat-e-Ism (11 alamat grouped) | PDF p-14 | 2026-05-28 |
| 8 | Fasl 2 review — Jumla ki 2 taqseemein (Zaati 4 + Sifati 6) | PDF p-12, p-13 | 2026-05-28 |
| 9 | Alamat-e-Fi'l (8) + Alamat-e-Harf (negative + 3 link-types) | PDF p-15 | 2026-05-28 |
| 10 | **Mudmaraat (Qism #1) full taxonomy** — 3 i'rab × 2 attachment patterns × 6 paradigm tables × 14 forms = 84 total | PDF p-18, p-19, p-20 | 2026-05-30 |
| 11 | **Asma-e-Mausoolah (Qism #2)** — 10 forms (gender × number) + 3 exceptions + Sila rule | PDF p-20 | 2026-05-30 |
| 12 | **Asma-e-Ishara (Qism #3)** — 10 forms (Qareeb × Ba'eed × gender × number) + Mushar Ilayh rule | PDF p-21 | 2026-05-30 |

---

## Chart 1 — Kalimah (Mufrad) taxonomy

**Source:** PDF p-06 (Kalimah ki 3 qismein + Ism tareef + Ism ki 3 qismein), p-07 (Jamid/Masdar/Mushtaq + Fi'l + Harf tareefein + Harf ki 2 qismein).

**Concept:** *کلمہ ki 3 qismein* + un mein se Ism aur Harf ki andruni qismein. Yeh **Mufrad branch** ka mukammal review chart hai (Murakkab branch alag chart mein aayega).

**Read karne ka tareeqa:**
- **Sabz emerald** (root) = topic
- **Teal** (main) = 3 buniyadi qismein
- **Amber** (sub) = rule / cross-reference
- **Green** (leaf) = terminal qismein

```mermaid
flowchart TD
  K["کلمہ (Kalimah)<br/>= مفرد<br/>akela bamaani lafz"]:::root

  K --> I["اِسم (Ism)<br/>akela samjha jaye<br/>+ zamana NAHI"]:::main
  K --> F["فِعل (Fi'l)<br/>akela samjha jaye<br/>+ zamana HAI"]:::main
  K --> H["حَرف (Harf)<br/>akela bematlab<br/>(jodne wala)"]:::main

  I --> J["جَامِد (Jamid)<br/>na bana, na bante"]:::leaf
  I --> M["مَصدر (Masdar)<br/>source (na bana,<br/>bohot bante)"]:::leaf
  I --> S["مُشتَق (Mushtaq)<br/>Masdar se bana"]:::leaf

  F --> FQ["4 qismein:<br/>Maazi / Muzaari /<br/>Amr / Nahi<br/>→ tareefein Sarf mein"]:::sub

  H --> HA["عَامِل (Amil)"]:::leaf
  H --> HG["غَیر عَامِل<br/>(Ghair Amil)"]:::leaf

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check (CLAUDE.md rules):**
- 10 nodes (limit: 16 for topic-overview) ✅
- 4 classDefs (limit: 5) ✅
- No subgraphs ✅
- Each Arabic label paired with Roman transliteration ✅

**Kaise istemaal karein:**
- Chart kholo → kisi bhi node par dekho → us ki tareef yaad karo (notes.md mein dekhna minus points)
- "Fi'l ki 4 qismein" wala amber box reminder hai ke yeh aage Sarf book se aata hai
- Khali nodes (jaise Amil/Ghair Amil) jin ki tareef abhi nahi mili — yeh **placeholders** hain Bab 2 ke liye

**Aage ke charts** (Chart 2-5 batch — added 2026-05-28 after Fasl 1 mukammal hua):
- ✅ Chart 2 (added below)
- ✅ Chart 3 (added below)
- ✅ Chart 4 (added below)
- ✅ Chart 5 (added below)

---

## Chart 2 — Lafz parent tree (Mauzu'/Muhmal + Mufrad/Murakkab)

**Source:** PDF p-06 (Lafz tareef + Mauzu'/Muhmal + Mufrad/Murakkab), p-07 (Mufrad=Kalimah + Murakkab=Jumla equivalence).

**Concept:** Chart 1 ke "above" wala context — Kalimah aur Jumla kahaan se aate hain. Yeh **Fasl 1 ka master overview** hai. Leaf nodes (Chart 1, 3, 4, 5) ki taraf reference karte hain.

```mermaid
flowchart TD
  L["لَفظ (Lafz)<br/>jo awaaz<br/>muh se nikle"]:::root

  L --> MZ["مَوضُوع (Mauzu')<br/>bamaani lafz"]:::main
  L --> MH["مُہْمَل (Muhmal)<br/>bematlab — Nahw<br/>se khaarij"]:::leaf

  MZ --> MF["مُفرَد = کَلِمَہ<br/>(akela bamaani)<br/>→ Chart 1"]:::sub
  MZ --> MR["مُرَکَّب<br/>(2+ kalimon ka jod)"]:::main

  MR --> MU["مُفِید = جُملہ = کَلَام<br/>→ Chart 3 (Khabariya)<br/>→ Chart 4 (Insha'iya)"]:::sub
  MR --> GM["غَیر مُفِید<br/>→ Chart 5"]:::sub

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 7 nodes, 4 classDefs, no subgraphs. ✅

**Kaise istemaal:** Bara picture dekhne ke liye — Kalimah aur Kalam dono ki taxonomical position dikhata hai. Detailed sub-trees ke liye linked charts dekho.

---

## Chart 3 — Jumla Khabariya structure (Ismiya / Fi'liya + elements)

**Source:** PDF p-08 (Khabariya tareef + Ismiya/Fi'liya + Mubtada/Khabar/Fi'l/Fa'il + Musnad/MI cross-labels).

**Concept:** Jumla Khabariya ke 2 qismein aur har qism ke 2 ajzaa kya naam rakhte hain. Examples included.

```mermaid
flowchart TD
  K["جُملہ خَبَرِیَّہ<br/>(sach/jhoot keh sakein)"]:::root

  K --> I["جُملہ اِسمِیَّہ<br/>(pehla hissa Ism;<br/>doosra Ism ya Fi'l)"]:::main
  K --> F["جُملہ فِعلِیَّہ<br/>(pehla Fi'l + Fa'il)"]:::main

  I --> IM["مُبتَدا (Mubtada)<br/>= Musnad Ilayh<br/>pehla hissa"]:::leaf
  I --> IK["خَبَر (Khabar)<br/>= Musnad<br/>doosra hissa"]:::leaf
  I --> IE["misaal:<br/>زَیْدٌ عَالِمٌ<br/>زَیْدٌ عَلِمَ"]:::ex

  F --> FF["فِعل (Fi'l)<br/>= Musnad<br/>pehla hissa"]:::leaf
  F --> FA["فَاعِل (Fa'il)<br/>= Musnad Ilayh<br/>doosra hissa"]:::leaf
  F --> FE["misaal:<br/>عَلِمَ زَیْدٌ<br/>سَمِعَ بَکْرٌ"]:::ex

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
  classDef ex   fill:#ffe4e6,stroke:#be123c,color:#881337;
```

**Density check:** 9 nodes, 4 classDefs, no subgraphs. ✅

**Mukhya insight is chart se:** Ismiya aur Fi'liya ke elements ke 2-2 naam hote hain — ek "general" (Musnad/MI) aur ek "context-specific" (Mubtada-Khabar / Fi'l-Fa'il). Yeh aapko ek hi structure ko 2 lenses se dekhna sikhata hai.

**Note (chart mein nahi):** Insha'iya bhi Jumla ki qism hai, lekin Khabariya se elements alag hain (Insha'iya mein Mubtada/Khabar wali structure nahi hoti generally). Insha'iya ka apna chart hai (Chart 4).

---

## Chart 4 — Jumla Insha'iya ki 10 qismein

**Source:** PDF p-09 (qismein 1-6) + p-10 (qismein 7-10).

**Concept:** Insha'iya ki 10 sub-qismein, har ek ka ek-line description + Arabic example. **Yeh chart ka density limit (16) ke qareeb hai — review chart, beginner-open chart NAHI.**

```mermaid
flowchart TD
  IN["جُملہ اِنشَائِیَّہ<br/>(sach/jhoot na keh sakein)"]:::root

  IN --> Q1["اَمر (Amr)<br/>hukm<br/>اِضْرِبْ"]:::leaf
  IN --> Q2["نَہی (Nahi)<br/>mana<br/>لَا تَضْرِبْ"]:::leaf
  IN --> Q3["اِستِفہَام (Istefham)<br/>sawal<br/>هَلْ ضَرَبَ زَیْدٌ؟"]:::leaf
  IN --> Q4["تَمَنِّی (Tamanni)<br/>kaash<br/>لَیْتَ زَیْدًا حَاضِرٌ"]:::leaf
  IN --> Q5["تَرَجِّی (Tarajji)<br/>ummeed<br/>لَعَلَّ عَمْرًوا غَائِبٌ"]:::leaf
  IN --> Q6["عُقُود (Uqood)<br/>muamla<br/>بِعْتُ وَاشْتَرَیْتُ"]:::leaf
  IN --> Q7["نِدَا (Nida)<br/>pukar<br/>يَا اَللهُ"]:::leaf
  IN --> Q8["عَرض (Arz)<br/>narmi se<br/>اَلَا تَأْتِيْنِيْ<br/>فَأُعْطِیْكَ دِیْنَارًا"]:::leaf
  IN --> Q9["قَسَم (Qasam)<br/>qasam<br/>وَاللهِ لَأَضْرِبَنَّ زَیْدًا"]:::leaf
  IN --> Q10["تَعَجُّب (Ta'ajjub)<br/>hairat<br/>مَا اَحْسَنَهٗ"]:::leaf

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 11 nodes, 2 classDefs, no subgraphs. ✅

**Memory mnemonic (chart ke baahar — 5 pairs):**
| Pair | Qismein |
|------|---------|
| Hukm | Amr / Nahi |
| Khwahish | Tamanni / Tarajji |
| Sawal/Muamla | Istefham / Uqood |
| Pukar/Narmi | Nida / Arz |
| Qasam/Hairat | Qasam / Ta'ajjub |

---

## Chart 5 — Murakkab Ghair Mufid → 3 qismein

**Source:** PDF p-10 (Ghair Mufid tareef + 3 qismein + Idafi tafseel) + p-11 (Bina'i khaatma + Mana' Sarf tareef + examples).

**Concept:** Ghair Mufid ki 3 sub-qismein ka distinguishing features ke saath comparison.

```mermaid
flowchart TD
  GM["مُرَکَّب غَیر مُفِید<br/>(khabar/talab nahi)"]:::root

  GM --> ID["مُرَکَّب اِضافی<br/>(nisbat ek ism ki<br/>doosre ki taraf)"]:::main
  GM --> BI["مُرَکَّب بِنائی<br/>(2 ism ek;<br/>donon par fatha)"]:::main
  GM --> MS["مُرَکَّب مَنَع صَرف<br/>(2 ism ek;<br/>sirf pehla maftooh)"]:::main

  ID --> IDR["مُضاف +<br/>مُضاف الیہ"]:::sub
  ID --> IDE["misaal:<br/>غُلَامُ زَیْدٍ"]:::ex

  BI --> BIE["misaal: اَحَدَ عَشَرَ<br/>(asal: اَحَدٌ وَعَشَرٌ)<br/>exception: اِثْنَا عَشَرَ"]:::ex

  MS --> MSE["misaal: بَعْلَبَكُّ<br/>(shehar — بَعْل+بَكٌّ)"]:::ex

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef ex   fill:#ffe4e6,stroke:#be123c,color:#881337;
```

**Density check:** 8 nodes, 4 classDefs, no subgraphs. ✅

**Bina'i vs Mana' Sarf farq table** (chart ke baahar):

| | Bina'i | Mana' Sarf |
|--|--------|-------------|
| 2 ism ek? | ✅ | ✅ |
| Rabt-wala harf? | ❌ | ❌ |
| Harakaat | **Dono** fatha | **Sirf pehla** maftooh |
| Word-type | Numbers 11-19 (PDF: *"أَحَدَ عَشَرَ سے تِسْعَۃَ عَشَرَ تک"*) | Shehar ka naam (PDF misaal sirf بَعْلَبَكُّ) |
| Misaal | اَحَدَ عَشَرَ | بَعْلَبَكُّ |

---

## Chart 6 — Mu'arrab vs Mabni: Concrete demo (Zayd 3 forms + Hadha 3 forms)

**Source:** PDF p-16 (Mu'arrab + Mabni tareefein + Mahall-e-I'rab + Zayd 3-form walkthrough + Hadha 3-form walkthrough — Block 4 + Block 5).

**Concept:** Section 11 ka **pivot example** visually. Same lemma (Zayd or Hadha) ko 3 jumlon mein dekho — Mu'arrab walay (Zayd) ka akhri **harakah** badalta (zer/zabar/pesh), Mabni walay (Hadha) ka kuch nahi badalta. Yeh chart i'rab system ki **foundation concept** dikhata.

**Read karne ka tareeqa:**
- **Sabz emerald** (root) = central question
- **Teal** (main) = Mu'arrab side (badalta) vs Mabni side (yaksaan)
- **Amber** (sub) = key insight (mahall-e-i'rab)
- **Pink** (ex) = book ke 6 misaal jumlay

```mermaid
flowchart TD
  R["آخری حرف کی تبدیلی?<br/>(Mu'arrab vs Mabni)"]:::root

  R --> MU["مُعرَب<br/>akhri harakah BADALTI<br/>misaal: زَیْد"]:::main
  R --> MA["مَبنی<br/>akhri harakah YAKSAAN<br/>misaal: هٰذَا"]:::main

  MU --> Z1["جَاءَ زَیْدٌ<br/>(د par ضمہ)"]:::ex
  MU --> Z2["رَأَیْتُ زَیْدًا<br/>(د par فتحہ)"]:::ex
  MU --> Z3["مَرَرْتُ بِزَیْدٍ<br/>(د par کسرہ)"]:::ex

  MA --> H1["جَاءَ هٰذَا"]:::ex
  MA --> H2["رَأَیْتُ هٰذَا"]:::ex
  MA --> H3["مَرَرْتُ بِهٰذَا"]:::ex

  MU --> MUI["محل اعراب = 'د'<br/>(same letter, alag harakah)"]:::sub

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef ex   fill:#ffe4e6,stroke:#be123c,color:#881337;
```

**Density check (CLAUDE.md rules):**
- 10 nodes (limit: 16 for topic-overview) ✅
- 4 classDefs (limit: 5) ✅
- No subgraphs ✅

**Kaise istemaal karein:**
- Mu'arrab side dekho — 3 misaal jumlon mein **akhri harakah** par focus (ٌ → ً → ٍ).
- Mabni side dekho — har misaal mein **هٰذَا exactly same** form.
- Mahall-e-i'rab insight: "د" (akhri letter) **same** rehta, harakah par change aata. Yeh i'rab ka **mechanism** hai.

**Cross-reference:** Section 11 (PDF p-16) ka full narrative walkthrough.

---

## Chart 7 — Alamat-e-Ism: 11 alamat in 4 thematic groups

**Source:** PDF p-14 (11 alamat-e-Ism with book ki misaalein).

**Concept:** Ism pehchanne ke 11 signs. 4 thematic groups mein arrange:
- **Word-edge markers** (kinaaron par dikhne wale): alamat #1-3
- **Syntactic role markers** (jumlay mein role): alamat #4-5
- **Morphological forms** (Sarf-side derivational): alamat #6-9 — forward-refs Sarf
- **Quality + femininity markers**: alamat #10-11

Yeh **identification toolkit** chart hai — koi Arabic lafz dekho, in 11 mein se koi bhi alamat milay, to woh **Ism** hai.

**Read karne ka tareeqa:**
- **Sabz emerald** (root) = Ism
- **Teal** (main) = 4 thematic groups
- **Green** (leaf) = 11 alamat with PDF misaalein

```mermaid
flowchart TD
  I["اِسم — pehchaan ke<br/>11 alamat (PDF p-14)"]:::root

  I --> G1["Group 1: Word-edge markers"]:::main
  I --> G2["Group 2: Syntactic role markers"]:::main
  I --> G3["Group 3: Morphological forms<br/>(Sarf forward-refs)"]:::main
  I --> G4["Group 4: Quality + femininity markers"]:::main

  G1 --> A1["1. الف لام shuru mein<br/>misaal: اَلْحَمْدُ"]:::leaf
  G1 --> A2["2. حرفِ جر shuru mein<br/>misaal: بِزَیْدِ"]:::leaf
  G1 --> A3["3. تنوین aakhir mein<br/>misaal: زَیْدٌ"]:::leaf

  G2 --> A4["4. مسند الیہ ho<br/>misaal: زَیْدٌ قَائِمٌ"]:::leaf
  G2 --> A5["5. مضاف ho<br/>misaal: غُلَامُ زَیْدٍ"]:::leaf

  G3 --> A6["6. مُصَغَّر<br/>misaal: قُرَیْشٌ، رُجَیْلٌ"]:::leaf
  G3 --> A7["7. منسوب<br/>misaal: بَغْدَادِيٌّ، هِنْدِيٌّ"]:::leaf
  G3 --> A8["8. تثنیہ<br/>misaal: رَجُلَانِ"]:::leaf
  G3 --> A9["9. جمع<br/>misaal: رِجَالٌ"]:::leaf

  G4 --> A10["10. موصوف ho<br/>misaal: رَجُلٌ کَرِیْمٌ"]:::leaf
  G4 --> A11["11. تائے متحرک aakhir mein<br/>misaal: ضَارِبَۃٌ"]:::leaf

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 16 nodes (limit: 16 for topic-overview ✅), 3 classDefs, no subgraphs ✅.

**Note on Group 3** (Morphological forms): Sarf book mein in 4 forms ki tafseel hai (Musaghghar/Mansoob/Tathniya/Jam'). Yahaan sirf naam + PDF misaal — yeh **identification signs** ke taur par hain, tafseeli morphology Sarf side ka kaam.

**4-group framing (chart ke baahar):** *(yeh 4-group thematic arrangement meri taraf se hai — book ne 11 alamat bina grouping ke list ki; grouping pedagogically helpful)*

**Harakaat verification (2026-05-29 direct PDF re-read):** Pichle round mein 2 validator queries uthayi thin (`بِزَیْدِ` vs `بِزَیْدٍ`, `رَجُلَانِ` vs `رَجُلَان`). 2026-05-29 ko **direct PDF p-14 image re-read** ne dono resolve kiye:
- **A2 example `بِزَیْدِ`**: PDF par `د` ke neeche **single kasra** (ek diagonal stroke) clear hai — NOT tanween-kasra. Chart aur Section 9 ka reading correct hai. **RESOLVED.**
- **A8 example `رَجُلَانِ`**: PDF par final `ن` ke neeche **kasra** dikhayi deti hai. Chart aur Section 9 ka reading correct hai. **RESOLVED.**
- **Pattern note** (memory-fill-patterns.md): Native validators ki harakaat-reading bias — jab validator finding ambiguous PDF image se conflict kare, builder ka direct PDF re-read final hota hai. Yeh chart par confirmation cycle ka canonical example bana.

---

## Chart 8 — Fasl 2 review: Jumla ki 2 taqseemein

**Source:** PDF p-12 (Zaati 4 qismein + Sifati heading + Mubaiyana start), p-13 (Sifati qismein 2-6 mukammal).

**Concept:** Fasl 2 ka **complete picture**. Jumla ko **2 alag aitebar** se taqseem karna:
- **بااعتبارِ ذات** (zaati — by inherent structure): 4 qismein → "اصل جملہ"
- **بااعتبارِ صفت** (sifati — by role/quality): 6 qismein

Yeh **topic-overview** chart hai — built after sub-concepts taught.

```mermaid
flowchart TD
  J["جُملہ (Fasl 2 ki<br/>2 taqseemein)"]:::root

  J --> Z["بااعتبارِ ذات<br/>4 qismein = 'اصل جملہ'"]:::main
  J --> S["بااعتبارِ صفت<br/>6 qismein"]:::main

  Z --> Z1["اسمیہ<br/>misaal: زَیْدٌ قَائِمٌ"]:::leaf
  Z --> Z2["فعلیہ<br/>misaal: قَامَ زَیْدٌ"]:::leaf
  Z --> Z3["شرطیہ<br/>misaal: اِنْ تُکْرِمْنِيْ أُکْرِمْكَ"]:::leaf
  Z --> Z4["ظرفیہ<br/>misaal: عِنْدِيْ مَالٌ"]:::leaf

  S --> S1["مبینہ<br/>pehlay jumlay ko wazeh kare"]:::leaf
  S --> S2["معللہ<br/>علت bayan kare"]:::leaf
  S --> S3["معترضہ<br/>do jumlon ke darmiyaan interject"]:::leaf
  S --> S4["مستانفہ<br/>(= جملہ ابتدائیہ)<br/>naya kalam shuru kare"]:::leaf
  S --> S5["حالیہ<br/>حال واقع ho"]:::leaf
  S --> S6["معطوفہ<br/>عطف se juda jumla"]:::leaf

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 13 nodes (limit: 16 ✅), 3 classDefs ✅, no subgraphs ✅.

**Kaise istemaal:** Jumla dekho — 2 alag perspectives se classify karo. Zaati side se "wo asmiya ya fi'liya ya shartiya ya zarfiya?" Sifati side se "wo kis role mein hai — wazeh kar raha, علت bata raha, interject, naya shuru, حال, ya atf?"

---

## Chart 9 — Alamat-e-Fi'l (8) + Alamat-e-Harf (negative + 3 link-types) combined

**Source:** PDF p-15 (8 alamat-e-Fi'l with Arabic+Urdu glosses + علامتِ حرف negative def + 3 link-type misaalein).

**Concept:** Fi'l aur Harf ki identification toolkit — Chart 7 (Ism) ka complement.
- **Fi'l side**: 8 positive alamat (particle-prefix + structural + sigha-based)
- **Harf side**: 1 negative criterion + 3 link-type examples (Ism-Ism / Ism-Fi'l / Fi'l-Fi'l)

```mermaid
flowchart TD
  R["Fi'l aur Harf ki<br/>alamat (PDF p-15)"]:::root

  R --> F["فِعل — 8 positive alamat"]:::main
  R --> H["حرف — 1 negative criterion<br/>(Ism/Fi'l ki alamat na ho)"]:::main

  F --> F1["1. قَدْ shuru mein<br/>misaal: قَدْ ضَرَبَ"]:::leaf
  F --> F2["2. سَ shuru mein<br/>misaal: سَیَضْرِبُ"]:::leaf
  F --> F3["3. سَوْفَ shuru mein<br/>misaal: سَوْفَ یَضْرِبُ"]:::leaf
  F --> F4["4. حرفِ جزم daakhil<br/>misaal: لَمْ یَضْرِبْ"]:::leaf
  F --> F5["5. ضمیر متصل ho<br/>misaal: ضَرَبْتُ"]:::leaf
  F --> F6["6. تائے ساکن aakhir<br/>misaal: ضَرَبَتْ"]:::leaf
  F --> F7["7. اَمر<br/>misaal: اِضْرِبْ"]:::leaf
  F --> F8["8. نہی<br/>misaal: لَا تَضْرِبْ"]:::leaf

  H --> HK["Harf = محض ربط<br/>(mere linking)"]:::sub
  HK --> L1["Ism⟷Ism<br/>زَیْدٌ فِي الدَّارِ"]:::ex
  HK --> L2["Ism⟷Fi'l<br/>کَتَبْتُ بِالْقَلَمِ"]:::ex
  HK --> L3["Fi'l⟷Fi'l<br/>أُرِیْدُ أَنْ أُصَلِّيَ"]:::ex

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
  classDef ex   fill:#ffe4e6,stroke:#be123c,color:#881337;
```

**Density check:** 14 nodes (limit: 16 ✅), 5 classDefs (limit: 5 ✅), no subgraphs ✅.

**Kaise istemaal:** Koi Arabic lafz dekho — Chart 7 ki 11 Ism-alamat se start; agar koi na milay, Fi'l ki 8 alamat (yeh chart) check karo; agar koi na milay, **automatically Harf** hai. Phir Harf ka kaam = linking (یہاں 3 link-types dikhaye).

---

## Chart 10 — Mudmaraat (Qism #1 of 8) full taxonomy

**Source:** PDF p-18 (Section 13 — Mudmaraat ki 5 qismein), p-19 (Section 14 — Mansoob + Majroor sub-types), p-20 (Section 15 — Majroor bi Idafa completion + MUKAMMAL claim).

**Concept:** Fasl 5 ka pehla qism — **مُدْمَرَات** ki full taxonomy. **3 i'rab states** (Marfu'/Mansoob/Majroor) × **attachment patterns** (Muttasil/Munfasil) → **6 paradigm tables** × 14 forms each = **84 forms total**. Note: Marfu' + Mansoob ke 2-2 tables (Muttasil + Munfasil), Majroor ka sirf Muttasil hai magar 2 sub-types (bi Harf-e-Jarr + bi Idafa) — isliye 5 qismein lekin 6 tables.

**Read karne ka tareeqa:**
- **Sabz emerald** (root) = main qism
- **Teal** (main) = 3 i'rab states
- **Green** (leaf) = 6 paradigm tables with misaal-form

```mermaid
flowchart TD
  R["مُدْمَرَات / Damayer<br/>Qism #1 of 8<br/>(Section 13-15)<br/>5 qismein → 6 tables<br/>× 14 forms = 84 total"]:::root

  R --> MR["مَرفُوع / Marfu'<br/>Fa'il position"]:::main
  R --> MN["مَنصُوب / Mansoob<br/>Maf'ool position"]:::main
  R --> MJ["مَجرُور / Majroor<br/>after Jarr/Idafa"]:::main

  MR --> T1["مُتَّصِل (Table 1)<br/>e.g. ضَرَبْتُ"]:::leaf
  MR --> T2["مُنفَصِل (Table 2)<br/>e.g. اَنَا"]:::leaf

  MN --> T3["مُتَّصِل (Table 3)<br/>e.g. ضَرَبَنِيْ"]:::leaf
  MN --> T4["مُنفَصِل (Table 4)<br/>e.g. اِیَّایَ"]:::leaf

  MJ --> T5["بہ حَرف جَر<br/>(Table 5)<br/>e.g. لِيْ"]:::leaf
  MJ --> T6["بہ اِضافَت<br/>(Table 6)<br/>e.g. دَارِيْ"]:::leaf

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 10 nodes (limit: 16 ✅), 3 classDefs (limit: 5 ✅), no subgraphs ✅.

**Kaise istemaal:** Yeh **structural taxonomy** hai (84 forms ka full paradigm `irab-tables.md` Tables 1-6 mein hai). Chart se yaad karo ke har "qism" actually 2 dimensions ka intersection hai (i'rab × attachment). Mudmaraat MUKAMMAL hone ka **structural map**.

---

## Chart 11 — Asma-e-Mausoolah (Qism #2 of 8) — paradigm + exceptions + Sila rule

**Source:** PDF p-20 (Section 15 — Mausoolah ki 10-form paradigm + 3 exceptions + Sila tareef).

**Concept:** Fasl 5 ka doosra qism — **اَسْمَائے مَوْصُوْلَہ** ki taxonomy. **10 paradigm cells** in PDF p-20 table: **7 gender-specific** (3 masculine + 4 feminine) + **2 generic** (مَنْ/مَا) + **1 dual-form cell** (اَيٌّ/اَيَّۃٌ — also one of the 3 exceptions). Sath mein **3 special rules**: الف لام as اَلَّذِيْ in Ism Fa'il/Maf'ool, ذُو in Banu Tay, اَيٌّ/اَيَّۃٌ Mu'arrab+Idafa-only. Plus **Mausool+Sila** compound-unit rule (Section 15 ka root concept). **Note** *(yeh book ki structure se observation)*: اَيٌّ/اَيَّۃٌ **dual-role** rakhta — paradigm ka 10th cell AND exception list ka 1st item.

**Read karne ka tareeqa:**
- **Sabz emerald** = main qism
- **Teal** (main) = 2 specificity branches
- **Amber** (sub) = compound-unit rule + exceptions header
- **Green** (leaf) = actual form clusters

```mermaid
flowchart TD
  R["اَسْمَائے مَوْصُوْلَہ<br/>Mausoolah<br/>Qism #2 of 8<br/>(Section 15)<br/>10 paradigm cells<br/>+ 3 special rules"]:::root

  R --> SP["خاص (Specific)<br/>7 gender-specific"]:::main
  R --> GN["عام (Generic)<br/>2 generic"]:::main
  R --> EX["استثناء<br/>(3 special rules)"]:::sub

  SP --> M["مَردانہ (M) — 3 forms<br/>اَلَّذِيْ (sing) /<br/>اَلَّذَانِ (dual) /<br/>اَلَّذِيْنَ (pl)"]:::leaf
  SP --> F["مُؤنث (F) — 4 forms<br/>اَلَّتِيْ / اَلَّتَانِ /<br/>اَللَّتَیْنِ /<br/>اَللَّاتِيْ"]:::leaf

  GN --> G1["مَنْ (human) /<br/>مَا (non-human)"]:::leaf

  EX --> E1["اَيٌّ / اَيَّۃٌ<br/>Mu'arrab + Idafa-only<br/>(also fills 10th cell)"]:::leaf
  EX --> E2["الف لام = اَلَّذِيْ<br/>(in Ism Fa'il/Maf'ool)<br/>e.g. اَلضَّارِبُ"]:::leaf
  EX --> E3["ذُو = اَلَّذِيْ<br/>(Banu Tay tribe)"]:::leaf

  R --> RULE["Mausool + سِلَہ<br/>= compound unit<br/>(Section 15 rule)<br/>Sila ki return-ضمیر<br/>lazmi"]:::sub

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 11 nodes (limit: 16 ✅), 4 classDefs (limit: 5 ✅), no subgraphs ✅.

**Kaise istemaal:** Mausool jab dekho — pehle pehchaano specific (gender-based) ya generic (مَنْ/مَا)? Phir Sila zaroori (ek complete jumla with return-ضمیر). Compound unit ki tarah istemaal — alag se kaam nahi karta. 3 exceptions yaad rakho ke ye non-standard cases hain.

---

## Chart 12 — Asma-e-Ishara (Qism #3 of 8) — paradigm gender × number × distance

**Source:** PDF p-21 (Section 16 — Ishara Qareeb 5 + Ba'eed 5 + Mushar Ilayh tareef).

**Concept:** Fasl 5 ka teesra qism — **اَسْمَائے اِشَارَہ** ki taxonomy. **2 sub-qismein** (Qareeb/Ba'eed — distance) × **gender** (m/f/common) × **number** (sing/dual/plural) → **10 total forms**. Sath mein **Ishara+Mushar-Ilayh** compound-unit rule (Section 16 ka root concept).

**Read karne ka tareeqa:**
- **Sabz emerald** = main qism
- **Teal** (main) = 2 distance branches
- **Green** (leaf) = 10 individual forms (5 + 5)
- **Amber** (sub) = compound-unit rule

```mermaid
flowchart TD
  R["اَسْمَائے اِشَارَہ<br/>Ishara<br/>Qism #3 of 8<br/>(Section 16)<br/>10 forms total"]:::root

  R --> QR["اِشَارَہ قَرِیْب<br/>Qareeb (close)<br/>5 forms"]:::main
  R --> BD["اِشَارَہ بَعِیْد<br/>Ba'eed (far)<br/>5 forms"]:::main

  QR --> Q1["M sing: هٰذَا"]:::leaf
  QR --> Q2["M dual: هٰذَانِ"]:::leaf
  QR --> Q3["F sing: هٰذِهِ"]:::leaf
  QR --> Q4["F dual: هَاتَانِ"]:::leaf
  QR --> Q5["Plural<br/>(gender-common):<br/>هٰؤُلَاءِ"]:::leaf

  BD --> B1["M sing: ذٰلِكَ"]:::leaf
  BD --> B2["M dual: ذَانِكَ"]:::leaf
  BD --> B3["F sing: تِلْكَ"]:::leaf
  BD --> B4["F dual: تَانِكَ"]:::leaf
  BD --> B5["Plural<br/>(gender-common):<br/>اُولٰئِكَ"]:::leaf

  R --> RULE["Ishara + مُشار اِلَیہ<br/>= compound unit<br/>(Section 16 rule)<br/>e.g. هٰذَا الْقَلَمُ نَفِیْسٌ"]:::sub

  classDef root fill:#064e3b,stroke:#064e3b,color:#fff,font-weight:bold;
  classDef main fill:#cffafe,stroke:#0e7490,color:#0c4a6e;
  classDef sub  fill:#fef3c7,stroke:#b45309,color:#7c2d12;
  classDef leaf fill:#dcfce7,stroke:#166534,color:#14532d;
```

**Density check:** 14 nodes (limit: 16 ✅), 4 classDefs (limit: 5 ✅), no subgraphs ✅.

**Kaise istemaal:** Koi Ishara form dekho — pehle distance pehchaano (Qareeb 5 forms ya Ba'eed 5 forms — chart se match karo). Phir gender + number breakdown. Plural form **gender-common** hai (m + f dono ke liye same lafz). **Mushar Ilayh** Ishara ke saath compound unit banata (Mausool+Sila ke same pattern par — Section 16 cross-pattern observation).

**Builder pattern observation** *(mera observation; book ne yeh tabseera nahi diya)*: Qareeb forms usually **هٰ-** prefix se shuru (هٰذَا/هٰذَانِ/هٰذِهِ/هٰؤُلَاءِ — magar هَاتَانِ exception); Ba'eed forms usually **-كَ** suffix se khatam (ذٰلِكَ/ذَانِكَ/تِلْكَ/تَانِكَ/اُولٰئِكَ — yeh consistent hai). Yeh **heuristic** hai, formal rule nahi.

---

## Aage ke charts (Fasl 5 MUKAMMAL ke baad — 2026-05-30 update)

**Status update**: Charts 1-12 ab build ho chuke. Fasl 1 + 2 + 3 + Fasl 4 pivot + **Fasl 5 ke pehle 3 qismein (Mudmaraat/Mausoolah/Ishara)** — sab visual review done.

**Pending future charts** (next phases mein):
- **Chart 13 candidate**: Ism Ghair Mutamakkin **8 qismein full taxonomy tree** — Fasl 5 ka topic-overview chart (ab build kiya ja sakta kyunke saari 8 qismein covered).
- **Chart 14 candidate**: Mabni-ending classification (Section 20 Faida 1) — visual grouping of all Zarf items by damma/fatha/kasra/sukoon.
- **Chart 15+ candidates**: Aage ke pages (p-26+) ke naye concepts ke saath new charts emerge honge:
  - Mabni-Mu'arrab full taxonomy tree (Mabni-al-Asl 3 + Mushabahat 4 tareeqein) — Section 12 conceptual map
  - Case-state names (Marfu'/Mansoob/Majroor) — Bab-level i'rab system overview
  - Amil / Ma'mool chart (jab Ma'mool ki tareef milti — p-12 ka 4th forward-ref still pending)
