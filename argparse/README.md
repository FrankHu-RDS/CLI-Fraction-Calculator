# Calculator Welcome
Hello, welcome to the CLI fraction processor.
A command-line program that will take equations with whole numbers/mixed numbers/fractions as an input and produce a fractional result.

## Information regarding calculator
    Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
    Operands and operators shall be separated by one or more spaces
    Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
    Improper fractions and whole numbers are also allowed as operands 
    Only two operands are allowed

## Usage:
The -h command will show the below dialogue.

    Usage: process [-h] [--loglevel {debug,info,warning,error,critical}]
                {how-to,calc} {equation}

    Command line interface for the process package

    positional arguments:
    {how-to, calc}         Sub-commands

    optional arguments:
    -h, --help            show this help message and exit
    --loglevel            {debug,info,warning,error,critical}
                                     Log level

## Setup environment and run
Be sure to be using versions of python3 and up to handle negative numbers properly. This is discussed in the known-issues section.

The commands to setup and run this program are below, with the present working directory being argparse.
        
        python -m pip install -e .
        python -m process how-to
        python -m process -h
        python -m process calc '{equation}'


## Example runs:
    python -m process calc '1/2 * 3_3/4'
         Output : 1_7/8
    python -m process calc '2_3/8 + 9/8'
         Output: 3_1/2
    python -m process calc '2_3/8 + 9/8'
         Output:   '3_4/8'
    python -m process calc '2/4 + 3/4'
         Output:   '1_1/4'
    python -m process calc '3_1/2 + 10/20'
         Output:   '4'
    python -m process calc '2 + 3'
         Output:   '5'
    python -m process calc '1_1/2 + 1_7/8'
         Output:   '3_3/8'
    python -m process calc '1/2 / 7/8'
         Output:   '8/14'
    python -m process calc '2_100/200 / 3/8'
         Output:   '6_400/600'
    python -m process calc '2 / 4'
         Output:   '2/4'
    python -m process calc '1_2/3 / 4_1/10'
         Output:   '50/123'
    python -m process calc '2 / 1_4/3'
         Output:   '6/7'
    python -m process calc '2_2/3 / 2_4/3'
         Output:   '24/30'
    python -m process calc '2/3 / 4/9'
         Output:   '1_6/12'
    python -m process calc '2 + 4'
         Output:   '6'
    python -m process calc '2/5 + 4/10'
         Output:   '8/10'
    python -m process calc '2_2/5 + 1_4/10'
         Output:   '3_8/10'
    python -m process calc '2 + 1_4/10'
         Output:   '3_4/10'
    python -m process calc '0 + 1_4/10'
         Output:   '1_4/10'
    python -m process calc '2 * 4'
         Output:   '8'
    python -m process calc '2/5 * 4/10'
         Output:   '8/50'
    python -m process calc '2_2/5 * 1_4/10'
         Output:   '3_18/50'
    python -m process calc '2 * 1_4/10'
         Output:   '2_8/10'
    python -m process calc '0 * 1_4/10'
         Output:   '0'
    python -m process calc '2 - 4'
         Output:   '-2'
    python -m process calc '2/5 - 4/10'
         Output:   '0'
    python -m process calc '2_2/5 - 1_4/10'
         Output:   '1'
    python -m process calc '2 - 1_4/10'
         Output:   '6/10'
    python -m process calc '0 - 1_4/10'
         Output:   '-1_4/10'

## Edge Cases Tested: (See edge test cases file for more details)
    python -m process calc '2/3 / 0'
    python -m process calc '2/3 / 1/0'
    python -m process calc 
    python -m process calc 'asdf'
    python -m process calc 'asdf asdf asdf'
    python -m process calc '2_10 / 2'
    python -m process calc  '10 asdf 10'

## Loglevel details:
There are also different loglevels utilized. I utilized loglevel debug to track debugging the system.
    
    Example run: python -m process --loglevel debug calc '2_3/8 + 9/8'

## Testing
In process > cli > tests, you will find all unit tests for this program. 

To run the tests use the command below while in the argparse directory.
    
    python -m pytest -v

![alt text](PyTest%20Results.png)

## Known Issues
In order for negative numbers to work properly, you will need to use python3 versions and up.
This is because of a known python2 division discrepancy found here : https://www.python.org/dev/peps/pep-0238/

For example when you do 8/-7, you will receive -2 in python2, however you will receive -1 in python3.
This is because it the result is using integer division and is being rounded down toward the more negative value of -2. (This is also known as "Floor division")

In order to get proper results, using python3 is suggested.



# CLI using argparse

This is an example using the recommended pattern as explained here:

https://docs.python.org/3/library/argparse.html#sub-commands

Tests always go via `main`, like execution from the command line would.
