# Minimal Academic Homepage Refresh

## Goal

Refresh Zhu Liu's personal academic homepage with a restrained black-and-white visual system, add the new TPAMI homography paper, update the biography to fourth-year Ph.D. status, and replace every generic white publication placeholder with a paper-specific thumbnail.

## Scope

The implementation will retain the existing static HTML, CSS, Bootstrap, and GitHub Pages architecture. It will modify `index.html`, `style.css`, and publication assets under `data/paper_thumbnail/`. No framework migration, build system, CMS, or unrelated content rewrite is included.

## Content Changes

1. Change “third-year Ph.D. student” to “fourth-year Ph.D. student”.
2. Add the following paper at the top of Selected Publications:
   - Title: *Toward Reliable Homography Estimation under Adverse Degradations: An Optimization-Driven Approach*
   - Authors: Risheng Liu, Jiahao Zhang, Zengxi Zhang, Zhu Liu
   - Venue: IEEE Transactions on Pattern Analysis and Machine Intelligence
   - Badge: `Q1A*+`
   - Primary link: the Google Scholar citation URL supplied by the author
3. Add a concise News entry for the TPAMI paper when publication timing can be represented consistently with the existing reverse-chronological News list. If the source page does not provide a reliable month, use a year-only entry rather than inventing a month.
4. Preserve existing paper titles, author order, venues, links, and emphasis unless a direct source reveals an obvious typo.

## Visual Direction

The page will use a minimal monochrome academic style:

- White background, near-black headings, and neutral gray secondary text.
- Thin rules and subtle borders instead of colored panels or heavy shadows.
- A compact centered content column with more consistent vertical rhythm.
- Clear typography hierarchy across identity, section headings, paper titles, authors, venues, and links.
- Understated monochrome link treatment with visible hover and keyboard-focus states.
- A fixed or sticky navigation treatment that remains lightweight and does not obscure anchored sections.
- Motion limited to short thumbnail and link transitions, with reduced-motion support.

## Publication Cards

Each publication remains a horizontal row on desktop and becomes a stacked card on narrow screens.

- Thumbnails use one consistent aspect ratio and crop behavior.
- Images appear slightly desaturated in the default state and return toward full color on hover or focus.
- The paper title is the strongest textual element.
- Authors and venue remain compact and legible.
- Venue and distinction labels use small outlined monochrome badges; the new paper receives `IEEE TPAMI` and `Q1A*+` labels.
- Existing Paper and Code links remain available and gain consistent spacing and focus styles.

## Thumbnail Strategy

Every publication currently using `data/paper_thumbnail/default.jpg` will receive a paper-specific image.

Source priority:

1. Reuse the matching publication thumbnail from `https://rsliu.tech/Publication.html` when the title matches.
2. Use a thumbnail derived from the paper's first page, teaser, or principal method/result figure when a matching source-page image is unavailable.
3. For papers without accessible visual material, create a restrained topic-specific scientific thumbnail that contains no fabricated quantitative results, logos, or claims.

All local assets will use descriptive stable filenames, web-friendly formats, and meaningful `alt` text. Remote images will be copied into the repository rather than hot-linked, so the homepage remains stable if the source site changes.

## Responsive and Accessibility Behavior

- Desktop publication rows use a fixed thumbnail column and flexible text column.
- Mobile rows stack image above text without forcing Bootstrap's current narrow `col-3`/`col-9` biography layout.
- Navigation wraps or collapses cleanly at small widths.
- Images have informative alternative text; decorative visuals use empty alternative text.
- Focus indicators remain visible, text contrast meets normal-content expectations, and hover-only effects have keyboard equivalents.
- Anchor targets account for the sticky header.

## Data Flow and Failure Handling

The page remains fully static. Assets are resolved at implementation time and stored locally. If a source thumbnail cannot be downloaded or is too low-resolution, the implementation falls back to a paper PDF teaser or a newly produced topic illustration. No broken remote image URL will be shipped.

## Verification

The completed page will be checked for:

- Correct biography status and exact new-paper metadata.
- No remaining references to `default.jpg` in active publication entries.
- Every local image path resolving successfully.
- Valid document structure and absence of obvious console errors.
- Desktop and mobile rendering, including overflow, card alignment, navigation, and image cropping.
- Keyboard-visible links and reduced-motion behavior.
- A final Git diff limited to the homepage refresh and associated assets.

## Non-Goals

- Rewriting the research statement or awards and services content.
- Adding analytics, a publication database, filtering, search, or JavaScript-heavy interactions.
- Redesigning posts or migrating the site to another generator.
- Inventing paper results, publication dates, project links, or citation metrics.
