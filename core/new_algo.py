import time
import cv2
import logo
import os
import colors

target_images_dir_name = ""
target_images_dir_name_default = "images"


def check_match(source):
    try:
        import numpy as np
    except ImportError:
        print("[-] Error importing numpy module.")
        exit(1)
    list_search_images = os.listdir(
        os.path.join(os.getcwd(), target_images_dir_name))
    colors.success("Search image list grabbed ")
    print(
        "\n{}\
        ----------------------------------------------------------------------\
        {}".format(
            colors.red, colors.green
        )
    )
    print("\n\t {}:: Similar images found are :: \n".format(colors.lightgreen))
    for path in list_search_images:
        src_image = cv2.imread(os.path.join(target_images_dir_name, path), 0)
        if custom_hashing(source) == custom_hashing(src_image):
            print("Image : {}".format(path))


def custom_hashing(image, hash_size=8):
    image = cv2.resize(image, (hash_size + 1, hash_size), cv2.INTER_AREA)
    pixel = []
    [rows, cols] = image.shape
    for i in range(0, rows):
        for j in range(0, cols):
            pixel.append(image.item(i, j))
    pixels = list(pixel)

    difference = []
    for row in range(hash_size - 1):
        for col in range(hash_size - 1):
            pixel_left = image.item(row, col)
            pixel_right = image.item(row, col + 1)
            difference.append(pixel_left > pixel_right)
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2 ** (index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, "0"))
            decimal_value = 0
    return "".join(hex_string)


def main():
    global target_images_dir_name

    source_path = None

    logo.banner()
    print("\n")

    try:
        import argparse
        import sys
    except ImportError:
        print("[-] Error importing argparse or sys module")
        exit(1)

    parser = argparse.ArgumentParser(
        description='A program which given a source image'
        'and a set of target images '
        "will match the source image to the target images to find its matches"
    )
    parser.add_argument("-p", "--path", help=" Path of source image")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0.0(beta)",
        help="Prints the version " "of Photoroid",
    )
    parser.add_argument(
        "-t",
        "--target",
        help=" Path of target images directory",
        default=target_images_dir_name_default,
    )

    if len(sys.argv) > 1:
        args = parser.parse_args()
        source_path = args.path
        target_images_dir_name = args.target
    if target_images_dir_name is "":
        target_images_dir_name = target_images_dir_name_default
    if source_path is None:
        source_path = str(
            input(
                "[ {}!{} ] Enter path of source image: {}".format(
                    colors.white, colors.end, colors.lightgreen
                )
            )
        )

    print("\n")  # Some serious end of line, for UI purpose LOL ...

    # Getting the image to be searched
    source = cv2.imread(source_path, 0)
    start_dir = os.getcwd()  # Saving the start directory

    # Creating template sections of source image.
    initial_time = time.time()
    os.chdir(start_dir)
    colors.process("Setting 'Core' as current directory.")
    check_match(source)
    colors.info("Total time: " + str(time.time() - initial_time))
    print("{}\nThank you for using my tool\n".format(colors.blue))


if __name__ == "__main__":
    main()
