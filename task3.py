"""
Name(s): Christian Ninh and Jinku Tang
Due Date: 11/24/23
Assignment: Ch.7 Project (File I/O)
Description: Reading in a file and outputting and graphing data
Academic Honesty Pledge: We, Christian Ninh and Jinku Tang, do hereby certify that we
have derived no assistance for this project from any sources other than those listed as references.
References: Python for Everyone 2e
[Code Only] Replit: https://replit.com/@cninh27/Ch7Project
"""

from matplotlib import pyplot
from csv import reader


def main():
    # defining 2 lists to hold data
    movies = []
    years = []
    # opening file and using csvReader to read in the data
    try:
        infile = open("movies.csv")
    except FileNotFoundError:
        print("No such directory")
    csvReader = reader(infile)
    count = 0
    # getting the first 30 movies and adding it to list data
    for row in csvReader:
        if count == 0:
            pass
        elif count < 30:
            movies.append(row[0])
            years.append(int(row[1]))
        else:
            break
        count += 1

    # setting up graph and showing it to user
    pyplot.figure(figsize=(15,6))
    pyplot.ylim(1800, 2100)
    pyplot.xticks(rotation=90)
    pyplot.plot(movies, years, "c--o")
    pyplot.xlabel("Movie")
    pyplot.ylabel("Release Year")
    pyplot.tight_layout()
    pyplot.show()


if __name__ == '__main__':
    main()
