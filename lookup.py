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

import os, errno
import sqlite3 as dbase

# Define variables to be used
user_db = dbase.connect('user.db') # connect to or create user database for scanned/imported UPC's
disc_db = dbase.connect('dvd_list.db') #connect to list of physical media for the purpose of UPC crossover

movies_directory = "resources/temp/movies/" # movie library directory variable
directory_to_add = "discs" # movie folder variable
textfilecontents = "<discstub> <title> No location available</title>    <message> No location was given.</message>  </discstub>"
movie_url = "http://database.com/movie"

# Define function to create directory.
def mk_file(file_path, title, file_conents,movieurl):
    try:
        os.makedirs(file_path)
    except Exception as e:
        if e != errno.EEXIST:
            # print("error is EEXIST")
            # os.rmdir(file_path)
            # os.makedirs(file_path)
            # raise
            print("Folder already exists")
            pass
    else:
        print("made file folder. no errors")
    finally:
        try:
            print("Making disc file")
            make_file = open(
                '{path}/{movie_title}.dvd.disk'.format(path=file_path, movie_title=title), 'w')
            # information to enter into file
            make_file.write(file_conents)
            # close the file
            make_file.close()
            print('done')
            print("Making nfo file")
            make_file = open(
                '{path}/{movie_title}.nfo'.format(path=file_path, movie_title=title), 'w')
            # information to enter into file
            make_file.write(movieurl)
            # close the file
            make_file.close()
        except OSError as e:
            if e.errno != errno.EEXIST:
                print(e)
                raise
        else:
            print("Made file successfully")


mk_file(movies_directory + directory_to_add, 'movietitle', textfilecontents, movie_url)

# upc_input = raw_input('Enter number to find\n')

# class lookup:
#     "UPC Lookup class"
#     def __init__(self):
#         self.upc_in = upc_in
#         self.disc_title = disc_title