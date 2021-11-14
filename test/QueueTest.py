import sys, os, unittest
sys.path.append(os.path.relpath('.'))
sys.path.append(os.path.relpath('..'))
from Queue import Queue
from typing import Any, List, Optional


################################################################################
class TestQueue(unittest.TestCase):

    def test_QueueEmpty(self):
        q = Queue()
        self.assertListEqual(q.data(), [])
        self.assertEqual(q.length(), 0)
        self.assertTrue(q.isEmpty())


    def test_QueueInt(self):
        testConstructionWith(self, [0,1,2])
        testPushWith(self, [0])
        q = testPushWith(self, [0,1,2])
        q.push(3)
        self.assertListEqual(q.data(), [0,1,2,3])
        q.push(4,5,6)
        self.assertListEqual(q.data(), [0,1,2,3,4,5,6])


    def testQueueString(self):
        q = testConstructionWith(self, ['hi'])
        q.push('a')
        self.assertListEqual(q.data(), ['hi','a'])
        q.push('b', 'c')
        self.assertListEqual(q.data(), ['hi','a','b','c'])


################################################################################
if __name__ == '__main__':
    unittest.main()


################################################################################
def testConstructionWith(ut :unittest.TestCase, data: List[Any]):
    q = Queue(*data)
    ut.assertEqual(q.length(), len(data))
    ut.assertListEqual(q.data(), data)
    return q


def testPushWith(ut:unittest.TestCase, data:List[Any]):
    q = Queue()
    q.push(*data)
    ut.assertListEqual(q.data(), data)
    ut.assertEqual(q.length(), len(data))
    if (not len(data)): ut.assertTrue(q.isEmpty())
    else: ut.assertFalse(q.isEmpty())
    return q
