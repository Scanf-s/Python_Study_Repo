def get_admin_form_data(form):
    username = form.username.data
    password = form.password.data
    return username, password


def get_question_form_data(form):
    content = form.content.data
    order_num = form.order_num.data
    is_active = form.is_active.data
    return content, order_num, is_active
