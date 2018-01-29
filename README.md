 # Styled in Color

**Vision:**

Styled in Color helps those who struggle with color coordinating there outfits, as well as those whose eyes struggle to see colors in their true tones.

The app works to establish the top three colors in a person's outfit and then utilizes simple color theory principles to inform the user whether or not their outfit follows color coordination rules.

As with all fashion, it is completely acceptable for anyone to make up their own fashion rules. Wear what colors make you happy.

**Methodology:**

  This model was trained utilizing **A Vast Number of images**
  A small handful of the images were independently visually inspected to determine the ideal pixel location. This step was taken to ensure that the model was built off colors found in the clothing and to take precautions to prevent background colors from being considered.

**Working in Colorspaces:**

  In order to capture the top three colors in the images, the RGB values were transcribed in to HSV values. The HSV color wheel naturally divides itself into 24 different colors. These 24 colors were grouped into sets of two and hand labeled. All the colors that were captured from the model were then binned into the 12 labeled colors.

**The HSV Colorspace:**

  Hue : "True Color"
  Saturation: "How white" pure red, value = 1, tints of red < 1,
              0 = white
  Value: "How black" 0 = black,

**Color Coordination:**
  Simple color theory states that colors that are equally spaced out around the color wheel are said to be complimentary. In other words, they look well placed together.

  Additional color rules:
    This model does take into a few additional fashion rules:
      -Red & Green should not be worn together unless it's Christmas

**Methodology:**

  1. Find contours
  2. Establish Bounding Box
  3. Extract pixel color values from both inside and outside bounding box
  4. Convert color values from rgb space to hsv space
  5. Calculate most frequently appearing hsv values, excluding top three background colors
  6. Run top three colors through algorithm to calculate if they are coordinated or not.

![Starting Image](https://github.com/NRahm/styled_in_color/blob/master/data/read_me_photos/sample_image_original.jpg)

![Bounding Box Location](https://github.com/NRahm/styled_in_color/blob/master/data/read_me_photos/bounding_box.jpg)

![HSV Colorwheel](https://github.com/NRahm/styled_in_color/blob/master/data/read_me_photos/color_wheel.jpg)

**Results**

![Man in Purple](https://github.com/NRahm/styled_in_color/blob/master/data/read_me_photos/man_in_purple.jpg)


('Magenta', 261), ('Magenta', 261), ('Magenta', 261)

![Lady in Red](https://github.com/NRahm/styled_in_color/blob/master/data/read_me_photos/red_bounding_box.jpg)

('Red', 8), ('Orange or Brown', 31), ('Red', 8)

**Libraries Used:**

  1. Opencv2 was utilized for image manipulation.
  2. Python Imaging Library (PIL) was used to access RGB values for pixels of interest.
  3. Numpy was utilized for vector and matrix manipulation.

**Future:**

I will continue improving Styled in Color by continuing to advance the color algorithms so that they become better at distinguishing the subtleties in different tones and colors.

Eventually I will make my project into a working website where people may upload a photo of their current outfit for immediate feedback. I would someday like to make this project into a working phone app.

Someday, I would like to devise a neural network that will be able to ensure even more background colors are excluded from the color analysis: ideally, making it possible to run the algorithm on outfits regardless of what is in the background.
