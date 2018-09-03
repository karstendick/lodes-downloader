from setuptools import find_packages, setup

setup(
    name='lodes_downloader',
    version='0.0.1',
    description='Package to download Census LODES data',
    author='Joshua Karstendick',
    url='https://github.com/karstendick/lodes-downloader',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'wget==3.2',
        'beautifulsoup4==4.6.3',
        'requests==2.19.1',
    ],
)
