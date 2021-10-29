from PIL import Image,ImageFilter

im = Image.open("ziemia.jpg")

#im.show()

# im1 = im.filter(ImageFilter.BLUR)
# im1.save("obrazy/ziemia1.jpg")

im1 = im.filter(ImageFilter.CONTOUR)
im1.save("obrazy/ziemia2.jpg")

