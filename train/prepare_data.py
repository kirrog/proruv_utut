import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

import cv2
from tqdm import tqdm

full_images_path = Path('../data/data_v2')
processed_path = Path('../data/processed')
images_path = processed_path / "images"
labels_path = processed_path / "labels"
processed_path.mkdir(parents=True, exist_ok=True)
images_path.mkdir(parents=True, exist_ok=True)
labels_path.mkdir(parents=True, exist_ok=True)

rename_dict = {
    "нет дефекта": "0",  # "no_defect",
    "царапины": "1",  # "scratch",
    "проблемы с клавишами": "2",  # "key_problem",
    "иные повреждения": "3",  # "others",
    "битые пиксели": "4",  # "pixels",
    "сколы": "5",  # "chips",
    "замок": "6",  # "lock",
    "отсутствует шуруп": "7",  # "missing_screw"
}


def resize_image(image, size=(320, 320)):
    return cv2.resize(image, size)


if __name__ == "__main__":
    classes = defaultdict(int)
    images_paths_list = list(full_images_path.glob("*.jpg"))
    labeles_paths_list = list(full_images_path.glob("*.xml"))
    files_pairs_paths = defaultdict(dict)
    for image_path in images_paths_list:
        case_name = "__".join(str(image_path.name).split(".")[:-1])
        files_pairs_paths[case_name]["image"] = image_path
    for label_path in labeles_paths_list:
        case_name = "__".join(str(label_path.name).split(".")[:-1])
        files_pairs_paths[case_name]["label"] = label_path

    shape_y_min = 1000
    shape_x_min = 1000
    shape_y_max = 0
    shape_x_max = 0

    for case_name, case_paths in tqdm(files_pairs_paths.items(), total=len(files_pairs_paths), desc="Files processing"):
        if not ("image" in case_paths and "label" in case_paths):
            print(f"Missed: {case_name}")
            continue

        image_path = case_paths["image"]
        label_path = case_paths["label"]

        image_data = cv2.imread(image_path)
        if image_data.shape[2] != 3:
            print("Strange size")

        shape_y_min = min(shape_y_min, image_data.shape[0])
        shape_x_min = min(shape_x_min, image_data.shape[1])
        shape_y_max = max(shape_y_max, image_data.shape[0])
        shape_x_max = max(shape_x_max, image_data.shape[1])

        parsed_xml = ET.parse(label_path)
        root_node = parsed_xml.getroot()

        bbx_list = list()
        for bbx in root_node.findall("object"):
            new_bbx = dict()
            for name in bbx.findall("name"):
                new_bbx["name"] = str(name.text)
            for bndbox in bbx.findall("bndbox"):
                for xmin in bndbox.findall("xmin"):
                    new_bbx["xmin"] = int(xmin.text)
                for xmax in bndbox.findall("xmax"):
                    new_bbx["xmax"] = int(xmax.text)
                for ymin in bndbox.findall("ymin"):
                    new_bbx["ymin"] = int(ymin.text)
                for ymax in bndbox.findall("ymax"):
                    new_bbx["ymax"] = int(ymax.text)
            bbx_list.append(new_bbx)

        image_resized = resize_image(image_data)
        cv2.imwrite(images_path / image_path.name, image_resized)
        label_out_name = ".".join(str(label_path.name).split(".")[:-1]) + ".txt"
        with (open(labels_path / label_out_name, 'w') as f):
            for annotation in bbx_list:
                cls = rename_dict[annotation["name"]]

                # if cls == "6" or cls == "7":
                #     continue

                # cls = annotation["name"]
                x1 = annotation["xmin"]
                y1 = annotation["ymin"]
                x2 = annotation["xmax"]
                y2 = annotation["ymax"]

                # x1 = max(x1 - 2, 3)
                # y1 = max(y1 - 2, 3)
                # x2 = max(x2 - 2, 3)
                # y2 = max(y2 - 2, 3)

                # x1 = min(x1, image_data.shape[1] - 3)
                # x2 = min(x2, image_data.shape[1] - 3)
                # y1 = min(y1, image_data.shape[0] - 3)
                # y2 = min(y2, image_data.shape[0] - 3)

                if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
                    print(f"Zero coord! {x1} {x2} {y1} {y2} {image_data.shape[1]} {image_data.shape[0]}")

                if (x1 >= image_data.shape[1] or
                        x2 >= image_data.shape[1] or
                        y1 >= image_data.shape[0] or
                        y2 >= image_data.shape[0]):
                    print(f"High coord! {x1} {x2} {y1} {y2} {image_data.shape[1]} {image_data.shape[0]}")

                x_center = (x1 + x2) / 2 / image_data.shape[1]
                y_center = (y1 + y2) / 2 / image_data.shape[0]
                width = abs(x2 - x1) / image_data.shape[1]
                height = abs(y2 - y1) / image_data.shape[0]
                if x_center >= 1.0 or y_center >= 1.0 or width >= 1.0 or height >= 1.0:
                    print(f"High! {x_center} {y_center} {width} {height} {image_data.shape[1]} {image_data.shape[0]}")
                if x_center <= 0.0 or y_center <= 0.0 or width <= 0.0 or height <= 0.0:
                    print(f"Low! {x_center} {y_center} {width} {height} {image_data.shape[1]} {image_data.shape[0]}")

                if (x_center + (width / 2) >= 1.0 or
                        y_center + (height / 2) >= 1.0 or
                        x_center - (width / 2) <= 0.0 or
                        y_center + (height / 2) <= 0.0):
                    # pass
                    print(
                        f"Borders! {x_center} {y_center} {width} {height} {image_data.shape[1]} {image_data.shape[0]}")
                    # continue

                f.write(f"{cls} {x_center} {y_center} {width} {height}\n")

                classes[cls] += 1
    print(classes)

print(shape_y_min)
print(shape_x_min)
print(shape_y_max)
print(shape_x_max)
