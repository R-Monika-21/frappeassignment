frappe.ui.form.on("Library member", {
    refresh(frm) {

        
        frm.add_custom_button("Create Membership", () => {
            frappe.new_doc("Library Membership", {
                library_member: frm.doc.name
            });
        });

        
        frm.add_custom_button("Create Transaction", () => {
            frappe.new_doc("Library Transaction", {
                library_member: frm.doc.name
            });
        });

        
        frm.add_custom_button("Create Contact", () => {

            let dialog = new frappe.ui.Dialog({
                title: "Create Contact",

                fields: [
                    {
                        label: "First Name",
                        fieldname: "first_name",
                        fieldtype: "Data"
                    }
                ],

                primary_action_label: "Create Contact",

                primary_action(values) {
                    let first_name = values.first_name;

                    dialog.hide();

                    frappe.route_options = {
                        first_name: first_name
                    };

                    frappe.new_doc("Contact");
                }
            });

            dialog.show();
        });

        
        frm.add_custom_button("Create Library Member", () => {
    let dialog = new frappe.ui.Dialog({
        title: "Create Library Member",

        fields: [
            {
                label: "First Name",
                fieldname: "first_name",
                fieldtype: "Data",
                reqd: 1
            },
            {
                label: "Last Name",
                fieldname: "last_name",
                fieldtype: "Data"
            },
            {
                label: "Email Address",
                fieldname: "email_address",
                fieldtype: "Data"
            }
        ],

        primary_action_label: "Create Member",

        primary_action(values) {
            frappe.call({
                method: "library_management.api.create_library_member",
                args: {
                    first_name: values.first_name,
                    last_name: values.last_name,
                    email_address: values.email_address
                },

                callback: function(response) {
                    dialog.hide();

                    frappe.msgprint({
                        title: "Success",
                        message: "Library Member " + response.message + " created successfully.",
                        indicator: "green"
                    });
                }
            });
        }
    });

    dialog.show();
});
    }
});

