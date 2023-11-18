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
5. [Generating PDF from AsciiDoc](#generating-pdf-from-asciidoc)
    1. [Install Asciidoctor-PDF](#install-asciidoctor-pdf)
    2. [Generate HTML Output](#generate-pdf-output)
6. [Final Folder Structure](#final-folder-structure)

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

For detailed instructions on converting Word documents to AsciiDoc format, please see the [word2asciidoc README](https://github.com/admin-shell-io/word2asciidoc/). 

## Generating HTML from AsciiDoc

### Install Asciidoctor

To generate an HTML file from your AsciiDoc document, install Asciidoctor for [Windows](https://docs.asciidoctor.org/asciidoctor/latest/install/windows/), [Linux](https://docs.asciidoctor.org/asciidoctor/latest/install/linux-packaging/) or [macOS](https://docs.asciidoctor.org/asciidoctor/latest/install/macos/)

### Generate HTML Output

Execute the following command to generate an HTML file from your AsciiDoc document:

```shell
asciidoctor -a [Your_Folder_Path]/[YOUR_AAS_SPECIFICATION].adoc
```

Optionally, link your document in the 'docs/[YOUR_AAS_SPECIFICATION].adoc' file and generate an HTML file accordingly.

## Generating PDF from AsciiDoc

### Install Asciidoctor-PDF

To generate a PDF file from your AsciiDoc document, install [Asciidoctor-PDF](https://docs.asciidoctor.org/pdf-converter/latest/install/)

### Generate PDF Output

Execute the following command to generate a PDF file from your AsciiDoc document:

```shell
 asciidoctor-pdf -a pdf-theme=theme.yml pdf-themesdir=[PATH_TO_YOUR_THEME] --doctype=book [Your_Folder_Path]/[YOUR_AAS_SPECIFICATION].adoc
```

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
