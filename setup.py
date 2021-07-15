from setuptools import setup, find_packages

setup(
    name='TechnicalTask',
    version='1.0.0',
    url='https://github.com/IollyM/TechnicalTask.git',
    author='Iolly',
    author_email='matveeva.anastasiia.a@gmail.com',
    description='TechnicalTask for interview',
    packages=find_packages(),
    install_requires=['numpy >= 1.21.0', 'pandas==1.3.0'],
)
