from setuptools import setup
from mxtheme import __version__

setup(
    name = 'mxtheme',
    version = __version__,
    author = 'Mu Li',
    author_email= 'mli@amazon.com',
    url="https://github.com/mli/mx-theme",
    description='MXNet Website Theme, adapted from Sphinx Material Design Theme',
    packages = ['mxtheme'],
    include_package_data=True,
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    entry_points = {
        'sphinx.html_themes': [
            'mxtheme = mxtheme',
        ]
    },
)

