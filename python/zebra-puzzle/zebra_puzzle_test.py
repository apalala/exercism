import unittest

from zebra_puzzle import solution


class ZebraPuzzleTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(('Norweigan', 'Japanese'), solution())


if __name__ == '__main__':
    unittest.main()
