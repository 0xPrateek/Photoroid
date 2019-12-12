
<h1 align="center">
  <br>
  <a href="https://github.com/0xprateek"><img src="https://i.imgur.com/UiskoMY.jpg" alt="Stardox"></a>
</h1>

<p align="center">  
  <a href="https://docs.python.org/3/download.html">
    <img src="https://img.shields.io/static/v1?label=Python&message=3.x&color=green&style=flat-square">
  </a>
  <a href="https://github.com/0xprateek/Photoroid">
    <img src="https://img.shields.io/static/v1?label=Version&message=v1.0.0(beta)&color=blue&style=flat-square">
  </a>
  <a href="https://github.com/0xPrateek/Photoroid/blob/master/LICENSE">
    <img src="https://img.shields.io/static/v1?label=License&message=GPLv3&color=orange&style=flat-square">
  </a> 
  <a href="https://github.com/0xprateek/Photoroid">
    <img src="https://img.shields.io/static/v1?label=OS&message=Linux&color=yellow&style=flat-square">
  </a>
</p>

# [Photoroiod](https://github.com/0xprateek/Photoroid)
Photoroid is a photo-scanning, duplicate detection algorithm. It uses template matching algorithm in order to match a template against a large dataset of images of varying sizes.

## Algorithm

The current algorithm used is opencv's matchTemplate(). matchTemplate() has the following parameters: 
* The source image
* The template to check against
* A match metric 
<br>
<p>
<strong>templateMatch()</strong> is a built in OpenCV function, which performs matching by sliding the template against the source image. This is similar to 2D convolution operation. The template slides one pixel at a time, and returns a grayscale image where each pixel denotes how much does the neighbourhood of the pixel match with template.  
</p>
<br>
<p>
The implemented method involves bisecting the template image into 12 sub-templates of size 160x160 px.<br>
Each and every sub-template is checked against the source image, and if the result is greater than a threshold, and if that's the case for every sub-template, then the image is flagged as <strong>duplicate</strong>.
</p>

## How to run
* ```python3 photo.py```
* Command line parameters: 
    * ```-p``` : Path of source/template image
    * ```-v``` : Current version of program
    * ```-t``` : Path of target image directory
    * ```-o``` : Path of sub-template directory

## Performance
<p>
At present, the algorithm is in the initial stages.<br>
The algorithm was run against a dataset of 10 images and took approximately <b>0.54ms</b> to find duplicates (there were 2 duplicates).
</p>

## Requirements
Run  ```pip3 -r requirements.txt``` to get all the requirements.
* Python 3.X.X
* numpy
* OpenCV
