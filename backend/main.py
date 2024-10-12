from flask import Flask, render_template, request

from backend.src.db_controller import DBController
from backend.src.image_controller import ImageController
from backend.src.model_processor import ModelProcessor

app = Flask(__name__)

## LIST OF arms
# get image list
# post load image
# post load images
# get dump results
# get image
# post add bounding box
# post update bounding box

model_processor = ModelProcessor()
db_controller = DBController()
img_control = ImageController(db_controller, model_processor)


@app.route('/')
def endpoint_index():
    return render_template('index.html')


@app.route("/check", methods=['GET'])
def endpoint_check():
    return "<p>Still alive!</p>"


@app.route("/get_image_list", methods=['GET'])
def endpoint_get_image_list():
    return img_control.get_image_list()


@app.route("/post_load_image", methods=['POST'])
def endpoint_post_load_image():
    image_data = request.json()
    img_id = img_control.add_image(image_data)
    img_control.process_img(img_id)
    return img_id


@app.route("/post_load_images", methods=['POST'])
def endpoint_post_load_images():
    images_data = request.json()
    img_id_list = []
    for image_data in images_data:
        img_id = img_control.add_image(image_data)
        img_control.process_img(img_id)
        img_id_list.append(img_id)
    return img_id_list


@app.route("/get_dump_results", methods=['GET'])
def endpoint_get_dump_results():
    return img_control.dump_results()


@app.route("/get_image", methods=['GET'])
def endpoint_get_image():
    image_id = request.json()
    return img_control.get_image(image_id)


@app.route("/post_add_bounding_box", methods=['POST'])
def endpoint_post_add_bounding_box():
    image_data = request.json()
    img_id = image_data["img_data"]
    bounding_boxes = image_data["bounding_boxes"]
    return img_control.add_bounding_box(img_id, bounding_boxes)


@app.route("/post_update_bounding_box", methods=['POST'])
def endpoint_post_update_bounding_box():
    image_data = request.json()
    img_id = image_data["img_data"]
    bounding_boxes = image_data["bounding_boxes"]
    return img_control.update_bounding_box(img_id, bounding_boxes)


@app.route("/get_start_retrain", methods=['GET'])
def endpoint_post_update_bounding_box():
    state = img_control.model_processor.retrain()
    return state


if __name__ == '__main__':
    app.run(host='0.0.0.0')
