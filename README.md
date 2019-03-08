<h1 align="center">
  <br>
  <a href="https://github.com/0xprateek"><img src="https://i.imgur.com/UiskoMY.jpg" alt="Stardox"></a>
</h1>

<p align="center">  
  <a href="https://docs.python.org/3/download.html">
    <img src="https://img.shields.io/badge/Python-3.x-green.svg">
  </a>
  <a href="https://github.com/0xprateek/Photoroid">
    <img src="https://img.shields.io/badge/Version-v1.0.0%20(Beta)-blue.svg">
  </a>
  <a href="https://github.com/0xPrateek/Photoroid/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-GPLv3-orange.svg">
  </a> 
  <a href="https://github.com/0xprateek/Photoroid">
    <img src="https://img.shields.io/badge/OS-Linux-orange.svg">
  </a>
</p>

## About [Photoroid](https://github.com/0xprateek/Photoroid)
Photoroid is the fastest, Lightweight, easy to use image scanner tool. Photoroid is made using OpenCV with Python. It can be used to find a similar image from a list of images without taking much time. Photoroid can be very helpful in finding similar images when the number of images to scan is bigger. It can also be helpful in finding duplicate images.</p>

#### Key points

1. Template image path(here) requires an image path and this image will be scanned in the list of images.
2.  It's necessary that all the images from which you have to find similar images should be present at `/photoroid/core/images`.

#### Improvements

1. Currently, photoroid supports only images with 640 X 480 dimension. Further improvements will add support of scanning images of all the dimensions.</p>
2. Currently we are using ![`cv2.matchTemplate()`](opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html) function for finding similar images. Further improvements will replace it with a new algorithm for more faster detection of similar images.</p>
3. Currently, it scans into offline images only. Further updates will add support for scanning images from online databases as well.</p>


### Gallery

**Template image path.**
![Image 1](https://i.imgur.com/CHt2RhL.jpg)


 **List of images found.**
![Image 2](https://i.imgur.com/QoVH8d6.jpg)


### Getting Started

#### Steps to setup :

1. `git clone https://github.com/0xprateek/Photoroid`
2. `cd photoroid`
3. `pip install -r requirements.txt`

#### Starting Stardox :

1. `cd Photoroid/core`<br/>
2.  a)  **Using Command line arguments** <br/>
         `python3 photo.py /home/proton/Desktop/image1.jpg`<br/>
    b)  **Without Command line arguments**<br/>
     `    python3 photo.py`<br/>

### Contributing
Any and all contributions, issues, features and tips are welcome.

### License
**Photoroid** is licence under [GPL v3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html)
