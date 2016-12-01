import unittest

# Change directory to import the Spintax module
import sys
from os import path
testdir = path.dirname(__file__)
srcdir = '../spintax/'
sys.path.insert(0, path.abspath(path.join(testdir, srcdir)))

import spintax


class TestSpintax(unittest.TestCase):
    def test_simple(self):
        self.assertIn(spintax.spin('{Hello|Hi}'), ['Hello', 'Hi'])

    def test_nested(self):
        self.assertIn(spintax.spin('{{Hello|Hi}|{Hey|Yo}}'),
                      ['Hello', 'Hi', 'Hey', 'Yo'])

    def test_escaped(self):
        self.assertEqual(spintax.spin(r'\{test}'), r'{test}')

    def test_not_escaped(self):
        self.assertEqual(spintax.spin(r'\\{test}'), r'\test')

    def test_escaped_with_backslash(self):
        self.assertEqual(spintax.spin(r'\\\{test}'), r'\{test}')

    def test_escaped_seperator(self):
        self.assertEqual(spintax.spin('{Hello\|Hi}'), r'Hello|Hi')

    def test_not_escaped_seperator(self):
        self.assertIn(spintax.spin(r'{Hello\\|Hi}'), ['Hello\\', 'Hi'])

    def test_escaped_seperator_with_backslash(self):
        self.assertEqual(spintax.spin(r'{Hello\\\|Hi}'), r'Hello\|Hi')

if __name__ == '__main__':
    unittest.main()
