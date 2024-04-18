from rembg import remove
from PIL import Image
input = "/content/WIN_20221023_02_14_45_Pro.jpg"
output = "/content/output.png"
i = Image.open(input)
o = remove(i)
o.save(output)
