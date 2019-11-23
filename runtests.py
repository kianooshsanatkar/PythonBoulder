import unittest

test_modules_list = [
'core/coretests/tests',
'infra/infratests/tests',
'infra/infratests/functionaltests'
]

if __name__ == '__main__':
    tests = unittest.TestSuite()
    for module in  test_modules_list:
        tests.addTest(unittest.TestLoader().discover(module, '*test.py'))

    unittest.TextTestRunner(verbosity=2).run(tests)
