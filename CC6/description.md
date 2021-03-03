**CC6 - SS21- Airport Organizer**
=================================

**Due: Tuesday, March 9th, 11:59 pm**

_This is not a team project, do not copy someone else’s work._

**Introduction**
================

Your local airport is at risk of shutting down due to the cost of operation being greater than the revenue generated.  One place the airport notices it can reduce costs is by using less gates.  At the moment, more gates are staffed than are being used.  As a result, the airport has tasked you with optimizing the amount of personnel to station at gates throughout the airport.

**![Ref51ffd4b0a718db74b92887dcdd1f01.jpg](https://s3.amazonaws.com/mimirplatform.production/files/9391a4d0-b66d-4873-b5ff-ba12e03d8806/Ref51ffd4b0a718db74b92887dcdd1f01.jpg)**
================================================================================================================================================================================

**Challenge**
=============

**Overview**
------------

For this challenge, you will be making a function that will find the least number of gates that need to be in use in order for the day’s airport operations to run smoothly.  You will be given a list of departure times and arrival times of aircraft for a day, and asked to return the maximum number of gates in use that day.

Your function will receive two python lists of floats.  One will represent departure times and one will represent arrival times.  A float represents the amount of time (in seconds) after midnight on that day.

_Modify the following functions_

**gates\_needed(departures: List\[float\], arrivals: List\[float\]) -> int**

*   **departures: List\[float\]**: A python list of floats containing departure times of flights at the airport
*   **arrivals: List\[float\]**: A python list of floats containing arrival times of flights at the airport
*   **Return:** An integer that represents the maximum number of gates needed at any point during the day of these departures and arrivals
*   **Time Complexity:** O(n + m), where n is the length of departures and m is the length of arrivals
*   **Space Complexity:** O(n + m)

#### **Guarantees**

*   There will never be a more departures than arrivals at the airport (no negative gates)
*   The first arrival will happen before the first departure
*   The amount of gates used leftover from the previous night will always be 0

#### **Notes**

*   You may **_NOT_** have more than max(len(departures), len(arrivals)) in any structure you create at any given time.  Think about what kind of data structure may be useful to solve this problem.  You can use multiple of them
*   You might want to use Queue.SimpleQueue (https://docs.python.org/3/library/queue.html#queue.SimpleQueue)
*   .pop(0) is O(n), using it will more than likely violate time complexity!
*   The first plane to arrive will also be the first to depart **_(HINT)_**
*   If a plane has the same departure time as its arrival time, you can assume the plane performed a “touch-and-go”, and didn’t need a gate

#### **Examples:**

**Ex 1:**

**departures = \[1, 5, 8, 20\]****arrivals = \[0, 1.5, 3, 19\]**

**Return**: 2.  The time frame where most planes are ever on the ground is between time 3 and time 5.  A plane arrives at 0 and then leaves at 1.  At this point, only one gate had to be staffed.  A plane arrives at 1.5 and another at 3.  Now, two gates have to be staffed on this day.  The first of these two flights leaves at 5 and the other at 8.  With no gates in use, a plane arrives at 19 and then leaves at 20.

**Ex 2:**

**departures = \[1, 5, 8, 20\]****arrivals = \[0, 1.5, 3, 19, 21, 21.5, 22, 22.5, 23, 23.5\]**

**Return**: 6.  At the end of the night, 6 planes are on the ground at the airport, that means that 6 gates had to be in use, which is the maximum number over the day.

**Submission**
==============

**Deliverables**
----------------

Be sure to upload the following deliverables in a .zip folder to Mimir by **11:59PM** Eastern Time on **Tuesday, 03/09/2021**.

Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:

CC6.zip

 |— CC6/

 |— README.xml       (for coding challenge feedback)

 |— \_\_init\_\_.py      (for proper Mimir testcase loading)

 |— solution.py      (contains your solution source code)

**Grading**
-----------

The following 100-point rubric will be used to determine your grade on CC3:

*   **Tests (75)**

*   00 - Coding Standard: \_\_/5
*   01 - Test Basic: \_\_/10
*   02 - Test None Left at End of Night: \_\_/10
*   03 - Test Multiple Left at End of Night: \_\_/10
*   04 - Test Comprehensive Small: \_\_/20
*   05 - Test Comprehensive Large: \_\_/20

*   **Manual (25)**

*   README.md is _completely_ filled out with (1) NetID, (2) Feedback, (3) Time to Completion and (4) Citations: \_\_/5
*   Time Complexity (O(n + m)): \_\_/10
*   Space Complexity (O(n + m)): \_\_/10

**Tips, Tricks, and Notes**
===========================

*   **_You must fill out docstrings_**
*   **_You must remove REPLACE in README, and put appropriate text on each section_**
*   Again, the first plane to arrive will also be the first to depart! This is a big hint!

Created by Max Huang and Ian Barber