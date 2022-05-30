import setuptools


# get __version__
exec( open( 'sqlimit/_version.py' ).read() )

with open( 'README.md', 'r' ) as f:
    long_desc = f.read()

setuptools.setup(
    name='sqlimit',
    version = __version__,
    author='Brian Carlsen <carlsen.bri@gmail.com>, C. Marcus Chuang <marcus.chchuang@gmail.com>',
    author_email = 'carlsen.bri@gmail.com',
    description = 'Shockley-Quiesser limit calculations.',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/bicarlsen/Shockley-Queisser-limit',
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
