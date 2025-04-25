import os
import sys
# Get the absolute path to the directory containing code_to_test.py
base_dir = os.path.abspath(os.path.dirname(__file__))

# Add base_dir to sys.path if it's not already included
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

import pytest
from code_to_test import AgentState
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage


@pytest.fixture
def state():
    """
    Fixture for the AgentState, keeping in mind that it is mutable.
    """
    return AgentState(
        question="What is AI?",
        messages=[HumanMessage(content="What is AI?")],
        prompt="Please answer the question:",
        answer="",
        on_topic="yes",
        context=[Document(page_content="test1"), Document(page_content="test2")],
    )
