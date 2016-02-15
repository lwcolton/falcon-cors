from setuptools import setup, find_packages

setup(
    name = "falcon-cors",
    version = "1.0.0",
    description = "Falcon CORS middlware",
    package_dir = {"":"src"},
    packages = find_packages("src"),
)
