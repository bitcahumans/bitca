from bitca.agent import Agent
from bitca.models.deepseek import DeepSeek
from bitca.models.openai import OpenAIChat

task = (
    "Discuss the concept of 'The Ship of Theseus' and its implications on the notions of identity and change. "
    "Present arguments for and against the idea that an object that has had all of its components replaced remains "
    "fundamentally the same object. Conclude with your own reasoned position on the matter."
)

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
    markdown=True,
)
reasoning_agent.print_response(task, stream=True)
