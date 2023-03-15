from flask import Blueprint, render_template
from website import mongo
import gridfs
import codecs

routes = Blueprint("routes", __name__)


@routes.route("/")
def home():

    # WRITE IMAGE TO MONGO DB FROM LOCAL (Eg Upload)

    # file_name = "website/dog2.png"
    # fs = gridfs.GridFS(mongo.temp_database)
    # with open(file_name, "rb") as f:
    #     contents = f.read()
    # # Now store/put the image via GridFs object.
    # fs.put(contents, filename="dog_pic2")

    # READ IMAGE FROM MONGO DB

    # img = fs.find_one({"filename": "dog_pic"}).read()
    # base64_img = codecs.encode(img, "base64")
    # actual_img = base64_img.decode("utf-8")
    return render_template("home.html")


@routes.route("/blogs")
def blogs():
    return render_template("blogs.html")
    # return render_template("blogs.html", blogs = Blogs)
