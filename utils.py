import cv2
import json


def load_config():
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)

    except FileNotFoundError:
        print("config.json not found in working directory")
        print("Using in-built values")
        config = {
            "meta_data": {
                "width": 256,
                "height": 256,
                "channels": 3
            },
            "camera_params": {
                "f_x": 0.0,
                "f_y": 0.0,
                "k_1": 0.0,
                "k_2": 0.0,
                "p_1": 0.0,
                "p_2": 0.0,
                "k_3": 0.0
            }
        }
    return config


def read_image_file(img_file):
    config = load_config()['meta_data']

    width, height, channels = config.values()

    src = cv2.imread(str(img_file), cv2.IMREAD_UNCHANGED)
    src = cv2.resize(src, (width, height))

    return src


def write_image_file(img, file_name):

    cv2.imwrite(file_name, img)

    return True
