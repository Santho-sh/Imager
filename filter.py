from PIL import Image
from sys import exit
import re


def main():

    print("---WELCOME---")
    # get image name
    image_name = input("Enter Image Name: ")

    if validate_image():
        try:
            image = Image.open(image_name)

        except FileNotFoundError():
            exit("File doesn't exit, Image must be in same directory")

        # getting wich filter to use from user
        filter = get_filter()

        # apply that filter and save it
        apply_filter(image, filter)

    else:
        print("Please Enter Valid input")


def validate_image(name):

    # validate image
    if image := re.search(r"^.+\.(.+)$", name, re.IGNORECASE):
        file_type = image.group(1)
        if file_type in ["png", "jpeg", "jpg"]
            return True
        else:
            return False

    # return image name
    else:
        return False


def get_filter():
    # get which filter to use
    ...


def apply_filter(image, filter):
    # Greyscale
    ...
    # Reverse
    ...
    # chanege file format
    ...
    # blur image
    ...
    # Rotate
    ...
    # resize
    ...
    # watermark


if __name__ == "__main__":
    main()
