from setuptools import setup, find_packages

setup(
    name = "falcon-cors",
    version = "1.0.1",
    description = "Falcon CORS middlware",
    package_dir = {"":"src"},
    packages = find_packages("src"),
    install_requires=["falcon"],
    author = 'Colton Leekley-Winslow',
    author_email = 'lwcolton@gmail.com',
    url = 'https://github.com/lwcolton/falcon-cors',
    download_url = 'https://github.com/lwcolton/falcon-cors/archive/master.zip',
    keywords = ['falcon', 'cors', 'http'],
    classifiers = []
)
