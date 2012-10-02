#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import sys
import unittest

test_file_paths = glob.glob('test_*.py')
test_names = [path[:-3] for path in test_file_paths]
test_suites = [unittest.defaultTestLoader.loadTestsFromName(name) for name in test_names]
suite = unittest.TestSuite(test_suites)
unittest.TextTestRunner(verbosity=2).run(suite)

