from setuptools import setup, find_packages


# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='propositional-retriever',  
    version='0.1',  
    author='ChimiaDAO',  
    author_email='chimiadao@example.com',  # Replace with your email
    description='Implemets propositional retrieval using LangChain for ChimiaDAO',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/chimiadao/ChimiaResearch',
    packages=find_packages(exclude=('tests', 'docs')), 
    install_requires=requirements, 
    classifiers=[
        # Choose classifiers: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10', 
)
