import omdb
import csv

with open("movie_names", 'r') as f:
    names = f.read().splitlines()


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
            if omdb.imdbid(omdb.search(n)[0].imdb_id).metascore == 'N/A':
                invnames.append(n)
            else:
                metascore.append(omdb.imdbid(omdb.search(n)[0].imdb_id).metascore)
    return title, invnames, metascore


def writetxt(invtitles):
    with open("invalid_titles.txt", 'w') as i:
        for t in invtitles:
            i.write(t)


def writecsv(header, titles, bids):
    ratings = [[k, int(v)] for k, v in dict(zip(titles, bids)).items()]
    with open("ratings.csv", 'w', newline='') as r:
        csvwriter = csv.writer(r, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, )
        csvwriter.writerow(header)
        csvwriter.writerows(ratings)


header = ["Title", "Metascore"]
titles = search(names)[0]
invtitles = "\n".join(search(names)[1])
bids = search(names)[2]

writetxt(invtitles)
writecsv(header, titles, bids)
