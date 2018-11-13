#! usr/bin/env/python

'''
FileMover developed by David Platt Copyright © 2018
FileMover is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

FileMover is distributed as a useful tool for linux users, but it is
distributed without any warranty or the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
'''
import os, sys, time, datetime, shutil

PATH =  "/home/dave/Downloads"
'''
checks in the donwloads folder for files downloaded today that can be
moved to Documents, Music, or Pictures puts them in a list of files to be moved
'''
def search_for_files():
    now = datetime.datetime.now().strftime("%d/%m/%y")
    files_to_move = []
    for files in os.listdir(PATH):
        try:
            full_file_p = PATH + "/" + files
            timestamp = os.path.getctime(full_file_p)
        except (FileNotFoundError, IOError):
            print("Could not find file named %s" % files)
            pass
        day_mo_yr = datetime.datetime.fromtimestamp(timestamp).strftime("%d/%m/%y")
        #print(day_mo_yr)
        if day_mo_yr == now:
            files_to_move.append(full_file_p)
            #print(files_to_move)
    if not files_to_move:
        input("No files were found that need to be moved. press any key to continue...")
        exit(0)
    else:
        return files_to_move
'''
checks if there are files to be moved, confirms the types of files to
be moved, puts them in the proper list for each file type
that is sent to the move files function
'''
def file_types():
    files_list = search_for_files()
    text_files = []
    music_files = []
    img_files = []
    if not files_list:
        input("No files were found that need to be moved. press any key to continue...")
        exit(0)

    for name in files_list:
        f_name, ext = os.path.splitext(name)
        if ext == ".txt" or ext == ".pdf" or ext == ".doc" or ext == ".docx":
            text_files.append(name)
        if ext == ".mp3":
            music_files.append(name)
            print(music_files)
        if ext == ".jpeg" or ext == ".jpg" or ext ==".img" or ext == ".png" or ext == ".gif" or ext == ".bmp":
            img_files.append(name)
    move_files(text_files, music_files, img_files)
'''
checks to see there are new files that can be moved to the specified folders for each type of files
'''
def move_files(txt_files, music_files, img_files):
    keywords = ["Document", "text", "Pictures", "image", "Music", "music"]
    user_in = None
    if not txt_files and not music_files and not img_files:
        print("There are no feels that need to be moved. press any key to continue...")
        input()
        exit(0)
    if txt_files:
        doc_path = "/home/dave/Documents"
        for path in txt_files:
            complete_move(keywords[1], keywords[0], path, doc_path)
        pass
    if music_files:
        music_path = "/home/dave/Music"
        for path in music_files:
            complete_move(keywords[5], keywords[4], path, music_path)
        pass
    if img_files:
        pic_path = "/home/dave/Pictures"
        for path in img_files:
            complete_move(keywords[3], keywords[2], path, pic_path)
        pass
'''
function moves the files to the correct folder
'''
def complete_move(folder, file_type, file_path, new_path):
        user_in = input("Would you like to move new " + file_type + " files to your "
        + folder + " folder Y/N")
        if user_in.upper() == "Y":
            shutil.move(file_path, new_path)
            f_name, ext = os.path.splitext(file_path)
            print("You have moved the following file: " + f_name)
        else:
            print("Your " + file_type + " file(s) are still in the Downloads folder")
            pass
            
def main():
    file_types()

if __name__ == "__main__" :
    main()
