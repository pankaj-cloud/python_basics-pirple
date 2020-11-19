"""
Homework Assignment #7: : Dictionaries and Sets
Details:
Return to your first homework assignments, when you described your favorite song.
Refactor that code so all the variables are held as dictionary keys and value.
Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.

"""
Song = {
"Artist" : "Drake",
"SongName" : "Fake Love",
"AlbumName" : "More Life",
"Genre" : "Alternative R&B",
"DurationInSeconds" : 196.80,
"DurationInMinutes" : 3.28,
"YearReleased" : 2016,
"DateofRelease" : "October 29",
"Songwriters" : " Aubrey Graham, Brittany Hazzard, Anderson Hernandez, Adam Feeney ",
"Producers" : " Vinylz Frank Dukes ",
}
for key, value in Song.items():
    print(key, value)
