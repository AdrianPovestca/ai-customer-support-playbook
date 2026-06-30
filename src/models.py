"""
Data models used throughout the project.
"""

from dataclasses import dataclass


@dataclass
class Document:
    """
    Represents a single knowledge base document.
    """

    title: str
    filename: str
    content: str
