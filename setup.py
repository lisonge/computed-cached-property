'''
@Date: 2020-06-19 22:55:45
@LastEditors: code
@Author: code
@LastEditTime: 2020-06-19 23:34:27
'''
import setuptools

with open("./README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="computed-cached-property",
    license='MIT',
    version="0.0.1",
    author="Li Songe",
    author_email="i@songe.li",
    description="A decorator for caching computed properties in classes. like Vue's Computed-Properties",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lisonge/computed-cached-property",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
