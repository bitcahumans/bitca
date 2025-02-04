from bitca.agent import Agent, RunResponse  # noqa
from bitca.models.cohere import Cohere

agent = Agent(model=Cohere(id="command-r-08-2024"), markdown=True)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
