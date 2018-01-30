 # Styled in Color

**Vision:**

I desired a project that melded my two passions together: **fashion and data**.

My vision was to take data science and apply it to outfit photos, by extracting out appearences of color in clothing according to number of pixels present in each color group. 

The goal of this project is to **help those who struggle to put together outfits that are pleasing to the eye**, regardless of how well they are able to perceive color.

As with all fashion, it is completely acceptable for anyone to make up their own fashion rules. Wear what colors make you happy.

**Key Findings**

Working in the HSV color space leant itself well to binning simmilar colors together; however, its classification of balck, white, and red is unreliable. 

Early on in the process of creating a model to achieve my project's goals, I realized working with color and especially going from one color space to another was going to be a large challenge. 

The RGB color space has millions of possibilities and although the HSV color space has drastically fewever posibilities, it is still very challenging to assing groups of pixels to a single hue. 

Average to subpar image quality worked well for my model. 

**Methodology:**

I began this project with thousands of neatly posed images with a light grey background. 

I then iterated over the following steps:

1. Create reliable **bounding boxes** with minimal background utilizing **OpenCv** 
2. **Extract** the Red, Green, Blue **(RGB)** value for each pixel within the bounding box
3. **Convert** the **colors** from RGB to Hue, Saturation, Value **(HSV)** numbers for better color classification
4. Determine **top two** most occurring **colors** by binning them according to my hand-written color categories
5. **Calculate** the **distance** between the top two occurring colors to determine if the color combination is pleasing to the eye 


**Working in Colorspaces:**

  In order to capture the top three colors in the images, the RGB values were transcribed in to HSV values. The HSV color wheel naturally divides itself into 24 different colors. These 24 colors were grouped into sets of two and hand labeled. All the colors that were captured from the model were then binned into the 12 labeled colors.

**Working in Color Spaces:**

Red, Green, Blue (RGB) is a color space in which colors are assigned three different values based on how much of each color is present. 

![RGB Color Space]()

The Hue, Saturation, Value (HSV) color space assigns three values to colors as well, except that in HSV the colors are based on how much white and black are present, as well as the degree on the color wheel at which point the human eye tends to identify the true color to be. 

![HSV Color Space]()
![HSV Color Degree]()

HSV is challenged by extremely dark or light shades and can be tricked by red. 

**Color Coordination:**
Considering this project is built more for those who struggle to put together their own visually pleasing outfits and not for people with strong confidence in their established style, I based my outfit analysis on the basic principles of color theory.

#Astatically Pleasing Color Combinations#

![Analogous Colors]()
Grouping of colors near or within the same family on the color wheel.

![Complementary Colors]()
Two colors directly across from each ofther on the color wheel.

#Unastatically Pleasing Color Combinations#

![Inharmonious Colors]()
Two colors that are approximately 90• apart on the color wheel.

Basic fashion rules, such as seasonality and only wearing green and red together on December 25th were ignored.

**Image Manipulation**

The images in my dataset did come with supplied bounding box coordinates, but I found these x,y coordinates did not always generate an area of interest that appropriately captured as much of the outfits as possible.

I utilized Canny edge detection in the OpenCV library to establish bounding boxes that more reliably included nearly all the outfit in the images. 

#Original Image#

![Image Without Bounding Box]()

#Bounding Box According to Dataset Labels#
![Provided Bounding Box]()

#Coded Bounding Box#

![Hand Coded Bounding Box]()

**Results:**



**Future:**

I will continue improving Styled in Color by continuing to advance the color algorithms so that they become better at distinguishing the subtleties in different tones and colors.

Eventually I will make my project into a working website where people may upload a photo of their current outfit for immediate feedback. I would someday like to make this project into a working phone app.

Someday, I would like to devise a neural network that will be able to ensure even more background colors are excluded from the color analysis: ideally, making it possible to run the algorithm on outfits regardless of what is in the background.

**Libraries Used:**

  1. Opencv2 was utilized for image manipulation.
  2. Python Imaging Library (PIL) was used to access RGB values for pixels of interest.
  3. Numpy was utilized for vector and matrix manipulation.