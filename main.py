from flask import Flask

app = Flask(__name__)


## LIST OF arms
# get image list
# post load image
# post load images
# post dump results
# get image
# post add bounding box
# post update bounding box

@app.route("/check", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_image_list", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post_load_image", methods=['POST'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post_load_images", methods=['POST'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post_dump_results", methods=['POST'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_image", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post_add_bounding_box", methods=['POST'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post_update_bounding_box", methods=['POST'])
def hello_world():
    return "<p>Hello, World!</p>"
