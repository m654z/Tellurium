6. Language specs - Conditional statements
******************************************

Conditional statements, also known as if-statements, are built into Tellurium.

The basic syntax of conditionals in Tellurium is: ``?value|code]``.

6.1 Examples
============

6.1.1 Example 1
===============

If the input is 0, output "0" forever.

``I?0|[i|^]]``

6.1.2 Example 2
===============

If the input is ``a``, output "Hello".

``i?a|µHello~^]``