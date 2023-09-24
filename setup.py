from setuptools import find_packages, setup

#with open("README.md", "r") as f:
#    long_description = f.read()

install_requires = open('requirements.txt').readlines()

setup(
    name="page_alert",
    version="0.0.1",
    description="Script to check if webpage structure has changed",
    package_dir={"": "page_alert"},
    packages=find_packages(where="page_alert"),
#    long_description=long_description,
#    long_description_content_type="text/markdown",
    url="",
    author="JakLjk",
    author_email="jakub@lejk.net",
#    install_requires=install_requires,
    python_requires=">=3.10",
)