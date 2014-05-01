---
layout: lesson
root: ../..
github_username: DevasenaInupakutika
bootcamp_slug: 2014-05-08-soton
title: Python Unit Testing
---

** Based on materials by original SWC Lecture Series, Katy Huff, Rachel Slaybaugh, and Anthony Scopatz**

## Introduction

Now that you understand the basics of programming in Python, we'll move on to 
discuss a topic in "software engineering", which is how to test your code 
for accuracy.

## Unit Testing Concepts

As practicing scientists, we would never trust a lab measurement that we made 
with uncalibrated instruments. Similarly, as computational scientists, we 
shouldn't trust the results that our code gives us until we have tested it. 
Without calibration/testing, how do we know that our code is giving us the 
right answers?

In this lesson, we'll focus on unit tests, perhaps the most basic type of 
testing that we can run.

**Unit Tests:** Unit tests are a type of test which test the fundamental
units of a program's functionality. Often, this is on the class or
function level of detail. i.e. Unit tests focus on a single "unit" of code, which in our case
will be functions that we've written. However what defines a *code unit* is not
formally defined.

We'll write tests to ensure that 
when our function is given a certain set of arguments as input, it generates 
output that we know to be correct. Once we have a complete test suite for a 
function, we can run the entire suite to make sure that all the tests pass (ie, 
that our function gives the correct output for all the combinations of input 
that we have decided to test).

For example, let's say that we have a function that reads in a data file, does 
some processing, and returns a result. We can test the function by giving it a 
small data file, for which we can calculate the correct result by hand, and 
making sure that the function gives the correct answer for this small file. 
This gives us more confidence that if we run the function on a different data 
set, perhaps a huge one for which we can't verify the results by hand, that 
we'll get an accurate result.

Even better, if we make changes to the internals of our function, we can run 
our tests again to make sure that we haven't accidentally broken anything (this 
is known as a "regression"). This makes us more free to continue to improve the 
performance of our code over time, and avoids the dreaded "it's working, don't 
touch it" phenomena.

In this session, we're going to use the simple and very popular `nose` package 
to write and run our tests.

**Unit Testing Example**

We'll practice unit testing using a function that we've already written to 
extract the mean number of stations with *Harmonic* tidal wave prediction type per sightings from a csv file. First, let's place this function in an external module. To do this, copy the code 
below into a text file in this directory, and name it `mean_sightings.py`.

    import matplotlib.mlab as ml
	import numpy as np
	
	def get_sightings(filename, focusstation):
	
		# Load table
		tab = ml.csv2rec(filename)
	
		# Find number of records and total count of stations where Harmonic tidal waves are seen
		isfocus = (tab['station'] == focusstation)
		totalrecs = np.sum(isfocus)
		meancount = np.mean(tab['count'][isfocus])
	
		# Return num of records and stations where tides are seen
		return totalrecs, meancount

This function uses boolean arrays to calculate the total number of records and 
mean number of stations per sighting for the focus station.

To confirm that everything's working correctly, open up a new IPython notebook 
(in this same directory) and run the following in a cell:

	from mean_sightings import get_sightings
	print get_sightings('sightings_tab_sm.csv', 'Nazan Bay')

This should give you the correct answer for the Nazan Bay (check to make sure by 
looking at the raw data file and counting by hand).

Now that we have the function in a module, let's write some unit tests to make 
sure that the function is giving us the correct answers. Create a new text file 
called `test_mean_sightings.py`, which will hold our unit tests. At the top of 
this file, type (or copy) in the following code, which will import the function 
that we wish to test and set the filename that we want to use for the testing.

	from mean_sightings import get_sightings

	filename = 'sightings_tab_sm.csv'

Note that we are using a small, "toy" data set for testing so that we can 
calculate correct answers by hand.

Now, let's write our first test function, which will simply test to make sure 
that our function gives the correct answer when called using this small data 
set and the Nazan Bay as arguments. Test functions (written for the `nose` testing 
package) can contain any type of Python code, like regular functions, but have 
a few key features. First, they don't take any arguments. Second, they contain 
at least one `assert` statement - the test will pass if the condition following 
the `assert` statement is True, and the test will fail if it's False.

An example will make this more clear. Here's a test that checks whether the 
function returns the correct answers for the small data set and the Nazan Bay. Copy 
and paste this at the end of the `test_mean_sightings.py` file.

	def test_bay_is_correct():
	    bayrec, baymean = get_sightings(filename, 'Nazan Bay')
		assert bayrec == 2, 'Number of records for Nazan Bay is wrong'
	    assert baymean == 17, 'Mean Tidal wave sightings at Nazan Bay is wrong'

Note that we calculated the correct values of `bayrec` and `baymean` by hand. 
Make sure that you get these right!

Now we're ready to run our suite of tests (so far, just this one test). Open a 
command line window, and `cd` to the directory containing your new Python 
files. Type `nosetests`, and examine the output. It should look something like 
this:

	.
	----------------------------------------------------------------------
	Ran 1 test in 0.160s
	
	OK

The dot on the first line shows that we had one test, and that it passed. There 
is one character printed for each test. A '.' means the test passed, a 'F' 
means the test failed, and an 'E' means there was an error in the test function 
itself.

Just for fun, try changing your test so that it fails (for example, assert that 
the number of Nazan Bay records should be 3). What output do you see now? Don't 
forget to change the test back so that it passes after you're done.

>### Exercise 1 - Test the Fire Island results
>
>Add an additional test to your test file to make sure that your function also 
>gives the right answer when the station is  Fire Island. Run `nosetests` and make 
>sure both tests pass.

Great, now we have two tests that pass. However, both of these tests were 
fairly straightforward, in that they tested the expected behaviour of the 
function under "normal" inputs. What about corner or boundary cases? For 
example, what should our function do if the station is not found anywhere in the 
data set?

Let's say that we decide that our function should return 0 for the number of 
records and 0 for the mean stations per record if the station is not found in the 
data set. Let's write a test to see if our function does this already:

	def test_station_not_present():
	    statrec, statmean = get_sightings(filename, 'NotPresent')
		assert statrec == 0, 'Station missing should return zero records'
	    assert statmean == 0, 'Station missing should return zero mean'

If we run our test suite now, we see that this test fails. The output doesn't 
give us much of a hint as to what went wrong though - we know that statmean was 
not equal to zero, but what was it?

To find out, add the line `print statrec, statmean` right above the first 
assert statement, run the test suite again, and look at the output. Now we can 
see that the statmean was 'nan', which stands for "not a number". This is 
because when station is not found, our current function returns 0 for the 
number of records and 0 for the total count. To calculate the mean, it tries to 
divide 0/0, and gets 'nan'.

>### Exercise 2 - Fixing our function for a boundary case
>
>Modify the function `get_sightings` so that if the station is not present, both 
>totalrecs and meancount are 0. HINT: Check if totalrecs is zero before 
>calculating meancount - if totalrecs is zero, meancount must also be zero.
>
>Run your test suite again to make sure all three tests now pass.

Here's another special case - all of the station names in the data sets are 
capitalised, with the first letter in uppercase and the rest of the letters in 
lowercase. What if someone enters the name of the station using the wrong case. 
For example, they might call the function with the argument 'Nazan bAy' for the 
station name.

>### Exercise 3 - Fixing our function for bad input
>
>Write a test function that will pass only if your function returns the correct
>answer for stations if the input argument focusstation is set to 'Nazan bAy'. Run this 
>test, and see that it currently fails.
>
>Then, modify the function so that this test passes. HINT: You can use the 
>method 'capitalize' on any string to correct its capitalization.
>
>Run your test suite again to make sure all four tests now pass.
>
>__Bonus__
>
>Determine what your function should return if a user gives the function a file 
>that does not exist. Write a test that checks that this value is indeed 
>returned for the case of a missing file, and modify your function to return it 
>as desired.

You can imagine adding more test functions as you think of more unusual cases 
that you want your function to correctly address. It is not unusual for the 
file containing test cases to be several times longer than the file containing 
the actual functions!

Now we're in a great position - we now have more confidence that our code is 
doing what we expect it to do.

Now let's say that we are planning to share our code with a colleague who is 
less experienced with programming, and we think that he/she might not 
understand the neat boolean indexing tricks that we've been using. For clarity, 
we decide that we'll replace the guts of our `get_sightings` function with code 
that calculates the same thing but uses a for loop instead. We've already 
written this code in the previous lesson, so we can simply erase our existing 
`get_sightings` function and replace it with this code instead:


	def get_sightings(filename, focusstation):
	
	    # Load table
	    tab = ml.csv2rec(filename)
		
		# Standardize capitalization of focusstation
		focusstation = focusstation.capitalize()

	    # Loop through all records, countings recs and stations
	    totalrecs = 0
	    totalcount = 0
	    for rec in tab:
			if rec['station'] == focusstation:
	            totalrecs += 1
	            totalcount += rec['count']
	
	    meancount = totalcount/totalrecs
	
	    # Return num of records and stations where Harmonic Tidal Waves are seen
	    return totalrecs, mean count

Thinking ahead, we made sure to add a line to fix the capitalization problem 
right away so that our fourth unit test should pass. Since this code worked 
before, we're confident that it will work now. Just to be sure, though we run 
our test suite again.

>### Exercise 4 - Examining and fixing regressions
>
>You are shocked to discover that two of the four tests now fail! How can this 
>be? We were sure that the new for loop code was correct, and we looked at its 
>output before to convince ourselves that it was correct...
>
>Try to uncover the causes of this regression. One failure should have a fairly 
>obvious cause (it relates to the issue of a station not being present, which 
>we check with the third test). The second failure has a more subtle cause - 
>try to figure out the problem, and correct the function to give the right 
>answer.

### Test Driven Development - the joy of Red/Green/Refactor

Instead of fixing the above code, we're going to delete get_sightings, and do a very simple run through TDD.

The big idea here is that you think about your problem and write your unit tests *before* 
you write a single line of code. 
- This forces you to think about what your problem in terms of different modes of 
  success/failure and various edge cases, rather than just the basic functionality. 
- It means that you implement the right amount of functionality without overbuilding.
- It also gives you a ready-made specification for your design

We have already written our first 4 test cases. 
- Run ``nosetests``. You will see everything fail (Red)

Now we're going to write a bare minimum ``get_sightings`` that passes the first test case. The code will be 
really stupid

    def get_sightings(filename, focusstation):
		return (2, 17)
	
This is clearly wrong BUT it passes a couple of test cases. It has also forced you to think about the structure of your function. 

Now that you have a couple of Greens you would refactor the code to be a little smarter. 

Continue to repeat this process of turning Red to Green; then refactoring and cleaning up.

Hopefully, this actually helps you write better code that has fewer bugs, and gives you deeper insight into the structure of your 
program.

Example:

    def get_sightings(filename, focusstation):
    
    	# Load table
    	tab = ml.csv2rec(filename)
    
    	# Standardize capitalization of focusstation
    	focusstation = focusstation.capitalize()
    
    	# Loop through all records, countings recs and stations
        totalrecs = 0.
        totalcount = 0.
    	for rec in tab:
            if rec['station'] == focusstation:
            	totalrecs += 1
            	totalcount += rec['count']
    
    	if totalrecs==0:
            meancount = 0
    	else:
        	meancount = totalcount/totalrecs
    
    	# Return num of records and stations where Harmonic Tidal waves are seen
    	return totalrecs, meancount

__BONUS__ If there is time, write some tests that will pass for a different csv file.
























