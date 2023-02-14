# to use on linux use mpg123
# apt install mpg123

import os

def main():
    # Get file list
    path = "/home/sarah/Music/"
    dir_list = os.listdir(path)

    #get a song
    filename = dir_list[0]
    print(filename)

    # escape spaces by wrapping in quotes
    fullpath = path + '"' + filename + '"'
 
    # Play the song
    os.system('mpg123 ' + fullpath)

    # on mac afplay stands for audio file play
    # os.system("afplay " + file_name)


main()
