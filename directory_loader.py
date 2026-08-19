# ============================================================
# WORKFLOW
# ============================================================
#
# books/ folder
#    ↓
# DirectoryLoader
#    ↓
# Find all files matching "*.pdf"
#    ↓
# For each PDF:
#    ↓
# PyPDFLoader loads and processes the PDF
#    ↓
# Convert PDF content into LangChain Document objects
#    ↓
# lazy_load()
#    ↓
# Returns a lazy iterator of Document objects
#    ↓
# for document in docs:
#    ↓
# Process one Document at a time
#    ↓
# document.metadata
#    ↓
# Print metadata for that Document
#
# ============================================================


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------

# DirectoryLoader is used to load multiple files from a directory.
#
# It can:
# - Look inside a folder
# - Find files matching a pattern
# - Use another loader to process each file
#
# PyPDFLoader is used specifically for loading PDF files.
#
# It reads PDF files and converts their content into
# LangChain Document objects.
from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader
)


# ------------------------------------------------------------
# 1. CREATE THE DIRECTORY LOADER
# ------------------------------------------------------------

# Create a DirectoryLoader object.
#
# This loader will search inside the "books" folder.
loader = DirectoryLoader(

    # --------------------------------------------------------
    # path
    # --------------------------------------------------------
    #
    # Specify the directory/folder where the files are located.
    #
    # The folder structure might look like this:
    #
    # project/
    # ├── app.py
    # └── books/
    #     ├── book1.pdf
    #     ├── book2.pdf
    #     └── book3.pdf
    #
    path="books",


    # --------------------------------------------------------
    # glob
    # --------------------------------------------------------
    #
    # Specify which files should be loaded.
    #
    # "*.pdf" means:
    #
    # *      → Any file name
    # .pdf   → Must have the PDF extension
    #
    # Examples that will match:
    #
    # book.pdf
    # notes.pdf
    # python-guide.pdf
    #
    # Examples that will NOT match:
    #
    # image.png
    # notes.txt
    # data.csv
    #
    glob="*.pdf",


    # --------------------------------------------------------
    # loader_cls
    # --------------------------------------------------------
    #
    # Specify which loader should be used to load each file.
    #
    # Since the files found are PDF files,
    # we use PyPDFLoader.
    #
    # Conceptually:
    #
    # DirectoryLoader finds:
    #
    # books/book1.pdf
    # books/book2.pdf
    #
    # Then it uses:
    #
    # PyPDFLoader(book1.pdf)
    # PyPDFLoader(book2.pdf)
    #
    loader_cls=PyPDFLoader
)


# ------------------------------------------------------------
# 2. LAZILY LOAD THE DOCUMENTS
# ------------------------------------------------------------

# lazy_load() does not immediately create and return a complete
# Python list containing every Document object.
#
# Instead, it returns a lazy iterator.
#
# This means documents are loaded one at a time as we iterate.
#
# Workflow:
#
# lazy_load()
#     ↓
# Iterator is created
#     ↓
# for loop starts
#     ↓
# Load/process next Document
#     ↓
# Load/process next Document
#     ↓
# Continue until all PDF content is processed
#
# This can be useful when working with many files because you
# can process documents gradually instead of handling everything
# at once.
docs = loader.lazy_load()


# ------------------------------------------------------------
# 3. ITERATE THROUGH THE DOCUMENTS
# ------------------------------------------------------------

# docs is a lazy iterator.
#
# The for loop gets one Document object at a time.
#
# "document" represents the current LangChain Document object.
#
# Conceptually:
#
# First iteration:
# document → First Document
#
# Second iteration:
# document → Second Document
#
# Third iteration:
# document → Third Document
#
# ...and so on.
for document in docs:

    # --------------------------------------------------------
    # 4. ACCESS DOCUMENT METADATA
    # --------------------------------------------------------
    #
    # Every LangChain Document generally contains:
    #
    # document.page_content
    #     → The actual extracted text/content
    #
    # document.metadata
    #     → Additional information about the document
    #
    # Metadata may include information such as:
    #
    # - Source file path
    # - Page number
    # - Other loader-related information
    #
    # The exact metadata can depend on the loader being used.
    print(document.metadata)