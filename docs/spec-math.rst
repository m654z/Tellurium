4. Language specs - Math
************************

Tellurium has some builtin math commands, which make it easier to calculate.
The commands take the value in the current cell, and the value in the next cell, and add/subtract/etc. them. The result is stored in the selected cell.

For example, ``+>+<a^`` adds 1+1 and displays the result.

4.1 - "a"
=========

``a`` is the addition command, which adds two values together and stores the result in the selected cell.
Example: ``+>+<a^`` calculates 1+1.

4.2 - "s"
=========

``s`` is the subtraction command. It subtracts two values and stores the result in the selected cell.
Example: ``/>++<s^`` calculates 11-2.

4.3 - "m"
=========

``m`` is the multiplication command. It multiplies two values and stores the result in the selected cell.
Example: ``+++>+++<m^`` calculates 3*3.

4.4 - "d"
=========

``d`` is the division command. It divides two values and stores the result in the selected cell.
Example: ``/>++<d^`` calculates 10/2.

4.5 - "n"
=========

``n`` converts the selected cell's value to an integer.
Example: ``in`` gets input and converts it to an integer.

4.6 - "f":
==========

``f`` converts the selected cell's value to a float. Useful for doing math with numbers that have decimals.
Example: ``in`` gets input and converts it to a float.
