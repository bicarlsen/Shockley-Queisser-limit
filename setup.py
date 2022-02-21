import setuptools

with open( 'README.md', 'r' ) as f:
    long_desc = f.read()

setuptools.setup(
    name='sqlimit',
    version = '0.0.1',
    author='C. Marcus Chuang',
    author_email = 'marcus.chchuang@gmail.com',
    description = 'Shockley-Quiesser limit calculations.',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/marcus-cmc/Shockley-Queisser-limit.git',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'numpy',
        'pandas',
        'matplotlib',
        'scipy'
    ],
    package_data = {
        'sqlimit': [ 'data/*' ]
    },

)
