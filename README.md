# styled_in_color

This is about Styled in Color.

Styled in Color helps those who struggle with color coordinating there outfits, as well as those whose eyes struggle to see colors in their true tones.

The app works to establish the top three colors in a person's outfit and then utilizes simple color theory principles to inform the user whether or not their outfit follows color coordination rules.

As with all fashion, it is completely acceptable for anyone to make up their own fashion rules. Wear what colors make you happy.

Model Training:
  This model was trained utilizing **A Vast Number of images**
  A small handful of the images were independently visually inspected to determine the ideal pixel location. This step was taken to ensure that the model was built off colors found in the clothing and to take precautions to prevent background colors from being considered.

Colors:
  In order to capture the top three colors in the images, the RGB values were transcribed in to HSV values. The HSV color wheel naturally divides itself into 24 different colors. These 24 colors were grouped into sets of two and hand labeled. All the colors that were captured from the model were then binned into the 12 labeled colors.

Color Coordination:
  Simple color theory states that colors that are equally spaced out around the color wheel are said to be complimentary. In other words, they look well placed together.

  Additional color rules:
    This model does take into a few additional fashion rules:
      -Red & Green should not be worn together unless it's Christmas


Models Used:
  **Histogram of colors**


Libraries Used:
