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
extract the mean number of stations with *Harmonic* tidal wave prediction type per day from a csv file. First, let's place this function in an external module. To do this, copy the code 
below into a text file in this directory, and name it `mean_predictions.py`.

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
mean number of stations per day for the focus station.




















