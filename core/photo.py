# Importing modules
import os
import cv2
import colors
import logo

template_image_dir_name = ''
target_images_dir_name = ''
template_image_dir_name_default = 'Template_images'
target_images_dir_name_default = 'images'


def template_images(temp_image):
    template_image_dir_path = os.path.join(os.getcwd(), template_image_dir_name)
    try:
        if os.path.isdir(template_image_dir_name):
            colors.info('Template image sections folder already exists.')
        else:
            os.mkdir(template_image_dir_path)
            colors.success('Template image sections folder created.')
    except OSError:
        colors.error('Permission denied at {}: Cannot create template image sections folder'
                     .format(template_image_dir_path))
        exit(1)

    os.chdir(os.path.join(os.getcwd(), template_image_dir_name))
    colors.success('Directory set to new location ')

    # Loading Template image.
    colors.success('Image read into memory')

    x = y = 0
    width = [160, 320, 480, 640]  # Respective width dimension for the template image.
    height = [160, 320, 480]  # Respective height dimension for the template image.
    count = 0

    for h in height:
        for w in width:
            image_section = temp_image[y:h, x:w]  # Creating section of image.
            x = w
            cv2.imwrite(str(count) + ".jpg",
                        image_section)  # writing each template image section to template directory.
            count += 1
        x = 0
        y = h


# Function to match template image.
def check_match():
    try:
        import numpy as np
    except ImportError:
        print("[-] Error importing numpy module.")
        exit(1)

    list_temp_images = os.listdir(os.path.join(os.getcwd(), template_image_dir_name))
    colors.success("Template image list grabbed.")
    list_search_images = os.listdir(os.path.join(os.getcwd(), target_images_dir_name))
    colors.success("Search image list grabbed ")
    print(
        "\n{}----------------------------------------------------------------------{}".format(colors.red, colors.green))
    print("\n\t {}:: Similar images found are :: \n".format(colors.lightgreen))

    for path in list_search_images:
        checked = []
        pos = 0

        # Reading images to be matched one by one.
        src_image = cv2.imread(os.path.join(target_images_dir_name, path), cv2.IMREAD_COLOR)

        # Converting image to grayscale.
        src_gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

        # Checking if all the templates are there in image or not.
        while pos < 12:
            template_path = list_temp_images[pos]
            template_image = cv2.imread(os.path.join(template_image_dir_name, template_path), cv2.IMREAD_GRAYSCALE)

            # Using cv2.matchTemplate() to check if template is found or not.
            result = cv2.matchTemplate(src_gray, template_image, cv2.TM_CCOEFF_NORMED)
            thresh = 0.9
            loc = np.where(result > thresh)
            if str(loc[0]) == str(loc[1]):
                checked.append("False")
                break
            else:
                checked.append("True")
            pos += 1

        if "False" not in checked:
            print("Image : {}".format(path))


def main():
    global template_image_dir_name
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

    parser = argparse.ArgumentParser(description='A program which given a source image and a set of target images '
                                                 'will match the source image to the target images to find its matches')
    parser.add_argument('-p', '--path', help=' Path of source image')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0(beta)', help='Prints the version '
                                                                                                  'of Photoroid')
    parser.add_argument('-t', '--target', help=' Path of target images directory',
                        default=target_images_dir_name_default)
    parser.add_argument('-o', '--output', help='Path of template images directory',
                        default=template_image_dir_name_default)

    if len(sys.argv) > 1:
        args = parser.parse_args()
        source_path = args.path
        template_image_dir_name = args.output
        target_images_dir_name = args.target

    if source_path is None:
        source_path = str(
            input("[ {}!{} ] Enter path of source image: {}".format(colors.white, colors.end, colors.lightgreen)))

    print("\n")  # Some serious end of line, for UI purpose LOL ...

    # Getting the image to be searched
    source = cv2.imread(source_path, cv2.IMREAD_COLOR)
    colors.process("Creating template sections of source image.")

    start_dir = os.getcwd()  # Saving the start directory

    # Creating template sections of source image.
    template_images(source)
    colors.success("12 template sections of source image created.")
    os.chdir(start_dir)
    colors.process("Setting 'Core' as current directory.")
    check_match()
    print("{}\nThank you for using my tool\n".format(colors.blue))


if __name__ == '__main__':
    main()
