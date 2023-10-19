# AsciiDoc Guide for Template Specifications

## Table of Contents

- [Writing a Template Specification in AsciiDoc](#writing-a-template-specification-in-asciidoc)
- [Installing an AsciiDoc Viewer/Editor](#installing-an-asciidoc-viewereditor)
- [Converting Word Documents to AsciiDoc](#converting-word-documents-to-asciidoc)
- [Generating HTML from AsciiDoc](#generating-html-from-asciidoc)

## Writing a Template Specification in AsciiDoc

### Step 1: Clone the Repository

Clone the repository using the following Git command:

```shell
git clone https://github.com/admin-shell-io/aas-specs
```

### Step 2: Create a Specification Folder

Duplicate the "docs/AAS_Submodel_Templates/Empty_Template" folder and rename it with your specification name, removing
any media files. Refer to "index_with_format_comments.adoc" for commonly used AsciiDoc formatting in specifications. For
a comprehensive understanding of AsciiDoc,
visit [AsciiDoctor Documentation](https://docs.asciidoctor.org/asciidoc/latest/).

If you have a specification written or available in Word, refer
to [Converting Word Documents to AsciiDoc](#converting-word-documents-to-asciidoc).

### Step 3: Generate HTML Documentation

See [Generating HTML from AsciiDoc](#generating-html-from-asciidoc) for details.

## Installing an AsciiDoc Viewer/Editor

AsciiDoc syntax is plain text, enabling you to write documents using any text editor without requiring complex word
processing programs. However, using a dedicated viewer/editor for AsciiDoc files is recommended for previewing rendered
files.

Explore various ways to preview and edit your AsciiDoc
documents [here](https://docs.asciidoctor.org/asciidoctor/latest/tooling/). Online tools
like [AsciiDocLive](https://asciidoclive.com/edit/scratch/1) are also available.

> **Recommendation:** GitHub.Dev can also be utilized for AsciiDoc viewing and editing.

## Converting Word Documents to AsciiDoc

### Prerequisites

Ensure you have an AsciiDoc Viewer/Editor installed.
See [Installing an AsciiDoc Viewer/Editor](#installing-an-asciidoc-viewereditor).

### Step 1: Convert Word-Specification to AsciiDoc using Pandoc

#### Variant A: Online Conversion

- Go to https://github.com/zrgt/aas_word2asciidoc/issues/new/choose and create a new issue in the Template "Transform Word Document to AsciiDoc". 
- Upload your Word file and wait for the conversion to be done.
- You will be notified when the conversion is done.
- Follow the link in the comment to download the converted AsciiDoc file.

#### Variant B: Local Conversion

##### 1. Install Pandoc

Visit [Pandoc Installation Guide](https://pandoc.org/installing.html).

##### 2. Execute Conversion in Terminal

Create a folder to store your Word file, the generated AsciiDoc file, and extracted images. Execute the following
command in the terminal, replacing file and folder names accordingly:

```shell
pandoc [Your_Word_File_Path].docx -f docx -t asciidoctor --wrap=none --markdown-headings=atx --extract-media=[Your_Folder_Path] -o [Your_Folder_Path]/[Generated_AsciiDoc_File].adoc
```

##### 3. Run Scripts to Resolve Conversion Issues

Utilize scripts from the 'aas_word2asciidoc' repository to fix issues in the generated AsciiDoc file.

###### Install Package

Install the package directly from GitHub using Pip:

```shell
pip install git+https://github.com/rwth-iat/aas_word2asciidoc.git@master
```

###### Execute Fixing Scripts

Run the following command to fix issues and generate a refined 'index.adoc' file:

```shell
fix_adoc --adoc_input [Path_to_Generated_AsciiDoc_File].adoc --adoc_output [Path_to_Folder]/index.adoc
```

Or, if the above doesn't work:

```shell
python -m word2asciidoc.fix_adoc --adoc_input [Path_to_Generated_AsciiDoc_File].adoc --adoc_output [Path_to_Folder]/index.adoc
```

The following fixes will be done by running scripts:

1. Removes table of index from asciidoc file, we just provide start and endline to the function remove_lines_between().
2. Convert all the images from emf to png and also their occurrence in the the asciidoc.
3. Remove certain commonly occurring expressions(defined as regular expression in code) in asciidoc, for instance links,
   references from docx to asciidoc conversion.
4. Escaping angular brackets, as it is read as a keyword in asciidoc.
5. Recolor notes, examples in asciidoc so they are highlighted from rest of the text.
6. Create anchor for bibliography and link the references to them in the document.
7. Fixing the image captions, by moving text before image tags, and also converting associated text to captions as per
   asciidoc formatting.
8. Replacing class names enclosed in double qoutes with `.

### Step 3: Manual Bug Fixes

Review the 'index.adoc' file and manually resolve any remaining issues. For detailed AsciiDoc information, refer to
the [AsciiDoc Documentation](https://docs.asciidoctor.org/asciidoc/latest/).

The following should be done manually:
1. Remove table of index from asciidoc file
2. Add the config and metainfo to the beginning of adoc file (Consider where you place the used css file. In this case a css file from upper folders will be used):
```
   :toc: left
   :toc-title: SOME TITLE 1
   :stylesheet: ../../style.css
   :favicon: ../../favicon.png
   :nofooter:
   
   = SOME TITLE 2
   :author: IDTA OR OTHER
   :version-label: Number
   :revnumber: 1234-5-6
   :revdate: Month YEAR
   :revremark: SOME TITLE 3
```
3. Fix Tables. If needed:
   - Add header to the first row: "options=header"
   - Add header to the first column with "h": "cols="16%h,50%,25%,9%" or cols="h,d,d,d""
   - You can also format a single cell with a header style e.g. "h|header cell |normal cell h|header cell"  
   - Remove empty rows
   - Search for tables with complex structure and split them. Format headers and write before the first table "[.table-with-appendix-table]"
4. Others:
   - Search for "image:media.*].*". These are places where text directly follows images. Add a blank line after image.


## Generating HTML from AsciiDoc

Install [Asciidoctor](https://docs.asciidoctor.org/asciidoctor/latest/install/windows/) and execute the following
command to generate an HTML file from your AsciiDoc document:

```shell
asciidoctor -a [Your_Folder_Path]/index.adoc
```

Optionally, link your document in the 'docs/index.adoc' file and generate an HTML file accordingly.

Final Folder Structure:

```
- docs
    - AAS_Submodel_Templates
        - [Your_Folder_Name]
            - media
                - image 1
                - image 2
                - ...
            - [Generated_AsciiDoc_File].adoc
            - index.adoc
            - index.html
            - [Your_Word_File].docx
    - style.css
    - favicon.png
```
