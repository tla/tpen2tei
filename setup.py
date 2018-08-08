from setuptools import setup, find_packages

setup(
    name='tpen2tei',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='A module for conversion of SharedCanvas-JSON transcription data to TEI XML',

    # The project's main homepage.
    url='https://github.com/DHUniWien/tpen2tei',

    # Author details
    author='Tara L Andrews',
    author_email='tla@mit.edu',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Markup :: XML',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='TEI-XML SC-JSON manuscript transcription',
    packages=find_packages(exclude=['contrib', 'tests']),
    install_requires=['lxml'],
    python_requires='>3'
)
