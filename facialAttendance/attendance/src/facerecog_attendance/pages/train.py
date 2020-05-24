import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = "/home/amar/BCP/FaceDb"
face_recog = cv2.CascadeClassifier(
    '/home/amar/BCP/attendance/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
# print(image_dir)
current_id = 0
label_id = {}
x_train = []
y_labels = []

for root, dirs, files in os.walk(image_dir):
    # print("Root {}" .format(root))
    # print("Dirs {}" .format(dirs))
    # print("Files {}" .format(files))
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            # print(path)
            labels = os.path.basename(file.replace(" ", "-").lower())
            id = os.path.basename(root)
            # print(labels)
            # print(id)
            dot = labels.find('.')
            name = ""
            for x in range(dot):

                if labels[x].isalpha():
                    name += labels[x]

            # print(name)
            if not name in label_id:
                label_id[name] = int(id)
            #
            # print(label_id)
            id_ = label_id[name]
            # print("id_ {}".format(id_))
            # print("id_type {}".format(type(id_)))
            # print("Label IDS {}".format(label_id))
            # print(name, path)
            # x_train.append(path)
            # y_labels.append(name)
            pil_image = Image.open(path).convert("L")
            size = (450, 450)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            #             # print(image_array)
            faces = face_recog.detectMultiScale(image_array, 1.3, 5)
            for x, y, w, h in faces:
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(int(id_))
    #
    # print(" y_labels : {}".format(y_labels))
    # print(x_train)
    #
    with open("labels.pickle", "wb") as f:
        pickle.dump(label_id, f)
#


recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
