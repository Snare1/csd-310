""" 
    Title: pytech_queries.py
    Author: Sara Babauta
    Date: 6 February 2022
    Description: Test program for updating a document in the pytech collection
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.xxikp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

    # test document
test_doc = {
    "student_id": "1010",
    "first_name": "Johnny",
    "last_name": "Bravo"
}

test_doc_id = students.insert_one(test_doc).inserted_id

print("\n --INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id " + str(test_doc_id))

student_test_doc = students.find_one({"student_id": "1010"})

# display message
print("\n  -- DISPLAYING STUDENT TEST DOC --")

print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

deleted_student_test_doc = students.delete_one({"student_id": "1010"})

new_student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FORM find() QUERY --")

for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name:" + doc["first_name"] + "\n Last Name:" + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")