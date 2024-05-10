from flask import jsonify, flash, request, redirect, url_for, render_template
from sqlalchemy.exc import IntegrityError
from config.db import db

from views.question_views import question_blp


@question_blp.errorhandler(404)
def page_not_found(e):
    return render_template('admin/error/404.html'), 404


@question_blp.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "message": str(e)}), 500


@question_blp.errorhandler(IntegrityError)
def sqlalchemy_integrity_error(e):
    db.session.rollback()
    flash("Database error: Integrity issue.", category="error")
    return False


@question_blp.errorhandler(Exception)
def exception_handler(e):
    db.session.rollback()
    flash(f'Error: {e}', 'error')
    return False
