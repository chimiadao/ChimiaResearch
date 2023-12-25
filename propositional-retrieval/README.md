# Dense X Retrieval Implementation for ChimiaResearch

## Overview
This repository hosts the implementation of the innovative approach introduced in the paper "Dense X Retrieval: What Retrieval Granularity Should We Use?". Focused on optimizing dense retrieval in open-domain NLP tasks, this implementation is a key component of ChimiaResearch, enhancing our AI-driven chemical research capabilities.

## Features
- Proposition-Based Retrieval: A novel retrieval unit that focuses on atomic expressions within text, encapsulating distinct factoids.
- Enhanced Dense Retrieval: Improved performance over traditional passage or sentence-based methods.
- Optimized for QA Tasks: Reduced input token length and minimized irrelevant information, making it ideal for downstream QA tasks in chemical research.

## Getting Started
### Prerequisties
- python >=3.10

### Installation
1. Clone the repository
```bash
git clone https://github.com/chimiadao/ChimiaResearch.git
```

2. Change directory
```bash
cd ChimiaResearch/propositional_retriever
```

3. Install
```bash
pip install -e .
```

### Resources
- The paper: https://arxiv.org/abs/2312.06648
- Langchain Implementation: https://github.com/langchain-ai/langchain/tree/master/templates/propositional-retrieval/propositional_retrieval



