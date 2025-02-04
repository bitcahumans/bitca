from __future__ import annotations

from typing import List, Optional

from bitca.models.base import Model
from bitca.models.message import Message
from bitca.utils.log import logger


def get_groq_reasoning_agent(reasoning_model: Model, monitoring: bool = False) -> "Agent":  # type: ignore  # noqa: F821
    from bitca.agent import Agent

    return Agent(model=reasoning_model, monitoring=monitoring)


def get_groq_reasoning(reasoning_agent: "Agent", messages: List[Message]) -> Optional[Message]:  # type: ignore  # noqa: F821
    from bitca.run.response import RunResponse

    # Update system message role to "system"
    for message in messages:
        if message.role == "developer":
            message.role = "system"

    try:
        reasoning_agent_response: RunResponse = reasoning_agent.run(messages=messages)
    except Exception as e:
        logger.warning(f"Reasoning error: {e}")
        return None

    reasoning_content: str = ""
    if reasoning_agent_response.content is not None:
        # Extract content between <think> tags if present
        content = reasoning_agent_response.content
        if "<think>" in content and "</think>" in content:
            start_idx = content.find("<think>") + len("<think>")
            end_idx = content.find("</think>")
            reasoning_content = content[start_idx:end_idx].strip()
        else:
            reasoning_content = content

    return Message(
        role="assistant", content=f"<thinking>\n{reasoning_content}\n</thinking>", reasoning_content=reasoning_content
    )


async def aget_groq_reasoning(reasoning_agent: "Agent", messages: List[Message]) -> Optional[Message]:  # type: ignore  # noqa: F821
    from bitca.run.response import RunResponse

    # Update system message role to "system"
    for message in messages:
        if message.role == "developer":
            message.role = "system"

    try:
        reasoning_agent_response: RunResponse = await reasoning_agent.arun(messages=messages)
    except Exception as e:
        logger.warning(f"Reasoning error: {e}")
        return None

    reasoning_content: str = ""
    if reasoning_agent_response.content is not None:
        # Extract content between <think> tags if present
        content = reasoning_agent_response.content
        if "<think>" in content and "</think>" in content:
            start_idx = content.find("<think>") + len("<think>")
            end_idx = content.find("</think>")
            reasoning_content = content[start_idx:end_idx].strip()
        else:
            reasoning_content = content

    return Message(
        role="assistant", content=f"<thinking>\n{reasoning_content}\n</thinking>", reasoning_content=reasoning_content
    )
