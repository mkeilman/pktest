# -*- coding: utf-8 -*-
"""pktest setup script

:copyright: Copyright (c) 2023 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import pykern.pksetup

pykern.pksetup.setup(
    name="pktest",
    author="RadiaSoft LLC",
    author_email="pip@radiasoft.net",
    description="test_project",
    install_requires=[
        "pykern",
    ],
    license="http://www.apache.org/licenses/LICENSE-2.0.html",
    url="https://github.com/radiasoft/pktest",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
