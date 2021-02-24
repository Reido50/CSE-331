Project 4: Circular Deques
==========================

**Due: Friday, February 26th @ 11:59pm EST**

*This is not a team project, do not copy someone else’s work.*

*![CircularDeque.png](https://s3.amazonaws.com/mimirplatform.production/files/ee009eaf-1d8b-4a24-8e62-722a6db1ef29/CircularDeque.png)*

Assignment Overview
-------------------

In a typical FIFO (First in First out) queue, elements are added to one
end of the underlying structure, and removed from the opposite. These
are natural for storing sequences of instructions: Imagine that
instructions are added to the queue when first processed, and removed
when completed. The first instruction processed will also be the first
completed - we add it to the front, and remove it from the back.

A deque is a [double-ended
queue](https://en.wikipedia.org/wiki/Double-ended_queue), meaning
elements can be added or removed from either end of the queue. This
generalizes the behavior described above to account for more complex
usage scenarios. The ability to add or remove from both ends of the
deque allows the structure to be used as both a FIFO queue, and a LIFO
stack, simultaneously.

This structure is useful for storing undo operations, where more recent
undos are pushed and popped from the top of the deque and old/expired
undos are removed from the back of the deque. Trains, consisting of
sequences of cars, can also be thought of as a deques: cars can be added
or removed from either end, but never the middle.

A circular queue is a queue of fixed size with end-to-end connections.
This is a way to save memory as deleted elements in the queue can simply
be overwritten. In the picture above at index 0, the element 1 has been
removed (dequeued) from the queue but the value remains. If two new
values are enqueued, then that 1 will be overwritten. After this, the
circular queue will have reached capacity, and need to grow.

Circular queues are useful in situations with limited memory. Consider a
router in an internet network. A package (a set of bits sent across the
network) is sent to this router and it joins the router's processing
queue. This router can only hold so many packets before it has to start
dropping some. A circular queue would be useful here, as it optimizes
memory usage.

A circular deque is a combination of a deque and a circular queue. It
sets a max size and can grow and shrink like a circular queue, and it
can enqueue/dequeue from both ends. This is what you will be
implementing in this project.

Assignment Notes
----------------

-   The use of [modulo
    (%)](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
    is highly recommended
-   Understand what [amortized
    runtime](https://medium.com/@satorusasozaki/amortized-time-in-the-time-complexity-of-an-algorithm-6dd9a5d38045)
    is (also explained below)
-   The use of Python's Queues library is **NOT ALLOWED** and will
    result in loss of points
-   The use of .pop() is **PROHIBITED**
    -   .pop(x) has a runtime of *O(n-x)*, where *n* is the length of
        the python list .pop(x) is called on - in most situations, this
        will violate time complexity.
-   Fill out the README, easiest 5 points of your life!
    -   Note: Your netid is what comes before the "@msu.edu" in your
        email
        -   email: smithjoh@msu.edu
        -   netid: smithjoh

Assignment Specifications
-------------------------

#### class CircularDeque:

*DO NOT MODIFY the following attributes/functions*

-   **Attributes**
    -   **capacity: int:** the total amount of items that can be placed
        in your circular deque. This grows and shrinks dynamically, but
        is never less than 4. Will always be greater than **size**.
    -   **size: int:** the amount of items currently in your circular
        deque
    -   **queue: list[T]:** The underlying structure holding the data of
        your circular deque. Many elements may be **None**, if your
        current **size** is less than **capacity**. This grows and
        shrinks dynamically.
    -   **front: int:** an index indicating the location of the first
        element in the circular deque
    -   **back: int:** an index indicating the location of the last
        element in your circular deque
-   **\_\_init\_\_(self, data: list[T], capacity: int) -\> None**
    -   Constructs a circular deque
    -   **data: list[T]: **list containing all data to be inserted into
        the circular deque
        -   This is solely used for testing purposes and can be
            considered bad practice. Mutable default arguments may not
            always work as intented (as demonstrated
            [here](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)).
            The default is included so when you create an instance of
            CircularDeque in your application problem, you do not need
            to include an empty list.
        -   [Here](https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/)
            is another link detailing an example and a possible solution
            to problems that can occur with mutable function parameters
    -   **capacity: int: **the capacity of the circular deque
    -   **Returns: **None
-   **\_\_str\_\_(self) -\> str** and **\_\_repr\_\_(self) -\> str**
    -   Represents the circular deque as a string
    -   **Returns: **str

*IMPLEMENT the following functions*

-   **\_\_len\_\_(self) -\> int**
    -   Returns the length/size of the circular deque - this is the
        number of items currently in the circular deque, and will not
        necessarily be equal to the **capacity**
    -   This is a [magic
        method](https://www.tutorialsteacher.com/python/magic-methods-in-python)
        and can be called with **len(object\_to\_measure)**
    -   Time complexity: *O(1)*
    -   Space complexity: *O(1)*
    -   **Returns:** int representing length of the circular deque
-   **is\_empty(self) -\> bool**\
    -   Returns a boolean indicating if the circular deque is empty
    -   Time complexity: *O(1)*
    -   Space complexity: *O(1)*
    -   **Returns:** True if empty, False otherwise
-   **front\_element(self) -\> T**\
    -   Returns the first element in the circular deque
    -   Time complexity: *O(1)*
    -   Space Complexity: *O(1)*
    -   **Returns:** the first element if it exists, otherwise None
-   **back\_element(self) -\> T**\
    -   Returns the last element in the circular deque
    -   Time complexity: *O(1)*
    -   Space complexity: *O(1)*
    -   **Returns:** the last element if it exists, otherwise None
-   **front\_enqueue(self, value: T) -\> None**
    -   Adds value to the front of the circular deque
    -   Will always call **grow() **
    -   **param value: T:** value to add into the circular deque
    -   Time complexity: *O(1)\**
    -   Space complexity: *O(1)\**
    -   **Returns:** None
-   **back\_enqueue(self, value: T) -\> None**\
    -   Adds value to the end of the circular deque
    -   Will always call **grow()**
    -   **param value: T:** value to add into the circular deque
    -   Time complexity: *O(1)\**
    -   Space complexity: *O(1)\**
    -   **Returns: **None
-   **front\_dequeue(self) -\> T**
    -   Removes the item at the front of the circular deque
    -   Will always call **shrink() **
    -   Time complexity: *O(1)\**
    -   Space complexity: *O(1)\**
    -   **Returns: **item at the front of the circular deque, None if
        empty
-   **back\_dequeue(self) -\> T**
    -   Removes the item at the end of the circular deque
    -   Will always call **shrink() **
    -   Time complexity: *O(1)\**
    -   Space complexity: *O(1)\**
    -   **Returns: **item at the end of the circular deque, None if
        empty
-   **grow(self) -\> None**
    -   If the current size is equal to the current capacity, double the
        capacity of the circular deque
    -   Time complexity: *O(n)*
    -   Space complexity: *O(n)*
    -   **Returns: **None
-   **shrink(self) -\> None**
    -   If the current size is less than or equal to one fourth the
        current capacity, and 1/2 the current capacity is greater than
        or equal to 4, halves the capacity.
    -   Will never have a capacity lower than 4, **DO NOT **shrink when
        when shrinking would result in a capacity \<= 4
    -   Time complexity: *O(n)*
    -   Space complexity: *O(n)*
    -   **Returns: **None

\***[Amortized](https://medium.com/@satorusasozaki/amortized-time-in-the-time-complexity-of-an-algorithm-6dd9a5d38045)**.
*Amortized Time Complexity* means 'the time complexity a majority of the
time'. Suppose a function has amortized time complexity *O(f(n))* - this
implies that the majority of the time the function falls into the
complexity class *O(f(n)),*however there may exist situations where the
complexity exceeds *O(f(n)).*The same logic defines the concept
of *Amortized Space Complexity*.

Example:  front\_enqueue(self, value: T)has an amortized time complexity
of *O(1)*: In the majority of situations, enqueueing an element occurs
through a constant number of operations. However, when the Circular
Deque is at capacity, grow(self) is called - this is an
*O(n) *operation, therefore in this particular scenario, front\_enqueue
exceeds its amortized bound.

### Application Overview: *Trains!*
* {.code-line}

![vT2v9NuV7s-temple\_mills\_marshalling\_yard\_2042992\_09382afe.jpg](https://s3.amazonaws.com/mimirplatform.production/files/d27d4132-8823-4e5e-b0a7-4087a830aa7b/vT2v9NuV7s-temple_mills_marshalling_yard_2042992_09382afe.jpg)

This semester, you have enrolled in Trains 101 (a requirement for your
trains cognate). Your attendance, though, has been shabby at best.
Luckily without attending a single lecture, you remember just enough of
*Thomas the Train* and *Polar Express* to earn a 49% on the midterm.
Your professor takes pity and offers you an ultimatum: you may replace
your midterm grade, but in order to do so, you must implement the
[Shunting-yard
Algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).

A [shunting yard](https://en.wikipedia.org/wiki/Classification_yard)
(seen above) is a railway yard, where train cars are
[shunted](https://en.wikipedia.org/wiki/Shunting_(rail)): detached from
engines and split along several tracks for processing.

Computer science giant Edsger Dikstra devised the Shunting-yard for use
in converting
[infix-notation](https://en.wikipedia.org/wiki/Infix_notation) to
[post-fix (or "Reverse Polish")
notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation). The
algorithm named for its visual similarity to railway shunting-yards,
though it has little substantive relation to trains:

*![Screenshot from 2021-02-18
13-37-22.png](https://s3.amazonaws.com/mimirplatform.production/files/7e33112f-509c-49c1-923b-a4f45b0cf180/Screenshot%20from%202021-02-18%2013-37-22.png)*

Though applications in abstract syntax trees and semantics have been
discovered, Dikstra's work was born to reduce computer memory access and
to use the application stack for evaluating expressions.

You'll be doing exactly this: processing mathematical expressions given
in infix notation, converting them to postfix notation, and evaluating
the result.

### **Expectations**:

You will write an algorithm that converts a mathematical expression from
infix to postfix notation. You must then evaluate the expression in
postfix notation.

The following operators are valid:

-   \+ : Add
-   -  : Subtract
-   \* : Multiply
-   / : Divide
-   \^ : Exponent
-   (  : Left parenthesis
-   )  : Right parenthesis

Your converter will have to properly deal with negative numbers. You are
expected to handle negative numbers as shown in the examples below:

-   5 + -3 -\> 5 -3 +
-   (3 + 4) × 5 – 6  -\> 3  4  +  5  ×  6  –

Your converter will also have to properly deal with decimals. An example
is below:

-   "4 \^ 0.5 -\> 4 0.5 \^

### **Function:**

``` {style="background-color: #ffffff; color: #080808; font-family: 'JetBrains Mono',monospace; font-size: 9.8pt;"}
LetsPassTrains102(infix : str) -> Tuple[int, str]:
```

-   Convert a mathematical expression from in-fix notation to post-fix
    notation (also known as Reverse Polish Notation). Then evaluate the
    mathematical expression in postfix notation.
-   You **MUST** use a CircularDeque.
-   You **MUST **evaluate post-fix notation directly, once it has been
    computed. Simply evaluating the infix notation with built-in methods
    will result in loss of points.
-   Time complexity: *O(n)*
-   Space complexity: *O(n)*
-   **Inputs**: string\
    -   string: A valid mathematical expression in infix notation.
-   **Returns:**tuple(int ans, string postfix)
    -   ans: Evaluated expression
    -   postfix: Expression in postfix notation
    -   Example: (3,  "2 2 +")

### Examples (infix -\> postfix):

-   8 + 3 -\> 8 3 +
-   5 + 87 + 47 - 0 -\> 5 87 + 47 + 0 -
-   6 - 16 + 3 -\> 6 16 - 3 +
-   2 \* 98 \* 6 -\> 2 98 \* 6 \*
-   4 \* 0 \^ 0 -\> 4 0 0 \^ \*
-   4 \^ -2 -\> 4 -2 \^

Guarantees/Notes
----------------

-   No division by zero - You don't need to worry about it!
-   All input will be valid:
    -   Matching parentheses
    -   Numbers or operators only
-   Though in-fix notation is natural to the human mind, it is more
    challenging (and thus more time consuming) for a computer to
    evaluate. Post-fix notation can be read in one pass by
    [stack-machines](https://en.wikipedia.org/wiki/Stack_machine), and
    is more easily parsed by compilers/interpreters.

-   There will be a space between all operators (+, -, \*, / , \^) and
    operands (numbers)

Submission
----------

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir
by 11:59p Eastern Time on Friday, 02/26/21.

Your .zip folder can contain other files (for example, description.md
and tests.py), but must include (at least) the following:

``` {.code-line}
|- Project4.zip
    |— Project4/
        |— README.xml          (for project feedback)
        |— __init__.py         (for proper Mimir testcase loading)       
        |— CircularDeque.py    (contains your solution source code)
```

#### **Grading**

The following 100-point rubric will be used to determine your grade on
Project4:

-   Tests (74)
    -   00 - Coding Standard: \_\_/5
    -   01 - len(): \_\_/2
    -   02 - is\_empty: \_\_/2
    -   03 - front\_element: \_\_/2
    -   04 - back\_element: \_\_/2
    -   05 - enqueue withouth grow: \_\_/4
    -   06 - front\_enqueue: \_\_/6
    -   07 - back\_enqueue: \_\_/6
    -   08 - dequeue without shrink: \_\_/4
    -   09 - front\_dequeue: \_\_/6
    -   10 - back\_dequeue: \_\_/6
    -   11 - grow: \_\_/5
    -   12 - shrink: \_\_/5
    -   13 - Circular Deque Comprehensive: \_\_/10
    -   14 - Application: \_\_/4
    -   15 - Application Comprehensive: \_\_/5
-   Manual (26)
    -   M0 - len(): \_\_/0.5
    -   M1 - is\_empty: \_\_/0.5
    -   M2 - front\_element: \_\_/0.5
    -   M3 - back\_element: \_\_/0.5
    -   M4 - front\_enqueue: \_\_/2
    -   M5 - back\_enqueue: \_\_/2
    -   M6 - front\_dequeue: \_\_/2
    -   M7 - back\_dequeue: \_\_/2
    -   M8 - grow: \_\_/3
    -   M9 - shrink: \_\_/3
    -   M10 - application: \_\_/5
    -   `README.xml` is completely filled out with (1) netID, (2)
        Feedback, (3) Time to Completion and (4) Citations: \_\_/5

*This project was created by Angelo Savich, Olivia Mikola, and Andrew
Haas*
