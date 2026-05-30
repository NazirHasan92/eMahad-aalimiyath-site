# Nazir's eMahad Notes

Page-by-page notes for the **8-year Aalim course** at eMahad, built directly from the source PDFs of each subject's book. Notes are written using a strict **PDF-truthfulness** discipline — Arabic quoted verbatim with harakaat, no memory-fill, explicit `[?]` markers where source is unclear.

> **Status:** Pre-build / live-affirmation hybrid. Most Sections are at `PRE-BUILD` — content matches PDF (validator PASS) but Nazir's physical-book verification is still pending. Sections progress: PRE-BUILD → PDF-VERIFIED → VERIFIED.

---

## Subjects

| Subject | Book | Entry point | Progress |
|---|---|---|---|
| **Nahw** (نحو) | *Ilm-un-Nahw al-Bushra* | [Nahw home](Nahw/index.md) | Bab 1 Fasl 1-5 MUKAMMAL, Fasl 6 IN-PROGRESS (Section 21 latest) |
| **Sarf** (صرف) | *Muallim u Sarf* | [Sarf notes](Sarf/notes.md) | Sub Topic 1.7 MUKAMMAL — Topic 1.0 structurally complete (Slides 1-48) |

Arabic and Fiqh subjects begin in later years of the course.

---

## Cross-cutting references

| Resource | Subject | What it holds |
|---|---|---|
| [Nahw charts](Nahw/charts.md) | Nahw | Mermaid concept charts (taxonomy trees, classification grids) |
| [Nahw i'rab tables](Nahw/irab-tables.md) | Nahw | Paradigm tables (Mudmaraat, Mausoolah, Ishara, etc.) |
| [Sarf charts](Sarf/charts.md) | Sarf | Mermaid concept charts for Sarf taxonomy |
| [Sarf gardaan tables](Sarf/gardaan-tables.md) | Sarf | 14-form paradigm tables (Muzaari', Maazi, Amr, etc.) |

---

## About the project

- **Source-of-truth discipline:** every line in the notes traces to a specific PDF page. Builder reads the PDF page at letter-perfect resolution, narrates what's visible, then writes. Anything not visible on the PDF is either marked `[?]` or omitted. No AI-generated Arabic grammar from training data.
- **Validator-checked:** a second AI pass (the `nahw-validator` / `sarf-validator` agents) re-reads each Section against the PDF independently and flags any drift before the section is committed.
- **Status levels:**
    - `PRE-BUILD (YYYY-MM-DD)` — builder wrote from PDF Read tool render
    - `PDF-VERIFIED (YYYY-MM-DD)` — validator agent confirmed full PDF match
    - `VERIFIED (YYYY-MM-DD)` — Nazir verified against physical printed book
- **Repo:** [github.com/NazirHasan92/eMahad-aalimiyath](https://github.com/NazirHasan92/eMahad-aalimiyath)
