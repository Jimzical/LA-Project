import PySimpleGUI as sg
import cv2
'''
Requirements
    - PySimpleGUI
    - OpenCV (specifically pip install opencv-contrib-python, if error persists uninstall both opencv-contrib-python  and opencv-python(if installed) and "pip install --no-cache-dir opencv-contrib-python")

'''
def ChangeBrightness(img,value = 30):
    '''
   # To change the brightness of an image

    - @img = the image that you want to change the brightness of
    optional:
    - @value = the value of the brightness (default = 30) (Range[0-255])

     Return the image with the brightness changed
    '''
    value = int(value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


    return img

def ChangeSaturation(img,value = 30):
    '''
    # To change the Saturation of an image
    ### not sure how this works

    - @img = the image that you want to change the Saturation of
    optional:
    - @value = the value of the Saturation (default = 30) (Range[0-255])

     Return the image with the Saturation changed
    '''
    value = int(value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s[s > 255 - value] = 255
    s[s <= 255 - value] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


    return img

def ImageBlur(img,sigma = 1.3):
    '''
    # To blur an image

    - @img = the image that you want to blur
    - @sigma = the value of the blur (default = 1.3) (Range[0-5])


     Return the image blured
    '''
    img = cv2.GaussianBlur(img, (0, 0), sigma)
    img = cv2.addWeighted(img, 1.5, img, -0.5, 0)
    return img


def OilPainting(img, size = 5, levels = 10):
    '''
    # To apply oil painting effect to an image

    - @img = the image that you want to apply the effect on
    optional:
    - @size = the size of the effect (default = 5)
    - @levels = the levels of the effect (default = 10)

     Return the image with the effect applied
    '''
    
    size = int(size)
    levels = int(levels)
    
    img = cv2.xphoto.oilPainting(img, size, levels)
 
    return img

def Water(img, NeighbourhoodSize = 60, Range = 4):
    '''
    # To apply WaterColor effect to an image

    - @img = the image that you want to apply the effect on
    optional:
    - @NeighbourhoodSize = the NeighbourhoodSize of the effect (default = 60) (Range[1-255])
    - @Range = the Range of the effect (default = 0.4) (Range[0-1])

     Return the image with the effect applied
    '''

    NeighbourhoodSize = int(NeighbourhoodSize)
    Range = float(Range)
    # fixing range value
    Range = Range/10

    img = cv2.stylization(img, NeighbourhoodSize, Range)

    return img

def GrayScale(img):
    '''
    # To make an image gray scale

    - @img = the image that you want to make gray scale

     Return the image gray scaled
    '''
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img


def ImageHue(frame,val):
    '''
    # To change the hue of an image

    - @frame = the image that you want to change the hue of
    - @val = the value of the hue (Range[0-255])

    Return the image with the hue changed
    '''
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame[:, :, 0] += int(val)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    return frame
def EnhanceImage(frame, value = 40):
    '''
    # To enhance an image
    
    - @frame = the image that you want to enhance

    optional:
    - @value = the value of the enhancement (default = 40) (Range[0-255])
    
    Return the image enhanced
    '''
    enh_val = value / 40
    clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])
    frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return frame

def ScreenMask(frame,R_LOWER = 0,G_LOWER = 0,B_LOWER = 0,R_UPPER = 255,G_UPPER = 255,B_UPPER = 255):
    '''
    # To make a mask for the screen

    - @frame = the image that you want to make the mask on

    optional:
    - @R_LOWER = the lower value of the red channel (default = 0) (Range[0-255])
    - @G_LOWER = the lower value of the green channel (default = 0) (Range[0-255])
    - @B_LOWER = the lower value of the blue channel (default = 0) (Range[0-255])
    - @R_UPPER = the upper value of the red channel (default = 255) (Range[0-255])
    - @G_UPPER = the upper value of the green channel (default = 255) (Range[0-255])
    - @B_UPPER = the upper value of the blue channel (default = 255) (Range[0-255])

    Return the masked image
    '''
    lower = (R_LOWER, G_LOWER, B_LOWER)
    upper = (R_UPPER, G_UPPER, B_UPPER)
    mask = cv2.inRange(frame, lower, upper)
    frame = cv2.bitwise_and(frame, frame, mask=mask)

    return frame

def BuildGUI():
    '''
    # To build the GUI
    
    Return the GUI
    '''


    sg.theme("DarkBrown2")
    column = [
        sg.Column([
            [
            sg.Radio("Oil Painting", "Radio", size=(10, 1), key="-OIL-",font=("Cascadia Code SemiBold", 12)),
            sg.Slider(
                (1, 50),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-OIL SLIDER SIZE-",
            ),
            sg.Slider(
                (1, 100),
                tick_interval=0.1,
                orientation="h",
                size=(20, 15),
                key="-OIL SLIDER LEVEL-",
            )
            ],
            [
                sg.Radio("Water Color", "Radio", size=(10, 1), key="-WATER-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (1, 400),
                    orientation="h",
                    size=(20, 15),
                    key="-WATER SLIDER SIZE-",
                ),
                sg.Slider(
                    (1, 100),
                    orientation="h",
                    size=(20, 15),
                    key="-WATER SLIDER LEVEL-",
                )
            ],
            [
                sg.Radio("Brightness", "Radio", size=(10, 1), key="-BRIGHTNESS-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (0, 100),
                    orientation="h",
                    size=(40, 15),
                    key="-BRIGHTNESS SLIDER-",
                ),
            ],
            [
                sg.Radio("Saturation", "Radio", size=(10, 1), key="-SATURATION-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (0, 100),
                    orientation="h",
                    size=(20, 15),
                    key="-SATURATION SLIDER-",
                )
            ],
            [
                sg.Radio("Blur", "Radio", size=(10, 1), key="-BLUR-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (1, 100),
                    orientation="h",
                    size=(40, 15),
                    key="-BLUR SLIDER-",
                ),
            ],
            [
                sg.Radio("Hue", "Radio", size=(10, 1), key="-HUE-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (0, 225),
                    orientation="h",
                    size=(40, 15),
                    key="-HUE SLIDER-",
                ),
            ],
            [
                sg.Radio("Enhance", "Radio", size=(10, 1), key="-ENHANCE-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (1, 255),
                    orientation="h",
                    size=(40, 15),
                    key="-ENHANCE SLIDER-"
                ),
            ],
            [
                sg.Radio("GrayScale", "Radio", size=(10, 1), key="-GRAYSCALE-", font=("Cascadia Code SemiBold", 12)),
            ],
            [
            sg.Radio("Mask", "Radio", size=(10, 1), key="-MASK-",font=("Cascadia Code SemiBold", 12)),
            ],
            [sg.Text("Lower Threshold",font=("Cascadia Code SemiBold", 12))],
            [
                sg.Text("R                   ", font=("Cascadia Code SemiBold", 12)),
                sg.Text("G                   ",font=("Cascadia Code SemiBold", 12)),
                sg.Text("B",font=("Cascadia Code SemiBold", 12)),
            ],
            [sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-RLOWER-",
            ),
            sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-GLOWER-",
            ),
            sg.Slider(
                (0, 255),
                tick_interval=0.1,
                orientation="h",
                size=(20, 15),
                key="-BLOWER-",
            )
            ],
            [sg.Text("Upper Threshold",font=("Cascadia Code SemiBold", 12))],
            [
                sg.Text("R                   ", font=("Cascadia Code SemiBold", 12)),
                sg.Text("G                   ",font=("Cascadia Code SemiBold", 12)),
                sg.Text("B",font=("Cascadia Code SemiBold", 12)),
            ],
            [sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-RUPPER-",
                default_value=255
            ),
            sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-GUPPER-",
                default_value=255
            ),
            sg.Slider(
                (0, 255),
                tick_interval=0.1,
                orientation="h",
                size=(20, 15),
                key="-BUPPER-",
                default_value=255
            )
            ],
            [sg.Button("Exit", size=(10, 1), font=("Cascadia Code SemiBold" , 12))],
            
    ],scrollable=True,vertical_scroll_only=True)
]

    # Define the window layout
    layout = [
        [
        sg.Column(
            [
                [sg.Text("Image Editing", font=("Cascadia Code SemiBold", 25))],
                [sg.Image(filename="", key="-IMAGE-", size=(800, 800))]],element_justification='center')
            ]
            ,
            column
        ]

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(400, 0),grab_anywhere=True,resizable=True,size=(600, 1000) )

    return window

def main():
    window = BuildGUI()

    cap = cv2.VideoCapture(0)
    while True:
        event, values = window.read(timeout=20)

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        _, frame = cap.read()

        if values["-BRIGHTNESS-"]:
            frame = ChangeBrightness(frame, values["-BRIGHTNESS SLIDER-"])
        elif values["-SATURATION-"]:
            frame = ChangeSaturation(frame, values["-SATURATION SLIDER-"])
        elif values["-BLUR-"]:
            frame = ImageBlur(frame, values["-BLUR SLIDER-"])
        elif values["-HUE-"]:
            frame = ImageHue(frame, values["-HUE SLIDER-"])
        elif values["-ENHANCE-"]:
            frame = EnhanceImage(frame, values["-ENHANCE SLIDER-"])
        elif values["-OIL-"]:
            frame = OilPainting(
                frame,
                values["-OIL SLIDER SIZE-"],
                values["-OIL SLIDER LEVEL-"],
            )
        elif values["-WATER-"]:
            frame = Water(
                frame,
                NeighbourhoodSize = values["-WATER SLIDER SIZE-"],
                Range = values["-WATER SLIDER LEVEL-"]
            )
        elif values["-GRAYSCALE-"]:
            frame = GrayScale(frame)
        elif values["-MASK-"]:
            frame = ScreenMask(frame,values["-RLOWER-"],values["-GLOWER-"],values["-BLOWER-"],values["-RUPPER-"],values["-GUPPER-"],values["-BUPPER-"])
        
        
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

        
    window.close()

if __name__ == "__main__":
    main()


