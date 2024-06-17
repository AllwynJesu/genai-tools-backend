from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv, find_dotenv

from models.request import RequestData
from models.response import RewriteResponse, SummaryResponse

load_dotenv(find_dotenv())

llm = OpenAI(temperature=0)
chat_llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0.5)

SUMMARY_TEMPLATE = PromptTemplate.from_template(
    """
    You are an expert in text summarization. Your task is to analyze the provided text and generate a concise summary 
    that captures and conveys all the essential information. Please summarize the following text: {input_text}
    """
)

REWRITE_PROMPT = PromptTemplate.from_template(
    """
    You are an expert in rewriting text. Your task is to correct the grammar and rephrase the provided content using 
    simple and formal English. Do not invent or add any information outside of the given content. Please rewrite the 
    following text: {input_text}
    """
)

EXTRACT_TECHNICAL_DETAILS_PROMPT = PromptTemplate.from_template(
    """
    You are an expert in extracting and analyzing important information from given text. Your task is to identify and 
    elaborate on all the details related to the extracted details. Each points is wrapped inside HTML ordered list tags i.e. 
    <ol>...</ol>.

    Please perform the following steps:

    Extract all the important details from the provided content.
    Present these details as clear, concise, and elaborated points. Ensure generate content that is easy to understand.
    Ensure all the points wrapped inside HTML ordered list tags.
    Make sure to use code snippets are wrapped in code blocks/tags. Also, include relevant HTML tags where necessary.

    For example
        <ol>
            <li>Coffee< is good/li>
            <li>Tea is bad</li>
            <li>Milk is great</li>
        <ol>

    Here is the content: {input_text}
    """
)

def get_summary(input: RequestData) -> SummaryResponse:
    loader = WebBaseLoader(input.page_url)
    docs = loader.load()
    llm_chain = LLMChain(llm=chat_llm, prompt=SUMMARY_TEMPLATE)
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="input_text")
    result = stuff_chain.invoke(docs)
    return {"page_url": input.page_url,
            "summary": result["output_text"]}

def get_rewrite(input: RequestData) -> RewriteResponse:
    chain = REWRITE_PROMPT | llm
    result = chain.invoke(input.input_text)
    return {"page_url": input.page_url,
            "rewrite": result,
            "original_text": input.input_text}

def extract_important_details(input: RequestData) -> SummaryResponse:
    loader = WebBaseLoader(input.page_url)
    docs = loader.load()
    llm_chain = LLMChain(llm=chat_llm, prompt=EXTRACT_TECHNICAL_DETAILS_PROMPT)
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="input_text")
    result = stuff_chain.invoke(docs)
    return {"page_url": input.page_url,
            "tech_details": result["output_text"]}