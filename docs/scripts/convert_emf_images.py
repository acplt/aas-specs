from PIL import Image


# Define emf images to convert
IMAGES_TO_CONVERT = []


def convert_emf_to_png(emf_file, png_file):
    # Open the EMF file
    im = Image.open(emf_file)

    # Save it as PNG
    im.save(png_file, 'PNG')


# Usage example
for image in IMAGES_TO_CONVERT:
    convert_emf_to_png(image, image.replace(".emf", ".png"))