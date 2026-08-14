# ACM MM 2026 Publication Entry Design

## Goal

Add the accepted ACM Multimedia 2026 paper from `MM_Thermal_IR.pdf` to the academic homepage while preserving the established editorial visual system and keeping the existing TPAMI paper first.

## Verified publication data

- Title: *Decoupling Corruption from Observation: A Physics-Informed Generative Model for Infrared Image Super-Resolution*
- Authors: Benzhuang Zhang, Zhu Liu, Siyuan Ding, Wengeng Chen, Xingyuan Li, Jinyuan Liu, Long Ma, and Risheng Liu
- Venue: Proceedings of the 34th ACM International Conference on Multimedia (ACM MM), 2026
- Zhu Liu is the second author and is highlighted with the homepage's existing underline treatment.
- Paper: `https://doi.org/10.1145/3767308.3834923`
- Code: `https://github.com/bzHunter/DECO`

## Page changes

1. Add a 2026 News item announcing one ACM MM 2026 paper.
2. Insert the publication immediately after the featured TPAMI item and before the ICML 2026 item.
3. Create a local WebP thumbnail from Figure 1 on the PDF's first page. The crop will retain the quantitative radar plots and real-camera comparison, avoiding body text and author information.
4. Use the existing publication card markup, typography, spacing, lazy loading, and responsive image behavior. No unrelated layout changes are included.

## Validation

- Add a regression test for the title, second-author markup, venue, DOI, code link, News item, and local thumbnail path.
- Update the expected active thumbnail count and confirm every thumbnail path is unique and exists.
- Run the full homepage test suite and `git diff --check` before committing.

