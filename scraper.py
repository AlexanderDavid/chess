# chess.com API -> https://www.chess.com/news/view/published-data-api
# The API has been used to download monthly archives for a user using a Python3 program.
# This program works as of 24/09/2018
# https://www.reddit.com/r/chess/comments/9ifkaq/how_i_downloaded_all_my_chesscom_games_using/

import urllib
import urllib.request
from pathlib import Path
from os import mkdir
from tqdm import tqdm

username = "hikaru" #change 
baseUrl = "https://api.chess.com/pub/player/" + username + "/games/"
archivesUrl = baseUrl + "archives"

#read the archives url and store in a list
f = urllib.request.urlopen(archivesUrl)
archives = f.read().decode("utf-8")
archives = archives.replace("{\"archives\":[\"", "\",\"")
archivesList = archives.split("\",\"" + baseUrl)
archivesList[len(archivesList)-1] = archivesList[len(archivesList)-1].rstrip("\"]}")

if not Path(f"./{username}").exists():
    mkdir(f"./{username}")

#download all the archives
for i in tqdm(range(len(archivesList)-1)):
    url = baseUrl + archivesList[i+1] + "/pgn"
    filename = archivesList[i+1].replace("/", "-")

    if Path(f"./{username}/{filename}.pgn").exists():
        continue
    
    urllib.request.urlretrieve(url, f"./{username}/{filename}.pgn") #change
    print(filename + ".pgn has been downloaded.")

print ("All files have been downloaded.")
