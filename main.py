import json
import os

import redis
from dotenv import load_dotenv
from flask import Flask, render_template, request
from requests_toolbelt import MultipartEncoder

from src.db_controller import DBController
from src.image_controller import ImageController
from src.model_processor import ModelProcessor

load_dotenv()

redis_controller = redis.Redis(host='redis', port=6379, db=0,
                               username=os.getenv("REDIS_USER"),
                               password=os.getenv("REDIS_USER_PASSWORD"))

try:
    info = redis_controller.info()
    print(info['redis_version'])
    response = redis_controller.ping()
    if response:
        print("Подключение успешно!")
    else:
        print("Не удалось подключиться к Redis.")
except redis.exceptions.RedisError as e:
    print(f"Ошибка: {e}")

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
db_controller = DBController(redis_controller)
img_control = ImageController(db_controller, model_processor)


@app.route('/')
def endpoint_index():
    return render_template('index.html')


@app.route("/check", methods=['GET'])
def endpoint_check():
    return "<p>Still alive!</p>"


@app.route("/get_image_list", methods=['GET'])
def endpoint_get_image_list():
    image_instance = img_control.get_image_list()
    return image_instance


@app.route("/post_load_image", methods=['POST'])
def endpoint_post_load_image():
    img_data = request.files['img_data'].read()
    image_data = request.form
    print(img_data[:100])
    print(image_data)
    img_id = img_control.add_image(img_data, image_data)
    img_control.process_img(img_id)
    return img_id


@app.route("/post_load_images", methods=['POST'])
def endpoint_post_load_images():
    images_data = request.json
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
    req_json = request.json
    img_entity = img_control.get_image(req_json["img_id"])
    m = MultipartEncoder(fields={'img_id': img_entity.img_id,
                                 'img_name': img_entity.img_name,
                                 'img_comment': img_entity.img_comment,
                                 'img_defect_list': json.dumps(img_entity.img_defect_list),
                                 'files': ("image", img_entity.img_data, 'image.png')})
    return (m.to_string(), {'Content-Type': m.content_type})


@app.route("/post_add_bounding_box", methods=['POST'])
def endpoint_post_add_bounding_box():
    image_data = request.json
    img_id = image_data["img_data"]
    bounding_boxes = image_data["bounding_boxes"]
    return img_control.add_bounding_box(img_id, bounding_boxes)


@app.route("/post_update_bounding_box", methods=['POST'])
def endpoint_post_update_bounding_box():
    image_data = request.json
    img_id = image_data["img_data"]
    bounding_boxes = image_data["bounding_boxes"]
    return img_control.update_bounding_box(img_id, bounding_boxes)


@app.route("/get_start_retrain", methods=['GET'])
def endpoint_start_retrain():
    state = img_control.model_processor.retrain()
    return state


if __name__ == '__main__':
    app.run(host='0.0.0.0')
