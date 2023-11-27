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
from csv import reader
from matplotlib import pyplot
def test(file_path):
    dates = []
    prices = []
    # seeing if file path exists
    try:
        infile = open(file_path)
    except FileNotFoundError:
        print("File not found")
    csvReader = reader(infile)
    # appending dates and respective prices
    for row in csvReader:
        dates.append(row[0])
        prices.append(float(row[1]))

    # creating graph with data
    pyplot.xlim(500, 600)
    pyplot.barh(range(len(dates)), prices)
    pyplot.yticks(range(len(dates)), dates)
    pyplot.ylabel("Date")
    pyplot.xlabel("Opening Price in USD")
    pyplot.show()

def main():
    file_path = "google.csv"
    test(file_path)

if __name__ == '__main__':
    main()