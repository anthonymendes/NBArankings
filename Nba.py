# python2.7 code to rank NBA teams; written by Tony Mendes (aamendes@calpoly.edu)
import urllib, re
from numpy import *

Teams = ["ATL","BOS","BRK","CHO","CHI","CLE","DAL","DEN","DET","GSW",
         "HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK",
         "OKC","ORL","PHI","PHO","POR","SAC","SAS","TOR","UTA","WAS"]

matrix = []

for team in Teams:
    url = "http://www.basketball-reference.com/teams/" + team + "/2017/splits/"
    f = urllib.urlopen(url)
    html = f.read()
    f.close()
    row = []
    for opponent in Teams:
        find = "/teams/" + opponent + "/2017\D*\d"
        games = int(re.search(find,html).group()[-1]) if re.search(find,html) else 0
        find += "\D*\d"        
        wins = int(re.search(find,html).group()[-1]) if games != 0 else 0
        row += [games - wins]
    matrix += [[r*1.0/sum(row) for r in row]]
matrix = [list(x) for x in zip(*matrix)] 

eigenvalues, eigenvectors = linalg.eig(array(matrix))
ranking = eigenvectors[:,argmax(eigenvalues)]

scaled_ranking = [r*1.0/sum(ranking) for r in ranking]
power_rank = zip(scaled_ranking, Teams)
power_rank.sort(reverse=True)

print eigenvalues

for rank, team in power_rank:
    print rank, team
