# to use on linux use mpg123
# apt install mpg123

import os

def main():
    # location of the mp3 file
    file_name = "suprabatham.mp3"
    # os.system("mpg123 " + file) on linux
    # on mac afplay stands for audio file play
    os.system("afplay " + file_name)


main()
