from setuptools import setup, find_packages

setup(
    name='axologgle',
    version='0.1.0',
    description='Logging tools but cooler',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/my_module',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',  # Or whatever license you're using
    packages=find_packages(),  # Automatically find your packages (submodules)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    install_requires=[],  # List dependencies here (e.g., ['numpy', 'requests'])
)
