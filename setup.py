from setuptools import setup, find_packages

setup(
    name="DepthAI_Agent",
    version="0.1.0",
    description="A framework for building AI agents using ChatGPT",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai>=0.27.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
