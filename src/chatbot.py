"""
AI Customer Support Playbook

Main application entry point.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_BASE_PATH = PROJECT_ROOT / "knowledge_base"


def show_banner():
    print("=" * 50)
    print("🤖 AI Customer Support Playbook")
    print("=" * 50)


def load_knowledge_base():
    """Load all markdown files from the knowledge base."""

    files = list(KNOWLEDGE_BASE_PATH.glob("*.md"))

    print(f"\nKnowledge base loaded: {len(files)} document(s)\n")

    for file in files:
        print(f"• {file.name}")


def main():
    show_banner()
    load_knowledge_base()


if __name__ == "__main__":
    main()
