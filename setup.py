from setuptools import setup, find_packages

setup(
    name='legacy',
    version='1.1.1',
    description='This package sorts folders by their extension',
    long_description='This package provides a command line utility that can be used to sort files in a folder based on their extensions. '
                     'It supports a variety of options that can be used to customize the sorting behavior.',
    url='https://github.com/Sinazija/legacy',
    author='sinazija',
    author_email='Sinazija987@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'legacy=legacy:main']
    }
)
