from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f :
    readme = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f :
    requires = f.read().splitlines()

setup(
    name='scraping_news',
    version='0.0.1',
    description='web scraping for news contents',
    long_description=readme,
    install_requires=requires,
    packages=find_packages(),
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: LINUX',
        'Programming Language :: Python :: 3.8.6'
    ]
)