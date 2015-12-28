from setuptools import setup

try:
    with open('readme.rst') as f:
        long_description = f.read()
except IOError:
    with open('readme.md') as f:
        long_description = f.read()

setup(
    name='draw-compose',

    version='0.0.3',

    description='Render Docker compose files',
    long_description=long_description,

    # The project's main homepage.d
    url='https://github.com/Alexis-benoist/draw-compose',

    # Author details
    author='Alexis Benoist',
    author_email='alexis.benoist@gmail.com',

    # Choose your license
    license='Apache License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Database',
    ],

    # What does your project relate to?
    keywords='docker diagram render',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[
        'draw_compose',
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'docker-compose',
        'pygraphviz'
    ],
    entry_points={
        'console_scripts': [
            'draw-compose=draw_compose:cli',
        ],
    },
)