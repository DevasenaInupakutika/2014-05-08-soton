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
	
		# Find number of records and total count of animals seen
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
	    assert baymean == 17, 'Mean sightings at Nazan Bay is wrong'

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
























