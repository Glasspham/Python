from rembg import remove
from PIL import Image
input_Path = 'Path'
output_Path = 'NameFile.png' # Make sure the image extension is .png
inp = Image.open(input_Path)
outputPath = remove(inp)
outputPath.save(output_Path)