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
Use a browser to open the tutorial on github, located at: http://github.com/{{page.github_username}}/{{page.bootcamp_slug}}Click on the directory named `/lessons/nocs/nocs-shell`.
A *terminal* is a program you run that gives you access to the shell. There are many different terminal programs that vary across operating systems.There are many reasons to learn about the shell. In my opinion, the most important reasons are that:
1.	It is very common to encounter the shell and command-line-interfaces in scientific computing, so you will probably have to learn it eventually2.	The shell is a really powerful way of interacting with your computer. GUIs and the shell are complementary - by knowing both you will greatly expand the range of tasks you can accomplish with your computer. You will also be able to perform many tasks more efficiently.
The shell is just a program and there are many different shell programs that have been developed. The most common shell (and the one we will use) is called the Bourne-Again SHell (bash). Even if bash is not the default shell, it is usually installed on most systems and can be started by typing bash in the terminal. Many commands, especially a lot of the basic ones, work across the various shells but many things are different. I recommend sticking with bash and learning it well. (Here is a link for more information). Shell script allows us to program commands in chains and have the system execute them as a scripted event similar to batch files.To open a terminal, just single click on the "Terminal" icon on the Desktop.## The Example: Manipulating Experimental Data Files

We will spend most of our time learning about the basics of the shell by manipulating some experimental altimetry data from Global Ocean tide solution models. To get data for this test, you’ll need Internet access. Just enter the command:
`git clone https://github.com/{{page.github_username}}/{{page.bootcamp_slug}}. git` Followed by:`cd {{page.bootcamp_slug}}` These 2 commands will grab all of the data needed for this workshop from the Internet.## Let’s get started

One very basic command is ‘echo’. This command just prints text to the terminal. Try the command:`echo Hello, World`
 Then press enter. You should see the text "Hello, World" printed back to you. The echo command is useful for printing from a shell script, for displaying variables, and for generating known values to pass to other programs.## Files and Directories

## Moving around the file system

Let’s learn how to move around file system using command line scripts. This is really easy to do in GUI. But, once you learn basic Unix commands, you’ll see that it is pretty easy to do in shell too.
For this purpose, we need to know our current location. The command `pwd` (print working directory) tells you where you are sitting in the directory tree. The command `ls` will list the files in files in the current directory. Directories are often called "folders" because of how they are represented in GUIs. Directories are just listings of files. They can contain other files or directories. Several commands are frequently used to create, inspect, rename and delete files and directories. In order to explore them, let’s open shell window, which starts usually with a dollar sign prompt indicating that shell is waiting for input:`$` Whenever you start up a terminal, you will start in a special directory called the home directory. Every user has their own home directory where they have full access to do whatever they want. For example, if our user ID is `user`, the `pwd` command tells us that we are in the `/home/user` directory.  At any moment, our current working directory is our current default directory, i.e., the directory that the computer assumes we want to run commands in unless we explicitly specify something else. Here, the computer's response is `/users/user`, which is user’s home directory:`$ pwd
 /users/user`This is the home directory for the `user` user. That is our user name. You can always find out your user name by entering the command `whoami`.`$ whoami
 user`
More specifically, when we type `whoami` the shell:1.	Finds a program called `whoami`,2.	Runs that program,3.	Displays that program's output, then4.	Displays a new prompt to tell us that it's ready for more commands.

## File types

When you enter the `ls` command lists the contents of the current directory. There are several items in the home directory, notice that they are all coloured blue. This tells us that all of these items are directories as opposed to files.Lets create an empty file using the `touch` command. Enter the command: `touch testfile`
 Then list the contents of the directory again. You should see that a new entry, called `testfile`, exists. It is coloured white meaning that it is a file, as opposed to a directory. The `touch` command just creates an empty file.
Some terminals will not colour the directory entries in this very convenient way. In those terminals, use `ls -F` instead of `ls`. The `-F` argument modifies the results so that a slash is placed at the end of directories. If the file is *executable* meaning that it can be run like a program, then a star will be placed at the end of the file name.You can also use the command `ls -l` to see whether items in a directory are files or directories. `ls -l` gives a lot more information too, such as the size of the file and information about the owner. If the entry is a directory, then the first letter will be a "d". The fifth column shows you the size of the entries in bytes. Notice that `testfile` has a size of zero.
Now, let's get rid of `testfile`. To remove a file, just enter the command: `rm testfile`
 The `rm` command can be used to remove files. If you enter `ls` again, you will see that `testfile` is gone.

## Changing directories

Now let’s move to a different directory.  The command `cd`(change directory) is used to move around. Let's move into the `{{page.bootcamp_slug}}` directory. Enter the following command: `cd {{page.bootcamp_slug}}`
 Now use the `ls` command to see what is inside this directory. You will see that there is an entry, which is green. This means that this is an executable. If you use `ls -F` you will see that this file ends with a star.
This directory contains all of the material for this bootcamp. Now move to the directory containing the data for the shell tutorial which is present at `/lessons/nocs/nocs-shell` : 
`cd nocs-shell`
 If you enter the `cd` command by itself, you will return to the home directory. Try this, and then navigate back to the `nocs-shell`  directory.`cd` doesn't print anything, but if we run `pwd` after it, we can see the path of the directory we’re in currently. If we run `ls` without parameters now, it lists the contents of current directory.  
We now know how to go down the directory tree: How do we go up? We could use an absolute path:`$ cd /users/user`
but it's almost always simpler to use cd .. to go up one level:`$ cd ..`
 `..` is a special directory name meaning "the directory containing this one", or more succinctly, the parent of the current directory. Sure enough, if we runpwd after running `cd ..`, we're back in `/users/user`:`$ pwd
 /users/user` The special directory `..` doesn't usually show up when we run `ls`. If we want to display it, we can give `ls` the `-a` flag:`$ ls -F -a
 ./           ../   <rest of the files/ directories>`
`-a` stands for "show all"; it forces ls to show us file and directory names that begin with `.`, such as `..` (which, if we're in `/users/user`, refers to the `/users` directory). As you can see, it also displays another special directory that's just called `.`, which means "the current working directory". It may seem redundant to have a name for it, but we'll see some uses for it soon.

