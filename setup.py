import os.path
from setuptools import setup, find_packages

package_dir = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(package_dir, "version")
with open(version_file) as version_file_handle:
    version = version_file_handle.read()

setup(
    name = "falcon-cors",
    version = version,
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
