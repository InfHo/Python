import exif
from exif import Image

#https://pypi.org/project/exif/

# open image as my_image
with open('1.jpg', 'rb') as image_file:
    my_image = Image(image_file)

# show all image attributes
print(my_image.list_all())

### show model attribute from my_image
##print(my_image.model)

# set image attributes
my_image.focal_length = 99
my_image.model = "iPhone 13"

# print for testing
print(">>", my_image.focal_length)

# save modified image as modified_image.jpg
with open('modified_image.jpg', 'wb') as new_image_file:
    new_image_file.write(my_image.get_file())
