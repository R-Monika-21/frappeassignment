# Copyright (c) 2026, Monika R and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report."""
	columns = get_columns()
	data = get_data()

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report."""
	return [
		{
			"label": _("No."),
			"fieldname": "serial_no",
			"fieldtype": "Int",
			"width": 80,
		},
		{
			"label": _("Author Name"),
			"fieldname": "author_name",
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"label": _("Email"),
			"fieldname": "email",
			"fieldtype": "Data",
			"width": 250,
		},
		{
			"label": _("Created On"),
			"fieldname": "creation",
			"fieldtype": "Datetime",
			"width": 180,
		},
	]


def get_data() -> list[dict]:
	"""Return Book Author data."""
	authors = frappe.get_all(
		"Book Author",
		fields=["author_name", "email", "creation"],
		order_by="author_name asc",
	)

	data = []

	for index, author in enumerate(authors, start=1):
		data.append(
			{
				"serial_no": index,
				"author_name": author.author_name,
				"email": author.email,
				"creation": author.creation,
			}
		)

	return data