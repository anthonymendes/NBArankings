The file Nba.py contains python code to rank the 30 NBA basketball teams using the
"pagerank" or Perron eigenvector method.  The idea is as follows.

Imagine a graph with each node one of the 30 NBA teams.  A directed edge from team A to team B exists every time A has lost a basketball game to team B.

Randomly select a start team, say A.  Randomly follow an edge from team A to another team,
say team B.  Then randomly follow an edge from team B to team C. Keep following edges many
times over, say a million times.

After we finally stop, the idea is that we will land on a higher ranked team more often
than a lower ranked team.

Let M be the matrix with A, B entry the probability that team B will land on team A after
one step.  Then multiplying by M gives one step in the random walk.

There is a special eigenvector r which has entries in [0,1] such that M r = r.  This is an
eigenvector with eigenvalue 1.  This r gives the probabilities of landing on a certain
team.
