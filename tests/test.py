
import unittest

class TestSuiteName(unittest.TestCase):
    def setUp(self):
        # print(1) 
        pass
    def tearDown(self):
        pass

    def test_sumSuccess(self):
        #do some things to get the actual
        actual = sum([1,3,4])
        expected = 8
        self.assertEqual(actual, expected)

    def test_sumFail(self):
        #do some things to get the actual
        actual = sum([1,3,4])
        expected = 7
        self.assertEqual(actual, expected)

    def test_isEven(self):
        #do some things to get the actual
        numberToTest = 6
        actual = numberToTest % 2 == 0
        self.assertTrue(actual)

    def test_isEvenFalse(self):
        #do some things to get the actual
        numberToTest = 7
        actual = numberToTest % 2 == 0
        self.assertFalse(actual)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

