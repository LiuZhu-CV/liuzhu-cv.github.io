# Minimal Academic Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a restrained black-and-white academic homepage with fourth-year Ph.D. status, the new TPAMI homography paper, and a real paper-specific thumbnail for every active publication.

**Architecture:** Keep the existing static GitHub Pages structure. `index.html` remains the content source, `style.css` owns the monochrome responsive presentation, and optimized local WebP files under `data/paper_thumbnail/` provide stable publication artwork without remote hot-linking. A standard-library Python test validates content, asset paths, accessibility basics, and removal of the generic placeholder.

**Tech Stack:** HTML5, CSS3, Bootstrap 5.1.3, Python 3 standard library, Pillow for image normalization, GitHub Pages.

## Global Constraints

- Preserve static HTML/CSS/Bootstrap; add no framework, CMS, build system, or JavaScript-heavy interaction.
- Use a white, near-black, and neutral-gray palette with thin rules and understated transitions.
- Store every publication thumbnail locally; do not hot-link remote images.
- Prefer matching visuals from `https://rsliu.tech/Publication.html`, then authoritative paper/project teasers, then restrained topic-specific scientific artwork.
- Do not fabricate results, dates, links, metrics, logos, or quantitative claims.
- Preserve current publication metadata unless an authoritative source proves an obvious typo.
- Provide responsive layout, useful alt text, visible keyboard focus, anchor offset, and reduced-motion support.

---

## File Map

- Modify `index.html`: biography, navigation semantics, News, TPAMI entry, publication markup, image paths, alt text, and badges.
- Modify `style.css`: monochrome design tokens, layout, publication cards, responsive behavior, focus states, and reduced motion.
- Create `tests/test_homepage.py`: regression checks for content, asset paths, unique thumbnails, and accessibility hooks.
- Create 21 WebP files under `data/paper_thumbnail/`, one per active publication.

## Thumbnail Filename Contract

Use these exact filenames in publication order:

```text
homography-adverse-degradations.webp
diffuse-to-detect.webp
semantic-priors-irstd.webp
hidra.webp
hybrid-space-fusion.webp
eagle-vql.webp
progressive-prompt-infrared.webp
bilevel-adversarial-learning.webp
caf-image-fusion.webp
deal-infrared-imaging.webp
ivif-data-task.webp
meha-bilevel-optimization.webp
timfusion.webp
crmef.webp
balistd.webp
optimization-learning.webp
paif.webp
segmif.webp
bdlfusion.webp
hierarchical-fusion-search.webp
video-deraining.webp
```

### Task 1: Add Homepage Regression Tests

**Files:**
- Create: `tests/test_homepage.py`
- Read: `index.html`, `style.css`, `data/paper_thumbnail/`

**Interfaces:**
- Consumes: existing static homepage and the thumbnail contract.
- Produces: `python -m unittest tests.test_homepage -v`, used by all later tasks.

- [ ] **Step 1: Write the failing test**

Create a standard-library `unittest` module that strips HTML comments, parses active publication `<img>` elements, and asserts:

```python
self.assertIn("fourth-year Ph.D. student", active_html)
self.assertNotIn("third-year Ph.D. student", active_html)
self.assertIn("Toward Reliable Homography Estimation under Adverse Degradations", active_html)
self.assertIn("Risheng Liu", active_html)
self.assertIn("Jiahao Zhang", active_html)
self.assertIn("Zengxi Zhang", active_html)
self.assertIn("Q1A*+", active_html)
self.assertIn("citation_for_view=WDjOXbIAAAAJ:qUcmZB5y_30C", active_html)
self.assertEqual(21, len(publication_sources))
self.assertEqual(21, len(set(publication_sources)))
self.assertTrue(all("default.jpg" not in src for src in publication_sources))
self.assertTrue(all((ROOT / src).is_file() for src in publication_sources))
self.assertTrue(all(alt.strip() for alt in publication_alts))
self.assertIn('aria-label="Primary navigation"', active_html)
self.assertIn(":focus-visible", css)
self.assertIn("prefers-reduced-motion", css)
```

- [ ] **Step 2: Run the test and verify the baseline fails**

```powershell
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_homepage -v
```

Expected: FAIL for the old Ph.D. year, missing TPAMI entry, duplicated placeholder image, missing assets, and absent accessibility hooks.

- [ ] **Step 3: Commit the test baseline**

```powershell
git add tests/test_homepage.py
git commit -m "test: define homepage refresh requirements"
```

### Task 2: Acquire and Normalize Publication Thumbnails

**Files:**
- Create: all 21 WebP files in the filename contract.
- Read: `https://rsliu.tech/Publication.html` and existing paper/project links.

**Interfaces:**
- Consumes: exact active paper titles and ordered target filenames.
- Produces: 21 local WebP files, at least 480 px wide on consistent 16:9 canvases.

- [ ] **Step 1: Match titles to VLOG images**

Match every active homepage title case-insensitively to the VLOG publication title. Accept only substantive title agreement; author overlap is not sufficient. Record each selected source URL with its target filename.

- [ ] **Step 2: Save exact source-page images locally**

Download each confirmed associated image to a temporary folder. Do not reuse an image across papers and do not reference remote URLs from `index.html`.

- [ ] **Step 3: Fill gaps from authoritative paper material**

For unmatched titles, use the teaser or main method/result figure from the paper PDF, arXiv/OpenReview/CVF page, or linked project repository. For the new homography paper, use the exact image attached to its VLOG entry.

- [ ] **Step 4: Normalize every asset**

Use Pillow to crop or white-pad each source to 16:9, resize to at least 480 px wide, and save as WebP with quality 86 and method 6. Preserve readable scientific diagrams; do not stretch or clip key labels.

- [ ] **Step 5: Verify the asset contract**

Run an image inspection that fails unless all 21 files exist, decode as WebP, are at least 480 px wide, and have a width/height ratio from 1.70 through 1.86.

- [ ] **Step 6: Commit the assets**

```powershell
git add data/paper_thumbnail/*.webp
git commit -m "assets: add paper-specific publication thumbnails"
```

### Task 3: Update Biography and Publication Markup

**Files:**
- Modify: `index.html`
- Test: `tests/test_homepage.py`

**Interfaces:**
- Consumes: 21 normalized image paths.
- Produces: semantic navigation, fourth-year copy, new TPAMI metadata, unique images, alt text, and reusable publication classes.

- [ ] **Step 1: Improve header semantics**

Use a `nav` element with `aria-label="Primary navigation"`. Keep the existing labels/anchors and change the empty Posts link to `posts.html`.

- [ ] **Step 2: Update the biography**

Replace exactly `a third-year Ph.D. student` with `a fourth-year Ph.D. student`, preserving the remaining research statement.

- [ ] **Step 3: Add the TPAMI News item**

Add a reverse-chronological item stating the homography paper was accepted by IEEE TPAMI. Use `(2026)` if the sources do not provide a reliable month.

- [ ] **Step 4: Add the TPAMI publication first**

Insert an active `.pub-item.featured-publication` before “Diffuse to Detect” containing the exact supplied title, `Risheng Liu, Jiahao Zhang, Zengxi Zhang, <u>Zhu Liu</u>`, the full TPAMI venue, `IEEE TPAMI` and `Q1A*+` outlined badges, the supplied Scholar URL, and `homography-adverse-degradations.webp`.

- [ ] **Step 5: Normalize every active publication row**

For all active papers, remove inline thumbnail heights, assign its ordered unique filename, add `class="publication-image" loading="lazy" decoding="async"`, write a concise paper-specific alt description, wrap titles in `<h3 class="paper-title">`, and apply `paper-authors`, `paper-meta`, and `paper-links` without changing metadata.

- [ ] **Step 6: Run content tests**

```powershell
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_homepage -v
```

Expected: biography, paper metadata, image count, uniqueness, existence, and alt tests pass; CSS hook tests remain failing until Task 4.

- [ ] **Step 7: Commit markup**

```powershell
git add index.html
git commit -m "feat: add TPAMI paper and publication artwork"
```

### Task 4: Implement the Monochrome Academic Design

**Files:**
- Modify: `style.css`
- Test: `tests/test_homepage.py`

**Interfaces:**
- Consumes: semantic classes and articles from Task 3.
- Produces: desktop/mobile academic presentation with focus and reduced-motion support.

- [ ] **Step 1: Define design tokens**

Add `--ink: #171717`, `--muted: #666`, `--line: #dedede`, `--soft: #f7f7f7`, `--paper: #fff`, `--max-width: 1040px`, and `--transition: 160ms ease`.

- [ ] **Step 2: Restyle shell and navigation**

Use a white background, readable Source Sans Pro/system stack, translucent white sticky header, 1 px lower border, safe `z-index`, centered maximum width, and `scroll-margin-top` for anchored sections.

- [ ] **Step 3: Refine biography and sections**

Improve prose measure and vertical rhythm, give the portrait a thin monochrome frame, stack biography columns below 768 px, make section headings typographically clear with a thin rule, and align News bullets consistently.

- [ ] **Step 4: Style publication articles**

Use thin separators and 24–28 px vertical padding with no large shadows. Give images `aspect-ratio: 16 / 9`, `object-fit: cover`, restrained rounding, mild grayscale by default, and color restoration on hover/focus. Style titles, author lines, venues, links, and outlined badges in monochrome hierarchy.

- [ ] **Step 5: Add accessibility and responsive rules**

Add visible `:focus-visible` outlines, card stacking below 768 px, compact wrapping navigation below 640 px, and a `@media (prefers-reduced-motion: reduce)` rule that removes nonessential transitions.

- [ ] **Step 6: Run the full regression test**

```powershell
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_homepage -v
```

Expected: PASS for every test.

- [ ] **Step 7: Commit styling**

```powershell
git add style.css
git commit -m "style: refine homepage with monochrome academic layout"
```

### Task 5: Browser QA and Final Verification

**Files:**
- Modify if defects are found: `index.html`, `style.css`, or affected WebP files.
- Test: `tests/test_homepage.py`

**Interfaces:**
- Consumes: completed static site.
- Produces: a verified homepage ready for GitHub Pages deployment.

- [ ] **Step 1: Start a local server**

```powershell
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m http.server 4173 --directory .
```

- [ ] **Step 2: Inspect desktop at approximately 1440 × 1000**

Verify header, biography balance, new-paper prominence, image/title correspondence, row rhythm, all local images, keyboard focus, and absence of horizontal overflow.

- [ ] **Step 3: Inspect mobile at 390 × 844**

Verify navigation wrapping, biography stacking, paper-title readability, image ratios, link targets, section anchor offsets, and absence of clipping.

- [ ] **Step 4: Inspect diagnostics**

Confirm there are no missing assets, console errors, invalid nested interactive elements, or mixed-content requests.

- [ ] **Step 5: Run final checks**

```powershell
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_homepage -v
git diff --check
git status --short
```

Expected: tests pass, `git diff --check` is silent, and status contains only intentional corrections if any remain.

- [ ] **Step 6: Commit QA corrections when needed**

```powershell
git add index.html style.css data/paper_thumbnail tests/test_homepage.py
git commit -m "fix: polish responsive homepage presentation"
```

- [ ] **Step 7: Review final scope**

```powershell
git diff HEAD~4..HEAD --stat
git log -5 --oneline
```

Confirm the diff contains only design documentation, plan, test, homepage HTML/CSS, and 21 publication images.
