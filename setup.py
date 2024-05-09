from setuptools import setup, find_packages

setup(
    name='productapi',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='product management',
    url='https://github.com/rakhi641557/product.git',
    author='Rakhipr',
    author_email='rakhi.pr@beinex.com',
    install_requires=[
        'Django>=2.0',
        
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)
