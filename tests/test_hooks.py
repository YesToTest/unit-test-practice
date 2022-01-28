import unittest


class HooksTestCase(unittest.TestCase):
    def setUp(self):
        print("This is the setup")

    def tearDown(self):
        print("This is the teardown")

    def test_successful_sum(self):
        print("This is the success sum")
        self.assertEqual(3 + 2, 5)
