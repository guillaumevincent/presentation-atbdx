import unittest
from fizzbuzz import FizzBuzz, GenerateurFizz, GenerateurBuzz, GenerateurBang, GenerateurWoopee

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzBuzz = FizzBuzz()
        self.fizzBuzz.generateurs.append(GenerateurFizz())
        self.fizzBuzz.generateurs.append(GenerateurBuzz())
        self.fizzBuzz.generateurs.append(GenerateurBang())
        self.fizzBuzz.generateurs.append(GenerateurWoopee())

    def testFizzBuzzPeutDireUn(self):
        self.assertEquals(1, self.fizzBuzz.dit(1))
    
    def testFizzBuzzPeutDireDeux(self):
        self.assertEquals(2, self.fizzBuzz.dit(2))

    def testFizzBuzzPeutDireFizz(self):
        self.assertEquals('Fizz!', self.fizzBuzz.dit(3))
    
    def testFizzBuzzPeutDireBuzz(self):
        self.assertEquals('Buzz!', self.fizzBuzz.dit(5))
        
    def testFizzBuzzPeutDireFizzBuzz(self):
        self.assertEquals('FizzBuzz!', self.fizzBuzz.dit(3*5))

    def testFizzBuzzPeutDireBang(self):
        self.assertEquals('Bang!', self.fizzBuzz.dit(7))
        
    def testFizzBuzzPeutDireFizzBang(self):
        self.assertEquals('FizzBang!', self.fizzBuzz.dit(3*7))
        
    def testFizzBuzzPeutDireFizzBuzzBang(self):
        self.assertEquals('FizzBuzzBang!', self.fizzBuzz.dit(3*7*5))
    
    def testFizzBuzzPeutDireWoopee(self):
        self.assertEquals('Woopee!', self.fizzBuzz.dit(69))
        
    def testGenerateurFizzPeutDireFizz(self):
        gf = GenerateurFizz()
        self.assertEquals('', gf.dit('', 2))
        self.assertEquals('Fizz', gf.dit('', 3))

if __name__ == '__main__':
    unittest.main()
