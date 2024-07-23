import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="selenium_google_login",
    version="0.1.0",
    author="ksks",
    author_email="nose2002kr@gmail.com",
    description="Helps you sign in to Google and remember it automatically.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nose2002kr/selenium-google-login",
    install_requires=requirements,
    #package_data={'': ['requirements.txt']},
    #include_package_data=True,
    packages = setuptools.find_packages(where='src'),
    python_requires=">=3.5",
)