import math #lets us use the math module
import unittest #unittest lets us test small sections of code

def circleArea(radius): 
    return radius * radius * math.pi

def rectArea(base, height):
    return base * height

def trapArea(base1, base2, height):
    return height * (base1 + base2) / 2

def triArea(base,height):
    return (base * height) / 2
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest module
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25 * math.pi)
        self.assertEqual(circleArea(2), 4 * math.pi)
    def testRectArea(self):
        self.assertEqual(rectArea(2, 2), 2 * 2)
        self.assertEqual(rectArea(123, 321), 123 * 321)
    def testTrapArea(self):
        self.assertEqual(trapArea(3, 4, 5), 5 * (3 + 4) / 2)
        self.assertEqual(trapArea(1, 2, 3), 3 * (1 + 2) / 2)
    def testTriArea(self):
        self.assertEqual(triArea(1, 3), (1 * 3) / 2)
        self.assertEqual(triArea(9, 8), (9 * 8) /2)
    
    