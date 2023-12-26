import re
import os
import logging
import langchain
import paperscraper
from dotenv import load_dotenv
from pypdf.errors import PdfReadError
from langchain.base_language import BaseLanguageModel
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from langchain.agents import AgentType, initialize_agent

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

load_dotenv('../.env')
import paperqa


llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.1,
)

def paper_search(search, pdir="query"):
    try:
        import paperscraper
        return paperscraper.search_papers(
            search, 
            pdir=pdir,
            limit=4
        )
    except (KeyError, ModuleNotFoundError):
        return {}
    
    except Exception as e:
        print(e)
        return {}
    

def scholar2result_llm(llm, query, search=None):
    """Useful to answer questions that require technical knowledge. Ask a specific question."""

    prompt = langchain.prompts.PromptTemplate(
        input_variables=["question"],
        template="I would like to find scholarly papers to answer this question: {question}. "
        'A search query that would bring up papers that can answer this question would be: "',
    )
    query_chain = langchain.chains.LLMChain(llm=llm, prompt=prompt)

    if not os.path.isdir("./query"):
        os.mkdir("query/")

    if search is None:
        search = query_chain.run(query)
        
    print("\nSearch:", search)
    papers = paper_search(search, pdir=f"query/{re.sub(' ', '', search)}")
    print("\nFound papers:", papers)

    if len(papers) == 0:
        return "Not enough papers found"
    
    docs = paperqa.Docs(llm=llm)
    not_loaded = 0
    for path, data in papers.items():
        try:
            docs.add(path, data["citation"])
        except (ValueError, FileNotFoundError, PdfReadError) as e:
            print(e)
            not_loaded += 1

    print(f"\nFound {len(papers.items())} papers but couldn't load {not_loaded}")
    return docs.query(query, length_prompt="about 100 words").answer

class LitSearch(BaseTool):
    name = "LiteratureSearch"
    description = (
        "Input a specific question, returns an answer from literature search. "
        "Do not mention any specific molecule names, but use more general features to formulate your questions."
    )
    llm: BaseLanguageModel
    def _run(self, query: str) -> str:
        return scholar2result_llm(self.llm, query)
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")

if __name__ == "__main__":
    # Simple example
    # query = "What is the best way to make a battery?"
    # print(scholar2result_llm(llm, query))

    # Agent example
    tools = [LitSearch(llm=llm)]
    agent = initialize_agent(
        llm=llm,
        tools=tools,
        verbose=True,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

    query = "What is the best way to make a battery?"
    print(agent.run(query))