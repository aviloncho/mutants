"""Test Mutant"""
import unittest
import mutant


class TestMutant(unittest.TestCase):

    def test_is_mutant_example(self):
        """
        Test human DNA example with \
        3 sequences (Diagonal, horizontal, vertical).
        """
        dna = [
            'ATGCGA',
            'CAGTGC',
            'TTATGT',
            'AGAAGG',
            'CCCCTA',
            'TCACTG'
        ]

        self.assertTrue(mutant.is_mutant(dna))

    def test_is_mutant_2_diagonals(self):
        """
        Test human DNA with 2 sequences (Diagonal, anti-diagonal).
        """
        dna = [
            'TTGCGC',
            'CAGTCC',
            'ATTCGT',
            'AACAGG',
            'CCACTA',
            'TCAATG'
        ]

        self.assertTrue(mutant.is_mutant(dna))

    def test_is_mutant_1_seq(self):
        """
        Test human DNA with 1 sequence (Vertical).
        """
        dna = [
            'ATGCGA',
            'CCGTTC',
            'TTATGG',
            'AGAAGG',
            'CAGCTG',
            'TCACTG'
        ]

        self.assertFalse(mutant.is_mutant(dna))

    def test_is_mutant_human(self):
        """
        Test human DNA without sequences.
        """
        dna = [
            'CTGCTA',
            'CAGTGC',
            'TTCTGT',
            'AGAAGG',
            'CGCCTA',
            'TCACTG'
        ]

        self.assertFalse(mutant.is_mutant(dna))
