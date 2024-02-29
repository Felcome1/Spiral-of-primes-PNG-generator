Spiral of primes

This code creates an image (1:1) of spiral of primes with given resolution.
Resolution must be uneven to be symmetric and avoid bugs.
After getting an input given number multiplies by itself.
It could take time to calculate huge numbers ( > 200**2 ).

In my interpretation it works like this:
1. Get an input ( *input* );
2. Create an array with *input* arrays, containing *input* items (0);
3. Put (1) in array[int( *input* / 2 ) + 1][int( *input* / 2) ] as it's center of entire array;
4. Put key numbers in diagonal down-right;
5. Moving from array[int( *input* / 2 ) + 2] upside down, right-side left starting of diagonally placed numbers and symmetrically stops;
6. Changing direction clockwise; 
7. Calculating prime numbers in given range;
8. Replasing numbers in array with 1 for prime numbers and 0 if not;
9. Generating picture using data from array.
10. Done!
