# -*- coding: utf-8 -*-
# Filippo Riva
# CS1000
# Fall 2024
#
# Group roles:
#   - Lucas: Spoken person
#   - Bryce: Process Analyst
#   - Filippo: Manager
#   - Hugo: Quality assurance
#
# =============================================================================
# Homework Assignment #5
# Chapter 4 & 10: Graphics and Intro to OOP
# 5 questions worth 10 points each.
#
# NOTE:
# - This assignment uses graphics.py (NOT part of standard Python).
# - For Question 3, random is also not part of graphics.py (but it IS a standard
#   library). If your instructor considers "random" an extra library, replace
#   the random color selection with a fixed color change.
#
# IMPORTANT:
# - Graphics windows are interactive. Questions 1–3 open windows and wait for
#   mouse clicks.
# =============================================================================

# If graphics.py is in this folder:
import sys
sys.path.append("/Users/filipporiva/Documents/CS1000")

import graphics
from graphics import *


# =============================================================================
# Question #1
#
# Using the graphics.py library draw a jack-o-lantern.
# =============================================================================
def question1_draw_jack_o_lantern():
    win = GraphWin("Jack-o'-Lantern", 400, 400)
    win.setBackground("black")

    # Pumpkin body
    pumpkin_body = Circle(Point(200, 220), 100)
    pumpkin_body.setFill("orange")
    pumpkin_body.draw(win)

    # Stem
    stem = Rectangle(Point(190, 100), Point(210, 140))
    stem.setFill("dark green")
    stem.draw(win)

    # Eyes (triangles)
    left_eye = Polygon(Point(160, 190), Point(185, 170), Point(185, 210))
    left_eye.setFill("black")
    left_eye.draw(win)

    right_eye = Polygon(Point(240, 190), Point(215, 170), Point(215, 210))
    right_eye.setFill("black")
    right_eye.draw(win)

    # Nose (triangle)
    nose = Polygon(Point(200, 215), Point(190, 235), Point(210, 235))
    nose.setFill("black")
    nose.draw(win)

    # Mouth (simple zig/triangle style)
    mouth = Polygon(Point(150, 275), Point(200, 305), Point(250, 275))
    mouth.setFill("black")
    mouth.draw(win)

    # Keep window open until clicked
    win.getMouse()
    win.close()


# =============================================================================
# Question #2
#
# Using the graphics.py library, create a blank window.
# Accept two mouse clicks and draw a circle:
#   - 1st click = center
#   - 2nd click = point on the outside (radius distance)
#
# Distance formula:
#   d(P,Q) = sqrt( (x2-x1)^2 + (y2-y1)^2 )
#
# Use a 3rd mouse click to exit the program.
# =============================================================================
def question2_draw_circle_from_clicks():
    win = GraphWin("Circle from Clicks", 500, 500)

    # First click: center
    center = win.getMouse()
    x1 = center.getX()
    y1 = center.getY()
    print("Center coordinates:", x1, y1)

    # Second click: outer point (must be different)
    while True:
        outer = win.getMouse()
        x2 = outer.getX()
        y2 = outer.getY()
        print("Outer point coordinates:", x2, y2)

        if (x1, y1) != (x2, y2):
            break
        print("Outer point cannot be the same as the center. Please click again.")

    # Distance formula for radius
    radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print("Calculated radius:", radius)

    circle = Circle(center, radius)
    circle.draw(win)

    # Third click exits
    win.getMouse()
    win.close()


# =============================================================================
# Question #3
#
# Using the graphics.py library, draw 3 rectangles on the screen.
# If the user clicks inside one of the rectangles, change the color of that rectangle.
# If the user clicks inside the window but outside all rectangles, close the window.
#
# NOTE:
# This solution changes colors in a cycle (no random module needed).
# =============================================================================
def point_inside_rectangle(pt, rect):
    p1 = rect.getP1()
    p2 = rect.getP2()

    left = min(p1.getX(), p2.getX())
    right = max(p1.getX(), p2.getX())
    top = min(p1.getY(), p2.getY())
    bottom = max(p1.getY(), p2.getY())

    return left < pt.getX() < right and top < pt.getY() < bottom


def question3_rectangles_click_color():
    win = GraphWin("Rectangles", 500, 500)

    rect1 = Rectangle(Point(100, 50), Point(300, 150))
    rect2 = Rectangle(Point(100, 175), Point(300, 275))
    rect3 = Rectangle(Point(100, 300), Point(300, 400))

    rect1.draw(win)
    rect2.draw(win)
    rect3.draw(win)

    colors = ["grey", "green", "yellow", "blue", "red", "pink"]
    idx1 = 0
    idx2 = 0
    idx3 = 0

    while True:
        click = win.getMouse()

        if point_inside_rectangle(click, rect1):
            idx1 = (idx1 + 1) % len(colors)
            rect1.setFill(colors[idx1])

        elif point_inside_rectangle(click, rect2):
            idx2 = (idx2 + 1) % len(colors)
            rect2.setFill(colors[idx2])

        elif point_inside_rectangle(click, rect3):
            idx3 = (idx3 + 1) % len(colors)
            rect3.setFill(colors[idx3])

        else:
            win.close()
            break


# =============================================================================
# Question #4
#
# Extend the bankAccount class by allowing transfers between accounts.
#
# Scenario:
#   checking = BankAccount()
#   savings = BankAccount()
#   checking.deposit(500)
#   checking.transfer(200, savings)
#   print(checking.balance())  # 300
#   print(savings.balance())   # 200
# =============================================================================
class BankAccount:
    def __init__(self):
        self._balance = 0.0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def balance(self):
        return self._balance

    def transfer(self, amount, target_account):
        if amount < 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds for transfer.")

        self.withdraw(amount)
        target_account.deposit(amount)


def question4_test():
    checking = BankAccount()
    savings = BankAccount()

    checking.deposit(500)
    checking.transfer(200, savings)

    print("Checking balance:", checking.balance())  # 300
    print("Savings balance:", savings.balance())    # 200


# =============================================================================
# Question #5
#
# Create a class called Number that has one attribute called value.
# Create the following methods:
#   - isPrime: returns True if value is prime, False otherwise
#   - isEven: returns True if value is even, False otherwise
#   - squared: returns value squared
# =============================================================================
class Number:
    def __init__(self, value):
        self.value = value

    def isPrime(self):
        if self.value <= 1:
            return False
        if self.value == 2:
            return True
        if self.value % 2 == 0:
            return False

        i = 3
        while i * i <= self.value:
            if self.value % i == 0:
                return False
            i += 2
        return True

    def isEven(self):
        return self.value % 2 == 0

    def squared(self):
        return self.value ** 2


def question5_test():
    tests = [11, 58, 5, 1]
    for t in tests:
        num = Number(t)
        print("Number:", t)
        print("  isPrime:", num.isPrime())
        print("  isEven:", num.isEven())
        print("  squared:", num.squared())
        print()


# =============================================================================
# RUN (comment out any you do not want to run)
# =============================================================================
def main():
    # Q1–Q3 open graphics windows:
    question1_draw_jack_o_lantern()
    question2_draw_circle_from_clicks()
    question3_rectangles_click_color()

    # Q4–Q5 are console-based:
    print("===== Question 4 Test =====")
    question4_test()
    print()

    print("===== Question 5 Test =====")
    question5_test()


main()
