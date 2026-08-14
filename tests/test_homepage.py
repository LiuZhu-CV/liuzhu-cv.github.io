import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class PublicationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_publications = False
        self.section_depth = 0
        self.images = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "div" and attributes.get("id") == "publications":
            self.in_publications = True
            self.section_depth = 1
            return

        if self.in_publications and tag == "div":
            self.section_depth += 1

        if self.in_publications and tag == "img":
            src = attributes.get("src", "")
            if "paper_thumbnail" in src:
                self.images.append((src, attributes.get("alt", "")))

    def handle_endtag(self, tag):
        if self.in_publications and tag == "div":
            self.section_depth -= 1
            if self.section_depth == 0:
                self.in_publications = False


class HomepageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8")
        cls.active_html = re.sub(r"<!--.*?-->", "", cls.html, flags=re.S)
        cls.css = (ROOT / "style.css").read_text(encoding="utf-8")
        cls.parser = PublicationParser()
        cls.parser.feed(cls.active_html)

    def test_biography_identifies_fourth_year(self):
        self.assertIn("fourth-year Ph.D. student", self.active_html)
        self.assertNotIn("third-year Ph.D. student", self.active_html)

    def test_homography_paper_metadata_and_link_are_present(self):
        required = (
            "Toward Reliable Homography Estimation under Adverse Degradations",
            "Risheng Liu",
            "Jiahao Zhang",
            "Zengxi Zhang",
            "Q1A*+",
            "citation_for_view=WDjOXbIAAAAJ:qUcmZB5y_30C",
        )
        for value in required:
            with self.subTest(value=value):
                self.assertIn(value, self.active_html)

    def test_homography_paper_marks_co_corresponding_authors(self):
        self.assertIn("Risheng Liu<sup>†</sup>", self.active_html)
        self.assertIn("<u>Zhu Liu</u><sup>†</sup>", self.active_html)
        self.assertIn("† Co-corresponding authors", self.active_html)

    def test_mm26_publication_metadata_order_and_links_are_present(self):
        title = (
            "Decoupling Corruption from Observation: A Physics-Informed "
            "Generative Model for Infrared Image Super-Resolution"
        )
        required = (
            title,
            "Benzhuang Zhang, <u>Zhu Liu</u>, Siyuan Ding",
            "ACM International Conference on Multimedia",
            "https://doi.org/10.1145/3767308.3834923",
            "https://github.com/bzHunter/DECO",
            "One paper on thermal infrared image super-resolution was accepted by ACM MM 2026.",
            "data/paper_thumbnail/deco-thermal-ir.webp",
        )
        for value in required:
            with self.subTest(value=value):
                self.assertIn(value, self.active_html)

        self.assertLess(
            self.active_html.index("Toward Reliable Homography Estimation"),
            self.active_html.index(title),
        )
        self.assertLess(
            self.active_html.index(title),
            self.active_html.index("Diffuse to Detect"),
        )

    def test_each_active_publication_has_a_unique_local_thumbnail(self):
        sources = [src for src, _ in self.parser.images]
        self.assertEqual(22, len(sources))
        self.assertEqual(22, len(set(sources)))
        self.assertIn("data/paper_thumbnail/deco-thermal-ir.webp", sources)
        self.assertTrue(all("default.jpg" not in src for src in sources))
        for src in sources:
            with self.subTest(src=src):
                self.assertTrue((ROOT / src).is_file())

    def test_publication_thumbnails_have_descriptive_alt_text(self):
        alts = [alt.strip() for _, alt in self.parser.images]
        self.assertEqual(22, len(alts))
        self.assertTrue(all(alt and alt.lower() != "boot" for alt in alts))

    def test_navigation_and_motion_accessibility_hooks_exist(self):
        self.assertIn('aria-label="Primary navigation"', self.active_html)
        self.assertIn(":focus-visible", self.css)
        self.assertIn("prefers-reduced-motion", self.css)

    def test_academic_service_roles_are_complete(self):
        required = (
            "Program Committee:",
            "ICML, CVPR, ICCV, NeurIPS, IJCAI, AAAI, ACM MM",
            "Reviewer:",
            "IEEE TIP, IEEE TCSVT, IEEE TMM, IEEE TIM, Information Fusion",
        )
        for value in required:
            with self.subTest(value=value):
                self.assertIn(value, self.active_html)


if __name__ == "__main__":
    unittest.main()
