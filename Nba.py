# python3 code to rank NBA teams

import urllib.request, re
from numpy import *

print("Running NBA power ranking code.  Please wait while 30 web pages load...")

Teams = ["ATL","BOS","BRK","CHO","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL",
         "MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHO","POR","SAC","SAS","TOR",
         "UTA","WAS"]

matrix = []

for team in Teams:
    url = "http://www.basketball-reference.com/teams/" + team + "/2018/splits/"
    html = urllib.request.urlopen(url).read().decode('utf-8')
    row = []
    for opponent in Teams:
        find = "/teams/" + opponent + "/2018\D*\d"
        games = int(re.search(find,html).group()[-1]) if re.search(find,html) else 0
        find += "\D*\d"        
        wins = int(re.search(find,html).group()[-1]) if games != 0 else 0
        row += [games - wins]
    matrix += [[r*1.0/sum(row) for r in row]]

matrix = [list(x) for x in zip(*matrix)] 
eigenvalues, eigenvectors = linalg.eig(array(matrix))

ranking = eigenvectors[:,argmax(eigenvalues)]
scaled_ranking = [r*1.0/sum(ranking) for r in ranking]
power_rank = [(real(a).round(3),b) for (a,b) in zip(scaled_ranking, Teams)]
power_rank.sort(reverse=True)

for rank, team in power_rank:
    print(team, rank)
