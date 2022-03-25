# foxCsv.py
import csv
import random
import string

from datetime import datetime

class FoxCsv():
    def __init__(self, args):
        self.rows = int(args.r)
        self.output_path = args.o
        self.columns = args.c

    def get_random_string(self, length):
        # choose from all lowercase and upper letter
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    
    def create(self):
        now = datetime.now() # current date and time
        
        fileName = now.strftime("%Y-%m-%d-%H-%M-%S.csv") # YYYY-MM-DD-HH_MM_SS.csv

        # open the file in the write mode
        f = open(f"{self.output_path}/{fileName}", 'w', encoding='UTF8', newline='')

        # create the csv writer
        writer = csv.writer(f)

        new_column = []
        for v in range(len(self.columns)):
            col = self.columns[v].split(',')
            new_column.append(col)

        # write a header to the csv file
        column_names = [item[0] for item in new_column]
        writer.writerow(column_names)
        
        # write a row to the csv file
        column_types = [item[1] for item in new_column]
        rows = []
        for i in range(self.rows):
            row = []
            for column_type in column_types:
                match column_type:
                    case 'int':
                        row.append("%0.10d" % random.randint(0,9999999999))
                    case 'string':
                        row.append(self.get_random_string(random.randint(1, 10)))
            rows.append(row)
        writer.writerows(rows)

        # close the file
        f.close()