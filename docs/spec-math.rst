4. Language specs - Math
************************

Tellurium has some builtin math commands, which make it easier to calculate.
The four basic math commands (a, s, m, d) take the value in the current cell, and the value in the next cell, and add/subtract/etc. them. The result is stored in the selected cell.

For example, ``+>+<a^`` adds 1+1 and displays the result.

4.1 - "a" Addition
==================

``a`` is the addition command, which adds two values together and stores the result in the selected cell.
Example: ``+>+<a^`` calculates 1+1.

4.2 - "s" Subtraction
=====================

``s`` is the subtraction command. It subtracts two values and stores the result in the selected cell.
Example: ``/>++<s^`` calculates 11-2.

4.3 - "m" Multiplication
========================

``m`` is the multiplication command. It multiplies two values and stores the result in the selected cell.
Example: ``+++>+++<m^`` calculates 3*3.

4.4 - "d" Divison
=================

``d`` is the division command. It divides two values and stores the result in the selected cell.
Example: ``/>++<d^`` calculates 10/2.

4.5 - "§" Factorial
===================

``§`` calculates the factorial of the cell's value.
Example: ``µ200~n§^`` outputs 120.

4.6 - "½" Exponent
==================

``½`` calculates the exponent of the cell's value.
Example: `µ5~n½^`` outputs 148.4131591025766.

4.7 - "q" Square Root
=====================

``q`` calculates the square root of the cell's value.
Example: ``µ5~nq^`` outputs 2.23606797749979.

4.8 - "c" Ceiling
=================

``c`` calculates the ceiling of the cell's value.
Example: ``µ5.5~fc^`` outputs 6.

4.9 - "g" Floor
===============

``g`` calculates the floor of the cell's value.
Example: ``µ7.2~fg^`` outputs 7.

4.10 - "F" Fibonacci
====================

``F`` calculates the nth Fibonacci number (n is the cell's value) and stores it in the next cell.
Example: ``++++++F>^`` outputs 8.

4.11 - "I" Integer Input
========================

``I`` gets input and converts it to an integer.
Example: ``IT`` outputs "Integer".

4.12 - "n" Integer
==================

``n`` converts the selected cell's value to an integer.
Example: ``in`` gets input and converts it to an integer.

4.13 - "f" Float
================

``f`` converts the selected cell's value to a float. Useful for doing math with numbers that have decimals.
Example: ``in`` gets input and converts it to a float.
