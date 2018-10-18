#! usr/bin/env/python

import os, sys, time, datetime, shutil

PATH =  "C:\\Users\\Admin\\Downloads"
#############333
def search_for_files():
    now = datetime.datetime.now().strftime("%d/%m/%y")
    files_to_move = []
    for files in os.listdir(PATH):
        try:
            full_file_p = PATH + "\\" + files
            timestamp = os.path.getctime(full_file_p)
        except (FileNotFoundError, IOError):
            print("Could not find file named %s" % files)
            pass
        day_mo_yr = datetime.datetime.fromtimestamp(timestamp).strftime("%d/%m/%y")
        #print(day_mo_yr)
        if day_mo_yr == now:
            print("True")
            files_to_move.append(full_file_p)
            #print(files_to_move)
            return files_to_move

    if not files_to_move:
        input("No files were found that need to be moved. press any key to continue...")
        exit(0)
##############33
def file_types():
    files_list = search_for_files()
    text_files = []
    music_files = []
    img_files = []
    if len(files_list) == 0:
        input("No files were found that need to be moved. press any key to continue...")
        exit(0)

    for name in files_list:
        f_name, ext = os.path.splitext(name)
        if ext == ".txt" or ext == ".pdf" or ext == ".doc" or ext == ".docx":
            text_files.append(name)
        elif ext == ".mp3":
            music_files.append(name)
        elif ext == ".jpeg" or ext == ".jpg" or ext ==".img" or ext == ".png" or ext == ".gif" or ext == ".bmp":
            img_files.append(name)

    move_files(text_files, music_files, img_files)
#########33
def move_files(txt_files, music_files, img_files):
    keywords = ["Document", "text", "Pictures", "image", "Music", "music"]
    user_in = None
    if txt_files:
        user_in = input("Would you like to move new " + keywords[1] + " files to your " + keywords[0] + " folder Y/N")
        if user_in.upper() == "Y":
            for paths in txt_files:
                shutil.move(paths, "C:\\Users\\Admin\\Documents")
                f_name, ext = os.path.splitext(paths)
                print("You have moved the following file: " + f_name)
        else:
            print("Your text file(s) are still in the Downloads folder")
            pass
    else:
        print(False)
    if music_files:
        user_in = input("Would you like to move new " + keywords[5] + " files to your " + keywords[4] + " folder Y/N")
        if user_in.upper() == "Y":
            for paths in music_files:
                shutil.move(paths, "C:\\Users\\Admin\\Music")
                f_name, ext = os.path.splitext(paths)
                print("You have moved the following file: " + f_name)
        else:
            print("Your" + keywords[5] + "file(s) are still in the Downloads folder")
            pass
    if img_files:
        user_in = input("Would you like to move new " + keywords[3] + " files to your " + keywords[2] + " folder Y/N")
        if user_in.upper() == "Y":
            for paths in img_files:
                shutil.move(paths, "C:\\Users\\Admin\\Pictures")
                f_name, ext = os.path.splitext(paths)
                print("You have moved the following file: " + f_name)
        else:
            print("Your " + keywords[3] + " file(s) are still in the Downloads folder")
            pass
################
def main():
    file_types()

if __name__ == "__main__" :
    main()
