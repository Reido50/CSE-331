"""
Project 4
CSE 331 S21 (Onsay)
Your Name
tests.py
"""

# from __future__ import annotations
from CircularDeque import CircularDeque, LetsPassTrains102
import unittest, random
from math import floor

random.seed(1342)


class CircularDequeTests(unittest.TestCase):
    def test_len(self):
        cd = CircularDeque()
        self.assertEqual(0, len(cd))

        cd = CircularDeque([1])
        self.assertEqual(1, len(cd))

        cd = CircularDeque([1, 2])
        self.assertEqual(2, len(cd))

        cd = CircularDeque(list(range(50)), 50)
        self.assertEqual(50, len(cd))

    def test_is_empty(self):
        cd = CircularDeque()
        self.assertTrue(cd.is_empty())

        cd = CircularDeque([1])
        self.assertFalse(cd.is_empty())

        cd = CircularDeque([1, 2])
        self.assertFalse(cd.is_empty())

        cd = CircularDeque(list(range(50)), 50)
        self.assertFalse(cd.is_empty())

    def test_front_element(self):
        cd = CircularDeque()
        self.assertIsNone(cd.front_element())

        cd = CircularDeque([1])
        self.assertEqual(1, cd.front_element())
        cd.front = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.front_element())

        cd = CircularDeque([2, 1])
        self.assertEqual(2, cd.front_element())
        cd.front = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.front_element())

        cd = CircularDeque(list(range(50)), 50)
        self.assertFalse(cd.is_empty())
        self.assertEqual(0, cd.front_element())
        cd.front = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.front_element())

    def test_back_element(self):
        cd = CircularDeque()
        self.assertIsNone(cd.back_element())

        cd = CircularDeque([1])
        self.assertEqual(1, cd.back_element())
        cd.back = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.back_element())

        cd = CircularDeque([1, 2])
        self.assertEqual(2, cd.back_element())
        cd.back = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.back_element())

        cd = CircularDeque(list(range(50)), 50)
        self.assertFalse(cd.is_empty())
        self.assertEqual(49, cd.back_element())
        cd.back = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.back_element())

    def test_enqueue_basic(self):# (1) empty queue
        # (1a) front_enqueue
        for capacity in range(4, 50):
            for front in range(capacity):
                cd = CircularDeque(list(range(capacity)), capacity)
                cd.size = 0
                cd.front = cd.back = front
                cd.front_enqueue(1000)
                self.assertIn(1000, cd.queue)
                self.assertEqual(1, cd.queue.count(1000))
                self.assertEqual(cd.back, cd.front)
                self.assertEqual(1, cd.size)

        # (1b) back_enqueue
        for capacity in range(4, 50):
            for front in range(capacity):
                cd = CircularDeque(list(range(capacity)), capacity)
                cd.size = 0
                cd.front = cd.back = front
                cd.back_enqueue(1000)
                self.assertIn(1000, cd.queue)
                self.assertEqual(1, cd.queue.count(1000))
                self.assertEqual(cd.back, cd.front)
                self.assertEqual(1, cd.size)

        # (2) front_enqueue basics
        for capacity in range(4, 50):
            for front in range(capacity):
                for back in range(capacity):  # So grow isn't called upon
                    if front == back:  # Skip, means queue is empty
                        continue
                    list_representation = list(range(capacity))
                    size = back - front + 1 if front < back else capacity - (front - back)
                    if size == capacity - 1:  # Skip, means adding to the queue will make the queue full and then grow
                        continue
                    cd = CircularDeque(list(range(capacity)), capacity)
                    cd.front = front
                    cd.back = back
                    cd.size = size
                    cd.front_enqueue(1000)
                    list_representation[(front - 1) % capacity] = 1000
                    self.assertEqual(list_representation, cd.queue)
                    self.assertEqual((front - 1) % capacity, cd.front)
                    self.assertEqual(back, cd.back)
                    self.assertEqual(size + 1, cd.size)

        # (3) back_enqueue basics
        for capacity in range(4, 50):
            for front in range(capacity):
                for back in range(capacity - 1):  # So grow isn't called upon
                    if front == back:  # Skip, means queue is empty
                        continue
                    list_representation = list(range(capacity))
                    size = back - front + 1 if front < back else capacity - (front - back)
                    if size == capacity - 1:  # Skip, means adding to the queue will make the queue full and then grow
                        continue
                    cd = CircularDeque(list(range(capacity)), capacity)
                    cd.front = front
                    cd.back = back
                    cd.size = size
                    cd.back_enqueue(1000)
                    list_representation[back + 1] = 1000
                    self.assertEqual(list_representation, cd.queue)
                    self.assertEqual(front, cd.front)
                    self.assertEqual((back + 1) % capacity, cd.back)
                    self.assertEqual(size + 1, cd.size)

    def test_front_enqueue(self):
        cd = CircularDeque()
        for element in range(50):
            cd.front_enqueue(element)
        self.assertEqual(list(range(31, -1, -1)) + [None] * 14 + list(range(49, 31, -1)), cd.queue)

        cd = CircularDeque()
        for element in range(64):
            cd.front_enqueue(element)
        self.assertEqual(list(range(63, -1, -1)) + [None] * 64, cd.queue)

    def test_back_enqueue(self):
        cd = CircularDeque()
        for element in range(50):
            cd.back_enqueue(element)
        self.assertEqual(list(range(50)) + [None] * 14, cd.queue)

        cd = CircularDeque()
        for element in range(64):
            cd.back_enqueue(element)
        self.assertEqual(list(range(64)) + [None] * 64, cd.queue)

    def test_dequeue_basic(self):
        """
        Testing dequed values from any valid CircularQueue configuration.
        :return: None
        """
        def Test_CQ_dequeue_front(cd, ans, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    self.assertEqual(ans[i - 1], cd.front_dequeue())  # dequeued proper element

                # checks
                self.assertEqual(size, cd.size)  # check decrement size

        def Test_CQ_dequeue_back(cd, ans, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    self.assertEqual(ans[-1 * i], cd.back_dequeue())  # dequeued proper element

                # checks
                self.assertEqual(size, cd.size)  # check decrement size

        # Test 1
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 2
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 3
        size, cap = 10, 11
        queue = [10, 11, 12, 13, 14, 15, 16, 17, 18, None, 20]
        front, back = 10, 8

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 4
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 5
        size, cap = 15, 20
        queue = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None, None, None, None, None, 32, 33]
        front, back = 18, 12

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 6
        size, cap = 15, 20
        queue = [None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, None, None]
        front, back = 2, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 7
        size, cap = 20, 31
        queue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, None, None, None, None, None, None,
                 None, None, None, None, None, 46, 47, 48]
        front, back = 28, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

    def test_back_dequeue(self):
        """
        Testing wrapping, resizing, capacity, front, back, size, enquing, dequing
        :return: None
        """
        def Check_CQ(ans, size, front, back, cap, cd, b, f=0):
            # checks
            self.assertEqual(size, cd.size)  # check decrement size
            self.assertEqual(size, len(cd))  # check decrement size
            self.assertEqual(back, cd.back)
            self.assertEqual(front, cd.front)  # Front wraps around back of queue
            if size != 0:
                self.assertEqual(ans[f], cd.front_element())
                self.assertEqual(ans[-1 * b - 1], cd.back_element())
            else:
                self.assertEqual(None, cd.front_element())  # empty
                self.assertEqual(None, cd.back_element())  # empty
            self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals

        def Test_CQ_dequeue_back(cd, ans, front, back, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    if size <= cap // 4 and cap // 2 >= 4:  # if shrink
                        cap //= 2
                        front = 0  # reset front
                        back = size - 1  # back same until cd shrunk
                    else:
                        back = (back - 1) % cap
                    self.assertEqual(ans[-1 * i], cd.back_dequeue())  # dequeued proper element

                # checks
                Check_CQ(ans, size, front, back, cap, cd, b=i, f=0)

        # Test 1
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_back = CircularDeque(queue, cap)
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 3
        size, cap = 10, 11
        queue = [10, 11, 12, 13, 14, 15, 16, 17, 18, None, 20]
        front, back = 10, 8

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 4
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 5
        size, cap = 15, 20
        queue = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None, None, None, None, None, 32, 33]
        front, back = 18, 12

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 6
        size, cap = 15, 20
        queue = [None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, None, None]
        front, back = 2, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 7
        size, cap = 20, 31
        queue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, None, None, None, None,
                 None, None,
                 None, None, None, None, None, 46, 47, 48]
        front, back = 28, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 8
        size, cap = 20, 31
        queue = [None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 None,
                 None, None, None, None, None, None, None]
        front, back = 3, 22

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

    def test_front_dequeue(self):
        """
        Testing wrapping, resizing, capacity, front, back, size, enquing, dequing
        :return: None
        """
        def Check_CQ(ans, size, front, back, cap, cd, b, f=0):
            # checks
            self.assertEqual(size, cd.size)  # check decrement size
            self.assertEqual(size, len(cd))  # check decrement size
            self.assertEqual(back, cd.back)
            self.assertEqual(front, cd.front)  # Front wraps around back of queue
            if size != 0:
                self.assertEqual(ans[f], cd.front_element())
                self.assertEqual(ans[-1 * b - 1], cd.back_element())
            else:
                self.assertEqual(None, cd.front_element())  # empty
                self.assertEqual(None, cd.back_element())  # empty
            self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals

        def Test_CQ_dequeue_front(cd, ans, front, back, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    if size <= cap // 4 and cap // 2 >= 4:  # if shrink
                        cap //= 2
                        front = 0  # reset front
                        back = size - 1  # back same until cd shrunk
                    else:
                        front = (front + 1) % cap
                    self.assertEqual(ans[i - 1], cd.front_dequeue())  # dequeued proper element

                # checks
                Check_CQ(ans, size, front, back, cap, cd, b=0, f=i)

        # Test 1
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 3
        size, cap = 10, 11
        queue = [10, 11, 12, 13, 14, 15, 16, 17, 18, None, 20]
        front, back = 10, 8

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 4
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 5
        size, cap = 15, 20
        queue = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None, None, None, None, None, 32, 33]
        front, back = 18, 12

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 6
        size, cap = 15, 20
        queue = [None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, None, None]
        front, back = 2, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 7
        size, cap = 20, 31
        queue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, None, None, None, None,
                 None, None,
                 None, None, None, None, None, 46, 47, 48]
        front, back = 28, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 8
        size, cap = 20, 31
        queue = [None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 None,
                 None, None, None, None, None, None, None]
        front, back = 3, 22

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

    def test_grow(self):
        """
        Tests capacity and values of list while growing
        :return: None
        """
        r_sz = 100
        r_data = [random.randint(-1000, 1000) for val in range(r_sz)]

        # Checks grow via checking new capacity, that the list has been
        # extended, and that the data is properly ordered.
        # Checks ordering by offsetting data so that it can leverage
        # and test circular property without relying on
        # dequeue and enqueue methods.
        cap = 4
        amnt = 6  # log(len(data))
        for offset in range(1, amnt):
            queue = [r_data[j % cap]  # wraps to mimic circularity
                     for j in range((3 * offset), cap + (3 * offset))]

            cd = CircularDeque(queue, cap)  # Fill cd to max capacity
            cd.front, cd.back = (cap + cap - (3 * offset)) % cap, (cap + cap - (3 * offset) - 1) % cap  # correct circular

            queue = r_data[0:cap]  # correct queue order
            queue.extend([None] * cap)  # grow list

            cd.grow()
            cap *= 2  # new expected capacity

            self.assertEqual(cap, cd.capacity)  # check capacity is growing
            self.assertEqual(cd.queue, queue)  # check reordered data like expected

    def test_shrink(self):
        """
        Tests capacity and values of list while shrinking
        :return: None
        """

        r_sz = 100
        r_data = [random.randint(-1000, 1000) for val in range(r_sz)]
        cd = CircularDeque()

        # Checks grow via checking new capacity, that the list has been
        # extended, and that the data is properly ordered.
        # Checks ordering by offsetting data so that it can leverage
        # and test circular property without relying on
        # dequeue and enqueue methods.
        amnt = 6  # log(len(data))
        cap = (2 ** (amnt + 2))  # max capacity
        for offset in range(1, amnt):
            queue = [r_data[(j + (3 * offset)) % (cap // 4)]  # wraps pivot at i in rdata
                     if not (((cap // 4) - (3 * offset)) < j < cap - (3 * offset))  # left shifted
                     else None  # None between start and end
                     for j in range(0, cap)]  # cap * 4 works w/ j % cap
            cd = CircularDeque(queue, cap)  # Fill cd to 1/4 capacity
            cd.front = (cap + cap - (3 * offset)) % cap  # i ints wrapped around
            cd.back = (cap + cap // 4 - (3 * offset) - 1) % cap  # size - i not wrapped
            cd.size //= 4

            queue = r_data[0:(cap // 4)]  # correct queue order
            queue.extend([None] * (cap // 4))  # add extra space

            cd.shrink()
            cap //= 2  # new expected capacity

            self.assertEqual(cap, cd.capacity)  # check capacity is growing
            self.assertEqual(cd.queue, queue)  # check reordered data like expected

    def test_comprehensive(self):
        """
        Testing wrapping, resizing, capacity, front, back, size, enquing, dequing
        :return: None
        """

        def Check_CQ(ans, size, front, back, cap, cd, b, f=0):
            # checks
            self.assertEqual(size, cd.size)  # check decrement size
            self.assertEqual(size, len(cd))  # check decrement size
            self.assertEqual(back, cd.back)
            self.assertEqual(front, cd.front)  # Front wraps around back of queue
            if size != 0:
                self.assertEqual(ans[f], cd.front_element())
                self.assertEqual(ans[-1 * b - 1], cd.back_element())
            else:
                self.assertEqual(None, cd.front_element())  # empty
                self.assertEqual(None, cd.back_element())  # empty
            self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals

        # dequeing comprehensive
        # (1) front_dequeue without shrink
        for case in range(1, 20):
            for dir in range(-1, 2, 2):  # -1 then 1 : for bidirectional wraparound
                if case == 0 and dir == 1:
                    continue  # skip bc dir * 0 = same test as before
                # -- All initialization --
                # determines properties of cd - set difficulty
                base = 4 + (case - 1)  # base capacity changes, starts at 4 and increases
                offset = case - 1

                cap = base * case + abs(offset)  # sum size + offset bounded by cap
                size = cap - floor(cap / 13) * case - abs(offset)//3

                # generate a circular queue in a particular state depending on inputs.
                state = QueueStateMachine(cap, size, dir, offset)
                # print(state.queue)        # Uncomment this line to see what the state looks like

                # Generate starter CircularDeque
                cd = state.create_queue()
                front, back = state.front, state.back

                for i in range(size + 1):
                    if i > 0:  # checks initial list before dequeing
                        size -= 1
                        if size <= cap // 4 and cap // 2 >= 4:  # if shrink
                            cap //= 2
                            front = 0  # reset front
                            back = size - 1  # back same until cd shrunk
                        else:
                            front = (front + 1) % cap

                        self.assertEqual(state.get_front_val(i), cd.front_dequeue())  # dequeued proper element
                        self.assertEqual(front, cd.front)

                    # checks
                    self.assertEqual(size, cd.size)  # check d
                    # ecrement size
                    self.assertEqual(size, len(cd))  # check decrement size
                    self.assertEqual(back, cd.back)
                    self.assertEqual(front, cd.front)  # Front wraps around back of queue
                    if size != 0:
                        self.assertEqual(state.get_back_val(1), cd.back_element())
                        self.assertEqual(state.get_front_val(i + 1), cd.front_element())
                    else:
                        self.assertEqual(None, cd.front_element())  # empty
                        self.assertEqual(None, cd.back_element())  # empty
                    self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals

        # (2) back_dequeue without shrink
        for case in range(1, 20):
            for dir in range(-1, 2, 2):  # -1 then 1 : for bidirectional wraparound
                if case == 0 and dir == 1:
                    continue  # skip bc dir * 0 = same test as before
                # -- All initialization --
                # determines properties of cd - set difficulty
                base = 4 + (case - 1)  # base capacity changes, starts at 4 and increases
                offset = case - 1

                cap = base * case + abs(offset)  # sum size + offset bounded by cap
                size = cap - floor(cap / 13) * case - abs(offset)//4

                # generate a circular queue in a particular state depending on inputs.
                state = QueueStateMachine(cap, size, dir, offset)
                # print(state.queue)        # Uncomment this line to see what the state looks like

                # Generate starter CircularDeque
                cd = state.create_queue()
                front, back = state.front, state.back

                for i in range(size + 1):
                    if i > 0:  # checks initial list before dequeing
                        size -= 1
                        if size <= cap // 4 and cap // 2 >= 4:  # if shrink
                            cap //= 2
                            front = 0  # reset front
                            back = size - 1  # back same until cd shrunk
                        else:
                            back = (back - 1) % cap

                        self.assertEqual(state.get_back_val(i), cd.back_dequeue())  # dequeued proper element
                        self.assertEqual(back, cd.back)

                    # checks
                    self.assertEqual(size, cd.size)  # check decrement size
                    self.assertEqual(size, len(cd))  # check decrement size
                    self.assertEqual(back, cd.back)
                    self.assertEqual(front, cd.front)  # Front wraps around back of queue
                    if size != 0:
                        self.assertEqual(state.get_front_val(1), cd.front_element())
                        self.assertEqual(state.get_back_val(i + 1), cd.back_element())
                    else:
                        self.assertEqual(None, cd.front_element())  # empty
                        self.assertEqual(None, cd.back_element())  # empty
                    self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals


        # Initialze State
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd = CircularDeque(queue, cap)
        cd.front, cd.back, cd.size = front, back, size

        # Test enqueuing from state
        for i in range(35):
            cd.back_enqueue(i * 23)
            if i % (i + 5 // 4) == 0:
                cd.front_enqueue(i * 17)

        # Test dequeuing
        ans = [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322,
               345, 368, 391, 414, 437, 460, 483, 506, 529, 552, 575, 598, 621, 644, 667, 690, 713, 736, 759, 782]
        size = 46
        capacity = 88
        self.assertEqual(capacity, cd.capacity)
        for i in range(10):
            self.assertEqual(size, len(cd))
            self.assertEqual(ans[i], cd.front_dequeue())
            size -= 1

            self.assertEqual(size, len(cd))
            self.assertEqual(ans[-1 * (i + 1)], cd.back_dequeue())
            size -= 1

        self.assertEqual(size, len(cd))
        self.assertEqual(capacity, cd.capacity)
        self.assertEqual(10, cd.front)
        self.assertEqual(12, cd.front_element())

        # test enqueing
        for i in range(35):
            cd.back_enqueue(i * 23)
            if i % (i + 5 // 4) == 0:
                cd.front_enqueue(i * 17)

        self.assertEqual(62, len(cd))
        self.assertEqual(88, cd.capacity)
        self.assertEqual(9, cd.front)
        self.assertEqual(70, cd.back)
        self.assertEqual(782, cd.back_element())


    def test_application_comprehensive(self):
        """
        Testing application comprehensive
        :return: None
        """
        # Test Application
        result = LetsPassTrains102("")
        self.assertEqual("", result[1])
        self.assertEqual(eval("0"), result[0])

        result = LetsPassTrains102("111111")
        self.assertEqual("111111", result[1])
        self.assertEqual(eval("111111"), result[0])

        result = LetsPassTrains102("(0.6 / 2) / (1 / 3)")
        self.assertEqual("0.6 2 / 1 3 / /", result[1])
        self.assertEqual(eval("(0.6 / 2) / (1 / 3)"), result[0])

        result = LetsPassTrains102("(0.6 / 0.3) / (1 / 3)")
        self.assertEqual("0.6 0.3 / 1 3 / /", result[1])
        self.assertEqual(eval("(0.6 / 0.3) / (1 / 3)"), result[0])

        result = LetsPassTrains102("5 + 87 + 47 - 0")
        self.assertEqual("5 87 + 47 + 0 -", result[1])
        self.assertEqual(eval("5 + 87 + 47 - 0"), result[0])

        result = LetsPassTrains102("4 + 4 + 8 + 8")
        self.assertEqual("4 4 + 8 + 8 +", result[1])
        self.assertEqual(eval("4 + 4 + 8 + 8"), result[0])

        result = LetsPassTrains102("23 - 2 - 8")
        self.assertEqual("23 2 - 8 -", result[1])
        self.assertEqual(eval("23 - 2 - 8"), result[0])

        result = LetsPassTrains102("0 + 0")
        self.assertEqual("0 0 +", result[1])
        self.assertEqual(eval("0 + 0"), result[0])

        result = LetsPassTrains102("-1 - - 1")
        self.assertEqual("-1 - 1 -", result[1])
        self.assertEqual(eval("-1 - - 1"), result[0])

        result = LetsPassTrains102("6 - 16 + 3")
        self.assertEqual("6 16 - 3 +", result[1])
        self.assertEqual(eval("6 - 16 + 3"), result[0])

        # 1b: *, /
        result = LetsPassTrains102("36 / 6")
        self.assertEqual("36 6 /", result[1])
        self.assertEqual(int(eval("-36 / -6")), result[0])

        # 1d : *, /, +, -, ^
        result = LetsPassTrains102("4 ^ 2")
        self.assertEqual("4 2 ^", result[1])
        self.assertEqual(eval("4 ** 2"), result[0])

        # 2 : parenthesese
        result = LetsPassTrains102("(43 - 5) + 3")
        self.assertEqual("43 5 - 3 +", result[1])
        self.assertEqual(eval("(43 - 5) + 3"), result[0])

        result = LetsPassTrains102("-36 / -6")
        self.assertEqual("-36 -6 /", result[1])
        self.assertEqual(eval("-36 / -6"), result[0])

        result = LetsPassTrains102("2 * 98 * 6")
        self.assertEqual("2 98 * 6 *", result[1])
        self.assertEqual(eval("2 * 98 * 6"), result[0])

        result = LetsPassTrains102("4 * 0")
        self.assertEqual("4 0 *", result[1])
        self.assertEqual(eval("4 * 0"), result[0])

        result = LetsPassTrains102("3 / 3")
        self.assertEqual("3 3 /", result[1])
        self.assertEqual(eval("3 / 3"), result[0])

        result = LetsPassTrains102("64 / 8 * 5")
        self.assertEqual("64 8 / 5 *", result[1])
        self.assertEqual(eval("64 / 8 * 5"), result[0])

        # 1c : *, /, +, -
        result = LetsPassTrains102("44 / 4 - 71 * 39")
        self.assertEqual("44 4 / 71 39 * -", result[1])
        self.assertEqual(eval("44 / 4 - 71 * 39"), result[0])

        result = LetsPassTrains102("11 + 41 + 90 / 10")
        self.assertEqual("11 41 + 90 10 / +", result[1])
        self.assertEqual(eval("11 + 41 + 90 / 10"), result[0])

        result = LetsPassTrains102("4 + 38 * 81 * 35 * 41 - 61 / 1")
        self.assertEqual("4 38 81 * 35 * 41 * + 61 1 / -", result[1])
        self.assertEqual(eval("4 + 38 * 81 * 35 * 41 - 61 / 1"), result[0])

        # 1d : *, /, +, -, ^
        result = LetsPassTrains102("4 ^ 2")
        self.assertEqual("4 2 ^", result[1])
        self.assertEqual(eval("4 ** 2"), result[0])

        result = LetsPassTrains102("-5 - 5 / 1 - 3 ^ 5")
        self.assertEqual("-5 5 1 / - 3 5 ^ -", result[1])
        self.assertEqual(round(eval("-5 - 5 / 1 - 3 ** 5"), 5), round(result[0], 5))

        result = LetsPassTrains102("4 ^ 0 + 38 ^ 0 * 81 ^ 0 * 35 ^ 0 * 41 ^ 0 - 61 ^ 0  / 1 ^ 0")
        self.assertEqual("4 0 ^ 38 0 ^ 81 0 ^ * 35 0 ^ * 41 0 ^ * + 61 0 ^ 1 0 ^ / -", result[1])
        self.assertEqual(eval("4 ** 0 + 38 ** 0 * 81 ** 0 * 35 ** 0 * 41 ** 0 - 61 ** 0  / 1 ** 0"), result[0])

        result = LetsPassTrains102("4 * 0 ^ 0")
        self.assertEqual("4 0 0 ^ *", result[1])
        self.assertEqual(eval("4 * 0 ** 0"), result[0])

        result = LetsPassTrains102("4 ^ -2")
        self.assertEqual("4 -2 ^", result[1])
        self.assertEqual(eval("4 ** -2"), result[0])

        result = LetsPassTrains102("4 ^ 0.5")
        self.assertEqual("4 0.5 ^", result[1])
        self.assertEqual(eval("4 ** 0.5"), result[0])

        result = LetsPassTrains102("((4 ^ 0.5) / -2) * 3000")
        self.assertEqual("4 0.5 ^ -2 / 3000 *", result[1])
        self.assertEqual(eval("((4 ** 0.5) / -2) * 3000"), result[0])

        # 2 : parenthesese

        result = LetsPassTrains102("6 * (50 - 50)")
        self.assertEqual("6 50 50 - *", result[1])
        self.assertEqual(eval("6 * (50 - 50)"), result[0])

        result = LetsPassTrains102("(6 * 50) - 50")
        self.assertEqual("6 50 * 50 -", result[1])
        self.assertEqual(eval("(6 * 50) - 50"), result[0])

        result = LetsPassTrains102("(23 ^ 10)")
        self.assertEqual("23 10 ^", result[1])
        self.assertEqual(eval("(23 ** 10)"), result[0])

        result = LetsPassTrains102("(23 ^ 10) ^ 0")
        self.assertEqual("23 10 ^ 0 ^", result[1])
        self.assertEqual(eval("(23 ** 10) ** 0"), result[0])

        result = LetsPassTrains102("(43 - 5) + 3")
        self.assertEqual("43 5 - 3 +", result[1])
        self.assertEqual(eval("(43 - 5) + 3"), result[0])

        result = LetsPassTrains102("((100) ^ 10) / 10")
        self.assertEqual("100 10 ^ 10 /", result[1])
        self.assertEqual(eval("((100) ** 10) / 10"), result[0])

    def test_application(self):
        #   1a : +, -
        result = LetsPassTrains102("8 + 3")
        self.assertEqual("8 3 +", result[1])
        self.assertEqual(eval("8 + 3"), result[0])

        result = LetsPassTrains102("-67 - 46")
        self.assertEqual("-67 46 -", result[1])
        self.assertEqual(eval("-67 - 46"), result[0])

        result = LetsPassTrains102("8 - 5")
        self.assertEqual("8 5 -", result[1])
        self.assertEqual(eval("8 - 5"), result[0])

        result = LetsPassTrains102("7 + -3 - 2 - 3 - 8 + -3 - 2 + 50 + 46 + -35 + -13 - 9 - 100")
        self.assertEqual("7 -3 + 2 - 3 - 8 - -3 + 2 - 50 + 46 + -35 + -13 + 9 - 100 -", result[1])
        self.assertEqual(eval("7 + -3 - 2 - 3 - 8 + -3 - 2 + 50 + 46 + -35 + -13 - 9 - 100"), result[0])

        result = LetsPassTrains102("0 + 15 + 57 - 8")
        self.assertEqual("0 15 + 57 + 8 -", result[1])
        self.assertEqual(eval("0 + 15 + 57 - 8"), result[0])

        result = LetsPassTrains102("5 + 4 - 5 - 95 - 85 - 90 - 8")
        self.assertEqual("5 4 + 5 - 95 - 85 - 90 - 8 -", result[1])
        self.assertEqual(eval("5 + 4 - 5 - 95 - 85 - 90 - 8"), result[0])

        result = LetsPassTrains102("7 - 2")
        self.assertEqual("7 2 -", result[1])
        self.assertEqual(eval("7 - 2"), result[0])

        result = LetsPassTrains102("5 + 87 + 47 - 0")
        self.assertEqual("5 87 + 47 + 0 -", result[1])
        self.assertEqual(eval("5 + 87 + 47 - 0"), result[0])

        result = LetsPassTrains102("4 + 4 + 8 + 8")
        self.assertEqual("4 4 + 8 + 8 +", result[1])
        self.assertEqual(eval("4 + 4 + 8 + 8"), result[0])

        result = LetsPassTrains102("23 - 2 - 8")
        self.assertEqual("23 2 - 8 -", result[1])
        self.assertEqual(eval("23 - 2 - 8"), result[0])

        result = LetsPassTrains102("0 + 0")
        self.assertEqual("0 0 +", result[1])
        self.assertEqual(eval("0 + 0"), result[0])

        result = LetsPassTrains102("-1 - - 1")
        self.assertEqual("-1 - 1 -", result[1])
        self.assertEqual(eval("-1 - - 1"), result[0])

        result = LetsPassTrains102("6 - 16 + 3")
        self.assertEqual("6 16 - 3 +", result[1])
        self.assertEqual(eval("6 - 16 + 3"), result[0])

        # 1b: *, /
        result = LetsPassTrains102("36 / 6")
        self.assertEqual("36 6 /", result[1])
        self.assertEqual(int(eval("-36 / -6")), result[0])

        # 1d : *, /, +, -, ^
        result = LetsPassTrains102("4 ^ 2")
        self.assertEqual("4 2 ^", result[1])
        self.assertEqual(eval("4 ** 2"), result[0])

        # 2 : parenthesese
        result = LetsPassTrains102("(43 - 5) + 3")
        self.assertEqual("43 5 - 3 +", result[1])

        result = LetsPassTrains102("-36 / -6")
        self.assertEqual("-36 -6 /", result[1])

        result = LetsPassTrains102("2 * 98 * 6")
        self.assertEqual("2 98 * 6 *", result[1])
        self.assertEqual(eval("2 * 98 * 6"), result[0])

        result = LetsPassTrains102("4 * 0")
        self.assertEqual("4 0 *", result[1])
        self.assertEqual(eval("4 * 0"), result[0])

        result = LetsPassTrains102("3 / 3")
        self.assertEqual("3 3 /", result[1])
        self.assertEqual(eval("3 / 3"), result[0])

        result = LetsPassTrains102("64 / 8 * 5")
        self.assertEqual("64 8 / 5 *", result[1])
        self.assertEqual(eval("64 / 8 * 5"), result[0])

        # 1c : *, /, +, -
        result = LetsPassTrains102("44 / 4 - 71 * 39")
        self.assertEqual("44 4 / 71 39 * -", result[1])

        result = LetsPassTrains102("11 + 41 + 90 / 10")
        self.assertEqual("11 41 + 90 10 / +", result[1])
        self.assertEqual(eval("11 + 41 + 90 / 10"), result[0])

        result = LetsPassTrains102("4 + 38 * 81 * 35 * 41 - 61 / 1")
        self.assertEqual("4 38 81 * 35 * 41 * + 61 1 / -", result[1])

        # 1d : *, /, +, -, ^
        result = LetsPassTrains102("4 ^ 2")
        self.assertEqual("4 2 ^", result[1])
        self.assertEqual(eval("4 ** 2"), result[0])

        result = LetsPassTrains102("-5 - 5 / 1 - 3 ^ 5")
        self.assertEqual("-5 5 1 / - 3 5 ^ -", result[1])
        self.assertEqual(round(eval("-5 - 5 / 1 - 3 ** 5"), 5), round(result[0], 5))

        result = LetsPassTrains102("4 ^ 0 + 38 ^ 0 * 81 ^ 0 * 35 ^ 0 * 41 ^ 0 - 61 ^ 0  / 1 ^ 0")
        self.assertEqual("4 0 ^ 38 0 ^ 81 0 ^ * 35 0 ^ * 41 0 ^ * + 61 0 ^ 1 0 ^ / -", result[1])

        result = LetsPassTrains102("4 * 0 ^ 0")
        self.assertEqual("4 0 0 ^ *", result[1])

        result = LetsPassTrains102("4 ^ -2")
        self.assertEqual("4 -2 ^", result[1])
        self.assertEqual(eval("4 ** -2"), result[0])

        result = LetsPassTrains102("4 ^ 0.5")
        self.assertEqual("4 0.5 ^", result[1])

        result = LetsPassTrains102("((4 ^ 0.5) / -2) * 3000")
        self.assertEqual("4 0.5 ^ -2 / 3000 *", result[1])

        # 2 : parenthesese
        result = LetsPassTrains102("6 * (50 - 50)")
        self.assertEqual("6 50 50 - *", result[1])
        self.assertEqual(eval("6 * (50 - 50)"), result[0])

        result = LetsPassTrains102("(6 * 50) - 50")
        self.assertEqual("6 50 * 50 -", result[1])
        self.assertEqual(eval("(6 * 50) - 50"), result[0])

        result = LetsPassTrains102("(23 ^ 10)")
        self.assertEqual("23 10 ^", result[1])

        result = LetsPassTrains102("(23 ^ 10) ^ 0")
        self.assertEqual("23 10 ^ 0 ^", result[1])
        self.assertEqual(eval("(23 ** 10) ** 0"), result[0])

        result = LetsPassTrains102("(43 - 5) + 3")
        self.assertEqual("43 5 - 3 +", result[1])
        self.assertEqual(eval("(43 - 5) + 3"), result[0])

        result = LetsPassTrains102("((100) ^ 10) / 10")
        self.assertEqual("100 10 ^ 10 /", result[1])
        self.assertEqual(eval("((100) ** 10) / 10"), result[0])


class QueueStateMachine:
    """
    This class is used to generate a CircularDeque at a particular state.
    This implementation does not support changing states. You must instead regenerate any states,
    or query the data structure for its values at a particular index (state).
    """
    r_data = [random.randint(-1000, 1000) for val in range(100)]

    def __init__(self, cap, size, dir, offset, is_dequeing=True, r_data=r_data):
        """
        Initialize
        :param cap: CircularDeque capacity
        :param size: size
        :param dir: direction of offset
        :param offset: offset
        :param is_dequeing: Is the queue being used to test dequeing
        :param r_data: Data to use when generating state
        """
        # attributes
        self.cap = cap
        self.size = size
        self.dir = dir
        self.offset = offset
        self.total_off = dir * offset

        # data
        self.data = r_data
        self.queue = self.gen_data(self.size, self.cap, r_data)

        # queue positioning
        self.front = None
        self.back = None

        self.is_dequeing = is_dequeing  # Changes scope of data

    def gen_data(self, size, cap, data: list):
        """
        Generates imitation of a circular queue
        :param offset: index of starting item. Negative wraps to back, positve to front.
        :param size: Amount of valid data in list
        :param cap: Full Capacity of list
        :return: List imitating a circular queue
        """
        if cap < size + abs(self.offset):
            while(cap < size + abs(self.offset)):
                size = size//2 + size//16
        elif size == 0:
            return [None] * self.cap

        return [data[(j + self.total_off % size) % len(data)]  # + offset to ensures same order as rdata
                if ((
                                cap + self.total_off <= j or j < size + self.total_off)  # allows offset wrap backwards (neg offset)
                    and (j >= self.total_off))  # allows offset at front (pos offset)
                else None  # fills black space so len = capacity
                for j in range(0, cap)]

    def front_i(self, ind):
        """
        Index of first element in state queue based on current state
        :param ind: state
        :return:
        """
        # transforms to proper index in source data list
        if self.is_dequeing:
            return (self.cap + self.total_off + ind - 1) % self.cap

    def back_i(self, ind):
        """
        Index of last element in state queue based on current state
        :param ind: state
        :return:
        """
        # transforms to proper index in source data list
        if self.is_dequeing:
            return (self.cap + self.size + self.total_off - ind) % self.cap

    def create_queue(self, is_dequeing=None) -> CircularDeque:
        """
        Creates a CircularDeque at a particular state
        :param is_dequeing:
        :return:
        """
        if is_dequeing is not None:
            self.is_dequeing = is_dequeing

        cd = CircularDeque(self.queue, self.cap)
        self.front = (self.cap + self.total_off) % self.cap  # front w/ offset and wrapping
        self.back = (self.size - 1 + self.total_off) % self.cap  # back at size w/ offset and wrapping
        cd.front, cd.back, cd.size = self.front, self.back, self.size
        return cd

    def get_back_val(self, i):
        return self.queue[self.back_i(i)]

    def get_front_val(self, i):
        return self.queue[self.front_i(i)]


if __name__ == '__main__':
    unittest.main()
