from setuptools import setup, find_packages

setup(
    name="medical-ner-app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.27.0",
        "stanza>=1.5.0",
        "pandas>=2.0.3",
        "PyPDF2>=3.0.1",
        "python-docx>=0.8.11",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Streamlit app for medical named entity recognition using Stanza",
    keywords="nlp, medical, healthcare, named entity recognition, streamlit",
    url="https://github.com/yourusername/medical-ner-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
)
