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
    planets = []
    masses = []
    # opening file and using csvReader to read in the data
    try:
        infile = open("planets.csv")
    except FileNotFoundError:
        print("No such directory")
    csvReader = reader(infile)
    count = 0
    # getting data and appending to list but only the planet names and
    # their respective mass
    for row in csvReader:
        if count == 0:
            for i in range(1, 11):
                planets.append(row[i])
        elif count == 1:
            for i in range(1, 11):
                masses.append(float(row[i]))
        else:
            break
        count += 1
    # setting up graph and showing it to user
    pyplot.xticks(rotation=45)
    pyplot.yscale('log')
    pyplot.bar(planets, masses)
    pyplot.xlabel("Planet")
    pyplot.ylabel("Mass")
    pyplot.tight_layout()
    pyplot.show()


if __name__ == '__main__':
    main()
