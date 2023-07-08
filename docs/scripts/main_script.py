from convert_emf_images import read_emf_images
from remove_lines_between import remove_lines_between
from convert_emf_images import replace_emf_with_png
from remove_pattern_from_adoc import remove_text_matching_regex
from fix_angular_brackets import escape_double_angular_brackets
from recolor_notes import recolor_notes
from fix_the_biblio import add_anchor_to_biblio, add_link_to_biblio
from fix_image_captions_in_adoc import move_caption_to_beginning
from fixquotesonkeywords import replace_quotes_on_keyword
from fix_square_bracket import escape_square_brackets
import util.helper_func as utils

files = [("../AASiD_1_Metamodel","/AASiD_1_Metamodel_V3_0.adoc")]

for i in range(len(files)):
    filepath = files[i][0]+files[i][1]
    content = utils.read_file(filepath)

    # 1 Replace the Table of Contents in adoc file
    content = remove_lines_between(content, start_line=45, end_line=554)

    # 2 Convert the images in Asciidoc document

    # 2.1 Convert the emf files to png
    IMAGES_TO_CONVERT = read_emf_images(files[i][0] + "/extracted-media/media")
    # for image in IMAGES_TO_CONVERT:
    #     convert_emf_to_png(image, image.replace(".emf", ".png"))

    # 2.2 Replace all occurrences of emf to png in asciidoc file
    content = replace_emf_with_png(content)

    # 3 Remove certain commonly occurring patterns in asciidoc file - check the script for list of patterns
    content = remove_text_matching_regex(content)

    # 4 Escaping the angular brackets
    content = escape_double_angular_brackets(content)

    # 5 Style note boxes
    content = recolor_notes(content)

    # 6 Fix the bibliography

    # 6.1 Add anchors to bibliography
    keys, content = add_anchor_to_biblio(content)
    # 6.2 Connect the in-document references to bibliography
    content = add_link_to_biblio(content, keys)

    # 7 Fix the image captions
    content = move_caption_to_beginning(content)

    # 8 Fix the Quotes on keyword
    content = replace_quotes_on_keyword(content)

    # 9 Escape Square Brackets
    content = escape_square_brackets(content)

    # Writing all the edited content back to the file
    utils.write_file(filepath, content)