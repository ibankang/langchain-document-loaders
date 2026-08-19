# ============================================================
# WORKFLOW
# ============================================================
#
# 1. Load environment variables from .env
#        ↓
# 2. Load the cricket.txt file using TextLoader
#        ↓
# 3. Convert the file into LangChain Document object(s)
#        ↓
# 4. Get the text content from the Document
#        ↓
# 5. Insert the text into a prompt
#        ↓
# 6. Send the prompt to the OpenAI model
#        ↓
# 7. Parse the model's response into a simple string
#        ↓
# 8. Print the summary
#
# ============================================================


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------

# TextLoader is used to load plain text files (.txt)
# It converts the text file into LangChain Document objects.
from langchain_community.document_loaders import TextLoader


# ChatOpenAI is LangChain's interface for OpenAI chat models.
# It allows us to send prompts to an OpenAI LLM.
from langchain_openai import ChatOpenAI


# StrOutputParser converts the model's output into a normal
# Python string.
from langchain_core.output_parsers import StrOutputParser


# PromptTemplate helps us create a reusable prompt template.
from langchain_core.prompts import PromptTemplate


# load_dotenv loads environment variables from a .env file.
from dotenv import load_dotenv


# ------------------------------------------------------------
# 1. LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------------------

# This reads the .env file in the current project.
# For example:
#
# OPENAI_API_KEY=your_api_key_here
#
# After loading, ChatOpenAI can access the API key.
load_dotenv()


# ------------------------------------------------------------
# 2. CREATE THE OPENAI MODEL
# ------------------------------------------------------------

# Create an instance of the OpenAI chat model.
#
# If no model name is explicitly provided, the configured
# default behavior/version of the installed integration is used.
model = ChatOpenAI()


# ------------------------------------------------------------
# 3. CREATE A PROMPT TEMPLATE
# ------------------------------------------------------------

# {poem} is a placeholder.
#
# Later, we will replace {poem} with the actual text
# loaded from cricket.txt.
#
# Example:
#
# Template:
# "Write a summary for the following poem:
#  {poem}"
#
# After inserting actual text:
#
# "Write a summary for the following poem:
#  Cricket is a popular sport..."
prompt = PromptTemplate(
    template="""
    Write a summary for the following poem:

    {poem}
    """,
    input_variables=["poem"]
)


# ------------------------------------------------------------
# 4. CREATE OUTPUT PARSER
# ------------------------------------------------------------

# The AI model returns a LangChain AI message object.
#
# StrOutputParser extracts the actual text and converts it
# into a normal Python string.
parser = StrOutputParser()


# ------------------------------------------------------------
# 5. CREATE A TEXT LOADER
# ------------------------------------------------------------

# TextLoader loads a .txt file.
#
# File name: cricket.txt
#
# encoding='utf-8' tells Python how to read the characters
# inside the text file.
loader = TextLoader(
    "cricket.txt",
    encoding="utf-8"
)


# ------------------------------------------------------------
# 6. LOAD THE DOCUMENT
# ------------------------------------------------------------

# load() reads the file and returns a LIST of Document objects.
#
# Even though cricket.txt is one file, LangChain still returns
# a list because other loaders may return multiple documents.
#
# Example:
#
# docs = [
#     Document(
#         page_content="Actual content of cricket.txt",
#         metadata={"source": "cricket.txt"}
#     )
# ]
docs = loader.load()


# ------------------------------------------------------------
# 7. CHECK THE TYPE OF docs
# ------------------------------------------------------------

# docs is a Python list.
print(type(docs))


# ------------------------------------------------------------
# 8. CHECK HOW MANY DOCUMENTS WERE LOADED
# ------------------------------------------------------------

# For one normal text file, this will usually print:
# 1
print(len(docs))


# ------------------------------------------------------------
# 9. ACCESS THE ACTUAL TEXT CONTENT
# ------------------------------------------------------------

# docs[0] means:
#
# docs  -> List
# [0]   -> First Document in the list
#
# page_content contains the actual text from cricket.txt.
print(docs[0].page_content)


# ------------------------------------------------------------
# 10. ACCESS DOCUMENT METADATA
# ------------------------------------------------------------

# metadata contains additional information about the document.
#
# For example:
# {"source": "cricket.txt"}
#
# Metadata is information ABOUT the document, while
# page_content is the actual content OF the document.
print(docs[0].metadata)


# ------------------------------------------------------------
# 11. CREATE THE LANGCHAIN CHAIN
# ------------------------------------------------------------

# The | operator connects components together.
#
# prompt
#   ↓
# model
#   ↓
# parser
#
# The output of one component becomes the input of the next.
chain = prompt | model | parser


# ------------------------------------------------------------
# 12. RUN THE CHAIN
# ------------------------------------------------------------

# docs[0].page_content gets the text from cricket.txt.
#
# We pass that text into the {poem} variable.
#
# Input:
# {
#     "poem": "content from cricket.txt"
# }
#
# The prompt template replaces:
#
# {poem}
#
# with the actual text.
#
# Then:
#
# Prompt → OpenAI Model → String Parser
#
# The final summary is printed.
result = chain.invoke(
    {
        "poem": docs[0].page_content
    }
)

print(result)