# Better Numbers!


### ``class N`` Methods
Deals with **integers** in all bases greater than one.
> Note: Floats not implemented yet.

- ``n.to_base_ten()``
Returns the base ten equivalent of ``n``
- ``n.to_base(self, b: int)``
Return the base ``b`` equivalent of ``n``

### ``class N`` Operations
For the following operations, if they are in different bases it returns the result in the base of the first number.
- ``<N> - <N>``
Subtracts the two numbers.
- ``<N> + <N>``
Adds the two numbers.
- ``<N> * <N>``
Multiplies the two numbers.
- ``<N> / <N>``
Divides the two numbers, and returns an integer.
- ``<N> % <N>``
Remainder/Modulo function.
- ``abs(<N>)``
Return the absolute value of ``n``.
- ``n.op(func, *others)``
Returns the result of ``func(n, *others)``, if other operations aren't enough.
- ``n.is_prime()``
Return the boolean value of if it's a prime or not.
