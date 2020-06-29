from NQueen import *
import unittest


class TestNQueen(unittest.TestCase):


    def test_fitness(self):
        nq = NQueen()
        self.assertEqual(nq.fitness([5, 1, 6, 0, 3, 7, 4, 2]), 28)

    def test_population_generation(self):
        nq = NQueen()
        nq.no_of_queens=8
        self.assertEqual(len(nq.generate_population()), 100)

    def test_mutate(self):
        nq = NQueen()
        nq.no_of_queens = 8
        self.assertNotEqual(nq.mutate([5, 1, 6, 0, 3, 7, 4, 2]), [5, 1, 6, 0, 3, 7, 4, 2])

    def test_reproduce(self):
        nq = NQueen()
        nq.no_of_queens = 8
        self.assertNotEqual(nq.reproduce([5, 1, 6, 0, 3, 7, 4, 2], [2, 4, 6, 8, 3, 1, 7, 5]), [5, 1, 6, 0, 3, 7, 4, 2])

    def test_find(self):
        nq = NQueen()
        nq.no_of_queens = 8
        seq = nq.find(8)
        self.assertEqual(nq.fitness(seq), 28)

if __name__ == '__main__':
    unittest.main()