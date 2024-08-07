from custom_gui.gui_constants import *

# ------------------------------------------
# |       🎉   COMMON STYLING    🎉       |
# ------------------------------------------
COMMON_FONT_FAMILY = FontFamily.Consolas
COMMON_FONT_SIZE = 12
# ------------------------------------------

# # ------------------------------------------------------
#    In below code, update code as per your design. 
#    The color codes are available in gui_constants.py
#    Feel free to update as you wish.
#    Best of luck 🤪
# # ------------------------------------------------------

# [ 🚀 EXPLANATION ]
# width - width of the widget
# bg - background color
# fg - foreground color
# padx - padding-x - padding left and right side
# pady - padding-y - padding top and bottom
class WidgetConfig:
    class Common:
        padding = { "padx": 10, "pady": 10 }
    class Main:
        config = { 
            'bg': Color.Black
        }
    class Entry:
        config = {
            'width': 80,
            'bg': Color.SkyBlue,
            'fg': Color.Black,
            'font': ( 
                COMMON_FONT_FAMILY, 
                COMMON_FONT_SIZE 
            )
        }
    class Button:
        config = {
            'width': 30,
            'bg': Color.White,
            'fg': Color.Black,
            'font': (
                COMMON_FONT_FAMILY, 
                COMMON_FONT_SIZE, 
                FontStyle.bold + FontStyle.italic
            )
        }
    class ListBox:
        config = {
            'width': 40,
            'height': 10,
             'bg': Color.White,
            'fg': Color.Black,
            'font': (
                COMMON_FONT_FAMILY, 
                COMMON_FONT_SIZE, 
                FontStyle.italic
            )
        }
    class Label:
        config ={
            'width': 80,
            'bg': Color.Silver,
            'fg': Color.Blue,
            'font': (
                COMMON_FONT_FAMILY, 
                COMMON_FONT_SIZE, 
                FontStyle.bold
            )
        }