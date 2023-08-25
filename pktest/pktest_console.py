# -*- coding: utf-8 -*-
"""Front-end command line for :mod:`pktest`.

See :mod:`pykern.pkcli` for how this module is used.

:copyright: Copyright (c) 2023 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import pykern.pkcli
import sys


def main():
    return pykern.pkcli.main("pktest")


if __name__ == "__main__":
    sys.exit(main())
