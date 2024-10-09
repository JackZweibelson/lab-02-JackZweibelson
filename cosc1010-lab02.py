
# Jack Zweibelson
# UWYO COSC 1010
# 10/9/24
# HW 01
# Lab Section:
# Sources, people worked with, help given to:
# Chatgpt to give me an indpeth explanation of the importance of .items() while I also was analyzing lecture 9 notes
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student
#and their scores
# in different subjects.
#
# Student Data:
students = [
 {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
 {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
 {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
 {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]
#Write a Python program that:
# 1. Calculates the average score for each student.

for i in students:
    avg = sum(i["scores"].values())/len(i["scores"])
    print(f'{i["name"]} has an average of {avg}')

# 2. Stores these averages in a new dictionary where the student’s name is the key
#and their average score is the value.

grades = {}

for i in students:
    avg = sum(i["scores"].values())/len(i["scores"])
    grades[i["name"]] = avg
print(grades)

# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names
# of students whose average score is greater than 80.

for name, average in grades.items():
    if average > 80:
        print(f'{name} has an average greater than 80')

