n,m,t = map(int,input().split())
teams,teams_to_t, victories, matches = [], [], {}, {}
matches_to_play = n-1
for i in range(n):
    team = input()
    teams.append(team)
    if team not in victories:
        victories[team] = 0
    if team not in matches:
        matches[team] = 0
for i in range(m):
    team_1,team_2,score_1,score_2 = input().strip().split(":")
    score_1,score_2 = int(score_1),int(score_2)
    matches[team_1]+=1
    matches[team_2]+=1
    if score_1>score_2:
        victories[team_1] +=1
    else:
        victories[team_2] +=1
for team in teams:
    if victories[team]==t:
        teams_to_t.append(team)
    elif (victories[team]+(matches_to_play-matches[team]))>=t:
        teams_to_t.append(team)
teams_to_t.sort()
for team in teams_to_t:
    print(team)
