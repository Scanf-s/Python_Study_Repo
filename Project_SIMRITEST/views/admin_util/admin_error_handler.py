from flask import jsonify, flash
from sqlalchemy.exc import IntegrityError

from views.admin_views import admin_blp


@admin_blp.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found", "message": str(e)}), 404


@admin_blp.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "message": str(e)}), 500


@admin_blp.errorhandler(IntegrityError)
def sqlalchemy_integrity_error(e):
    flash("There are duplicate elements in database. Please use another username or email", "error")
    return jsonify({"error": "Integrity Error", "message": str(e)}), 400


@admin_blp.errorhandler(Exception)
def exception_handler(e):
    return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500
