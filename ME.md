# Introduction

This is an introduction of me and why I am in ROAR.

## About Me

<b>Name</b>: Tianqin Wu  
<b>Prefered name</b>: William Wu  
<b>Grade</b>: I'll be a Junior next year  
<b>School</b>: Woodside Priory School  
<iframe src="https://www.prioryca.org/" width="800" height="400"></iframe><br><!--<-->
<b>Socials</b>:<br>  
<a href="mailto:williamwutq@gmail.com">williamwutq@gmail.com</a><br>  
<a href="https://github.com/williamwutq">Github: github.com/williamwutq</a><br>
And you can find my links on my github page.

## Hobbies

I'm not exactly a boring person, but don't have many hobbied either

Some of them are:
- Doing hardware projects (such as 3D printing)
- Robotics (I'm in FRC [Team 751](https://www.team751.com/) doing hardware design)
- Painting
- Coding
- Gaming (Mainly Minecraft and KSP)
- I'm a big spaceflight fan
- Writing stuff

I love to collabrate with friends on projects

I am not exactly the most into CS, and teaching a week of Java Swing doesn't make me a nerd.

## Languages I know
- C++
- Java
- Python
- Kotlin
- C#

## Current Projects

<b>[HappyHex](https://github.com/williamwutq/game_HappyHex)</b>

State: Released as .jar, Version 1.4.0  

A hexagonal Block Blast (e.g. Hex FRVR) implementation using java and python. The core of the game and the graphics interfaces are implemented with Java, while a python script, executed as a child process of the Java code, is used for autoplay.

Some notable features:
- Great GUI with multiple pages, interactive components, and animation.  
- Custom hexagonal system.  
- Multithreading and parallel processing that speeds up all kinds of things.  
- Game mode and size configurable via settings and (Only if you can find it) special features.  
- Multiple themes, such as normal, dark, white, and holiday special themes that are automatically activates on those days.  
- Log in and save files that include metadata as .hpyhex format, 700 times more space efficient compare to JSON alternative.  
- Autoplay (we will talk about this a bit more).  

<b>[InfinityHex](https://github.com/williamwutq/game_InfinityHex)</b>  

State: Just released **beta**

A hexagonal infinite Snake game implementation with C#. All code are writen in C#. UI is built with Avalonia UI with cross platform support.

Some notable features:
- Infinite snake grid with efficient cache management
- Custom hexagonal system. (Exact same as HappyHex's, but with `HexLib` acceleration) 
- Themes configurable via JSON
- Keyboard control

<b>EducationForAll</b>

State: In progress
My position: Chief Engineer, Backend

Collabrative project with my friends to develop a website that facilitates learning **resource sharing** between students. These resources can also be managed by the school and used with external resources such as plagiarism checkers.

I cannot disclose more information due to NDA.

<b>Dorm Improvements Projects</b>

I live in the dorms. This is a series of hardware projects driven by me to improve it.

- <b>Shower Improvements Project</b>:

  3D printed hooks and plates for people to put stuff and hang cloth when showing. Designed on Onshape, printed by me with Prusa3D, and assembled by dormers with the help of me. Two phases of the project are finished.  

- <b>Shower Improvements Project</b>: 
  
  An **ongoing** project as collabration with a friend for 30 mailboxes for each room. Designed on Onshape and Solidworks, production streamlines with fine-turned 3D printing and CNC.

## SMART Goals

**S**pecific:

In the near term, I want to enhance the autoplay of HappyHex to use an AI model. Currently, the autoplay use a non-recursive entropy based greedy minimax algorithm implemented with python. The algorithm performs better than many players but as the developer and one of the most skilled players in this game, I see future for improvements for an intelligent prediction model with reinforcement learning. The model is to pick the best move out of M * N, M being the number of moves and N being the number of placement positions.

In addition to that, I also want to participate in the ROAR competition and hopefully get into a real autonomous racing team in the future. This is because I always wanted to do things that combine hardware and software.

**M**easurable:

I will simulate thousands of games on python (I wrote the game core in both Java, Python, and C++) with both the original entropy based greedy minimax algorithm and the AI-driven algorithm. I also read the hundreds of .hpyhex files played by me and other plays. Then I calculate the lowest, average, and highest score obtained by the two algorithms and human players (.hpyhex file reader is built in both Java and Python). If the AI-driven algorithm is superior than both the human players and the original algorithm in that it obtain better lowest, average, and highest score, then I have achieved my goal.  

For the ROAR competition, the goal is to train a model that performs well in the competition. The competition is the benchmark.  

**A**ctionable:

For AI-driven Autoplay of HappyHex:
- Build the game core in Python and Java
- Build .hpyhex file reader and writer in Python and Java
- Build basic autoplay and write IPC
- Preformance enhancements
- Learn how to use Python for AI ← **I'm here**
- Wrote core with Tensorflow for training
- Arrange with a friend and train the model
- Benchmark the model, possible improvements
- RL
- Benchmark again for final results

For ROAR Competition:
- Learn advanced python and attend the ROAR Academy ← **I'm here**
- Trying to start a team with people I meet
- Design model for competition
- Train model
- Compete in the competition

**R**ealistic:

The AI-driven Autoplay of HappyHex is realistic because I already have a basic version of autoplay working in python, and I will have learned how to use python for AI in the ROAR Academy. I also have obtained enough game data stored in my game files, and have talked to a friend to borrow a Nvidia GPU.

The goal for ROAR Competition is actually even more realistic because I am right here, learning things that are exactly needed for this competition and can find help among you.

Do I have enought time? I am not the exactly busy type student in schoolwork and I do not have to do Robotics during the off season. My only two projects that will be continued in the semester concurrently is the Dorm Mailbox Project, of which I have designed and optimized the production process, and EducationForAll, of which I already wrote a bunch of backend code.

**T**imebound:

I set deadlines.

For HappyHex Autoplay, I want to finish the first round of training by the end of the semester. This will enable me to evaluate the results and start the reinforcement portion in the second semester. I want to finish that portion by the start of AP exams.

I'm particitating in the next round of ROAR Competition. This set the deadline to August 22, if the team can make it.