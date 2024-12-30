from setuptools import  setup, find_packages

setup(
    name="pystack",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "annotated-types",
        "certifi",
        "charset-normalizer",
        "idna",
        "pydantic",
        "pydantic_core",
        "python-decouple",
        "requests",
        "typing_extensions",
        "urllib3",
    ],
    author="Nana Kwaku Sarpong",
    author_email="nksarps@gmail.com",
    description="A lightweight Python wrapper for Paystack API",
    long_description="""PayStackPay is a user-friendly and versatile Python library crafted to streamline interactions with the Paystack API,\n enabling developers to effortlessly integrate Paystack's payment processing features into their Python applications.""",
    url="https://github.com/nksarps/pystack", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
)