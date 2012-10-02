import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzBuzz = FizzBuzz()

    def testFizzBuzzPeutDireUn(self):
        self.assertEquals(1, self.fizzBuzz.dit(1))
    
    def testFizzBuzzPeutDireDeux(self):
        self.assertEquals(2, self.fizzBuzz.dit(2))

    def testFizzBuzzPeutDireFizz(self):
        self.assertEquals('Fizz', self.fizzBuzz.dit(3))
    
    def testFizzBuzzPeutDireBuzz(self):
        self.assertEquals('Buzz', self.fizzBuzz.dit(5))

if __name__ == '__main__':
    unittest.main()
