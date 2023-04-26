from flask import Blueprint, render_template
from website import mongo
import gridfs
import codecs

routes = Blueprint("routes", __name__)


@routes.route("/")
def home():

    # WRITE IMAGE TO MONGO DB FROM LOCAL (Eg Upload)

    # file_name = "website/dog2.png"
    fs = gridfs.GridFS(mongo.temp_database)
    # with open(file_name, "rb") as f:
    #     contents = f.read()
    # # Now store/put the image via GridFs object.
    # fs.put(contents, filename="dog_pic2")

    # READ IMAGE FROM MONGO DB

    # img = fs.find_one({"filename": "dog_pic"}).read()
    # base64_img = codecs.encode(img, "base64")
    # actual_img = base64_img.decode("utf-8")

    db = mongo.temp_database
    collection = db.test_pictures

    list_of_dicts = []

    for documents in collection.find():
        img_file_name = documents["img_file_name"]
        img = fs.find_one({"filename": img_file_name}).read()
        base64_img = codecs.encode(img, "base64")
        documents["base_64_img"] = base64_img.decode("utf-8")
        list_of_dicts.append(documents)

    return render_template("home.html", cards_to_render=list_of_dicts)


@routes.route("/login",methods=['GET'])
def login():
    return render_template("login.html")
    # return render_template("blogs.html", blogs = Blogs)
