import frappe
from frappe.tests.utils import FrappeTestCase


class TestArticle(FrappeTestCase):

    def test_article_creation(self):
        article = frappe.get_doc({
            "doctype": "Article",
            "section_break_fkqn": "My First Test",
            "status": "Published"
        })

        article.insert()

        self.assertEqual(article.section_break_fkqn, "My First Test")
        self.assertTrue(frappe.db.exists("Article", article.name))