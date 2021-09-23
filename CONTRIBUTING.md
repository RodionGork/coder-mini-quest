# Contributing to Coder's Mini Quest

Thanks for your intention to help with this project!

Let me quickly explain how you are supposed to do this.

### Two main ways to contribute

Quest consists of text descriptions of places through
which the user is "travelling" - and of programming exercises
encountered here and there. So naturally you can either:

1. Help improving the text - phrases, words, spelling, grammar etc.
2. Create or improve "checkers" - small programs which generate data
  for exercises, and later check user's answer.

As about 1-st way - it's pretty clear, though it is worth to understand how
the project works (we shall provide description in separate file).

### How Checker works

Look in the `cgi-bin/dat` folder. Here, besides text files are small programs
(e.g. `3410.sh` or `3410.py`). Each of them serves some specific challenge.

It could be executed in two ways - to generate data - and to check answer.

In both cases program should use the first argument from command line
as a "seed" for randomizer. It is going to be the same both when we generate
data for user and later when we check answer - so you'll be able to check
answer for exactly the data which user previously got from you :)

Second argument, if exists, is the answer itself.

If the answer is absent, produce brief problem statement text and then
the input data.

If the answer is here, check it and produce response message. Text of
response is simply shown to user (so technically it doesn't matter) - but
in case of "success" it should end with some flag to set. It is a brief
word separated with colon from the text.

### Example

Consider the exercise requiring user to provide "sum of squares" of two
numbers. In case of success flag "blade" should be produced.

```py
import random
import sys

random.seed(int(sys.argv[1]))

a = random.randint(100, 999)
b = random.randint(100, 999)

if len(sys.argv) == 2:
    # no answer yet, just generate data
    print("Calculate the Sum-of-Squares of these numbers:")
    print("%d %d" % (a, b))
else:
    # check the provided answer
    answer = int(sys.argv[2]) #bad code, ensure no conversion error
    if a ** 2 + b ** 2 == answer:
        print("You have found an ancient sword. Let's chop someone...:blade")
    else:
        print("Try harder, that was close.")
```