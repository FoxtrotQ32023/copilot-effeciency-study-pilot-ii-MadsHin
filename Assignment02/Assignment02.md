# __String Multimatching__

## __Input__
The input (_stringmultimatching.in_) consists of at most ten test cases.  
Each test case begins with an integer n on a line of its own, indicating the number of patterns. Then follow _n_ lines, each containing a non-empty pattern.  
The total length of all patterns in a test case is no more than 100.000.  
Then comes a line containing a non-empty text (of length at most 200.000).  
Input is terminated by end-of-file

## __Output__
For each test case, output n lines, where the _i_’th line contains the positions of all the occurrences of the _i_’th pattern in text, from first to last, separated by a single space.

## __Sample Input 1__

```
2
p
pup
Popup
2
You
peek a boo
you speek a bootiful language
4
anas
ana
an
a
bananananaspaj
```

## __Sample Output 1__

```
2 4
2

5
7
1 3 5 7
1 3 5 7
1 3 5 7 9 12
```

## __Problem Description__
I am tasked with finding the number of occurences (if any) of a number of substrings, n, in one string, S. The sum of chars across the n substrings cannot exceed 100.000, and the number of chars in S cannot exceed 200.000. 
There are multiple independent problems listed in the same file, and so an additional task is handling how to loop through the file to find and solve one problem at a time. The file is terminated by EOF.
As per the example we are handling the substring pattern matching with case sensitivty.
