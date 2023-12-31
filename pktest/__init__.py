# -*- coding: utf-8 -*-
""":mod:`pktest` package

:copyright: Copyright (c) 2023 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import pkg_resources

try:
    # We only have a version once the package is installed.
    __version__ = pkg_resources.get_distribution("pktest").version
except pkg_resources.DistributionNotFound:
    pass
