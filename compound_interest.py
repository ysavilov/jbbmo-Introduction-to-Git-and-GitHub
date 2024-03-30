# This script calculates yearly compound interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)

# Input:
# P, principal amount
# T, time period in years
# R, annual rate of interest

# Output:
# compound interest = P * (1 + R/100)^T


def compound_interest(P, T, R):
    return P * (pow((1 + R / 100), T))


if __name__ == "__main__":
    P = float(input("Enter the principal amount: "))
    T = float(input("Enter the time period: "))
    R = float(input("Enter the rate of interest: "))

    print("The compound interest is {:.2f}".format(compound_interest(P, T, R)))
