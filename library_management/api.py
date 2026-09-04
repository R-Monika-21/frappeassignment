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
def create_library_member(first_name, last_name, email_address):
    member = frappe.new_doc("Library member")
    member.first_name = first_name
    member.last_name = last_name
    member.email_address = email_address
    member.save()
    return member.name

@frappe.whitelist()
def update_books_with_query_builder():
    Book = DocType("Book")
    BookAuthor = DocType("Book Author")

    results = (
        frappe.qb.from_(Book)
        .join(BookAuthor)
        .on(Book.author == BookAuthor.name)
        .select(
            Book.name,
            Book.book_title,
            Book.status,
            BookAuthor.author_name,
        )
        .limit(5)
        .run(as_dict=True)
    )
    if results:
        book = frappe.get_doc("Book", results[0]["name"])
        book.status = "Borrowed"
        book.save()
    return results