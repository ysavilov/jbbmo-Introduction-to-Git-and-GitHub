#!/bin/bash
# This script calculates simple interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)
# Addtional Authors:
# <your Github username>

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# simple interest = p*t*r

echo "Enter the principal:"
read P
echo "Enter rate of interest per year:"
read R
echo "Enter time period in years:"
read T

S=$(expr $P \* $T \* $R / 100)
echo "The simple interest is: "
echo $S
