from setuptools import setup, find_packages

setup(
    name="local-code-review-bot",
    version="0.1.0",
    description="Local-first AI code review bot: Ollama for deep review, Groq for fast checks.",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "requests>=2.31.0",
        "groq>=0.9.0",
        "pyyaml>=6.0",
    ],
    
    entry_points={
        "console_scripts": [
            "reviewbot=reviewbot.cli:app",
        ],
    },
    python_requires=">=3.9",
)
