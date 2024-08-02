from setuptools import setup, find_packages

setup(
    name='PromptsAutomation',
    version='1.3',
    packages=find_packages(),
    author='Matheus Almeida Santos Mendonça',
    author_email='matheuzengenharia@gmail.com',
    description='Uma ferramenta para criar e gerenciar prompts de usuário no sistema Genesys Cloud de forma automatizada',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Matheus-Sueth/PromptsAutomation.git',
    install_requires=[
        'openpyxl',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
)
