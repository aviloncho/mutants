"""Test Mutant"""
import unittest

import mutant
import fixtures


class TestMutant(unittest.TestCase):

    def test_is_mutant_example(self):
        """
        Test human DNA example with \
        3 sequences (Diagonal, horizontal, vertical).
        """

        self.assertTrue(mutant.is_mutant(fixtures.EXAMPLE))

    def test_is_mutant_2_diagonals(self):
        """
        Test human DNA with 2 sequences (Diagonal, anti-diagonal).
        """

        self.assertTrue(mutant.is_mutant(fixtures.DIAGONAL2))

    def test_is_mutant_1_seq(self):
        """
        Test human DNA with 1 sequence (Vertical).
        """

        self.assertFalse(mutant.is_mutant(fixtures.VERTICAL1))

    def test_is_mutant_human(self):
        """
        Test human DNA without sequences.
        """

        self.assertFalse(mutant.is_mutant(fixtures.HUMAN))

    def test_big_dna(self):
        """
        Test big human DNA.
        """

        self.assertTrue(mutant.is_mutant(fixtures.BIGDNA))
