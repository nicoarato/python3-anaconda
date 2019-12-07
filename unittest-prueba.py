def multiplicar(n1,n2):
    return n1*n2

import unittest

class pruebas(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplicar(3,3),9)
        self.assertEqual(multiplicar(3,3),8)
        self.assertEqual(multiplicar(3,3),18)


if __name__ == '__main__':
    unittest.main()