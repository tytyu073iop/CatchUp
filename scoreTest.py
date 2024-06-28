import unittest
import json
from score import Score
from enum import Enum
import os

class MemberType(Enum):
    ADMIN = 'Admin'
    CUSTOMER = 'Customer'

class TestScore(unittest.TestCase):
    def setUp(self):
        os.remove('test_scores.json') if os.path.exists('test_scores.json') else None
        self.members = [MemberType.ADMIN.value, MemberType.CUSTOMER.value]
        self.score = Score(self.members, 'test_scores.json')

    def test_increase(self):
        self.assertEqual(self.score.score[MemberType.ADMIN.value], 0)
        self.assertEqual(self.score.score[MemberType.CUSTOMER.value], 0)

    def test_save(self):
        self.score.increase(7, MemberType.CUSTOMER.value)
        self.score.save()
        self.assertEqual(len(self.score.scores), 1)
        self.assertEqual(self.score.scores[0][MemberType.ADMIN.value], 0)
        self.assertEqual(self.score.scores[0][MemberType.CUSTOMER.value], 7)

    def test_multiple_saves(self):
        self.score.increase(5, MemberType.ADMIN.value)
        self.score.save()
        self.score.increase(3, MemberType.CUSTOMER.value)
        self.score.save()
        self.assertEqual(len(self.score.scores), 2)
        self.assertEqual(self.score.scores[0][MemberType.ADMIN.value], 5)
        self.assertEqual(self.score.scores[0][MemberType.CUSTOMER.value], 0)
        self.assertEqual(self.score.scores[1][MemberType.ADMIN.value], 5)
        self.assertEqual(self.score.scores[1][MemberType.CUSTOMER.value], 3)

    def test_saveToFile(self):
        self.score.increase(3, MemberType.ADMIN.value)
        self.score.save()
        self.score.saveToFile('test_scores.json')
        with open('test_scores.json', 'r') as f:
            saved_scores = json.load(f)
        self.assertEqual(saved_scores, [self.score.score])

    def test_multiple_saves_to_file(self):
        self.score.increase(2, MemberType.ADMIN.value)
        self.score.save()
        self.score.save()
        self.score.saveToFile('test_scores.json')
        self.score.saveToFile('test_scores.json')
        with open('test_scores.json', 'r') as f:
            saved_scores = json.load(f)
        self.assertEqual(saved_scores, self.score.scores)

    def test_loadFromFile(self):
        self.score.increase(2, MemberType.CUSTOMER.value)
        self.score.save()
        self.score.saveToFile('test_scores.json')
        new_score = Score(self.members, 'test_scores.json')
        self.assertEqual(new_score.scores, [self.score.score])

if __name__ == '__main__':
    unittest.main()
