from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


setup(
    name='mnist-py',
    version='0.6',
    author='Matt Petersen',
    description='Lighweight Numpy MNIST loader',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='peterm0273@gmail.com',
    url='https://github.com/mattpetersen/mnist-py',
    keywords=['mnist'],
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy',
        'requests',
    ],
    zip_safe=False,
)
