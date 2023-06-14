from convert_emf_images import read_emf_images
from remove_lines_between import remove_lines_between
from convert_emf_images import replace_emf_with_png
from remove_pattern_from_adoc import remove_text_matching_regex
from fix_angular_brackets import escape_double_angular_brackets
from recolor_notes import recolor_notes
from fix_the_biblio import add_anchor_to_biblio, add_link_to_biblio
from fix_image_captions_in_adoc import move_caption_to_beginning

file_name = "/AASiD_1_Metamodel_V3_0.adoc"
directory = "../AASiD_1_Metamodel"

# 1 Replace the Table of Contents in adoc file
remove_lines_between(directory+file_name, start_line=45, end_line=554)

# 2 Convert the images in Asciidoc document

# 2.1 Convert the emf files to png
IMAGES_TO_CONVERT = read_emf_images(directory + "/extracted-media/media")
# for image in IMAGES_TO_CONVERT:
#     convert_emf_to_png(image, image.replace(".emf", ".png"))

# 2.2 Replace all occurrences of emf to png in asciidoc file
replace_emf_with_png(directory+file_name)

# 3 Remove certain commonly occurring patterns in asciidoc file - check the script for list of patterns
remove_text_matching_regex(directory+file_name)

# 4 Escaping the angular brackets
escape_double_angular_brackets(directory+file_name)

# 5 Style note boxes
recolor_notes(directory+file_name)

# 6 Fix the bibliography

# 6.1 Add anchors to bibliography
keys = add_anchor_to_biblio(directory + file_name)
# 6.2 Connect the in-document references to bibliography
add_link_to_biblio(directory + file_name, keys)

# 7 Fix the image captions
move_caption_to_beginning(directory + file_name)
