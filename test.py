import detection_front
import prediction
import detection_back


def detect_face():
    return detection_front.detect_face()


def face_recovery():
    return prediction.face_recovery()


def combine():
    vertices, size = detection_front.detect_face_only_plot()
    return detection_back.combine(vertices, size)


def main():
    detect_face()
    print(1)
    face_recovery()
    print(2)
    combine()
    print(3)
    pass


if __name__ == "__main__":
    main()
