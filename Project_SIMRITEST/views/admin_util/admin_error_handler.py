from flask import jsonify, flash, request, redirect, url_for, render_template
from sqlalchemy.exc import IntegrityError
from config.db import db

from views.admin_views import admin_blp


@admin_blp.errorhandler(404)
def page_not_found(e):
    return render_template('admin/error/404.html'), 404


@admin_blp.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "message": str(e)}), 500


@admin_blp.errorhandler(IntegrityError)
def sqlalchemy_integrity_error(e):
    db.session.rollback()
    return render_template('admin/error/Integrity.html', error=str(e))


@admin_blp.errorhandler(AttributeError)
def attribute_error(e):
    flash(f"username : {request.form.get("username")} not exist", category="error")
    return redirect(url_for("admin.login"))


@admin_blp.errorhandler(Exception)
def exception_handler(e):
    flash(f"Error : {e}", category="error")
    return redirect(url_for("admin.home"))
