---
hide:
  - navigation
  - toc
---

# Nazir's eMahad Notes

<p style="font-size: 1.15em; line-height: 1.85; color: var(--md-default-fg-color--light); margin-top: -0.5em;">
Page-by-page notes for the <strong>8-year Aalim course</strong> at eMahad — built directly from the source PDFs of each book, with strict PDF-truthfulness discipline (Arabic quoted verbatim with harakaat, no memory-fill, explicit <code>[?]</code> markers where the source is unclear).
</p>

<div class="grid cards" markdown>

-   :material-script-text-outline:{ .lg .middle } &nbsp; **Nahw (نحو)**

    ---

    *Ilm-un-Nahw al-Bushra* — Arabic grammar.

    **Bab 1 (Kalimah aur Kalam):** Fasl 1–5 MUKAMMAL · Fasl 6 IN-PROGRESS. **Section 21** is the latest page-built (PDF p-26 / Fasl 6 ka aaghaaz: اسم منسوب).

    [:octicons-arrow-right-24: Enter Nahw](Nahw/index.md){ .md-button .md-button--primary }

-   :material-format-letter-case:{ .lg .middle } &nbsp; **Sarf (صرف)**

    ---

    *Muallim u Sarf* — Arabic morphology.

    **Topic 1.0** structurally complete (Slides 1–48, 7 Sub Topics). **Sub Topic 1.7 MUKAMMAL** (p-032 → p-034) — comprehensive 14-row nakshah; **Sub Topic 2.1** in progress.

    [:octicons-arrow-right-24: Enter Sarf](Sarf/index.md){ .md-button .md-button--primary }

</div>

## Cross-cutting references

<div class="grid cards" markdown>

-   :material-chart-tree:{ .lg .middle } &nbsp; **Nahw concept charts**

    ---

    13 Mermaid diagrams covering Lafz taxonomy, Jumla classification, Ism Ghair Mutamakkin tree, and more.

    [:octicons-arrow-right-24: Open](Nahw/charts.md)

-   :material-table-large:{ .lg .middle } &nbsp; **Nahw i'rab tables**

    ---

    6 paradigm tables (Mudmaraat 14-form set, Mausoolah, Ishara, etc.) with harakaat-perfect transcription.

    [:octicons-arrow-right-24: Open](Nahw/irab-tables.md)

-   :material-chart-arc:{ .lg .middle } &nbsp; **Sarf concept charts**

    ---

    11 Mermaid diagrams: morphology taxonomy, 6-baab system, 14-sigha wheels.

    [:octicons-arrow-right-24: Open](Sarf/charts.md)

-   :material-table-multiple:{ .lg .middle } &nbsp; **Sarf gardaan tables**

    ---

    14-form paradigm tables (Muzaari', Maazi, Amr, Nahi, etc.) — every harakah from the source.

    [:octicons-arrow-right-24: Open](Sarf/gardaan-tables.md)

</div>

---

## How these notes are built

<div class="grid" markdown>

!!! info "Source-of-truth discipline"
    Every line in the notes traces to a specific PDF page. The builder reads the PDF page at letter-perfect resolution, narrates what's visible, then writes. Anything not visible on the PDF is either marked `[?]` or omitted. **No AI-generated Arabic grammar from training data.**

!!! check "Validator-checked"
    A second AI pass (the `nahw-validator` / `sarf-validator` agents) re-reads each Section against the PDF independently and flags any drift before the section is committed. Memory-fill is the cardinal sin — caught at this layer.

!!! example "Status levels"
    - `PRE-BUILD (YYYY-MM-DD)` — builder wrote from PDF render
    - `PDF-VERIFIED (YYYY-MM-DD)` — validator agent confirmed full PDF match
    - `VERIFIED (YYYY-MM-DD)` — Nazir verified against the physical printed book

!!! abstract "Companion site"
    Ramsha's notes (Arabic Madinah Book 1 · Fiqh Nur al-Idah · Hadeeth Zad ut-Taalibeen) at [ramsha-aalimiyath site](https://nazirhasan92.github.io/ramsha-aalimiyath/).

</div>

---

<p style="text-align: center; opacity: 0.7; font-size: 0.9em;">
Built page-by-page, one PDF page per teaching session. Source repository: <a href="https://github.com/NazirHasan92/eMahad-aalimiyath-site">github.com/NazirHasan92/eMahad-aalimiyath-site</a>.
</p>
