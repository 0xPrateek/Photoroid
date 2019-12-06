# Importing modules
import os
import cv2
import colors
import logo


def template_images(temp_image):

    try:
        os.mkdir('Template images')
        colors.success("Folder Created")
    except:
        colors.error("Folder already exsist.")

    os.chdir(os.path.join(str(os.getcwd()), 'Template images'))
    colors.success("Directory set to new location ")

    # Loading Template image.
    colors.success("Image read into memory")

    x = y = 0
    # Respective width dimenision for the template image.
    width = [160, 320, 480, 640]
    # Respective height dimenision for the template image.
    height = [160, 320, 480]
    count = 0

    for h in height:
        for w in width:
            # Creating section of image.
            image_section = temp_image[y:h, x:w]
            x = w
            # writing each template image section to template directory.
            cv2.imwrite(str(count) + ".jpg", image_section)
            count += 1
        x = 0
        y = h

# Function to match template image.


def check_match():
    try:
        import numpy as np
    except:
        print("[-] Error importing module.")

    list_temp_images = os.listdir(os.path.join(os.getcwd(), "Template images"))
    colors.success("Template image list grabbed.")
    list_search_images = os.listdir(os.path.join(os.getcwd(), "images"))
    colors.success("search image list grabbed ")
    print("\n{}----------------------------------------------------------------------{}".format(colors.red, colors.green))
    print("\n\t {}:: Similar images found are :: \n".format(colors.lightgreen))

    for path in list_search_images:
        checked = []
        pos = 0

        # Reading images to be matched one by one.
        src_image = cv2.imread(os.path.join("images", path), 1)

        # Converting image to grayscale.
        src_gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

        # Checking if all the templates are there in image or not.
        while(pos < 12):
            template_path = list_temp_images[pos]
            template_image = cv2.imread(os.path.join(
                "Template images", template_path), 0)

            # Using cv2.matchTemplate() to check if template is found or not.
            result = cv2.matchTemplate(
                src_gray, template_image, cv2.TM_CCOEFF_NORMED)
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


if __name__ == '__main__':

    logo.banner()
    print("\n")

    try:
        import argparse
        import sys
    except:
        print("[-] Error importing module")

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help=' Path of template image')
    if len(sys.argv) > 1:
        args = parser.parse_args()
        template_path = args.path
    else:
        template_path = str(input("[ {}!{} ] Enter Template path : {}".format(
            colors.white, colors.end, colors.lightgreen)))

    print("\n")     # Some serious end of line, for UI purpose LOL ...

    # Getting the image to be serached
    template = cv2.imread(template_path, 1)
    colors.process("Creating section of template image.")

    # Creating secotion of template image.
    template_images(template)
    colors.success("12 Section of template image created.")
    os.chdir(os.path.join("..", ""))
    colors.process("Setting 'Core' as current directory.")
    check_match()
    print("{}\nThankyou for using my tool\n".format(colors.blue))
