from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Name_Entity_Recognition"
AUTHOR_USER_NAME = "deepakthakur-92"
SRC_REPO = "ner"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Name Entity Recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="deepak2009thakur@gmail.com",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)
