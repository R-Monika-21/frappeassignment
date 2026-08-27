# Copyright (c) 2026, Monika R and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Librarymember(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name or ''}"
		print("Full name calculated")
