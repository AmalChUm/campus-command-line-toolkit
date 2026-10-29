# Guide to tool naming and interface

This is a simple guide for how the tools should be named and how the interface should work.

## Tool Interface

The interface for the tool should follow the simple template of AUTHOR, APP_NAME, run().
AUTHOR should have the name of the person making the tool.
APP_NAME should simply be the name given to the app. It should be a self-explanatory name that tells you exactly what the app does without needing much of a explanation.
run() should just be the code that runs the app. Elements used in the code should have comments explaining how the code works.
This is the basis for how the interface within the tool should work.

## Tool Naming

The naming conventions within the tool should have some sort of relation to the tool. For instance, if you're trying to make a random dice roller, the name of the app should probably be something along the lines of "d<number> roller" which would explain what the app is pretty well.
The naming should be simple within the code too. For instance, if you are using randint to give a random number, the name should probably be rand_num = randint.(1,20) just to give an idea of what it could be. This should be the sort of convention used throughout the code. Just simple phrases related to what that part of the App's code is meant to do/be about.

## Final steps

The last things that should be mentioned are just some small things about the tool. The tool should make sure it is on topic and doesn't sway from the topic at hand with the tool. There should also be no private informatiion added, and lastly the README should be updated with the new tool info. These are just add-ons that should be done.