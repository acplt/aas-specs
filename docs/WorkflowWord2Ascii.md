# This is a Workflow description of transition Word files to ascii format

## 0. Install pandoc
See https://pandoc.org/installing.html

## 1. Convert Word to asciidoc with pandoc
The command converts a Microsoft Word document to an AsciiDoc file format with extraction of media files from the input document to a directory `extracted-media`.

`pandoc DetailsOfTheAssetAdministrationShell_Part1a_V3.0_final_altesLayout_lastFindings.docx -f docx -t asciidoctor --wrap=none --markdown-headings=atx --extract-media=extracted-media -o AASiD_1_Metamodel_V3_0.adoc`

## 2. Convert all emf-images in extracted-media to png

`pip install pillow`

Once you have Pillow installed, you can use the following Python code to convert an EMF file to PNG: 

`scripts/convert_emf_images.py`

## 3. Fix bugs

1. Remove such texts from table titles: "[#_Toc125537806 .anchor]####Table 31"
   2. Use the regex to delete it: `\[#_Toc\d* \.anchor]####Table \d* `
   3. Use the regex to delete it: `\[#_Ref\d* \.anchor]####Table \d* `
2. Remove such texts from image definitions:
   2. Use the regex to delete it: `\[\#_Ref\d* \.anchor\]\#\#`
   3. Use the regex to delete it: `\[\#_Toc\d* \.anchor\]\#\#`
3. Place image names ahead of the image:
   4. Search for: `\]Figure \d*`
   5. Choose all
   6. Press <-
   6. Press ->
   7. Press shift+ende
   8. ctrl+c
   9. Press Pos 1
   10. Press enter
   11. Press up
   12. ctrl+v
   13. Search for: `\]Figure \d*`
   5. Choose all
   6. Press <-
   6. Press ->
   7. Press shift+ende
   8. delete
   4. The same for: `\] Figure \d*`
4. TODO describe: Fix all references
5. TODO describe: Handle notes in blue boxes appropriately
5. TODO describe: Replace "" with `` where needed
6. TODO describe: Handle footnotes appropriately
   7. Replace footnotes with direct URLs where needed 

## 3. Create HTML from asciidoc with Table-of-Contents
`asciidoctor -a toc=left -a stylesheet=style.css output.adoc`

