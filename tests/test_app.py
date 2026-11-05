import unittest
from app import generate
class Tests(unittest.TestCase):
    def test_deterministic(self):
        self.assertEqual(generate(20,42),generate(20,42))
    def test_seed_changes(self):
        self.assertNotEqual(generate(20,1),generate(20,2))
    def test_schema(self):
        rows=generate(10)
        self.assertEqual([r["id"] for r in rows],list(range(1,11)))
        self.assertTrue(all(0<=r["score"]<=100 for r in rows))
    def test_empty(self):
        self.assertEqual(generate(0),[])
    def test_bad_count(self):
        with self.assertRaises(ValueError): generate(-1)
if __name__=="__main__": unittest.main()
