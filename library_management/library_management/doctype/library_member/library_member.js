// Copyright (c) 2026, Monika R and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library member", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Library member', {
 refresh: function(frm) {
 frm.add_custom_button('Create Membership', () => {
 frappe.new_doc('Library Membership', {
 library_member: frm.doc.name
 })
 })
 frm.add_custom_button('Create Transaction', () => {
 frappe.new_doc('Library Transaction', {
 library_member: frm.doc.name
 })
 })
 }
});
