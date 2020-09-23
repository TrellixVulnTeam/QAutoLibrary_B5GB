import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QAutoLibrary",
    version="0.0.3",
    author="QAutomate",
    author_email="contact@qautomate.fi",
    description="QAutofamily testing framework library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QAutofamily/QAutoLibrary",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'robotframework==3.2.1',
        'requests',
        'Pillow',
        'lxml',
        'simplejson',
        'pymongo',
        'pycryptodome',
        'tika'
    ],
    package_data={'QAutoLibrary.config': ['*.xml', '*.ini', '*.txt*']},
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ),
    entry_points = {'console_scripts': ['WebDriverUpdater = QAutoLibrary.WebDriverUpdater.check_and_update_drivers:main']}
)
