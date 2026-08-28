import frappe
from frappe.query_builder import DocType

def custom_logic(doc, method=None):
    frappe.msgprint("Hook executed!")


@frappe.whitelist()
def get_recent_todos():
    todos = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit_page_length=5,
    )

    for todo in todos:
        todo["email"] = frappe.db.get_value(
            "User",
            todo["owner"],
            "email"
        )

    timestamp = frappe.utils.now()

    return {
        "timestamp": timestamp,
        "records": todos,
    }
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