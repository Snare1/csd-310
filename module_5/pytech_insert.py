"""
    Title: pytech_insert.py
    Author: Sara Babauta
    Date: 6 February 2022
    Description: Test program for inserting new documents into the students collection
"""

""" import statements"""
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.xxikp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connection to the MongoDB cluster
client = MongoClient(url)

#connect to pytech database
db = client.pytech

""" three student documents """
# Peter Piper's document
peter = {
    "student_id": "1007",
    "first_name": "Peter",
    "last_name": "Piper",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.7",
            "start_date": "January 4, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "ARTH100",
                    "description": "Intro to Art History",
                    "instructor": "Bob Ross",
                    "grade": "B"       
                },
                {
                    "course_id": "MATH200",
                    "description": "Algebra",
                    "instructor": "Albert Einstein",
                    "grade": "C+"
                }
            ]
        }
    ]
}            

# Michael Jackson's data document
michael = {
    "student_id": "1008",
    "first_name": "Michael",
    "last_name": "Jackson",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.0",
            "start_date": "January 4, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "BIOL220",
                    "description": "Biology",
                    "instructor": "Whitney Houston",
                    "grade": "A-"
                },
                {
                    "course_id": "MATH200",
                    "description": "Algebra",
                    "instructor": "Albert Einstein",
                    "grade": "A+"     
                }
            ]
        }
    ]
}

# Jason Momoa's data document
jason = {
    "student_id": "1009",
    "first_name": "Jason",
    "last_name": "Momoa",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.4",
            "start_date": "January 4, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "PSY330",
                    "description": "Advanced Psychology",
                    "instructor": "Dr. Suess",
                    "grade": "A"
                },
                {
                    "course_id": "MATH200",
                    "description": "Algebra",
                    "instructor": "Albert Einstein",
                    "grade": "B-"      
                }
            ]
        }
    ]
}

# get the student collection
students = db.students

#insert statements with output
print("\n --INSERT STATEMENTS --")
print("\n --INSERT STATEMENTSS --")
peter_student_id = students.insert_one(peter).inserted_id
print(" Inserted student record Peter Piper into the students collection with student_id " + str(peter_student_id))
print(" Inserted student record Peter Piper into the students collection with document_id " + str(peter_student_id))

michael_student_id = students.insert_one(michael).inserted_id
print(" Inserted student record Michael Jackson into the students collection with student_id " + str(michael_student_id))
print(" Inserted student record Micahel Jackson into the students collection with document_id " + str(michael_student_id))

jason_student_id = students.insert_one(jason).inserted_id
print(" Inserted student record Jason Momoa into the students collection with student_id " + str(jason_student_id))
print(" Inserted student record Jason Momoa into the students collection with document_id " + str(jason_student_id))

input("\n\n End of program, press any key to exit...")
