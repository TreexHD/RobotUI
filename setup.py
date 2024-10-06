from setuptools import setup, find_packages

VERSION = '0.5.1'
DESCRIPTION = 'this is the robot UI library'
LONG_DESCRIPTION = 'A package that allows easy access to all functions of the robot via a UI in the web browser'

# Setting up
setup(
    name="robotui",
    version=VERSION,
    author="TreexHD, LinoDino",
    author_email="<no.mail>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'flask>=3.0.3',
        'psutil'
    ],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
    data_files = [('', ['robotui/templates/index.html'])]
)