from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

# Blogs  = [
#         {
#             'id': 1,
#             'title': 'blog1',
#             'body': 'blog1body',
#         },
#         {
#             'id': 2,
#             'title': 'blog2',
#             'body': 'blog2body',
#         },
#     ]

@routes.route("/")
def home():
    return render_template("home.html")

@routes.route("/blogs")
def blogs():
    return render_template("blogs.html")
    # return render_template("blogs.html", blogs = Blogs)
