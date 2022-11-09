import PIL.Image

# resizes the incoming image to a uniform size.
def Resize(image, newWidth = 100):
    
    width, height = image.size

    newHeight = int(newWidth * height/width)

    print((newWidth, newHeight))

    return image.resize((newWidth, newHeight))

# Converts the input image to the grayscale colormode.
def ImageToGrayscale(image):

    return image.convert("L")

# Maps the pixel valiues to an ascii value in the chacacter list.
def PixelsToAscii(image):

    #List of usable ascii characters
    asciichars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]    
    
    pixels = image.getdata()

    asciiStr = ""

    for pixel in pixels:
        asciiStr += asciichars[pixel//25]
    
    return asciiStr

# Splits the generated string to match the input image width.
def AsciiWordWrap(grayscaleImage, asciiString):
    
    imageWith = grayscaleImage.width
    
    asciiStringLength = len(asciiString)

    asciiImage = ""
    
    # Split the string
    for i in range(0, asciiStringLength, imageWith):
        asciiImage += asciiString[i:i+imageWith] + "\n"

    return asciiImage

# Saves the resulting string to the directory runnning the script.
def SaveStringToFile(asciiImage):
    
    with open("asciiImage.txt", "w") as f:
        
        try:
        
            f.write(asciiImage)

            f.close()

            print(f"Image saved successfully.")

        
        except Exception:

            f.close()

            print(f"Something went wrong when saving the file. {Exception}")

# Full flow taking an image and mapping it into ascii characters.
def Main():
    
    # C:\Users\Jeff\Documents\GitHub\AsciiArt\testimage.png
    path = input("Enter the path to the image file: ")

    try:

        image = PIL.Image.open(path)

    except Exception:

        print(Exception)

    # Resize the image
    image = Resize(image=image)

    # Convert the image to grayscale colormode
    grayscaleImage = ImageToGrayscale(image=image)

    # Convert grayscale image to ascii map
    asciiString = PixelsToAscii(image=grayscaleImage)

    # Split the string
    asciiImage = AsciiWordWrap(asciiString=asciiString, grayscaleImage=grayscaleImage)

    # Save the file
    SaveStringToFile(asciiImage=asciiImage)

if __name__ == "__main__":
    Main()