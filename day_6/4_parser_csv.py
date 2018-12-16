import csv

with open('date.csv','r') as fisier:
    parser_csv = csv.reader(fisier, delimiter=',')
    for row in parser_csv:
        # print(row)
        if(row[0] == 'Singapore'):
            print("GDP pentru Singapore = {}".format(row[3]))