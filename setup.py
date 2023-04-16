from setuptools import setup
    
    
def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name='just_logger', # project name
    version='0.2.1', # versiion
    author='Baoming Yu', # author's name
    author_email='dingxuanliang@icloud.com', # author's email
    url='https://github.com/Baoming520/just-logger', # url on github
    description='A logging tool is used to record all kinds of logs during program running.', # abstract
    long_description=readme(), # contents in README.MD file
    long_description_content_type="text/markdown", # type of long description
    packages=['just_logger'], # pakages waiting for packing
    package_data={}, # data files in package
    install_requires=[], # required packages
)