5. Language specs - String manipulation
***************************************

Tellurium has a special command, ``&``, that lets you use basic string manipulation commands. Using ``&`` brings the program into "string manipulation mode", so you can't use normal commands until you bring it out of string mode using the ``.`` command.

5.1 - "r" Reverse
=================

``r`` reverses a string that is in the selected cell.
Usage:

``µHello~&r.^`` outputs "olleH".

5.2 - "u" Uppercase
===================

``u`` makes a string uppercase.
Usage:

``µHello~&u.^`` outputs "HELLO".

5.3 - "l" Lowercase
===================

``l`` makes a string lowercase.
Usage:

``µHELLO~&l.^`` outputs "hello".

5.4 - "a" Append to end
=======================

``a`` appends text to the end of a string.
Syntax: ``&atext~.``
Usage:

``µHe~&allo~.^`` outputs "Hello".

5.5 - "b" Append to front
=========================

``b`` appends text to the front of a string.
Syntax: ``&btext~.``
Usage:

``µllo~&bHe~.^`` outputs "Hello".
