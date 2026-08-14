# ACM MM 2026 Publication Entry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Zhu Liu's second-author ACM MM 2026 paper, its acceptance news, official links, and a paper-specific thumbnail to the homepage.

**Architecture:** Extend the existing static publication list in `index.html` with one card that follows the current card contract. Derive one local WebP asset from Figure 1 of the supplied PDF, and protect all metadata, ordering, and asset behavior with the existing Python `unittest` suite.

**Tech Stack:** Static HTML/CSS, WebP image asset, Python `unittest`, Poppler rendering, Pillow image processing

## Global Constraints

- Keep the featured TPAMI publication first.
- Place the ACM MM 2026 paper second, before the ICML 2026 entry.
- Highlight Zhu Liu as second author with `<u>Zhu Liu</u>`.
- Use the official DOI `https://doi.org/10.1145/3767308.3834923` and code URL `https://github.com/bzHunter/DECO`.
- Reuse the existing publication styling; do not make unrelated layout changes.

---

### Task 1: Specify the ACM MM publication behavior

**Files:**
- Modify: `tests/test_homepage.py`
- Test: `tests/test_homepage.py`

**Interfaces:**
- Consumes: `HomepageTests.active_html` and `PublicationParser.images`
- Produces: regression requirements for the News text, publication metadata, author emphasis, links, ordering, and thumbnail count

- [ ] **Step 1: Write the failing test**

Add `test_mm26_publication_metadata_order_and_links_are_present` asserting the full title, `<u>Zhu Liu</u>`, `ACM International Conference on Multimedia`, DOI, code URL, News sentence, and that the title appears after the homography title but before `Diffuse to Detect`. Update thumbnail count assertions from 21 to 22 and require `data/paper_thumbnail/deco-thermal-ir.webp`.

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_homepage`

Expected: FAIL because the MM entry, News item, thumbnail path, and 22nd image do not yet exist.

### Task 2: Create the Figure 1 thumbnail

**Files:**
- Create: `data/paper_thumbnail/deco-thermal-ir.webp`

**Interfaces:**
- Consumes: page 1 of the supplied `MM_Thermal_IR.pdf`
- Produces: a local WebP image referenced by the new publication card

- [ ] **Step 1: Render and crop the paper figure**

Render page 1 with Poppler at 240 DPI. Crop the Figure 1 visual region containing the three radar charts and the Lepton/HIKMICRO/Boson comparison, excluding the author block, caption, and abstract. Resize to a sharp, publication-card-friendly width near 960 pixels and export as lossless WebP.

- [ ] **Step 2: Inspect the thumbnail**

Open the WebP at original detail and confirm that plot labels and camera comparison remain legible, with no author data or body text included.

### Task 3: Add the News item and publication card

**Files:**
- Modify: `index.html:88-105`
- Modify: `index.html:135-165`

**Interfaces:**
- Consumes: `data/paper_thumbnail/deco-thermal-ir.webp`
- Produces: one News list item and one publication card using existing CSS classes

- [ ] **Step 1: Add minimal homepage markup**

Add the News sentence `One paper on thermal infrared image super-resolution was accepted by ACM MM 2026.` near the top of the 2026 updates. Insert the publication card after the TPAMI card with the verified title and author list, `<u>Zhu Liu</u>`, venue `Proceedings of the 34th ACM International Conference on Multimedia, 2026`, DOI link labeled `Paper`, code link labeled `Code`, descriptive alt text, lazy loading, and async decoding.

- [ ] **Step 2: Run the full test suite**

Run: `python -m unittest tests.test_homepage`

Expected: all tests PASS.

- [ ] **Step 3: Verify repository formatting and changes**

Run: `git diff --check` and inspect `git diff -- index.html tests/test_homepage.py data/paper_thumbnail/deco-thermal-ir.webp`.

Expected: no whitespace errors; only the planned News, publication, test, and thumbnail changes appear.

- [ ] **Step 4: Commit**

```bash
git add index.html tests/test_homepage.py data/paper_thumbnail/deco-thermal-ir.webp
git commit -m "feat: add ACM MM 2026 publication"
```

