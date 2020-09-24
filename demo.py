import detection_front
# import prediction
# import detection_back

# from detection_front import detect_face


def main():
    print("Extracting Face...")
    detection_front.detect_face()
    print("Face Detection Complete!!")


if __name__ == "__main__":
    main()
