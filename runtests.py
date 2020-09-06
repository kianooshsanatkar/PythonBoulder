import unittest

test_modules_list = [
    'core/tests/unittests',
    'infra/tests/unittests',
    'infra/tests/functionaltests'
]

if __name__ == '__main__':

    tests = unittest.TestSuite()

    for module in test_modules_list:
        tests.addTest(unittest.TestLoader().discover(module, '*test.py'))

    unittest.TextTestRunner(verbosity=2).run(tests)
