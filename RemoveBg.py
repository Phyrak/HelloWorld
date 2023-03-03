from rembg import remove
from PIL import Image
Input_photo = "butterfly.jpg"
Output_photo= "butterfly No bg.png"
input = Image.open(Input_photo)
output=remove(input)
output.save(Output_photo