import unittest
from Question_1_v2 import BooleanExample

#单元测试实例

class CheckTest(unittest.TestCase):
    '''测试 Question_1_v2'''

    def test(self):
        if_equal = BooleanExample('asdawf','asdawf')
        self.assertEqual(if_equal,True)

if __name__ == "__main__":
    unittest.main()
