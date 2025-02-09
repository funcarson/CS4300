#Lists and Dicts

#Lists of fav books
fav_books = ["Lord of the Flies by William Golding", "Farenheight 451 By Ray Bradbury", "1984 by George Orwell", "Eye of Minds, by James Dashner" ]

#Gets the length of the list
book_length = len(fav_books)

#Prints only 3 books
for i in range(book_length -1):
    print(fav_books[i])

#Student Database Dict
student_database = {
    "Alice Johnson": "S001",
    "Bob Smith": "S002",
    "Charlie Brown": "S003",
    "Diana Prince": "S004"
}

#Prints the dict
for student, student_id in student_database.items():
    print(f"Student Name: {student}, Student ID: {student_id}")