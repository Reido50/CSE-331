**CC8 - SS21 - Taking Inventory**
=================================

**Due: Tuesday, March 23th @ 11:59pm**
======================================

*This is not a team project, do not copy someone else’s work.*

**Introduction**
================

 

![Caves\_and\_Cliffs.png](https://s3.amazonaws.com/mimirplatform.production/files/7a5a9c9b-6385-445d-acec-ec4956b8d9c3/Caves_and_Cliffs.png)

 

You are Mojang's most recent hire! Congratulations! They have brought
you to implement their new inventory system for the 1.17 Caves and
Cliffs update: [the bundle](https://minecraft.gamepedia.com/Bundle). This is a big job, however, so they have
assigned you a partner to write part of the system in tandem. You are
not concerned for you get the job of designing and implementing the base
system while your partner must integrate the bundle into the
pre-existing inventory system (a job that sounds much less interesting
than what you have been assigned).

You are informed that a bundle is an item that holds a [single stack of
items](https://minecraft.gamepedia.com/Tutorials/Units_of_measure#Amount_of_items), so a bundle could hold 64 dirt (1 stack of dirt is 64 dirt), or
32 cobblestone and 32 dirt (64 cobblestone in a stack), or 8 ender
pearls and 32 dirt (16 ender pearls in a stack). This is important as it
determines exactly how much of various items you can store inside said
bundle.

**Challenge**
=============

**Overview**
------------

You must implement and complete the class **Bundle**. You may and are
encouraged to use classes **ItemInfo** and **Items**. There is a
**constant** instance of the Items class, named **ALL\_ITEMS**. You WILL
want to use this. You do not have to worry about Bundle being integrated
into the existing inventory system as that is the responsibility of your
partner. While you can alter the classes ItemInfo, Items, and the
constant ALL\_ITEMS, you should not as  the test cases use files
completely independent of the ones provided to you.

In this problem, you must successfully add and remove a given amount of
a specific item to and from the bundle and return a boolean representing
whether the action could occur. Recall that a bundle can only hold a
single stack of items. Thankfully, the original Minecraft game
developers were nerds and set the precedent of all stack sizes being
powers of 2 (i.e. 2\^0, 2\^3, 2\^5) with a max stack size of 64 (2\^5)
and a min stack size of 1 (2\^0). 

The developers who hired you are leaving the exact implementation up to
you with the only restrictions being the runtime of your algorithms.

*Modify the following functions in the class Bundle*

**class Bundle:**

-   **\_\_init\_\_(self) -\> None:**
    -   This is currently empty, but you are allowed to create new
        attributes to help you store the items in the bundle (you will
        have to).
    -   **DO NOT** create any more parameters. i.e. Do not change the
        definition of \_\_init\_\_ from \_\_init\_\_(self) to
        \_\_init\_\_(self, someList, someString). You will fail the
        tests this way.
    -   **Return:** None
-    **to\_set(self) -\> Set[Tuple[str, int]]**

-   -   Converts the bundle to a set of tuples where the first index in
        the tuple is the item name and the second index is the amount of
        that item in the bundle.
    -   The order **DOES NOT MATTER** as this is a set where no order is given, this function is purely for test
        cases for us to see if you correctly added/removed an item
        to/from the bundle
    -   If you do not implement this function, you **WILL** fail all
        your tests
    -   **Time Complexity: O(n)**
    -   **Space Complexity: O(n)** 
-   **add\_to\_bundle(self, **item\_name**: str, amount: int) -\>
    bool:**

-   -   Adds an amount of an item to the bundle if possible
    -   You **WILL NEED** to use a **constant Items instance**
        called **ALL\_ITEMS**
        -   This constant stores all acceptable items and the amount of
            each item that is stored in a single stack
    -   **item\_name: str**: the name of the item to be added to the
        bundle (ex: Dirt, Cobblestone, Ender Pearls)
    -   **amount: int:** the amount of the itemName to be added to the
        bundle
    -   **Return:** a bool representing whether the add to the bundle
        was successful, True for added to the bundle, False for not
        added to the bundle
    -   **Time Complexity: O(1)**
    -   **Space Complexity: O(1)**
-   **remove\_from\_bundle(self, **item\_name**: str, amount: int) -\>
    bool:**

-   -   Removes an amount of an item from the bundle if possible
    -   In order for the tests to pass for this function, you need to
        have a **working add\_to\_bundle**function! This is because
        we leave the exact implementation up to you, so we cannot
        manually add items to your bundle, and in order to correctly
        remove from the bundle, items need to exist in the bundle.
    -   **item\_name: str**: the name of the item to be removed from
        the bundle (ex: Dirt, Cobblestone, Ender Pearls)
    -   **amount: int:** the amount of the itemName to be removed from
        the bundle
    -   **Return:** a bool representing whether the remove operation was
        successful, True for removed from the bundle, False for not
        removed/unable to removed from the bundle
    -   **Time Complexity: O(1)**
    -   **Space Complexity: O(1)**

 

*Do NOT modify the following functions. You however will want to use
them in your solution.*

**class ItemInfo:**

This class stores the name of an item and its corresponding stack size.
For example, the stack size of Dirt is 64, so the ItemInfo for Dirt
would be ItemInfo("Dirt", 64). It does NOT mean that I hold 64 Dirt in
my inventory. The stack size here represents the maximum amount of Dirt
that can be held in an inventory stack. It is merely a characteristic of
the Dirt item not the number of Dirt currently being held.

-   **Attributes:**
    -   **name: str:** the name of the item in the info is about
    -   **amountInStack: int:** the amount of the item that consists of
        one stack
        -   Ex: 64 Dirt makes a stack of Dirt, 16 Ender Pearls makes a
            stack of Ender Pearls
-   **\_\_init\_\_(self, name: str, amount\_in\_stack: int) -\> None:**
    -   Constructs an instance of ItemInfo
    -   **name: str:** the name of the item in the info is about
    -   **amount\_in\_stack: int:** the amount of the item that consists
        of one stack
    -   **Return:** None
-   **\_\_str\_\_(self) -\> str**and**\_\_repr\_\_(self) -\> str:**
    -   Represents the ItemInfo as a string in the form "\<ItemInfo\>
        name(stack: amountInStack)"
    -   Note that Python will automatically invoke this function when
        using printing an instance of ItemInfo to the console, and
        PyCharm will automatically invoke this function when displaying
        an ItemInfo in the debugger.
    -   Call this with str(ItemInfo) rather than ItemInfo.\_\_str\_\_().
    -   **Return:** str

**class Items:**

This class stores all ItemInfo instances. There will be a constant
instance of Items named **ALL\_ITEMS** for you to use and you will have
to use it in your addToBundle method in class Bundle. It can be indexed
similar to a Python's dictionary for ease of use.

-   **Attributes:**
    -   **items: Dict[str: ItemInfo]:** a dictionary where the name of
        the item is the key and its value is the corresponding ItemInfo
        -   Ex: A key-value pair in the dictionary could be {"Dirt":
            ItemInfo("Dirt", 64)}
-   **\_\_init\_\_(self, items\_to\_register: List[Tuple[str, int]] =
    None) -\> None:**
    -   Constructs an instance of Items
    -   **items\_to\_register: List[Tuple[str, int]]:** a list of items
        and their stack amounts to register as valid items\
        -   Ex: If itemsToRegister contains the tuple ("Ender Pearls",
            16), that would create the following key-value pair in
            self.items: {"Ender Pearls": ItemInfo("Ender Pearls", 16)}
    -   **Return:** None
-   **\_\_str\_\_(self) -\> str** and **\_\_repr(self) -\> str:**
    -   Represents Items as a string in the form "\<Items\> [{itemInfo}
        itemInfo\_string, ....]"
    -   Note that Python will automatically invoke this function when
        using printing an instance of Items to the console, and PyCharm
        will automatically invoke this function when displaying Items in
        the debugger.
    -   Call this with str(Items) rather than Items.\_\_str\_\_().
    -   **Return:** str
-   **\_\_getitem\_\_(self, item\_name: str) -\> ItemInfo:**
    -   Allows for Items to be indexed like Python's list or dictionary
    -   Ex: Let itemsInstance be an instance of Items
        -   Let self.items = {"Dirt": ItemInfo("Dirt", 64), "Ender
            Pearls": ItemInfo("Ender Pearls", 16)}
        -   Say I want to do x=itemsInstance["Dirt"]. Normally this
            would not work, but because the \_\_getitem\_\_ method is
            defined we can make this call. 
        -   So x = itemsInstance["Dirt] = ItemInfo("Dirt", 64)
    -   **item\_name: str:** the name of the item to find in Items
    -   **Return:** ItemInfo corresponding to itemName, None if itemName
        is not in self.items
-   **\_\_setitem\_\_(self, item\_name: str, item\_info: ItemInfo) -\>
    None:**
    -   Allows for key-value pairs to be added to Items like Python's
        list or dictionary
    -   Ex: Let itemsInstance be an instance of Items
        -   Let self.items = {"Dirt": ItemInfo("Dirt", 64), "Ender
            Pearls": ItemInfo("Ender Pearls", 16)}
        -   Say I want to add the key-value pair {"Iron Helmet": 1} to
            itemsInstance. I cannot say itemsInstance["Iron Helmet"] = 1
            without having \_\_setitem\_\_ defined. 
        -   By calling itemsInstance["Iron Helmet"] = 1, self.items for
            itemsInstance now looks like:
            -   {"Dirt": ItemInfo("Dirt", 64), "Ender Pearls":
                ItemInfo("Ender Pearls", 16), "Iron Helmet":
                ItemInfo("Iron Helmet", 1)}
    -   **item\_name: str:** name of the item to add to self.items, will
        be the key in self.items
    -   **item\_info: ItemInfo:** the ItemInfo corresponding with
        itemName, will be the value in self.items
    -   **Return:** None
-   **\_register(self, items: List[Tuple[str, int]]) -\> None:**
    -   Adds key-value pairs to self.items upon the initialization of
        Items
    -   **items: List[Tuple[str, int]]:** list of items to add to
        self.items
    -   **Return:** None

 

**Examples**:

**Ex 1:** Add 12 Dirt to a bundle already containing 2 Ender Pearls.

We know the max size of an Ender Pearl stack is 16, so we have 2/16 of a
stack. 2/16 is equivalent to 8/64. The max size of a Dirt stack is 64
and we want to add 12 Dirt, so 12/64 of a stack of Dirt to the Bundle.

If we add 8/64 and 12/64 together, we get 20/64. So the stack is not
full since our numerator is smaller than the denominator of 64. The Dirt
will be added to the bundle and the function will return True.

 

**Ex 2:** Add 56 Dirt to a bundle already containing 2 Ender Pearls.

The max size of an Ender Pearl stack is 16, so we have 2/16 of a stack
or 8/64 of a stack. The Dirt has a stack size of 64, so we have 56/64 of
a stack of Dirt. 

If we add these two values together, we get 8/64 + 56/64 = 64/64. This
is a full stack and will result in a full Bundle. This is still a valid
Bundle, however, and because the addition of the 56 Dirt does not cause
the Bundle size to go over a single stack, we can add the 56 Dirt to the
Bundle. The Dirt will be added to the bundle and the function will
return True.

 

**Ex 3:** Add 16 Cobblestone to a bundle already containing 4 Ender
Pearls, 5 Gold Nuggets, and 28 Dirt.

The max size of an Ender Pearl stack is 16, so we have 4/16 of a stack
or 16/64 of a stack. The max size of a Gold Nuggets stack is 64, so we
have 5/64 of a stack of Gold Nuggets. Dirt has a stack size of 64, so we
have 28/64 of a stack of Dirt. Cobblestone has a stack size of 64, so we
have 16/64 of a stack of Cobblestone.

Now, add them all together. 16/64 + 5/64 + 28/64 + 16/64 = 65/64 \>
64/64. The Cobblestone cannot be added to the Bundle since it would
cause the Bundle to contain more than one stack of items. The
Cobblestone will not be added to the Bundle and the function will return
False.

 

**Ex 4:** Remove 16 Cobblestone from a bundle already containing 48
Cobblestone and 10 Gold Nuggets.

We know we can remove 16 Cobblestone from our Bundle since we have at
least 16 Cobblestone already contained in the Bundle. The 16 Cobblestone
will be removed and this function will return True.

 

**Ex 5:** Remove 16 Cobblestone from a bundle already containing 12
Cobblestone and 40 Dirt.

There is less than 16 Cobblestone contained in the Bundle, so 16
Cobblestone cannot be removed. So nothing will change in the Bundle, the
Cobblestone will not be removed, and the function will return False.

Tips, Tricks, and Notes
=======================

-   You **must**fill out docstrings to receive Coding Standard points.
-   You may notice the use of
    [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
    in the given starter code, it may be wise to use one.
-   Fractions are your friend!!
-   The underlying structure of a [set](https://docs.python.org/3/tutorial/datastructures.html#sets) is in fact a hash, the same structure as a Python dictionary
-   If you need some music to listen to while coding [here is a playlist
    of various Minecraft
    discs](https://www.youtube.com/watch?v=J6oOE6jJXLo).

**Submission**
==============

**Deliverables**
----------------

Be sure to upload the following deliverables in a .zip folder to Mimir
by 11:59 PM Eastern Time on **Tuesday** **3/23/2021**.

Your .zip folder can contain other files (for example, description.md
and tests.py), but must include (at least) the following:


    CC8.zip    
        |— CC8/   
            |— README.xml       (for coding challenge feedback)        
            |— __init__.py      (for proper Mimir testcase loading)        
            |— solution.py      (contains your solution source code)

**Note:** your submitted solution does not need to include the
InventoryItems.py or the Minecraft\_Items.csv files. They are included
in our mimir tests and will overwrite any InventoryItems.py or
Minecraft\_Items.csv files you may submit. So while you *may* change
those files on your device, it will not affect the outcome of the mimir
tests. 

**Grading**
-----------

The following 100-point rubric will be used to determine your grade on
CC8:

-   Tests (65)
    -   00 - Coding Standard: \_\_/5
    -   01 - Basic: \_\_/5
    -   02 - add\_to\_bundle: \_\_/10
    -   03 - remove\_from\_bundle: \_\_/10
    -   04 - Small Comprehensive: \_\_/15
    -   05 - Large Comprehensive: \_\_/20
-   Manual (35)
    -   M0 - add\_to\_bundle Time O(1): \_\_/10
    -   M1 - add\_to\_bundle Space O(1): \_\_/5
    -   M2 - remove\_from\_bundle Time O(1): \_\_/10
    -   M3 - remove\_from\_bundle Space O(1): \_\_/5
    -   README.md is *completely* filled out with (1) Name, (2)
        Feedback, (3) Time to Completion, (4) Citations, and
        (Difficulty): \_\_/5

 
Coding Challenge created by Jacob Caurdy and Olivia Mikola
