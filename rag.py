from dsrag.llm import OpenAIChatAPI
from dsrag.reranker import NoReranker
from dsrag.knowledge_base import KnowledgeBase
from dotenv import load_dotenv
import os
load_dotenv(".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
llm = OpenAIChatAPI(model='gpt-4o-mini')

reranker = NoReranker()
kb_sem = KnowledgeBase(kb_id="semantic_html", reranker=reranker, auto_context_model=llm)
kb_mic = KnowledgeBase(kb_id="microdata_schema", reranker=reranker, auto_context_model=llm)
kb_ari = KnowledgeBase(kb_id="aria_text", reranker=reranker, auto_context_model=llm)

def read_file(file_path):
    file = open(file_path, "r")
    content = file.read()
    file.close()
    return content

#Semantic HTML
file_path1 = "website_data/semantic-html/semantic_html.txt"
file_path2 = "website_data/semantic-html/semantic_html_basics.txt"
#Microdata
file_path3 = "website_data/microdata-info/microdata_properties.txt"
file_path4 = "website_data/microdata-info/microdata_schema_guide.txt"
file_path5 = "website_data/microdata-info/schema_vocab.txt"
#ARIA
file_path6 = "website_data/aria-info/aria-basics.txt"
file_path7 = "website_data/aria-info/aria_properties.txt"
file_path8 = "website_data/aria-info/aria_roles.txt"
'''
kb_sem.add_document(doc_id=file_path1, text=read_file(file_path1))
kb_sem.add_document(doc_id=file_path2, text=read_file(file_path2))
kb_mic.add_document(doc_id=file_path3, text=read_file(file_path3))
kb_mic.add_document(doc_id=file_path4, text=read_file(file_path4))
kb_mic.add_document(doc_id=file_path5, text=read_file(file_path5))
kb_ari.add_document(doc_id=file_path6, text=read_file(file_path6))
kb_ari.add_document(doc_id=file_path7, text=read_file(file_path7))
kb_ari.add_document(doc_id=file_path8, text=read_file(file_path8))
'''
def semantic_html_rag_tool(input, top_k=10):
    return kb_sem.search(input, top_k)
def microdata_rag_tool(input, top_k=10):
    return kb_mic.search(input, top_k)
def aria_rag_tool(input, top_k=10):
    return kb_ari.search(input, top_k)
