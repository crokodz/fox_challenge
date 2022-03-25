# main.py
import sys
import argparse
from foxCsv import FoxCsv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store', metavar='Rows', required=True)
    parser.add_argument('-o', action='store', metavar='Output_Path', default='.')
    parser.add_argument('-c', action='store', metavar='Column_Name,Column_Type', required=True, nargs='*')
    args = parser.parse_args()

    c = FoxCsv(args)
    c.create()