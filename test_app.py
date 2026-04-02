import unittest
from app import add
class TestApp(unittest.TestCase):
 def test_add(self):
<<<<<<< HEAD
  self.assertEqual(add(2,3),5)
if __name__ == "__main__":
 unittest.main()
=======
    self.assertEqual(add(2,3),5)
if __name__ == "__main__":
    unittest.main()
>>>>>>> 97d8e2341ce4a76110eb876f9921817f34495233
