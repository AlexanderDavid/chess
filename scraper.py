# chess.com API -> https://www.chess.com/news/view/published-data-api
# The API has been used to download monthly archives for a user using a Python3 program.
# This program works as of 24/09/2018
# https://www.reddit.com/r/chess/comments/9ifkaq/how_i_downloaded_all_my_chesscom_games_using/

import urllib
import urllib.request
from pathlib import Path
from tqdm import tqdm
import argparse
import json

parser = argparse.ArgumentParser(description="Scrape all archived player games from chess.com")

parser.add_argument("-b", "--base", type=Path, default="./data", help="base of the path to download games to")
parser.add_argument("username", type=lambda x: str(x).lower(), help="user to download archive of")

args = parser.parse_args()

base_url = "https://api.chess.com/pub/player/" + args.username + "/games/"
archives_url = base_url + "archives"

# read the archives url and store in a list
f = urllib.request.urlopen(archives_url)
result = json.loads(f.read().decode("utf-8"))
archives = result["archives"]

if not (args.base / args.username).exists():
    Path(args.base / args.username).mkdir(parents=True)

#download all the archives
for archive in tqdm(archives):
    url = archive + "/pgn"
    filename = args.base / args.username / ("_".join(archive.split("/")[-2:]) + ".pgn")

    if filename.exists(): continue
    
    urllib.request.urlretrieve(url, filename)

print ("All files have been downloaded.")
