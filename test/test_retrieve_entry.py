import unittest
from unittest.mock import patch
from io import StringIO
from src import health


class TestRetrieveEntry(unittest.TestCase):

    def test_retrieve_entry(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            health.retrieve_entry("anu", 1)
            self.assertEqual(mock_stdout.getvalue(), "2024-06-07 20:13:32.883087: Test log entry\n")

if __name__ == "__main__":
    unittest.main()
