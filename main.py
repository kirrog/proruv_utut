from flask import Flask

app = Flask(__name__)

# LIST OF arms
# get image list
# post load image
# post load images
# post dump results
# get image
# post add bounding box
# post update bounding box

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"