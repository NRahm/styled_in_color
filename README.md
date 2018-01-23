# Styled in Color


Styled in Color helps those who struggle with color coordinating there outfits, as well as those whose eyes struggle to see colors in their true tones.

The app works to establish the top three colors in a person's outfit and then utilizes simple color theory principles to inform the user whether or not their outfit follows color coordination rules.

As with all fashion, it is completely acceptable for anyone to make up their own fashion rules. Wear what colors make you happy.

**Data & Model Training:**

  This model was trained utilizing **A Vast Number of images**
  A small handful of the images were independently visually inspected to determine the ideal pixel location. This step was taken to ensure that the model was built off colors found in the clothing and to take precautions to prevent background colors from being considered.

**Colors:**

  In order to capture the top three colors in the images, the RGB values were transcribed in to HSV values. The HSV color wheel naturally divides itself into 24 different colors. These 24 colors were grouped into sets of two and hand labeled. All the colors that were captured from the model were then binned into the 12 labeled colors.

**HSV Explanation:**

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

HELP ME!!!!
May need to change to top two colors.

**Libraries Used:**

  Opencv2 was utilized for image manipulation.
  Numpy was utilized for vector and matrix manipulation.

#MORE TIME#

If I had more time, I would find a way to recognize faces and subtract those color values from the "outfit" values. For the first iteration of the model, I believed it was fair that a person's face, arms and legs were only a fraction of the outfit being analyzed.   
