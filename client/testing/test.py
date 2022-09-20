import unittest

class TestingSomeMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Start')

    @classmethod
    def tearDownClass(cls):
        print('Tearmowd')

    def testUpperCase(self):
        s = 'abc'
        s_upper = s.upper()

        def errss():
            a, b = 1, 0
            if b == 0:
                return ZeroDivisionError


        self.assertEqual('ABC', s_upper)
        self.assertIn('upper', dir(str))

        with self.assertRaises(ZeroDivisionError):
            a = 1/0






if __name__ == '__main__':
    unittest.main()
