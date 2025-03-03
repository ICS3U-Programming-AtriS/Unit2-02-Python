#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 1, 2025
# Program that calculates the circumference of a circle,
# using tau and user-defined radius
import constants


def main():
    # Get the Radius from the user
    radius = float(input("Enter the radius (cm): "))

    # Calculate the circumference
    circumference = constants.TAU * radius

    # Display the circumference to the user
    print(f"The circumference is {circumference:.2f}cm")


if __name__ == "__main__":
    main()
