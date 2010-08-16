try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='ceropath',
    version='1.0',
    description='',
    author='CBGP',
    author_email='chaval@supagro.inra.fr',
    url='',
    install_requires=[
        "Pylons>=0.9.7",
        "uuid",
        "mongokit==0.5.10",
        "pypit>=0.2.2",
        "markdown==2.0.3",
        "statlib==1.1",
        "pyparsing==1.5.2",
        "biopython==1.54",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'ceropath': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'ceropath': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = ceropath.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
