"""
Data models for the project.
"""

from dataclasses import dataclass


@dataclass
class Document:
    """Represents a knowledge base document."""

    title: str
    filename: str
    content: str
