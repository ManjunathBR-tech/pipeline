import unittest
def add(a,b):
   return a+b
def subtract(a,b):
   return a-b
def multiply(a,b):
   return a*b
class TestCalculator(unittest,TestCase):
   def test_add(self):
      self.assertEqual(add(20,20),40)
   def test_subtract(self):
      self.assertEqual(add(2,1),1)
   def test_subtract(self):
      self.assertEqual(add(6,4),24)


if __name__=="__main__":
   print("student calculator application")
   print("addition:" ,add(20,20))
   print("subtrction:", subtract(2,1))
   print("multiplication",multiply(5,4))

   print("\n Executing automated tests..\n")
   unittest.main(argv=['first-arg-is-ignored'],exit=False)
