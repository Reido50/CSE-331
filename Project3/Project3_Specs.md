# Project 3: Hybrid Sorting

**Due: Friday, February 19th @ 11:59pm EST**

_This is not a team project, do not copy someone else’s work._

## Assignment Overview

![sorting_complexities.png](https://s3.amazonaws.com/mimirplatform.production/files/c3e7fecd-4807-44e5-bb0d-a41a9dfd2f0c/sorting_complexities.png)

A **sorting algorithm** is an algorithm that puts elements in a [certain order](https://en.wikipedia.org/wiki/Total_order). Such algorithms are often used to organize an array or list in numerical or lexicographical order, however their use is not limited in scope to such simple orderings, or to such simple structures - a fact that will be demonstrated in this project.

Throughout the 20th century, as the domain of problems to which computers were applied grew, so to did the size of data sets that required sorting. This resulted in the rapid development of sorting algorithms. Clearly _O(n<sup>2</sup>) _algorithms, such an selection and bubble sort, were inferior to faster _O(nlog(n))_ algorithms, such as quick or merge sort, but by the 1970s even these weren't achieving speeds desired. This led to the development of ultra-optimized hybrid sorting algorithms, which tie together multiple sorting procedures recursively so as to apply the optimal sort to each chunk of data based on its size.

This project focuses on the _Insertion Sort_ and the _Merge Sort_ algorithms, and on a hybrid of the two. This hybridization is not merely a toy exercise - in fact, Python sorts its built in lists through a [hybrid of merge and insertion sort](https://hg.python.org/cpython/file/tip/Objects/listsort.txt "timsort").

### Insertion Sort

![insertion_sort.png](https://s3.amazonaws.com/mimirplatform.production/files/71bf53c7-b452-46c3-9d3b-84d2da030187/insertion_sort.png)

Insertion sort is an in place comparison based sorting algorithm. It builds a final sorted array by comparing one element at a time and inserting it into it's appropriate location.

The worst case runtime is _O(n^2)_. The best case runtime is linear - in the case that the array is already sorted. The space complexity is O(1) for an in place implementation.

### Merge Sort

![merge_sort.png](https://s3.amazonaws.com/mimirplatform.production/files/5aa69ad1-1cfd-4909-b14f-765027587102/merge_sort.png)

Merge sort is one of the most efficient sorting algorithms. It works on the principle of [Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm). Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element and merges those sublists in a manner that results in a sorted list.

The runtime is _O(nlog(n)) and_ _Theta(nlog(n))_. The space complexity is _O(n)_ - new arrays are created everytime you divide. ([Why isn't the space _O(nlogn)_?](https://stackoverflow.com/a/28641693))

### Hybrid Sort

While Merge Sort has a faster average runtime than Insertion Sort, there are instances that an Insertion Sort is more efficient. Due to the overhead of recursively splitting containers with a Merge Sort, Insertion Sort can have a faster performance with small sets of data. Thus, the two algorithms are often combined, with recursive calls to merge sort ceasing once the data is subdivided into small enough arrays.

## Project Details

### Overview

You will be implementing the Insertion Sort Algorithm and the Merge Sort Algorithm. You will develop your Merge Sort such that it can be used as a Hybrid Sort when given a threshold value. The Hybrid Sort will rely on Merge Sort until the partitioned lists are less than or equal to a given threshold, at which point you will switch to Insertion Sort.

These sorting algorithms will have an optional parameter that accepts a _**callable** -_ an object that can accept its own arguments and can even return its own object. _Callable _is the alias used by python's typing module for a **_Function-_ in Python, functions are objects, and may be passed as arguments to other functions_._** For this project, you will be creating simple functions to pass in as callables, which should determine how your sorting algorithms will sort. The default callable argument to our functions is a lambda function that is intended to sort your objects in the usual increasing order. For the application problem, you may need to create more complex functions that cannot be written as a lambda.

![image0.jpg](https://s3.amazonaws.com/mimirplatform.production/files/424ee552-98e0-490c-9f45-1cd47680d425/image0.jpg)

You'll want to use the above example, _comparator_ to compare each element in the list you are sorting. _comparator_ will only return true if the first parameter passed in, x, is less than or equal to the second parameter passed in, y. To use the comparator shown in the image above in your code, you'd write

<pre class="code-line">if comparator(x, y):    # does the same thing as if x <= y in this case</pre>

In addition to these sorting algorithms, you will be implementing an algorithm to determine the _inversion count_ of a list of elements. This algorithm will be integrated into your merge_sort function. You will only calculate the inversion count when your function is not being used as a Hybrid Sort, that is, when the threshold is 0.

The inversion count is how far away a list of elements is from being sorted. The inversion count of a sorted array is 0\. You can think of the number of inversions as the number of pairs of elements that are out of order.

**Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j**

##### Examples:

**data = [3,2,9,0]**

*   data has 4 inversions:
    *   (3, 2): 3 > 2 but 3 comes before 2
    *   (3, 0): 3 > 0 but 3 comes before 0
    *   (2, 0): 2 > 0 but 2 comes before 0
    *   (9, 0): 9 > 0 but 9 comes before 0

**data = [1, 2, 3, 4, 5]**

*   data has 0 inversions

Note: Although you can swap the elements of the inversions to form a sorted array, the inversion count is not the same as the minimum number of swaps to sort the array.

For instance, data = [10, 1, 2, 0].

You could sort this in 1 _swap_ (10, 0), but there are 5 _inversions_ (10, 1), (10, 2), (10, 0), (1, 0), (2, 0).

### Assignment Specs

You are given one file, [HybridSort.py](http://hybridsort.py/ "http://HybridSort.py"). You must complete and implement the following functions. Take note of the specified return values and input parameters. **_Do not change the function signatures_.**

You must adhere to the required time & space complexities.

**[HybridSort.py](http://hybridsort.py/ "http://HybridSort.py"):**

*   <span style="font-family: geomanist, sans-serif;">**insertion_sort(data: List[T], comparator: Callable[[T,T], bool]) -> None:**</span>  

    *   Given a list of values and comparator, perform an insertion sort on the list using the comparator.

*   *   **param data:** List of items to be sorted
    *   **param comparator: **A function, which takes an argument two objects of the same type as those in the list **data** and returns `True` if the first argument is less than or equal to the second according to some ordering, else `False`.
    *   **return:** None
    *   Time Complexity: _O(n^2)_
    *   Space Complexity: _O(1]_

*   **merge_sort(data, threshold: int = 0, comparator: Callable[[T,T], bool]) -> int: **  

    *   Given a list of values, perform a merge sort to sort the list and calculate the inversion count. When a threshold is provided, use a merge sort algorithm until the partitioned lists are smaller than or equal to the threshold - then use insertion sort. Be sure to use the comparator.

*   *   **param data:** List of items to be sorted.
    *   **param threshold:** int representing the size of the data at which insertion sort should be used. Defaults to 0.
    *   **param comparator: **A function, which takes an argument two objects of like type to those in the list **data** and returns `True` if the first argument is less than or equal to the second according to some ordering, else `False`.
    *   **return:** int representing inversion count, else 0 if **threshold** > 0.
    *   **NOTE:** The inversion count will be calculated when only a `merge_sort()` algorithm is used! (when threshold is 0) return 0 otherwise.
    *   Time Complexity: _O(nlog(n))_
    *   Space Complexity: _O(n)_

*   **hybrid_sort(data: List[T], threshold: int, comparator: Callable[[T,T], boo]) -> None:**  

    *   [Wrapper](https://en.wikipedia.org/wiki/Wrapper_function) function to call `merge_sort()` as a Hybrid Sorting Algorithm. Should call `merge_sort()` with provided threshold, and comparator function.

*   *   **param data:** List of items to be sorted.
    *   **param threshold:** int representing the size of the data at which insertion sort should be used.
    *   **param comparator: **A function, which takes an argument two objects of like type to those in the list **data** and returns `True` if the first argument is less than or equal to the second according to some ordering, else `False`.
    *   **return:** None
    *   **NOTE: **If this is more than one line, you're probably doing something wrong.
    *   Time Complexity: _O(nlog(n))_
    *   Space Complexity: _O(n)_

*   **inversions_count(data: List[T]) -> int:**  

    *   Wrapper function to call `merge_sort()` on a **copy** of data to retrieve the inversion count. Should call `merge_sort()` with _no threshold, and the default comparator._
    *   This function should _copy the original data_ - we want to determine the number of inversions in its current ordering, not necessarily sort it.

*   *   **param data:** List of items to determine the inversion count of.
    *   **return:** int representing inversion count.
    *   Time Complexity: _O(nlog(n))_
    *   Space Complexity: _O(n)_

*   **reverse_sort(data: List[T], threshold: int) -> None:**  

    *   Wrapper function to use `merge_sort()` to sort the data in reverse. Should call `merge_sort()` with provided threshold, and a comparator you define.

*   *   **param data:** List of items to be sorted.
    *   **param threshold: **int represnting the size of the data at which insertion sort should be used.
    *   **return:** None
    *   Time Complexity: _O(nlog(n))_
    *   Space Complexity: _O(n)_

## Application: Password Sorter

Congratulations! You've been hired by a cybersecurity firm focused on protecting users from brute-force hackers. A recent trend concerning cybersecurity experts have been brute-force hacking bots that have been successfully guessing lexicographically sorted passwords.

As a simple proof of concept, your first project at this firm will be designing a simple algorithm for sorting lists of passwords, roughly based on their strength against attacks by these aforementioned bots.

Your managers have provided you with this algorithm to rate a password:

![password_rate.png](https://s3.amazonaws.com/mimirplatform.production/files/5d527c8d-a793-4847-8c81-9ce1fb6e55ac/password_rate.png)

_Where p is the password length, u is the number of unique characters in a password, and c is the inversion count._

#### Examples

Suppose a list of passwords is given to you in this order:

1.  password
2.  unicorn38
3.  ILikeApples

These are the ratings of each password:

*   **password**: 21.48
    *   sqrt(8 characters) * sqrt(7 unique characters) + 8 inversions
*   **unicorn38**: 33.49
    *   sqrt(9 characters) * sqrt(8 unique characters) + 25 inversions
*   **ILikeApples**: 23.95
    *   sqrt(11 characters) * sqrt(9 unique characters) + 14 inversions

Thus, the list of passwords should be reordered into:

1.  unicorn38
2.  ILikeApples
3.  password

*   **password_rate(password: str) -> float:**  

    *   Rate a given password via the equation given in the problem statement
    *   You may find Python's [built-in set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) data structure to be helpful in counting unique characters

*   *   **param password:** String of password
    *   **return:** Rating of password (float)
    *   Time Complexity: _O(p*log(p))_ - where p is the password length
    *   Space Complexity: _O(p)_ - where p is the password length

*   **password_sort(data: List[str]) -> None:**  

    *   Sort a list of passwords by their ratings (the results from `password_rate()`)
    *   Tip: cache the results from a single call to `password_rate()` for each password to optimize your code and avoid unnecessary work!

*   *   **param data:** List of passwords
    *   **return:** None, sort the list in place
    *   In the complexities given below, _p _represents the average password length, and _n_ is the number of passwords in **data**
    *   Time Complexity: _O(n*p*log(p) + n*log(n))_
    *   Space Complexity: _O(n)_

## Submission

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir by 11:59p Eastern Time on Friday, 02/12/21.

Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:

    |- Project3.zip
        |— Project3/
            |— README.xml       (for project feedback)
            |— __init__.py      (for proper Mimir testcase loading)       
            |— HybridSort.py    (contains your solution source code)

#### Grading

The following 100-point rubric will be used to determine your grade on Project2:

*   Tests (75)
    *   00 - Coding Standard: __/2
    *   01 - Insertion Sort Basic: __/4
    *   02 - Insertion Sort Comparator: __/4
    *   03 - Insertion Sort Comprehensive: __/4
    *   04 - Merge Sort Basic: __/2
    *   05 - Merge Sort Threshold: __/3
    *   06 - Merge Sort Comparator: __/5
    *   07 - Merge Sort Comprehensive: __/5
    *   08 - Hybrid Sort Basic: __/2
    *   09 - Hybrid Sort Comprehensive: __/3
    *   10 - Hybrid Sort Speed: __/3
    *   11 - Reverse Sort Basic: __/3
    *   12 - Reverse Sort Speed: __/3
    *   13 - Inversion Count: __/12
    *   14 - Application Small: __/8
    *   15 - Application Large: __/12
*   Manual (25)
    *   Insertion Sort Complexities: __/5
    *   Merge Sort Complexities: __/5
    *   Hybrid Sort Complexities: __/3
    *   Reverse Sort Complexities: __/3
    *   Application Complexities: __/6
        *   `README.xml` is completely filled out with (1) netID, (2) Feedback, (3) Time to Completion and (4) Citations: __/3

## Tips, Tricks & Notes

*   _**You must fill out function docstrings to receive Coding Standard points.**_
*   _**You may not use Python's built in sort, or any imported sorting methods**_
*   There are different ways to implement merge sort, but make sure you are aiming for a solution that will fit the time complexity! If your recursive calls are some form of `merge_sort(start + 1: end)`, this will _not_ be _O(nlog(n))_.
*   Your wrapper functions (`hybrid_sort(), inversions_count(), reverse_sort()`)  should be simple functions containing one call to `merge_sort()`. This may seem useless, but see [here](https://en.wikipedia.org/wiki/Wrapper_function "Wrapper Functions") for the significance of wrapper functions.
*   Test cases will only test the functions specified.
    *   Note: The Merge Sort testcases will not test for inversion count
*   Try these web applications to visualize sorting algorithms:
    *   [https://visualgo.net/bn/sorting](https://visualgo.net/bn/sorting "https://visualgo.net/bn/sorting") (includes inversion count - "inversion index")
    *   [https://opendsa-server.cs.vt.edu/embed/mergesortAV](https://opendsa-server.cs.vt.edu/embed/mergesortAV "https://opendsa-server.cs.vt.edu/embed/mergesortAV") (good merge sort visualization)
    *   [https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html "https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html")
*   The file `plot.py` has been provided for comparing your sorting function's runtime.
    *   Run this file to see a graphical representation of your functions' performances.
    *   You may need to install matplotlib and numpy.
        *   If you are not familiar with the terminal instructions are here: [https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html "https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html")
        *   Otherwise use these commands:
            *   pip install matplotlib
            *   pip install numpy
    *   You do not have to use this.

_This project was created by Sean Nguyen and Andrew Haas, based on work by Zosha Korzecke and Olivia Mikola._
