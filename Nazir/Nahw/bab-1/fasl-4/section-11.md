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

## Section 11 — Fasl 4 ka aaghaaz: Mu'arrab/Mabni taqseem + Amil + I'rab definitions + 2 qismein (Harki/Harfi) + Mahall-e-I'rab + Zayd 3-form walkthrough + Hadha 3-form walkthrough + Persian mnemonic (PDF p-16 / book p-۱۵)

> **Source note (2026-05-28):** PDF se direct render (`Read` tool with `pages: 16`).
> **Yeh page Fasl 4 ka shuru karta hai aur p-12 ke 4 forward-ref terms mein se 3 (Mu'arrab/Mabni/Amil) ko tareefein deta — saath I'rab ek naya bonus term hai. (Ma'mool abhi bhi pending.)** Kalimah ki naya angle se taqseem — uss ke akhri harf ki harakah tabdeeli (= **i'rab tabdeeli**) ke aitebar se. **Pivot moment** kyunke yahaan se Nahw ka **i'rab system** shuru hota.

**PDF par jo hai (literal blocks, top → bottom):**

1. **Header strip**:
   - Right: **فصل (۴)**
   - Center: **۱۵** (printed page number)
   - Left: **معرب و مبنی**

2. **Title (red, large, centered)**:
   - **فصل (۴)**
   - **معرب و مبنی**

3. **Block 1 — Kalimah ki 2 qismein bashaqul akhri-harf**:
   > آخری حرف کی تبدیلی کے اعتبار سے کلمہ کی **دو قسمیں** ہیں: ۱۔ **معرب**  ۲۔ **مبنی**۔

4. **Block 2 — Mu'arrab ki tareef + Amil + I'rab definitions**:
   > **معرب**: وہ کلمہ ہے جس کا آخری حرف ہمیشہ بدلتا رہتا ہو۔ پس جس سبب سے یہ تبدیلی ہوتی ہے اُس کو **عامل** کہتے ہیں، اور جو چیز آخری حرف سے بدلتی ہے اس کو **اعراب** کہتے ہیں۔

5. **Block 3 — I'rab ki 2 qismein**:
   > **اعراب** دو قسم کا ہوتا ہے: ۱۔ **حرکتی**  جیسے: **ضمہ، فتحہ، کسرہ**  ۲۔ **حرفی**  جیسے: **"الف، واو، یا"**۔

6. **Block 4 — Mahall-e-I'rab + Zayd 3-form walkthrough**:
   > **آخری حرف کو محل اعراب کہتے ہیں**، جیسے: **جَاءَ زَیْدٌ**، اس میں **جَاءَ عامل** ہے اور **زَیْدٌ پر ضمہ** ہے، **رَأَیْتُ زَیْدًا** میں **رَأَیْتُ عامل** ہے اور **زَیْدًا پر فتحہ** ہے، اور **مَرَرْتُ بِزَیْدٍ** میں **"بِ" حرف جار عامل** ہے اور **"زَیْدٍ" پر کسرہ** ہے، پس **"زَیْدٌ" معرب** ہے، اور **"زَیْدٌ" کا آخری حرف "د" محل اعراب** ہے اور **ضمہ، فتحہ، کسرہ اعراب** ہے۔

7. **Block 5 — Mabni ki tareef + Hadha 3-form walkthrough**:
   > **مبنی**: وہ کلمہ ہے جس کے آخری حرف کا اعراب **تمام حالتوں میں یکساں** رہتا ہے، یعنی **عامل کے بدلے سے** اس کی آخری حرکت میں کچھ تبدیلی **نہیں ہوتی**، جیسے: **جَاءَ هٰذَا، رَأَیْتُ هٰذَا، مَرَرْتُ بِهٰذَا**، اِن مثالوں میں **هٰذَا مبنی** ہے کہ ہر حالت میں یکساں ہے۔

8. **Block 6 — Persian poetic couplet (mnemonic)**:
   > **مبنی آں باشد کہ ماند برقرار**
   > **معرب آں باشد کہ گردد بار بار**

9. **Block 7 — Urdu paraphrase (in quotes)**:
   > **"مبنی وہ ہوتا ہے جو ایک ہی حالت میں برقرار رہے، معرب وہ ہوتا ہے جو بار بار بدلے۔"**

---

### Aaj ki kahani (page ka khulasa — pedagogical narrative)

#### Hissa A — Fasl 4 ka angle: Akhri harf ki tabdeeli ke aitebar se

Hum ne ab tak Kalimah ko 3 alag tareekon se dekha:
- **Fasl 1**: Kalimah = Ism/Fi'l/Harf (تعریف ke aitebar se)
- **Fasl 3**: Kalimah ke shanaakht ke signs (alamat)

**Fasl 4 naya angle deta**: Kalimah ka **آخری حرف dekhо** — har bar usay alag context mein use karo, kya **uska آخری harf badalta** hai ya **fix** rehta?

- Agar badalta → **معرب (Mu'arrab)**
- Agar fix rehta → **مبنی (Mabni)**

**Critical**: "آخری harf khud" nahi badalta — har bar wahi harf rehta. Jo badalti hai **uss par lagi harakah** (zer/zabar/pesh) — yahi tabdeeli **i'rab** kehlati. *(yeh wazaahat meri taraf se; book ki phrase loose hai magar Block 2 ki agli line clarify karti)*

**P-12 ka load resolve**: p-12 par humne 4 forward-ref terms dekhe thay (Mu'arrab/Mabni/Amil/Ma'mool) jin ki tareef pending thi. Aaj **un 4 mein se 3** (Mu'arrab/Mabni/Amil) defined hue + **اعراب** ek naya term hai jo p-12 ki list par nahi tha — yahaan introduce ho raha. Sirf **Ma'mool** abhi pending (probably agle pages par).

#### Hissa B — Mu'arrab + Amil + I'rab: 3-in-1 definitions (Block 2 ka unpack)

Block 2 mein book ne **3 buniyadi concepts** ek saath diye:

| Term | Tareef (PDF verbatim) | Roman gloss |
|------|------------------------|-------------|
| **معرب** | "وہ کلمہ ہے جس کا آخری حرف ہمیشہ بدلتا رہتا ہو" | Wo kalimah jis ka akhri harf hamesha badalta rehta |
| **عامل** | "جس سبب سے یہ تبدیلی ہوتی ہے" | Wo cheez/sabab jiski wajah se tabdeeli aati |
| **اعراب** | "جو چیز آخری حرف سے بدلتی ہے" | Wo cheez jo akhri harf par change hoti |

**Chain of causation**: **Amil** (cause) → **Akhri harakah change** (mechanism) → **I'rab** (the thing that changes).

**Aam zindagi se misaal**: Aap road par chal rahe (akhri harf = aap), traffic light (= **Amil**) red ho jata, aap ruk jate, harkat (= **I'rab**) badalti chalne se rukhne mein. Light agla rang dikhati hai to harkat phir badalti. Aap to wahi ho (akhri harf hamesha "د" of Zayd) magar har bar **alag harkat** karte traffic light ke اعتبار se. *(meri taraf se analogy; book mein nahi)*

#### Hissa C — I'rab ki 2 qismein (Block 3): Harki vs Harfi

| Qism | Matlab | Misaal |
|------|--------|--------|
| **حرکتی (Harki)** — "Harakah-based" | I'rab ek **harakah** (short vowel) ki shakal mein dikhe | **ضمہ** (pesh)، **فتحہ** (zabar)، **کسرہ** (zer) |
| **حرفی (Harfi)** — "Letter-based" | I'rab ek **harf** ki shakal mein dikhe (poora ek letter add ya cut hone se) | **الف**، **واو**، **یا** |

**Note on Harfi i'rab**: Ya book ka pehla mention hai — abhi tafseel nahi. Tathniya (-اَنِ) aur Jam' (-وْنَ/-یْنَ) jaisi shaklon mein i'rab خود ek letter ki shakal mein hota. Tafseel aage milegi. **Yahan sirf naam + misaal kaafi**.

**Common case = Harki**: Aksar Ism mein i'rab harakah hi hoti (ضمہ/فتحہ/کسرہ). Iska tafseeli walkthrough next Hissa mein.

#### Hissa D — Mahall-e-I'rab + Zayd 3-form walkthrough (the pivot example)

Book ne pehle ek nayi term di: **محل اعراب (Mahall-e-I'rab)** = "Wo jagah jahaan i'rab dikhe" = **آخری حرف**.

Phir **same word زَیْد ko 3 jumlon mein** dikhaya — har bar **alag Amil** + **alag i'rab**:

| Jumla (PDF verbatim) | Amil | Zayd ka roop | Harakah |
|----------------------|------|----------------|---------|
| **جَاءَ زَیْدٌ** ("Zayd aaya") | **جَاءَ** (Fi'l) | **زَیْدٌ** | **ضمہ** (pesh) |
| **رَأَیْتُ زَیْدًا** ("Main ne Zayd dekha") | **رَأَیْتُ** (Fi'l) | **زَیْدًا** | **فتحہ** (zabar) |
| **مَرَرْتُ بِزَیْدٍ** ("Main Zayd ke paas se guzra") | **بِ** (**Harf-e-Jarr**) | **زَیْدٍ** | **کسرہ** (zer) |

**Yeh hai i'rab system ka asal demo**:
- **آخری harf** "د" — har bar **same** (badla nahi)
- **Harakah** par "د" — har bar **alag** (ٌ → ً → ٍ)
- **Amil** har bar alag (جَاءَ، رَأَیْتُ، بِ)

**PDF ka conclusion (Block 4 ka aakhir)**:
- **زَیْدٌ معرب** hai (kyunke badalta)
- **"د" mahall-e-i'rab** hai (jahaan badalti dikhe)
- **ضمہ/فتحہ/کسرہ = اعراب** hai (jo badalti)

**Big picture**: Yeh **i'rab system** ka core hai. Nahw ka bohot bara hissa yahi hai — kis kalimah par kya i'rab aaye, aur **kis amil** ki wajah se. Book aage har Amil ki taxonomy + har i'rab ki specific terminology dega; **abhi sirf harakah ke naam** (ضمہ/فتحہ/کسرہ) hi kaafi hain. *(yeh "Nahw ka bara hissa = i'rab" claim mera observation; book ne yeh statement nahi ki yahaan)*

#### Hissa E — Mabni + Hadha walkthrough + Persian mnemonic

**Mabni tareef** (Block 5 PDF verbatim ka summary):
> Wo kalimah jis ka **akhri harakah** har Amil ke saath same rehta — koi tabdeeli nahi.

**Hadha 3-form walkthrough** (Block 5):

| Jumla | Tarjuma | هٰذَا ka roop |
|-------|---------|------------------|
| **جَاءَ هٰذَا** | "Yeh aaya" | **هٰذَا** (no change) |
| **رَأَیْتُ هٰذَا** | "Main ne yeh dekha" | **هٰذَا** (no change) |
| **مَرَرْتُ بِهٰذَا** | "Main yeh ke paas se guzra" | **هٰذَا** (no change) |

**Yeh hai Mabni ka demo**:
- Amil 3 bar alag (just like Zayd ke example)
- Magar **هٰذَا ka roop har bar yaksaan** — alif + zabar + dhaal + alif khari + waw — same hi
- Iska matlab **هٰذَا mabni** hai

**Forward-ref**: **هٰذَا** ek **اسمِ اشارہ** (demonstrative pronoun — "this") hai, jo Mabni Ism ki ek qism. Tafseel aage milegi (book ne yahan sirf misaal ki khaatir use kiya).

**Block 6 — Persian mnemonic couplet** (PDF verbatim, **classical Persian Nahw tradition** se):
> **مبنی آں باشد کہ ماند برقرار**
> **معرب آں باشد کہ گردد بار بار**

**Tarjuma** (Block 7 PDF ka apna Urdu):
> *"مبنی wo hota hai jo ek hi halat mein **barqarar** rahe, مَعرب wo hota hai jo **بار بار** badle."*

**Yaad rakhne ka mnemonic**: **MABNI = "MAANDA" (rehne wala / static)**، **MU'ARRAB = "GARDISH" (chakkar / change)**. *(yeh memorization aid meri taraf se; book ne explicit yeh mnemonic ki form mein nahi diya — sirf couplet aur Urdu paraphrase)*

---

### Naye terms (inline glossary) — p-16 par appear hue

| Term | Roman | Urdu / Matlab | Note |
|------|-------|----------------|------|
| **معرب** | Mu'arrab | Wo kalimah jis ka akhri harf hamesha badalta rehta | Block 2 — p-12 ka forward-ref ab defined |
| **مبنی** | Mabni | Wo kalimah jis ka akhri harakah har halat mein yaksaan | Block 5 — p-12 ka forward-ref ab defined |
| **عامل** | Amil | Wo sabab/cheez jiski wajah se akhri harakah badalti | Block 2 — p-12 ka forward-ref ab defined |
| **اعراب** | I'rab | Wo cheez jo akhri harf par badalti (the change itself) | Block 2 — naya buniyadi term |
| **حرکتی** | Harki | Adj. — "harakah-based i'rab" (ضمہ/فتحہ/کسرہ) | Block 3 |
| **حرفی** | Harfi | Adj. — "letter-based i'rab" (الف/واو/یا) | Block 3 — tafseel aage |
| **ضمہ** | Damma | Pesh (—ُ) | I'rab Harki ki misaal |
| **فتحہ** | Fatha | Zabar (—َ) | I'rab Harki ki misaal |
| **کسرہ** | Kasra | Zer (—ِ) | I'rab Harki ki misaal |
| **محل اعراب** | Mahall-e-I'rab | "Locus of i'rab" = akhri harf — wahaan i'rab dikhayi deti | Block 4 |
| **جَاءَ** | Jaa'a | "Aaya" — Fi'l Maazi 3rd person masc. singular | Block 4 — Amil misaal (causes **ضمہ** on **زَیْدٌ** in Block 4 jumla) |
| **رَأَیْتُ** | Ra'aytu | "Main ne dekha" — Fi'l Maazi + ضمیر متصل (1st person) | Block 4 — Amil misaal (causes **فتحہ** on **زَیْدًا** in Block 4 jumla) |
| **مَرَرْتُ** | Marartu | "Main guzra" — Fi'l Maazi + ضمیر متصل (1st person) | Block 4 |
| **بِ** | Bi | "Se / through" — Harf-e-Jarr (Amil for کسرہ) | Block 4 — yahan Amil bhi hai |
| **زَیْدٌ** | Zaydun | Zayd (with ضمہ-tanween) — جَاءَ ke saath Block 4 mein | Block 4 |
| **زَیْدًا** | Zaydan | Zayd (with فتحہ-tanween) — رَأَیْتُ ke saath Block 4 mein | Block 4 |
| **زَیْدٍ** | Zaydin | Zayd (with کسرہ-tanween) — بِ (Harf-e-Jarr) ke saath Block 4 mein | Block 4 |
| **هٰذَا** | Hadha | "Yeh" — اسمِ اشارہ (demonstrative pronoun), Mabni Ism | Block 5 — forward-ref Sarf for full Ism Ishara qisam |
| **برقرار** | Barqarar | "Stable, fixed" (Persian/Urdu) | Block 6/7 — Mabni ka feature |
| **بار بار** | Baar Baar | "Again and again" (Urdu) | Block 6/7 — Mu'arrab ka feature |

---

### Yaad rakho (page ke 5 mukhya cheezein)

1. **Kalimah ki naya taqseem (Akhri harf ke اعتبار se)**: **معرب** (badalta) vs **مبنی** (na badalta).
2. **3-concept chain (Block 2)**: **Amil** (cause) → tabdeeli mechanism → **I'rab** (the change). Amil bina i'rab nahi hota.
3. **I'rab ki 2 qismein**: **حرکتی** (ضمہ/فتحہ/کسرہ jaisi harakaat) + **حرفی** (الف/واو/یا jaise letters — tafseel aage).
4. **محل اعراب = آخری حرف** (jahaan i'rab dikhayi deti). Misaal: زَیْد ka "د" hi mahall hai.
5. **Pivot demonstration**: **زَیْد in 3 forms** (زَیْدٌ / زَیْدًا / زَیْدٍ) jab Amil 3 alag (جَاءَ / رَأَیْتُ / بِ) — **akhri harf "د" same**, **harakah alag** = Mu'arrab. **هٰذَا in same 3 contexts** — har bar same shakal = Mabni.
6. **Persian mnemonic**: "مبنی برقرار، معرب گردد بار بار" — yaad rakho.

---

### Sawal (Sabak — recall questions)

1. **Mu'arrab** aur **Mabni** ki tareef batao. Akhri harf khud badalta ya us par lagi harakah?
2. **Amil** kya hai? **I'rab** kya hai? Dono ka taluq apni misaal mein dikhao.
3. **I'rab ki 2 qismein** ke naam + har ek ki misaalein.
4. **محل اعراب** = ? Misaal **زَیْد** mein mahall kya hai?
5. **Zayd ki 3 forms** (PDF se yaad karo):
   - جَاءَ ___ — Amil + harakah?
   - رَأَیْتُ ___ — Amil + harakah?
   - مَرَرْتُ ___ ___ — Amil + harakah?
6. **هٰذَا 3 jumlon mein** kya rehta — Mu'arrab ka misaal ya Mabni ka? Kyon?
7. Persian couplet recite karo + uska Urdu tarjuma batao.
8. **Big picture sawal**: Agar koi Arabic lafz dekho aur uska akhri harakah har jumlay mein same rehta — woh Mu'arrab hai ya Mabni? Aur agar har bar badalta?
9. **Cross-reference**: P-12 Block 2 par 4 forward-ref terms aaye thay (Mu'arrab/Mabni/Amil/Ma'mool) — aaj un 4 mein se kitne defined hue? Naya bonus term kaunsa aaya (jo p-12 list par nahi tha)? Sirf kya pending?

---

**Status:** PRE-BUILD (2026-05-28) — Nazir ko PDF p-16 ke saath verify karna hai.

**Verification confidence:**
- ✅ **Title + Block 1 (Kalimah ki 2 qismein)** — verbatim.
- ✅ **Block 2 Mu'arrab tareef + Amil + I'rab** — sab 3 definitions verbatim from PDF.
- ✅ **Block 3 I'rab ki 2 qismein** (Harki/Harfi + misaalein) — verbatim.
- ✅ **Block 4 Mahall-e-I'rab + Zayd 3-form walkthrough** — verbatim with all 3 jumlay + Amil identification + harakah identification.
- ✅ **Block 5 Mabni tareef + Hadha 3-form walkthrough** — verbatim.
- ✅ **Block 6 Persian couplet** — verbatim (2 lines).
- ✅ **Block 7 Urdu paraphrase** — verbatim (in book's own quotes).
- ✅ **Builder analogies / observations marked transparent**:
  - "آخری harf khud nahi badalta" wazaahat (Hissa A) — `(yeh wazaahat meri taraf se; book ki phrase loose hai magar Block 2 ki agli line clarify karti)`
  - Traffic-light analogy for Amil/I'rab (Hissa B) — `(meri taraf se analogy; book mein nahi)`
  - "Nahw ka bohot bara hissa = i'rab" claim (Hissa D) — `(yeh observation mera; book ne yeh statement nahi ki yahaan)`
  - "MABNI = MAANDA, MU'ARRAB = GARDISH" mnemonic (Hissa E) — `(yeh memorization aid meri taraf se; book ne explicit yeh mnemonic ki form mein nahi diya — sirf couplet aur Urdu paraphrase)`
- ✅ **Forward-ref discipline**: **Marfu'/Mansoob/Majroor terms NOT introduced** (book ne yahan nahi diye — sirf harakah names ضمہ/فتحہ/کسرہ). **اسمِ اشارہ** for هٰذَا — sirf naam, tafseel "Sarf mein" flag.
- ✅ **No memory-fill of paradigms / case lists** — sirf jo PDF mein hai woh likha.
- ℹ️ **Pending p-12 forward-ref**: p-12 ki list ke 4 mein se **3 defined** (Mu'arrab/Mabni/Amil ✓) + **I'rab** ek naya term (p-12 list par nahi tha — yahaan introduce hua). **Ma'mool** abhi bhi pending — possibly agle pages.
- ℹ️ **Pending p-17 expected**: Possibly i'rab ki tafseeli taxonomy (Marfu'/Mansoob/Majroor cases names), ya Mabni ki qismein (Asma'-e-Mabniya), ya I'rabi Harfi ki tafseel.
- ℹ️ **Chart candidates (still 3 deferred)**: Pichli list (Fasl 2 review + Alamat-e-Ism + Fasl 3 closure) + ab **NEW Candidate D**: Mu'arrab-Mabni demo chart (Zayd 3 forms + Hadha 3 forms side-by-side). Per "1 chart per session" — Nazir's call.

---

