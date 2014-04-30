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
For this purpose, we need to know our current location. The command `pwd` (print working directory) tells you where you are sitting in the directory tree. The command `ls` will list the files in files in the current directory. Directories are often called "folders" because of how they are represented in GUIs. Directories are just listings of files. They can contain other files or directories. Several commands are frequently used to create, inspect, rename and delete files and directories. In order to explore them, let’s open shell window, which starts usually with a dollar sign prompt indicating that shell is waiting for input:`$` Whenever you start up a terminal, you will start in a special directory called the home directory. Every user has their own home directory where they have full access to do whatever they want. For example, if our user ID is `user`, the `pwd` command tells us that we are in the `/home/user` directory.  At any moment, our current working directory is our current default directory, i.e., the directory that the computer assumes we want to run commands in unless we explicitly specify something else. Here, the computer's response is `/users/user`, which is user’s home directory:`$ pwd`
 `/users/user`This is the home directory for the `user` user. That is our user name. You can always find out your user name by entering the command `whoami`.`$ whoami`
 `user`
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
 `..` is a special directory name meaning "the directory containing this one", or more succinctly, the parent of the current directory. Sure enough, if we runpwd after running `cd ..`, we're back in `/users/user`:`$ pwd`
 `/users/user` The special directory `..` doesn't usually show up when we run `ls`. If we want to display it, we can give `ls` the `-a` flag:`$ ls -F -a`
 `./           ../   <rest of the files/ directories>`
`-a` stands for "show all"; it forces ls to show us file and directory names that begin with `.`, such as `..` (which, if we're in `/users/user`, refers to the `/users` directory). As you can see, it also displays another special directory that's just called `.`, which means "the current working directory". It may seem redundant to have a name for it, but we'll see some uses for it soon.

## Arguments

Most programs take additional arguments that control their exact behaviour. For example, `-F` and `-l` are arguments to `ls`. The `ls` program, like many programs, takes a lot of arguments. But how do we know what the options are to particular commands?

Most commonly used shell programs have a manual. You can access the manual using the man program. Try entering: `man ls`
 This will open the manual page for `ls`. Use the space key to go forward and `b` to go backwards. When you are done reading, just hit `q` to exit.
Programs that are run from the shell can get extremely complicated. To see an example, open up the manual page for the `find` program, which we will use later this session. No one can possibly learn all of these arguments, of course. So you will probably find yourself referring back to the manual page frequently.

## Examining the contents of other directories

By default, the `ls` command lists the contents of the working directory (i.e. the directory you are in). You can always find the directory you are in using the `pwd` command. However, you can also give `ls` the names of other directories to view. Navigate to the home directory if you are not already there. Then enter the command: `ls {{page.bootcamp_slug}}`
 This will list the contents of the `{{page.bootcamp_slug}}` directory without you having to navigate there. Now enter: `ls {{page.bootcamp_slug}}/lessons/nocs/nocs-shell` This prints the contents of `nocs-shell`. The `cd` command works in a similar way. Try entering:
 `cd {{page.bootcamp_slug}}/ lessons/nocs/nocs-shell`
and you will jump directly to `nocs-shell` without having to go through the intermediate directory.

## Full vs. Relative Paths

The `cd` command takes an argument, which is the directory name. Directories can be specified using either a relative path a full path. The directories on the computer are arranged into a hierarchy. The absolute path tells you where a directory is in that hierarchy. Navigate to the home directory. Now, enter the `pwd` command and you should see: `/home/user`
 which is the full name of your home directory. This tells you that you are in a directory called `user`, which sits inside a directory called `home` which sits inside the very top directory in the hierarchy. The very top of the hierarchy is a directory called `/` which is usually referred to as the root directory. 

So, to summarize: `user` is a directory in home which is a directory in /.Now enter the following command:`cd /home/user/{{page.bootcamp_slug}}/lessons/nocs/nocs-shell`
This jumps to `nocs-shell`. Now go back to the `home` directory. We saw earlier that the command: `cd {{page.bootcamp_slug}}/lessons/nocs/nocs-shell`
 had the same effect - it took us to the `nocs-shell` directory. But, instead of specifying the absolute path (`/home/user/{{page.bootcamp_slug}}/lessons/nocs/nocs-shell`), we specified a relative path. In other words, we specified the path relative to our current directory. An absolute path always starts with a `/`. A relative path does not. You can usually use either an absolute path or a relative path depending on what is most convenient. If we are in the `home` directory, it is more convenient to just enter the relative path since it involves less typing.
Now, list the contents of the `/bin` directory. Do you see anything familiar in there?

## Saving time with shortcuts, wild cards, and tab completion## Shortcuts

There are some shortcuts, which you should know about. Dealing with the home directory is very common. So, in the shell the tilde character, `~`, is a shortcut for your `home` directory. Navigate to the `nocs-shell` directory, then enter the command: `ls ~`
 This prints the contents of your home directory, without you having to type the absolute path. The shortcut `..` always refers to the directory above your current directory. Thus: `ls ..` 
prints the contents of the `/home/user/{{page.bootcamp_slug}}`. You can chain these together, so: 
`ls ../../`
 prints the contents of `/home/user` which is your `home` directory. Finally, the special directory `.` always refers to your current directory. So, `ls`, `ls .`, and `ls ././././.` all do the same thing, they print the contents of the current directory. This may seem like a useless shortcut right now, but we'll see when it is needed in a little while.To summarise, the commands `ls ~`, `ls ~/.`, `ls ../../`, and `ls /home/user` all do exactly the same thing. These shortcuts are not necessary, they are provided for your convenience.

## Our data set: Cochlear Implants and NOCS sample data

A cochlear implant is a small electronic device that is surgically implanted in the inner ear to give deaf people a sense of hearing. More than a quarter of a million people have them, but there is still no widely accepted benchmark to measure their effectiveness. In order to establish a baseline for such a benchmark, our supervisor got teenagers with CIs to listen to audio files on their computer and report:
1.	The quietest sound they could hear2.	The lowest and highest tones they could hear3.	The narrowest range of frequencies they could discriminate
To participate, subjects attended our laboratory and one of our lab techs played an audio sample, and recorded their data - when they first heard the sound, or first heard a difference in the sound. Each set of test results was written out to a text file, one set per file. Each participant has a unique subject ID, and a made-up subject name. Each experiment has a unique experiment ID. The experiment has collected 351 files so far.Another experimental oceanography data folder `nocs`  exists which is based on estimated abstractions from tidal waters and all other sources.
The data is a bit of a mess! There are inconsistent file names, there are extraneous "NOTES" files that we'd like to get rid of, and the data is spread across many directories. We are going to use shell commands to get this data into shape. By the end we would like to:
1.	Put all of the data into one directory called "alldata"2.	Have all of the data files in there, and ensure that every file has a ".txt" extension3.	Get rid of the extraneous "NOTES" filesIf we can get through this example in the available time, we will move onto more advanced shell topics...## Wild cards

Navigate to the `nocs-shell/data/nocs` directory. This directory contains Estimated abstractions data from tidal waters and all other sources by purpose and environment agency region for a period 2000 – 2010.  Try this command:`ls *.csv`lists files in `nocs-shell/data/nocs`  directory that ends with characters `.csv`.`nocs-shell/data/thomas`  directory contains our hearing test data for Thomas. If we type `ls`, we will see that there are a bunch of files that are just four digit numbers. By default, `ls` lists all of the files in a given directory. The `*` character is a shortcut for "everything". Thus, if you enter `ls *`, you will see all of the contents of a given directory. Now try this command: `ls ../thomas/*1` This lists every file in `nocs-shell/data/thomas` directory that ends with a `1`. This command:
 `ls /usr/bin/*.sh`
 Lists every file in `/usr/bin` that ends in the characters `.sh`. And this command: `ls *2*.csv`
 lists every file in the current directory which contains the number `2`, and ends with characters `.csv`. There are two such files: `Allsource-201205.csv` and `Tidal-EA-201205.csv`.So how does this actually work? Well...when the shell (bash) sees a word that contains the `*` character, it automatically looks for files that match the given pattern. In this case, it identified two such files. Then, it replaced the `*2*.csv` with the list of files, separated by spaces. In other the two commands:
 `ls *2*.csv  ls Allsource-201205.csv Tidal-EA-201205.csv`
are exactly identical. The `ls` command cannot tell the difference between these two things._____________________________________________________________________________________________________________________________________________________________________________________

