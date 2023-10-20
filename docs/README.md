# AsciiDoc Guide for AAS Specifications

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    1. [Clone the Repository](#step-1-clone-the-repository)
    2. [Create a Specification Folder](#step-2-create-a-specification-folder)
    3. [Generate HTML Documentation](#step-3-generate-html-documentation)
3. [Working with AsciiDoc](#working-with-asciidoc)
    1. [Installing an AsciiDoc Viewer/Editor](#installing-an-asciidoc-viewereditor)
    2. [Converting Word Documents to AsciiDoc](#converting-word-documents-to-asciidoc)
        1. [Prerequisites](#prerequisites)
        2. [Online Conversion (Variant A)](#variant-a-online-conversion)
        3. [Local Conversion (Variant B)](#variant-b-local-conversion)
        4. [Manual Bug Fixes (Step 3)](#step-3-manual-bug-fixes)
4. [Generating HTML from AsciiDoc](#generating-html-from-asciidoc)
    1. [Install Asciidoctor](#install-asciidoctor)
    2. [Generate HTML Output](#generate-html-output)
5. [Final Folder Structure](#final-folder-structure)

## Introduction

This guide provides step-by-step instructions for working with AsciiDoc to create AAS specifications. AsciiDoc is a plain text format used for documenting technical specifications and can be easily converted into various output formats, including HTML.

## Getting Started

### Step 1: Clone the Repository

To begin, clone the repository where you'll be working on your template specifications using the following Git command:

```shell
git clone https://github.com/admin-shell-io/aas-specs
```

### Step 2: Create a Specification Folder

Duplicate the "docs/AAS_Submodel_Templates/Empty_Template" folder and rename it to match your specification's name. Remove any media files. To understand commonly used AsciiDoc formatting in specifications, refer to comments in "IDTA_Submodel_Wordtemplate_Layout.adoc". For a comprehensive AsciiDoc reference, visit [AsciiDoctor Documentation](https://docs.asciidoctor.org/asciidoc/latest/).

If you have a specification written or available in Word, refer to [Converting Word Documents to AsciiDoc](#converting-word-documents-to-asciidoc).

### Step 3: Generate HTML Documentation

Refer to [Generating HTML from AsciiDoc](#generating-html-from-asciidoc) for detailed instructions on creating HTML documentation from your AsciiDoc files.

## Working with AsciiDoc

### Installing an AsciiDoc Viewer/Editor

AsciiDoc syntax is plain text, allowing you to write documents using any text editor. However, using a dedicated viewer/editor for AsciiDoc files is recommended for previewing rendered files.

Explore various ways to preview and edit AsciiDoc documents [here](https://docs.asciidoctor.org/asciidoctor/latest/tooling/). Online tools like [AsciiDocLive](https://asciidoclive.com/edit/scratch/1) are also available.

> **Recommendation:** GitHub.Dev can also be utilized for AsciiDoc viewing and editing.

### Converting Word Documents to AsciiDoc

#### Prerequisites

Ensure you have an AsciiDoc Viewer/Editor installed (see [Installing an AsciiDoc Viewer/Editor](#installing-an-asciidoc-viewereditor)).

#### Online Conversion (Variant A)

1. Go to https://github.com/rwth-iat/word2asciidoc4aas/issues/new/choose and create a new issue in the Template "Transform Word Document to AsciiDoc."
2. Upload your Word file and wait for the conversion to complete.
3. You will receive a notification when the conversion is done.
4. Follow the provided link in the comment to download the converted AsciiDoc file.

#### Local Conversion (Variant B)

1. Install Pandoc by following the [Pandoc Installation Guide](https://pandoc.org/installing.html).
2. Create a folder to store your Word file, the generated AsciiDoc file, and extracted images.
3. Execute the following command in the terminal, replacing file and folder names accordingly:

```shell
pandoc [YOUR_AAS_SPECIFICATION].docx -f docx -t asciidoctor --wrap=none --markdown-headings=atx --extract-media=[Your_Folder_Path] -o [Your_Folder_Path]/[YOUR_AAS_SPECIFICATION].adoc
```

4. Utilize scripts from the 'word2asciidoc4aas' repository to fix issues in the generated AsciiDoc file.

##### Install Package

Install the package directly from GitHub using Pip:

```shell
pip install git+https://github.com/rwth-iat/word2asciidoc4aas.git@master
```

##### Execute Fixing Scripts

Run the following command to fix issues and generate a refined '[YOUR_AAS_SPECIFICATION].adoc' file:

```shell
fix_adoc --adoc_input [Path_to_YOUR_AAS_SPECIFICATION].adoc --adoc_output [Path_to_YOUR_AAS_SPECIFICATION].adoc
```

Or, if the above doesn't work:

```shell
python -m word2asciidoc.fix_adoc --adoc_input [Path_to_YOUR_AAS_SPECIFICATION].adoc --adoc_output [Path_to_YOUR_AAS_SPECIFICATION].adoc
```

Manually review the '[YOUR_AAS_SPECIFICATION].adoc' file and resolve any remaining issues. For detailed AsciiDoc information, refer to the [AsciiDoc Documentation](https://docs.asciidoctor.org/asciidoc/latest/).

Manual tasks may include:
1. Removing the table of contents from the AsciiDoc file.
2. Adding configuration and meta-information at the beginning of the adoc file.
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
3. Fixing tables and formatting.
   - Add header to the first row: "options=header"
   - Add header to the first column with "h": "cols="16%h,50%,25%,9%" or cols="h,d,d,d""
   - You can also format a single cell with a header style e.g. "h|header cell |normal cell h|header cell"  
   - Remove empty rows
   - Search for tables with complex structure and split them. Format headers and write before the first table "[.table-with-appendix-table]"
4. Addressing instances where text directly follows images.
   - Search for "image:media.*].*" 
   - Add a blank line after image


## Generating HTML from AsciiDoc

### Install Asciidoctor

To generate an HTML file from your AsciiDoc document, install [Asciidoctor](https://docs.asciidoctor.org/asciidoctor/latest/install/windows/).

### Generate HTML Output

Execute the following command to generate an HTML file from your AsciiDoc document:

```shell
asciidoctor -a [Your_Folder_Path]/[YOUR_AAS_SPECIFICATION].adoc
```

Optionally, link your document in the 'docs/[YOUR_AAS_SPECIFICATION].adoc' file and generate an HTML file accordingly.

## Final Folder Structure

Your final folder structure should resemble the following:

```
- docs
    - AAS_Submodel_Templates
        - [Your_Folder_Name]
            - media
                - image 1
                - image 2
                - ...
            - [YOUR_AAS_SPECIFICATION].adoc # AsciiDoc file
            - index.html
            - [YOUR_AAS_SPECIFICATION].docx # Word file
    - style.css
    - favicon.png
```

This structure organizes your AsciiDoc files, media assets, and generated HTML output for easy management and reference.