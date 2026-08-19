# ============================================================
# WORKFLOW
# ============================================================
#
# PDF File
#    ↓
# PyPDFLoader
#    ↓
# loader.load()
#    ↓
# docs (List of Document objects)
#    ↓
# docs[0] → First PDF page/content
# docs[1] → Second PDF page/content
#    ↓
# Each Document contains:
#    - page_content → Actual text
#    - metadata     → Information about the page/source
#
# ============================================================


# ------------------------------------------------------------
# IMPORT
# ------------------------------------------------------------

# PyPDFLoader is a LangChain document loader used to
# read PDF files.
#
# It extracts text and information from the PDF and
# converts the PDF content into LangChain Document objects.
from langchain_community.document_loaders import PyPDFLoader


# ------------------------------------------------------------
# 1. CREATE THE PDF LOADER
# ------------------------------------------------------------

# Tell the loader which PDF file to load.
#
# At this stage, we are creating the loader object.
# The PDF content is loaded when we call loader.load().
loader = PyPDFLoader("dl-curriculum.pdf")


# ------------------------------------------------------------
# 2. LOAD THE PDF
# ------------------------------------------------------------

# Read the PDF and convert its content into
# LangChain Document objects.
#
# docs is a Python list.
#
# For a PDF with multiple pages, there will typically be
# multiple Document objects.
docs = loader.load()


# ------------------------------------------------------------
# 3. PRINT ALL DOCUMENT OBJECTS
# ------------------------------------------------------------

# This prints the list of Document objects.
print(docs)


# ------------------------------------------------------------
# 4. COUNT THE DOCUMENTS
# ------------------------------------------------------------

# This prints the total number of Document objects.
#
# For a page-based PDF loader, this commonly corresponds
# to the number of pages loaded.
print(len(docs))


# ------------------------------------------------------------
# 5. GET THE CONTENT OF THE FIRST DOCUMENT
# ------------------------------------------------------------

# docs[0] → First Document object
#
# .page_content → Actual text/content stored in that document
print(docs[0].page_content)


# ------------------------------------------------------------
# 6. GET METADATA OF THE SECOND DOCUMENT
# ------------------------------------------------------------

# docs[1] → Second Document object
#
# .metadata → Information about the document/page,
# such as source and page-related information.
print(docs[1].metadata)