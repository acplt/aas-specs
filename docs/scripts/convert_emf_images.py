from PIL import Image
import os


def convert_emf_to_png(emf_file, png_file):
    # Open the EMF file
    im = Image.open(emf_file)

    # Save it as PNG
    print(emf_file)
    im.save(png_file, 'PNG')


def read_emf_images(folder_path):
    file_list = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.emf'):
            file_list.append(os.path.join(folder_path, file_name))
    return file_list


def replace_emf_with_png(content):
    return content.replace('.emf', '.png')
