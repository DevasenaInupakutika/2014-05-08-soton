---
layout: lesson
root: ../..
github_username: DevasenaInupakutika
bootcamp_slug: 2014-05-08-soton
title: The Unix Shell Scripting
---
**Based on material by Milad Fatenejad, Sasha Wood, and Radhika Khetani**

## Introduction

## What is the shell and how do I access it?

The *shell* is a program that presents a command line interface, which allows you to control your computer using commands entered with a keyboard instead of controlling graphical user interfaces (GUIs) with a mouse/keyboard combination.
Use a browser to open the tutorial on github, located at: http://github.com/{{page.github_username}}/{{page.bootcamp_slug}}Click on the directory named ‘/lessons/nocs/nocs-shell’.
A *terminal* is a program you run that gives you access to the shell. There are many different terminal programs that vary across operating systems.There are many reasons to learn about the shell. In my opinion, the most important reasons are that:
1.	It is very common to encounter the shell and command-line-interfaces in scientific computing, so you will probably have to learn it eventually2.	The shell is a really powerful way of interacting with your computer. GUIs and the shell are complementary - by knowing both you will greatly expand the range of tasks you can accomplish with your computer. You will also be able to perform many tasks more efficiently.
The shell is just a program and there are many different shell programs that have been developed. The most common shell (and the one we will use) is called the Bourne-Again SHell (bash). Even if bash is not the default shell, it is usually installed on most systems and can be started by typing bash in the terminal. Many commands, especially a lot of the basic ones, work across the various shells but many things are different. I recommend sticking with bash and learning it well. (Here is a link for more information). Shell script allows us to program commands in chains and have the system execute them as a scripted event similar to batch files.To open a terminal, just single click on the "Terminal" icon on the Desktop.## The Example: Manipulating Experimental Data Files

We will spend most of our time learning about the basics of the shell by manipulating some experimental altimetry data from Global Ocean tide solution models. To get data for this test, you’ll need Internet access. Just enter the command:
‘git clone https://github.com/{{page.github_username}}/{{page.bootcamp_slug}}. git’ Followed by:‘cd {{page.bootcamp_slug}}’ These 2 commands will grab all of the data needed for this workshop from the Internet.## Let’s get started

One very basic command is ‘echo’. This command just prints text to the terminal. Try the command:‘echo Hello, World’
 Then press enter. You should see the text "Hello, World" printed back to you. The echo command is useful for printing from a shell script, for displaying variables, and for generating known values to pass to other programs.