from flask import Blueprint, render_template
from website import mongo

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
    print(mongo.list_database_names())
    return render_template("home.html")


@routes.route("/blogs")
def blogs():
    return render_template("blogs.html")
    # return render_template("blogs.html", blogs = Blogs)
