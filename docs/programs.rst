2. Simple Tellurium Programs
****************************

Let's have a look at some simple programs you can create using Tellurium.

2.1 Input
=========

Getting input from the user is quite simple: use the ``i`` command. It gets input and stores it in the selected cell.

2.1.1 Cat
---------

A cat program, named after the Unix command cat, is a simple program that copies its input to its input. For example, if the user inputs "Hello", the program will output "Hello".
The Tellurium version of cat is quite short:
``i^``

``i``, as you remember, is the input command. ``^`` outputs whatever is in the selected cell. In the cat program, it's what the user input.

2.1.2 Hello, user (ugly output version)
---------------------------------------

This program will ask for the user's name, and output "Hello, (name)".
``µWhat is your name?~^i>µHello, ~^<^``

Don't worry, this is easy to explain.

* ``µWhat is your name?~^`` - "What is your name?" is stored in a cell and displayed.
* ``i`` - The program asks for input
* ``>`` - Go to the next cell on the tape
* ``µHello, ~^`` - Display "Hello, "
* ``<^`` -  Go to the previous cell and display its value (which is the input)

You might have noticed that "Hello, " and the name are on separate lines. We'll fix that right now.

2.1.3 Hello, user (nicer output version)
----------------------------------------

OK, let me explain something first. Tellurium has so many one-character commands that it was beginning to get a bit hard to implement new ones. Well, when I was trying to implement string manipulation commands, I created a "string manipulation mode", that can be used with the ``&`` command. String mode has separate commands for basic string manipulation. In this example, we'll be using the ``b`` command, which is the "append to front" command.

``µWhat is your name?~i&bHello, ~.^``

* You'll recognize the first part from example 2.1.2.
* ``&bHello, ~`` appends "Hello, " to the beginning of the selected cell's value.
* ``.`` exits string manipulation mode.

Try it out. The output is now "Hello, (name)" instead of "Hello,[newline](name)".

2.2 Loops
=========

2.2.1 Countdown
---------------

Loops in Tellurium are easy to use. The basic syntax is ``[times|code]``.
Let's create a countdown from 10 to 1.

``/+[10|-^]``

* ``/+`` adds eleven to the selected cell's value.
* ``[10|-^]`` - subtracts one from the value and outputs it ten times.

2.2.2 Fancy countdown
---------------------

Let's change the code from 2.2.1 to display the number at a speed of one per second. All you need to do is add the `¨` command, which waits 1 second before continuing.

``/+[10|-^¨]``


2.3 Functions
=============

Functions are pieces of code with a name, that can be "called", or run, from any place in the program. In Tellurium, creating functions is simple: ``@name|code```
Let's create a function that counts down from 10, using the program from 2.2.2.

``@count|/+[10|-^¨]-```

The extra ``-`` is there to make the function runnable more than one time. (It subtracts the 1 from the cell)
To call the function, you'll want to do ``=name.``. Let's call our ``count`` function.

``=count.``

You'll see the program count down from 10.

2.4 Variables
=============

Tellurium has an infinite amount of variables. To set a variable, the syntax is ``¤name|value]``. To set the value of the selected cell to a variable's value, you can to ``;name.``.
Let's make a variable called "h" that contains the text "Hello".

``¤h|Hello]``.

To display that variable, you can do ``;h.^``.
