from PIL import Image, ImageFilter
from sys import exit
from colorama import Fore
import re
import cv2
import numpy as np


def main():

    print("---WELCOME---")
    # get image name
    image_name = input("Enter Image Name: ")

    if validate_image(image_name):
        # getting wich filter to use from user
        filter = get_filter()

        # apply that filter and save it
        apply_filter(image_name, filter)

    else:
        print(Fore.RED + "Please Enter Valid input" + Fore.WHITE)


def validate_image(name):

    # validate image
    if image := re.search(r"^.+\.(.+)$", name, re.IGNORECASE):
        file_type = image.group(1)
        if file_type in ["png", "jpeg", "jpg"]:
            return True
        else:
            return False

    # return image name
    else:
        return False


def get_filter():
    # get which filter to use
    print(
        "Enter which filter you want to apply? \n[1] Greyscale \n[2] Blur \n[3] Sharpen \n[4] Reverse \n[5] Rotate \n[6] Change Resolutione (Only jpg/jpeg)\n")

    while True:
        filter = input("Filter No: ")

        match filter:
            case "1":
                return "greyscale"
            case "2":
                return "blur"
            case "3":
                return "sharpen"
            case "4":
                return "reverse"
            case "5":
                return "rotate"
            case "6":
                return "resolution"
            case _:
                print("Please Enter the filter [1 to 6]")
                continue


def apply_filter(image_name, filter_name):
    try:

        # Greyscale
        if filter_name == "greyscale":
            image = cv2.imread(image_name)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"edited_{image_name}", image)

        # blur image
        elif filter_name == "blur":
            image = Image.open(image_name)
            image = image.filter(ImageFilter.BLUR)
            image.save(f"edited_{image_name}")

        # Sharpen
        elif filter_name == "sharpen":

            # kernel = np.array([[0, -1, 0],
            #                    [-1, 5,-1],
            #                    [0, -1, 0]])
            # image = cv2.imread(image_name)
            # image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
            # cv2.imwrite(f"edited_{image_name}", image)

            image = Image.open(image_name)
            image = image.filter(ImageFilter.SHARPEN)
            image.save(f"edited_{image_name}")

        # Reverse
        elif filter_name == "reverse":
            image = Image.open(image_name)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image.save(f"edited_{image_name}")

        # Changing Image Resolution
        elif filter_name == "resolution":
            while True:
                print(
                    "Enter a Quality of an image You want [1 to 100]\n[100] is the highest quality\n[ 1 ] is the lowest quality\n")
                res = input("Enter [1 to 100]: ")

                if res.isdigit():

                    res = int(res)
                    if 1 <= res <= 100:
                        image = Image.open(image_name)
                        image.save(f"edited_{image_name}", quality=res)
                        break
                    else:
                        print("Please enter a number between 1 to 100")

        # Rotate
        elif filter_name == "rotate":
            while True:
                print(
                    "[1] Rotate 90 degree\n[2] Rotate 120 degree\n[3] Rotate 180 degree")
                rotate = input("Enter [1 to 3]: ")

                if rotate == "1":
                    image = Image.open(image_name)
                    image = image.transpose(Image.ROTATE_90)
                    break
                elif rotate == "2":
                    image = Image.open(image_name)
                    image = image.transpose(Image.FLIP_TOP_BOTTOM)
                    break
                elif rotate == "3":
                    image = Image.open(image_name)
                    image = image.transpose(Image.ROTATE_270)
                    break
                else:
                    continue

            image.save(f"edited_{image_name}")

    except FileNotFoundError:
        exit(Fore.RED + "File doesn't exit,\nImage must be in same directory" + Fore.WHITE)

    # save the image
    print(Fore.GREEN + "Image Saved Successfully" + Fore.WHITE)


if __name__ == "__main__":
    main()
