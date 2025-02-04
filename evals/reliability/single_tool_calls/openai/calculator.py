from typing import Optional

from bitca.agent import Agent
from bitca.eval.reliability import ReliabilityEval, ReliabilityResult
from bitca.tools.calculator import CalculatorTools
from bitca.models.openai import OpenAIChat
from bitca.run.response import RunResponse


def factorial():

    agent=Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[CalculatorTools(factorial=True)],
    )
    response: RunResponse = agent.run("What is 10!?")
    evaluation = ReliabilityEval(
        agent_response=response,
        expected_tool_calls=["factorial"],
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    result.assert_passed()


if __name__ == "__main__":
    factorial()
