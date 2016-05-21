3. Language Specs - Builtin Variables
*************************************

To keep the code short, Tellurium has some builtin variables that when used, expand to useful values such as 100 and 1000.

3.1 "!H" - 100
==============

The !H variable expands to the value 100.
For example:

``µ!H~^`` outputs 100.

3.2 "!K" - 1000
===============

The !K variable expands to the value 1000.
For example:

``[!K|+]`` adds one to the cell's value 1000 times.

3.3 "!a" - Lowercase alphabet
=============================

The !a variable expands to the lowercase alphabet, "abcdefghijklmnopqrstuvwxyz".
Example:

``µ!a~^`` displays the lowercase alphabet.

3.4 "!A" - Uppercase alphabet
=============================

The !A variable expands to the uppercase alphabet, "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
Example:

``µ!A~^`` displays the uppercase alphabet.

3.5 "´" - Newline
=================

The ´ variable works like a newline. (\n)
Example:

``µHello´there~^`` displays "Hello\nthere".
