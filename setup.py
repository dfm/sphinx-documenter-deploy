#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import re

from setuptools import find_packages, setup

# PROJECT SPECIFIC

NAME = "sphinx-documenter-deploy"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "sphinx_documenter_deploy", "__init__.py")
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
INSTALL_REQUIRES = ["numpy"]
EXTRA_REQUIRE = {
    "docs": [
        "sphinx>=3.3",
        "sphinx-book-theme",
        "myst-nb",
        "matplotlib",
    ],
}

# END PROJECT SPECIFIC


HERE = os.path.dirname(os.path.realpath(__file__))


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def find_meta(meta, meta_file=read(META_PATH)):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), meta_file, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        use_scm_version={
            "write_to": os.path.join(
                "src/{0}/{0}_version.py".format("sphinx_documenter_deploy")
            ),
            "write_to_template": '__version__ = "{version}"\n',
        },
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        url=find_meta("uri"),
        license=find_meta("license"),
        description=find_meta("description"),
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        package_dir={"": "src"},
        package_data={"sphinx_documenter_deploy": ["py.typed"]},
        include_package_data=True,
        python_requires=">=3.6",
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRA_REQUIRE,
        classifiers=CLASSIFIERS,
        zip_safe=True,
    )
