import unittest
from MinStack import MinStack

class test_MinStack(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_InitializeMinStack(self):
        minStack = MinStack()
        self.assertEqual(minStack.getStack(), [])
        self.assertIsInstance(minStack, MinStack)

    def test_PushIntoMinStack(self):
        minStack = MinStack()
        minStack.push(-2)

        self.assertEqual(minStack.getStack(), [-2])

    def test_PopFromMinStack(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.pop()

        self.assertEqual(minStack.getStack(), [])

    def test_GetTopFromMinStack(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        minStack.pop()
        
        self.assertEqual(minStack.top(), 0)

    def test_GetMinBeforeAndAfterPop(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-1)

        self.assertEqual(minStack.getMin(), -2)
        self.assertEqual(minStack.top(), -1)

        minStack.pop()

        self.assertEqual(minStack.getMin(), -2)

    def test_LeetCodeCaseOne(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        
        self.assertEqual(minStack.getMin(), -3)

        minStack.pop()

        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)

    def test_GeeksForGeeksTestCase(self):
        stack = MinStack()
        stack.push(3)
        stack.push(5)
        stack.getMin()
        self.assertEqual(stack.getMin(), 3)
        stack.push(2)
        stack.push(1)
        stack.getMin()
        self.assertEqual(stack.getMin(), 1)
        stack.pop()
        
        stack.getMin()
        self.assertEqual(stack.getMin(), 2)
        stack.pop()
    

