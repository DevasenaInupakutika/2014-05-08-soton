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












