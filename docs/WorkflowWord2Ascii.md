# This is a Workflow description of transition Word files to ascii format

## 0. Install pandoc
See https://pandoc.org/installing.html

## 1. Convert Word to asciidoc with pandoc
The command converts a Microsoft Word document to an AsciiDoc file format with extraction of media files from the input document to a directory `extracted-media`.

`pandoc DetailsOfTheAssetAdministrationShell_Part1a_V3.0_final_altesLayout_lastFindings.docx -f docx -t asciidoctor --wrap=none --markdown-headings=atx --extract-media=extracted-media -o AASiD_1_Metamodel_V3_0.adoc`

## 2. Install all dependencies by running,

`pip install -r requirements.txt`

## 3. Fix bugs
1. Run the main_script.py in scripts directory. The main script does has following steps:
   1. Removes table of index from asciidoc file, we just provide start and endline to the function remove_lines_between().
   2. Convert all the images from emf to png and also their occurrence in the the asciidoc.
   3. Remove certain commonly occurring expressions(defined as regular expression in code) in asciidoc, for instance links, references from docx to asciidoc conversion.
   4. Escaping angular brackets, as it is read as a keyword in asciidoc.
   5. Recolor notes, examples in asciidoc so they are highlighted from rest of the text.
   6. Create anchor for bibliography and link the references to them in the document.
   7. Fixing the image captions, by moving text before image tags, and also converting associated text to captions as per asciidoc formatting.
   8. Replacing class names enclosed in double qoutes with `.

## 3. Create HTML from asciidoc with Table-of-Contents
`asciidoctor -a toc=left -a stylesheet=style.css AASiD_1_Metamodel_V3_0.adoc`

