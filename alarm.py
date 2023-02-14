# to use on linux use mpg123
# apt install mpg123

import os
import random

def main():
    # Get file list
    folder_path = "/home/sarah/Music/"
    song_list = os.listdir(folder_path)

    # Shuffle
    random.shuffle(song_list)

    for filename in song_list:
        #get a song
        print(filename)

        # escape spaces by wrapping in quotes
        full_path = folder_path + '"' + filename + '"'
    
        # Play the song
        os.system('mpg123 ' + full_path)

        # on mac afplay stands for audio file play
        # os.system("afplay " + file_name)


main()
