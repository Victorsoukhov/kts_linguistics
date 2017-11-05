from setuptools import setup


setup(
    name='kts_linguistics',
    version='0.1.0',
    description='Set of packages: spellcheck, phonetics, text processing and more',
    long_description=open('README.md').read(),

    author='KTS',
    author_email='o.morozenkov@ktsstudio.ru',
    url='https://github.com/KTSStudio/kts_linguistics',
    license='MIT',

    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic'
    ],

    install_requires=[
        'transliterate>=1.10,<1.11',
        'python-Levenshtein>=0.12,<0.13',
        'pymorphy2>=0.8,<0.9',
        'nltk>=3.2,<3.3',
        'scikit-learn>=0.19,<0.20'
    ],

    packages=['kts_linguistics',
              'kts_linguistics.corpora',
              'kts_linguistics.phonetics',
              'kts_linguistics.spellcheck',
              'kts_linguistics.string_transforms',
              'kts_linguistics.synonyms',
              'kts_linguistics.test'],
    include_package_data=True,
)
