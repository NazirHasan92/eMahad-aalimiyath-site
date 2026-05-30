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

# Nahw — *Ilm-un-Nahw al-Bushra* (page-by-page notes)

> **Source-of-truth:** [IlmUnNahwAlBushraColor (1).pdf](IlmUnNahwAlBushraColor%20(1).pdf)
>
> **Project:** Nazir's eMahad Aalim course — Nahw subject.
>
> **Hosting status:** Not yet hosted publicly — pre-build phase, deferred per [_planning/architecture-v2.md](_planning/architecture-v2.md) until Bab 1 reaches `Status: VERIFIED` on every Section.

---

## Top-level navigation

| Resource | Description |
|---|---|
| [bab-1/README.md](bab-1/README.md) | Bab 1 — Kalimah aur Kalam — Fasl 1-6 status + per-Fasl entry points |
| [charts.md](charts.md) | Mermaid concept charts (single cross-cutting file) |
| [irab-tables.md](irab-tables.md) | Paradigm / i'rab tables (single cross-cutting file) |
| [notes.md](notes.md) | **Retired** — minimal redirect after Phase 2. All Sections moved to per-Section files under `bab-1/fasl-N/` |
| [_archive/notes-pre-split-2026-05-30.md](_archive/notes-pre-split-2026-05-30.md) | Pre-Phase-1 snapshot of monolithic notes.md (byte-identical reference, 4965 lines) |
| [_archive/notes-pre-phase2-2026-05-30.md](_archive/notes-pre-phase2-2026-05-30.md) | Pre-Phase-2 stub snapshot (byte-identical reference for the 2647-line Phase-1 stub state) |
| [_planning/architecture-v2.md](_planning/architecture-v2.md) | Approved architecture v2 plan (4 decisions, migration sequence, validators) |

---

## Bab status (current — 2026-05-30)

| Bab | Title | Status | Entry |
|---|---|---|---|
| 1 | Kalimah aur Kalam | Phase 1 + 2 migration COMPLETE: Fasl 1-5 all MUKAMMAL & migrated to bab-1/fasl-N/; Fasl 6 TBD (Phase 3 native builds) | [bab-1/README.md](bab-1/README.md) |
| 2+ | (forthcoming — Section 21+ continues the book) | TBD | — |
