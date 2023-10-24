# -*- coding: utf-8 -*-
"""
This is a simple script to obtain the file path to the newest or most recently
produced local PDF file.
"""

import glob
import os

# Generate pdf_folder path string.
pdf_folder = os.path.dirname(__file__)

# Create pdf_files list.
pdf_files = list(glob.glob(os.path.join(pdf_folder, '*.pdf*')))

# Produce modified date list.
mod_dates = [os.path.getmtime(f) for f in pdf_files]

# Create list of tuples, with each tuple having PDF file paths and their
# respective modified dates.
pdf_file_date_list = list(zip(pdf_files, mod_dates))

# Sort tuple list by descending modified dates.
def sort_tuple_list_reverse_chron(tup_list):
    tup_list.sort(key = lambda x: x[1], reverse = True)
    return tup_list

pdf_file_date_list = sort_tuple_list_reverse_chron(pdf_file_date_list)

newest_pdf_file_path = pdf_file_date_list[0][0]