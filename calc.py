import unittest
def add(a,b):
   return a+b
def subtract(a,b):
   return a-b
def multiply(a,b):
   return a*b
class TestCalculator(unittest,TestCase):
   def test_add(self):
      self.assertEqual(add(10,20),30)
   def test_subtract(self):
      self.assertEqual(add(22,11),11)
   def test_subtract(self):
      self.assertEqual(add(6,4),24)


if __name__=="__main__":
   print("student calculator application")
   print("addition:" ,add(10,20))
   print("subtrction:", subtract(22,11))
   print("multiplication",multiply(5,4))

   print("\n Executing automated tests..\n")
   unittest.main(argv=['first-arg-is-ignored'],exit=False)
