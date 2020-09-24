import detection_front
import prediction
import detection_back


def main():
    choice = 0
    size = 0
    while(1):
        choice = int(input("1: Face Detection\n2: Face Recovery\n4: Exit\n"))
        if choice == 4:
            print("Exit...")
            break
        elif choice == 1:
            print("Extracting Face...")
            detection_front.detect_face()
            print("Face Detection Complete!!")
        elif choice == 2:
            print("Recovering Face...")
            prediction.face_recovery()
            print("Face ReCovery Complete!!")
        elif choice == 3:
            print("Combine to Origin Picture...")
            detection_back.combine(size)
            print("Combine Complete!!")
        else:
            print("Wrong Command!\n")


if __name__ == "__main__":
    main()
