from langchain_core.messages import HumanMessage
from langchain_core.utils import print_text
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from ToolHandler import ToolHandler

load_dotenv()
toolHandler = ToolHandler()

def main():
    model = ChatOpenAI(temperature=0)

    tools = toolHandler.get_tools()
    agent_executor = create_react_agent(model, tools)

    print("Hello!!! I am an AI assistant that is here to help you. If you want to exit, just type 'quit'.\n You can chat with me or ask me to")