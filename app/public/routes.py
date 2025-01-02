from flask import abort, render_template
from werkzeug.exceptions import NotFound

from app.models import Post
from . import public_bp

@public_bp.route("/")
def index():
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        raise NotFound(slug)
        # También es válido emplear la siguiente línea como equivalente!
        # abort(404)
    return render_template("public/post_view.html", post=post)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)
