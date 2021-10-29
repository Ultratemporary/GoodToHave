import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='stefansfunktioner', #samma som python foldern
    version='0.0.2',
    author='Stefan Holmberg',
    author_email='stefan.holmberg@systementor.se',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ultratemporary/goodtohave',
    project_urls = {
        "Bug Tracker": "https://github.com/Ultratemporary/goodtohave/issues"
    },
    license='MIT',
    packages=['stefansfunktioner'], #ska vara samma som name
    install_requires=['requests']
)