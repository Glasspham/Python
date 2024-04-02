import os
import shutil
def copy_images(source_folder, dest_folder, num_images):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for i in range(1, num_images + 1):
        source_image_path = os.path.join(source_folder, f"{i}.jpg")
        dest_image_path = os.path.join(dest_folder, f"{i + num_images}.jpg")
        shutil.copyfile(source_image_path, dest_image_path)
source_folder = "Anh"
dest_folder = "Anh1"
num_images = 10
copy_images(source_folder, dest_folder, num_images)