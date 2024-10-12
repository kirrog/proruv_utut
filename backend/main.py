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
def endpoint_check():
    return "<p>Hello, World!</p>"


@app.route("/get_image_list", methods=['GET'])
def endpoint_get_image_list():
    return "<p>Hello, World!</p>"


@app.route("/post_load_image", methods=['POST'])
def endpoint_post_load_image():
    return "<p>Hello, World!</p>"


@app.route("/post_load_images", methods=['POST'])
def endpoint_post_load_images():
    return "<p>Hello, World!</p>"


@app.route("/post_dump_results", methods=['POST'])
def endpoint_post_dump_results():
    return "<p>Hello, World!</p>"


@app.route("/get_image", methods=['GET'])
def endpoint_get_image():
    return "<p>Hello, World!</p>"


@app.route("/post_add_bounding_box", methods=['POST'])
def endpoint_post_add_bounding_box():
    return "<p>Hello, World!</p>"


@app.route("/post_update_bounding_box", methods=['POST'])
def endpoint_post_update_bounding_box():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
