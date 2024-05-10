from flask import jsonify, render_template

from views.question_views import question_blp


@question_blp.errorhandler(404)
def page_not_found(e):
    return render_template('admin/error/404.html'), 404


@question_blp.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "message": str(e)}), 500