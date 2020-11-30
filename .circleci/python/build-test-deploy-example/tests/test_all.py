#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import dateutil

def test():
    print(dateutil.__version__)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
