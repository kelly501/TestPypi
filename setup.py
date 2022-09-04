import setuptools

setuptools.setup(
    name="TestPypi",
    version="0.0.1",
    author="kelly501",
    author_email="kellylink501@gmail.com",
    description="Test a small example package",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kelly501/TestPypi",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    packages=['TestPypi'],
)
