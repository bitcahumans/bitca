from bitca.agent import Agent
from bitca.models.deepseek import DeepSeek
from bitca.models.openai import OpenAIChat

task = "Plan an itinerary from Los Angeles to Las Vegas"

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
    markdown=True,
)
reasoning_agent.print_response(task, stream=True)
