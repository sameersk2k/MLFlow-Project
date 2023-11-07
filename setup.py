import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="MLFlow-Project"
AUTHOR_USER_NAME="sameersk2k"
SRC_REPO="MLops_Project"
AUTHOR_EMAIL="sameersk2k@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    author=AUTHOR_USER_NAME,
    description="A python package for ML App",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)