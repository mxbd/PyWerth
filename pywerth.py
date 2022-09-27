# import neccesary libraries
import os
import csv
import re

# for Werth-Tactile protocols measurement data normally starts on line 28
# lines before that are information regarding the test program

# if analyzing protocols where INFO_END is not always the same set to 0
# as lines starting with # are filtered anyway

INFO_END = 0
ID_LINE = 11 # ID-Number is in line 11

# True sets decimal output (English), False sets comma output (German)
DECIMAL = False

# prompts user to enter file paths
# ref_path : Path to reference protocol which will be used to determine headers
# protocols_path : Path to directory with .txt files to analyze (must contain only protocols!)
# output_path : Path to directory where output.csv should be saved

while True:
    ref_path = input("\nEnter path to reference protocol.txt :\n> ")

    if (os.path.exists(ref_path) and ref_path.endswith('.txt')):
        break
    print("Path does not exist! Please try again...")

while True:
    protocol_path = input("\nEnter path to the folder containing the protocols :\n> ")

    if (os.path.exists(protocol_path)):
        break
    print("Path does not exist! Please try again...")

while True:
    output_path = input("\nEnter path to store output.csv :\n> ")

    if (os.path.exists(output_path)):
        break
    print("Path does not exist! Please try again...")

while True:
    output_fname = input("\nEnter output csv filename (without extension):\n> ")

    if (re.match("^[0-9a-zA-Z_-]+$", output_fname)):
        break
    print("Wrong formatting! Please try again...")


# initialize variables to store data
CsvFile = []
headers = []
row = []

headers.append("ID-Number")

# open reference file for processing
with open(ref_path, 'r', encoding = "ISO-8859-1") as ref_file:

    # read the file line-by-line
    reader = ref_file.readlines()

    # extract ID-Number
    ID_NUMBER = reader[ID_LINE].split(' ')[-1].replace('\n','')

    # add ID-Number to row
    row.append(ID_NUMBER)

    # loop through file to extract header data and corresponding values
    for i,x in enumerate(reader):

        if (i > INFO_END):

            items = [x for x in x.split(' ') if x]

            # ignore lines without measurement values
            if ('#' not in x.split(' ')[0] and len(items) > 6):

                # clean data of unwanted elements leaving only numerical values
                clean = [s.replace('°', '') for s in items]

                # add col names, add col values
                if DECIMAL == True:
                    headers.append(clean[-1].replace('\n',''))
                    row.append(clean[1])
                else:
                    items_comma = [s.replace('.',',') for s in clean]
                    headers.append(items_comma[-1].replace('\n',''))
                    row.append(items_comma[1])

    # add row to csv file
    CsvFile.append(row)


# loop through list of files in protocol dir
for number, filename in enumerate(os.listdir(protocol_path)):

    # initialize new row for each file in dir
    row = []
    for x in headers:
        row.append('')

    if (os.path.join(protocol_path, filename).replace('\\', '') != ref_path.replace('\\', '')):

        with open (os.path.join(protocol_path, filename), encoding = "ISO-8859-1") as f:

            reader = f.readlines()

            ID_NUMBER = reader[ID_LINE].split(' ')[-1].replace('\n','')

            row[0] = ID_NUMBER

            for i,x in enumerate(reader):

                if (i > INFO_END):

                    items = [x for x in x.split(' ') if x]

                    if ('#' not in x.split(' ')[0] and len(items) > 6):

                        clean = [s.replace('°', '') for s in items]

                        if DECIMAL == True:
                            # based on ref file headers add corresponding values
                            try:
                                index = headers.index(clean[-1].replace('\n',''))
                                row[index] = clean[1]
                            except ValueError:
                                pass
                        else:

                            items_comma = [s.replace('.',',') for s in clean]

                            try:
                                index = headers.index(items_comma[-1].replace('\n',''))
                                row[index] = items_comma[1]
                            except ValueError:
                                pass

        # add row to csv
        CsvFile.append(row)
        print("Analyzing...", filename)

# sort csv rows ascending order according to ID-Number
CsvFile.sort()

# insert headers
CsvFile.insert(0, headers)

# export csv to output path
with open(os.path.join(output_path, output_fname + '.csv'), 'w', newline='') as csv_file:

    writer = csv.writer(csv_file, delimiter=';')

    for x in CsvFile:
        if (x not in ['', ' ']):
            writer.writerow(x)


print("\n********************************************************************")

print(f"""\nProtocols analysed sucessfully! Path to generated CSV:\n
> {os.path.join(output_path, output_fname + '.csv')}""")

print("\n********************************************************************")