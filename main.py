from PIL import Image
import numpy as np

"""
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
"""

# pixel_perfect = bool(int(input('Pixel perfect\nIf off, size is double.\n 0 - On    1 - Off\n')))
num = np.power(int(input('Input uneven number\n')), 2)
while not int(np.mod(np.sqrt(num), 2)):
    num = int(input('Input uneven number\n'))
sqrn = int(np.sqrt(num))
array = [[0 for i in range(sqrn)] for i in range(sqrn)]
prev = 1

center = int(np.divide(sqrn, 2))

for i in range(np.add(center, 1)):
    if not i:
        array[center][center] = 1
        continue
    array[np.add(center, i)][np.add(center, i)] = np.add(np.multiply(8, i), prev)
    for j in range(2 * i + 1):
        if not j:
            continue
        array[np.add(center, i)][np.subtract(np.add(center, i), j)] = np.subtract(np.add(np.multiply(8, i), prev), j)
    for k in range(np.add(np.multiply(i, 2), 1)):
        if not k:
            continue
        array[np.subtract(np.add(center, i), k)][np.subtract(np.add(center, i), j)] = np.subtract(
            np.subtract(np.add(np.multiply(8, i), prev), j), k)
    prev = array[np.add(center, i)][np.add(center, i)]

for i in range(np.add(center, 1)):
    if not i:
        continue
    prev = array[np.subtract(center, i)][np.subtract(center, i)]
    for j in range(np.add(np.multiply(i, 2), 1)):
        if not j:
            continue
        array[np.subtract(center, i)][np.add(np.subtract(center, i), j)] = np.subtract(
            array[np.subtract(center, i)][np.subtract(np.add(np.subtract(center, i), j), 1)], 1)
    for k in range(np.add(np.multiply(i, 2), 1)):
        if not k:
            continue
        if array[np.add(np.subtract(center, i), k)][np.add(np.subtract(center, i), j)]:
            break
        array[np.add(np.subtract(center, i), k)][np.add(np.subtract(center, i), j)] = np.subtract(
            array[np.subtract(np.add(np.subtract(center, i), k), 1)][np.add(np.subtract(center, i), j)], 1)
prime = [2, 3]
for i in range(np.add(num, 1)):
    if not np.mod(i, 1000):
        print(f'Calculating {i}, {round(np.multiply(np.divide(i, num), 100), 2)}% done')
    nope = False
    if i < 4:
        continue
    for j in prime:
        if j < 2:
            continue
        if np.mod(i, j) == 0:
            nope = True
            break
    if nope:
        continue
    prime.append(i)
# 1 is not a prime number
# prime.append(1)
prime.sort()

perc = 0
img = Image.new(mode='RGB', size=[np.multiply(sqrn, 2), np.multiply(sqrn, 2)], color='black')
for j, i in enumerate(array):
    if perc + 5 <= round(j / len(array) * 100, 2):
        print(f'Drawing {round(j / len(array) * 100, 2)}%')
        perc = round(j / len(array) * 100, 2)
    for l, k in enumerate(i):
        if k in prime:
            img.putpixel([np.multiply(l, 2), np.multiply(j, 2)], (255, 255, 255, 0))
            img.putpixel([np.add(np.multiply(l, 2), 1), np.multiply(j, 2)], (255, 255, 255, 0))
            img.putpixel([np.multiply(l, 2), np.add(np.multiply(j, 2), 1)], (255, 255, 255, 0))
            img.putpixel([np.add(np.multiply(l, 2), 1), np.add(np.multiply(j, 2), 1)], (255, 255, 255, 0))
img.save(f'sop_{num}.png')
print('Done')
print(f'File "sop_{num}.png" created.')
input('Press Enter to exit...')
