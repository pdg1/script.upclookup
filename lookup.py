# Incomplete.
# todo ISSUE1: The movie titles coming from file are irregular and not groomed to be file names.
# solutions could be;
# use Unicode to sanitize the file names.
# Can scrapers get URL information from media stub files. Maybe folders with media stub file and NFO file
#
# RESULT. can use NFO file with scraper URL. use ID number as folder name?
# NFO file and .disc file must have same name as folder.
#
#     todo ISSUE2: need solution for tv shows on dvd/bluray
# one tv dvd/bluray will have multiple episodes
# 
# IDEA: create database in kodi for physical items. could include support for items such as Comic books / CBR's,
# Books / eBooks, CD's(?), trading cards, etc.


import csv, os, errno
import sqlite3 as dbase

# Define variables to be used
user_db = dbase.connect('user.db') # connect to or create user database for scanned/imported UPC's
disc_db = dbase.connect('dvd_list.db') #connect to list of physical media for the purpose of UPC crossover

movies_directory = "resources/temp/movies" # movie library directory variable
directory_to_add = "test" # movie folder variable

# read csv, and split on "," the line
scanned_upc_list = csv.reader(open(scan_movie_upc, "rb"), delimiter=",")
upc_input = raw_input('Enter number to find\n')

class lookup:
    "UPC Lookup class"
    def __init__(self):
        self.upc_in = upc_in
        self.disc_title = disc_title

    def makedirectory():
        try:
            os.makedirs(movies_directory + "/" + directory_to_add)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


# Define function to create directory. todo add argument for movie ID

def mk_file(title): # Define function with argument title (returned movie title from csv_search)
    # make file at file path indicated with argument title
    make_file = open('C:\Users\Ryan\Desktop\movies\%s.dvd.disk' % title, 'w')
    # information to enter into file
    make_file.write(
        "<discstub> <title> No location available</title>    <message> No location was given.</message>  </discstub>")
    # close the file
    make_file.close()
