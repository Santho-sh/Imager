from PIL import Image, ImageFilter
from sys import exit
from colorama import Fore
import re


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
        print(Fore.RED  + "Please Enter Valid input" + Fore.WHITE)


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
    print("Enter which filter you want to apply? \n[1] Greyscale \n[2] Blur \n[3] Sharpen \n[4] Reverse \n[5] Rotate Upside Down \n[6] Resize the Image")
    while True:
        filter = input("Filter No: ")
        
        match filter:
            case "1":
                return "greyscale"
            case "2":
                return "blur"
            case "2":
                return "sharpen"
            case "3":
                return "reverse"
            case "4":
                return "rotale"
            case "5":
                return "resize"
            case _:
                print("Please Enter the filter [1 to 5] you want...")
                continue
    

def apply_filter(image_name, filter_name):
    try:
        image = Image.open(image_name)
        
    except FileNotFoundError:
        exit(Fore.RED  + "File doesn't exit,\nImage must be in same directory" + Fore.WHITE)
    
    # Greyscale
    # Sharpen
    if  filter_name == "sharpen":
        image = image.filter(ImageFilter.SHARPEN)
        image = image.save(f"edited_{image_name}")
    # Reverse
    # chanege file format
    # blur image
    elif filter_name == "blur":
        image = image.filter(ImageFilter.BLUR)
        image = image.save(f"edited_{image_name}")
    # Rotate
    # resize
    else:
        None



if __name__ == "__main__":
    main()
