from env import export_passwd # custom python file
import time
from PIL import Image
import PIL
import numpy as np

# list of ascii characters used when convert image to ascii text
list_ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# resize image according to a new width
def resize_image(pil_obj_image, new_width):
    width, height = pil_obj_image.size # obj_image = image object read using PIL.Image.open method
    ratio = height / width
    new_height = int(new_width * ratio) # you can modify height of resized-image here. [ e.g. new_height = int(new_width * ratio * 0.5) ]
    resized_image = pil_obj_image.resize((new_width, new_height))

    return resized_image


# convert each pixel in image to grayscale pixel
def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image


# convert each pixel to ASCII character
def convert_pixels_to_ascii(pil_obj_image):
    pixels = pil_obj_image.getdata()
    str_ascii_img = ''.join([list_ascii_chars[pixel//25] for pixel in pixels]) # return list of ASCII character for each pixel

    return str_ascii_img

def main():
    # 200 means the number of pixels in one line, which is the same meaning of the number of ASCII character in one line.
    new_width = 4000
    path = './test.jpg'
    image = PIL.Image.open(path)
    new_width = image.size[0]
    print(f"new_width: {new_width}")
    # print(path, "<- This is invalid path.")


    # convert image to ASCII string
    raw_ascii_image = convert_pixels_to_ascii(grayify(resize_image(image, new_width)))

    pixel_count = len(raw_ascii_image)
    ascii_image = '\n'.join(raw_ascii_image[i:(i+new_width)] for i in range(0, pixel_count, new_width)) # cutting raw ASCII image text to 200, which is 'new_width'

    # print result
    print(ascii_image)

    # save result(ASCII image) to 'img/apple.txt'
    with open('./test.txt', 'w') as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()
    # print(f"For Testing docker build First!")
    # passwd = export_passwd()
    # print(f"Your passwd is \"{passwd}\"")
    # print(f"For Testing docker build First!")
    