import frappe
from frappe.query_builder import DocType

def custom_logic(doc, method=None):
    frappe.msgprint("Hook executed!")


@frappe.whitelist()
def update_articles():
    Article = DocType("Article")
    Author = DocType("Author")

    query = (
        frappe.qb.from_(Article)
        .join(Author)
        .on(Article.author == Author.name)
        .select(
            Article.name,
            Article.article_name,
            Article.status,
            Author.name.as_("author")
        )
        .limit(5)
    )

    results = query.run(as_dict=True)

    print(results)

    return results