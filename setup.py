import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypackage",
    version="0.0.1",
    author="Clifford Whitworth",
    author_email="cliffo@protonmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cliffwhitworth/mypackage",
    project_urls={
        "Bug Tracker": "https://github.com/cliffwhitworth/mypackage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "mypackage"},
    packages=setuptools.find_packages(where="mypackage"),
    package_data={"mypackage": ["VERSION"]},
    python_requires=">=3.6",
)