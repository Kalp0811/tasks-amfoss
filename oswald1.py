from PIL import Image 
image= Image.open("oswald.png") 
image= image.convert('1') 
image.save("oswald.png")

image= Image.open("oswald.png") 
image.rotate(0).save("oswald.png")

image.transpose(Image.FLIP_LEFT_RIGHT).save("oswald.png")
image.show()

