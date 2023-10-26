import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()

__version__="0.0.0"
REPO_NAME="text-Summarizer"
AUTHOR_USER_NAME="iamrakib097"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="iamrakib097@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamrakib097/textSummarizer",
    project_urls={
        "Bug Tracker": "https://github.com/iamrakib097/textSummarizer/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)