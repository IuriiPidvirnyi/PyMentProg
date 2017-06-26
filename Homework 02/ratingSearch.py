# coding=utf-8
# !/usr/bin/env python

import omdb
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("movies_path", help="Path to input file with movie names specified")
parser.add_argument("-r", "--ratings_path", help="Path to output file with movie ratings")
parser.add_argument("-e", "--errors_path", help="Path to output file with movie names produced errors")
args = parser.parse_args()
print args.movies_path, args.ratings_path, args.errors_path

MOVIES = args.movies_path
RATINGS = args.ratings_path
ERRORS = args.errors_path


def open_and_read(MOVIES):
    try:
        with open(MOVIES) as f:
            names = f.read().splitlines()
            return names
    except IOError:
        print "Cannot open the {0} file".format(MOVIES)


def search(names):
    title = []
    invnames = []
    metascore = []
    for n in names:
        try:
            omdb.imdbid(omdb.search(n)[0].imdb_id).metascore
        except:
            invnames.append(n)
        else:
            title.append(omdb.search(n)[0].title)
            if not omdb.imdbid(omdb.search(n)[0].imdb_id).metascore:
                invnames.append(n)
            else:
                metascore.append(omdb.imdbid(omdb.search(n)[0].imdb_id).metascore)
    return title, invnames, metascore


def writetxt(invtitles, ERRORS="invalid_titles.txt"):
    with open(ERRORS, 'w') as i:
        for t in invtitles:
            i.write(t)


def writecsv(header, titles, bids, RATINGS='ratings.csv'):
    ratings = [[k, int(v)] for k, v in dict(zip(titles, bids)).items()]
    with open(RATINGS, 'w') as r:
        csvwriter = csv.writer(r, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, )
        csvwriter.writerow(header)
        csvwriter.writerows(ratings)


def main():
    header = ["Title", "Metascore"]
    names = open_and_read(MOVIES)
    titles = search(names)[0]
    invtitle = "\n".join(search(names)[1])
    bids = search(names)[2]
    if not args.errors_path:
        writetxt(invtitle)
    elif args.errors_path:
        writetxt(invtitle, ERRORS)
    if not args.ratings_path:
        writecsv(header, titles, bids)
    elif args.ratings_path:
        writecsv(header, titles, bids, RATINGS)


if __name__ == "__main__":
    main()
