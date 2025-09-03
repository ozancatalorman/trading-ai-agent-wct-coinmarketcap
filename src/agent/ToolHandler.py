from typing import Union, Callable, Any, Optional, Iterable, List
from langchain_core.tools import BaseTool

ToolLike = Union[BaseTool, Callable[..., Any]]

class ToolHandler:
    def __init__(self, tools: Optional[Union[ToolLike, Iterable[ToolLike]]] = None):
        self.tools: List[ToolLike] = []

        if tools is None:
            return

        if isinstance(tools, Iterable) and not isinstance(tools, (str, bytes)):
            for t in tools:
                try:
                    self.__validate_tool(t)
                except TypeError as e:
                    print(f"Skipping invalid tool {t!r}: {e}")
                    continue
                if t not in self.tools:
                    self.tools.append(t)
        else:
            try:
                self.__validate_tool(tools)
            except TypeError as e:
                print(f"Skipping invalid tool {tools!r}: {e}")
            else:
                if tools not in self.tools:
                    self.tools.append(tools)

    def add_tool(self, tool: ToolLike) -> None:
        try:
            self.__validate_tool(tool)
        except TypeError as e:
            print(f"Cannot add tool {tool!r}: {e}")
            return

        if tool in self.tools:
            print(f"Tool {tool} already exists.")
            return
        self.tools.append(tool)

    def remove_tool(self, tool: ToolLike) -> None:
        if tool in self.tools:
            self.tools.remove(tool)
            print(f"Tool {tool} has been removed.")
        else:
            print(f"Tool {tool} not found in the list.")

    def list_tools(self) -> str:
        if not self.tools:
            return "This tool handler has no tools yet."
        return "This tool handler has these tools:\n" + "\n- ".join(str(tool) for tool in self.tools)

    def get_tools(self) -> List[ToolLike]:
        return self.tools

    @staticmethod
    def __validate_tool(tool: Optional[ToolLike] = None) -> None:
        if isinstance(tool, BaseTool) or callable(tool):
            return
        expected = "a LangChain BaseTool instance or a callable function"
        raise TypeError(f"Invalid tool {tool!r}. Expected {expected}.")

