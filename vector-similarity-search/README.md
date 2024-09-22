# Vector Similarity Search
Build with MongoDB Atlas Vector Search

Simple Application to demonstrate the use of MongoDB Atlas Vector Search to perform similarity search on vectors and generating embeddings using Hugging Face [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) sentence transformer model.

## Setup

### Clone the repository
```bash
git clone https://github.com/mohits-git/rag.git
cd <repo-name>
```

### Create a virtual environment
```bash
python3 -m venv venv
```

### Activate the virtual environment
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

> Install certificates for ssl verification, if you are facing issues connecting to the mongodb
> you can manually install the certificates by running the following command (in macOS):
> ```bash
> /Applications/Python\ 3.x/Install\ Certificates.command
> ```
