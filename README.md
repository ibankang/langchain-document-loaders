# LangChain Document Loaders - Learning Repository

This repository demonstrates various **LangChain document loaders** for ingesting data from different sources into LangChain `Document` objects. Each example shows how to load, process, and use documents with LLMs.

## Overview

LangChain's document loaders convert various data sources (PDFs, text files, CSVs, web pages, directories) into a standard `Document` format containing:
- `page_content` — The actual text/content
- `metadata` — Source information (file path, page number, URL, etc.)

## Loaders Demonstrated

| Loader | File | Source Type | Key Features |
|--------|------|-------------|--------------|
| **TextLoader** | `text_loader.py` | `.txt` files | Simple text loading with encoding support |
| **PyPDFLoader** | `pdf_loader.py` | `.pdf` files | Page-by-page extraction with metadata |
| **CSVLoader** | `csv_loader.py` | `.csv` files | Row-based document creation |
| **DirectoryLoader** | `directory_loader.py` | Folder + pattern | Batch loading with `lazy_load()` for memory efficiency |
| **WebBaseLoader** | `webbase_loader.py` | Web URLs | HTML scraping and content extraction |

## Project Structure

```
langchain-document-loaders-main/
├── text_loader.py          # Text file loading example
├── pdf_loader.py           # PDF loading example
├── csv_loader.py           # CSV loading example
├── directory_loader.py     # Directory batch loading example
├── webbase_loader.py       # Web page loading example
├── cricket.txt             # Sample text file
├── dl-curriculum.pdf       # Sample PDF file
├── Social_Network_Ads.csv  # Sample CSV file
├── books/                  # Directory with PDF files
│   └── Building Machine Learning Systems with Python - Second Edition.pdf
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (create this)
```

## Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Running Examples

### Text Loader
```bash
python text_loader.py
```
Loads `cricket.txt`, extracts content, and generates a summary using OpenAI.

### PDF Loader
```bash
python pdf_loader.py
```
Loads `dl-curriculum.pdf` page by page, showing document count, content, and metadata.

### CSV Loader
```bash
python csv_loader.py
```
Loads `Social_Network_Ads.csv` — each row becomes a Document.

### Directory Loader
```bash
python directory_loader.py
```
Uses `DirectoryLoader` with `PyPDFLoader` to lazily load all PDFs in `books/` folder.

### WebBase Loader
```bash
python webbase_loader.py
```
Scrapes a Flipkart product page and queries the content with an LLM.

## Key Concepts

### Document Object
```python
Document(
    page_content="Actual text content...",
    metadata={"source": "file.pdf", "page": 1}
)
```

### Loading Methods
- `loader.load()` — Returns `List[Document]` (loads all into memory)
- `loader.lazy_load()` — Returns iterator (memory efficient for large datasets)

### Chaining with LLMs
```python
chain = prompt | model | parser
result = chain.invoke({"question": "...", "text": docs[0].page_content})
```

## Dependencies

- `langchain` — Core LangChain library
- `langchain-community` — Community document loaders
- `langchain-core` — Core abstractions
- `langchain-openai` — OpenAI integration
- `python-dotenv` — Environment variable loading
- `pypdf` — PDF processing
- `langchain-huggingface` — HuggingFace integration
- `transformers` — HuggingFace transformers
- `huggingface-hub` — HuggingFace Hub access

## Learning Outcomes

After exploring this repository, you will understand:
1. How to load different file formats into LangChain Documents
2. The structure of Document objects (content + metadata)
3. When to use `load()` vs `lazy_load()`
4. How to chain loaded documents with LLM prompts
5. Batch processing multiple files with DirectoryLoader

## License

MIT License — Feel free to use for learning and experimentation.