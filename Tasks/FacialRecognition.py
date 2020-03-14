import face_recognition
import os
import cv2
import Assistant


class FacialRecognition(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.KNOWN_FACES_DIR = "../data/known_faces"
        self.UNKNOWN_FACES_DIR = "data/unknown_faces"
        self.encodings = []
        self.names = []
        self.name = "I don't recognize you"
        self.FRAME_THICKNESS = 3
        self.FONT_THICKNESS = 1
        self.encode_images()

    def encode_images(self):
        for img in os.listdir(f"{self.KNOWN_FACES_DIR}"):
            image = face_recognition.load_image_file(f"{self.KNOWN_FACES_DIR}/{img}")
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image_encoding = face_recognition.face_encodings(image)[0]
            self.encodings.append(image_encoding)
            self.names.append(img[:-4])

    def recognize(self):
        video = cv2.VideoCapture(0)
        while True:
            rect, frame = video.read()
            unknown_image = frame
            unknown_image = cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR)
            unknown_location = face_recognition.face_locations(unknown_image)
            unknown_encoding = face_recognition.face_encodings(unknown_image, unknown_location)
            for face_location, encoding in zip(unknown_location, unknown_encoding):
                matches = face_recognition.compare_faces(self.encodings, encoding)
                if True in matches:
                    first_match_index = matches.index(True)
                    self.name = self.names[first_match_index]
                    print(self.name)
                    break
            if self.name in self.names:
                self.speak(f"Hello {self.name}")
                break
        return self.name
