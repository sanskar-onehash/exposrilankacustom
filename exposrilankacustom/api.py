import frappe

@frappe.whitelist()
def get_sub_branch_info(email):
    sub_branch = frappe.get_all('Sub Branch', filters={'email': email}, fields=['name', 'sub_branch', 'address', 'linked_user', 'email','region'], limit=1)
    
    if sub_branch:
        return sub_branch[0]

    return None