def tournamentWinner(competitions, results):
    # Write your code here.
    dic = {}

    for opponents_ids, opponents in enumerate(competitions):
        winner = results[opponents_ids]
        pos = 0
        if winner == 0:
            pos = 1
        if opponents[pos] in dic:
            dic[opponents[pos]] += 3
        else:
            dic[opponents[pos]] = 3

    max_key = max(dic, key=dic.get)
    return max_key

competitions = [
    ["HTML","C#"],
    ["C#","Python"],
    ["Python","HTML"]
]
results = [0,0,1]
print(tournamentWinner(competitions, results))
