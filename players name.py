def exactly_two(players):
    """
    Get hold of players who play exactly two sports

    Argument:
        players: dict of dicts
    Return:
        result: set of strings
    """
    #print(players)
    '''
    count = 0
    for name in players:
        #print(name)
        #print(players[name])
        for sport in players[name]:
            #print(players[name][s])
            if (players[name][sport] == True):
                count += 1
                print(count)
                #continue
        l = []
        if count == 2:
            l.append(name)
            #print(l)
            s = set(l)
            #print(s)
    return s
    '''

    pairs=[('Tennis','Cricket','Badminton'),('Badminton','Tennis','Cricket'),('Cricket','Badminton','Tennis')]
    names=set()
    for player in players:
        for s1,s2,s3 in pairs:
            if(players[player][s1] and players[player][s2] and (not players[player][s3])):
                names.add(player)
    return names

p1 = {'Ram': {'Tennis': False, 'Cricket': True, 'Badminton': True}, 'Rahim': {'Tennis': False, 'Cricket': True, 'Badminton': True}, 'Richard': {'Tennis': True, 'Cricket': False, 'Badminton': False}, 'Ravi': {'Tennis': False, 'Cricket': True, 'Badminton': True}, 'Rooney': {'Tennis': False, 'Cricket': False, 'Badminton': True}, 'Reshma': {'Tennis': False, 'Cricket': True, 'Badminton': False}, 'Radika': {'Tennis': False, 'Cricket': False, 'Badminton': False}, 'Ranjani': {'Tennis': True, 'Cricket': True, 'Badminton': True}, 'Rama': {'Tennis': False, 'Cricket': True, 'Badminton': True}, 'Rani': {'Tennis': True, 'Cricket': True, 'Badminton': False}}

p2 = {'Ram': {'Tennis': False, 'Cricket': False, 'Badminton': False}, 'Rahim': {'Tennis': False, 'Cricket': True, 'Badminton': False}, 'Richard': {'Tennis': True, 'Cricket': False, 'Badminton': False}, 'Ravi': {'Tennis': True, 'Cricket': True, 'Badminton': True}, 'Rooney': {'Tennis': True, 'Cricket': False, 'Badminton': False}, 'Reshma': {'Tennis': False, 'Cricket': True, 'Badminton': True}, 'Radika': {'Tennis': True, 'Cricket': False, 'Badminton': True}, 'Ranjani': {'Tennis': True, 'Cricket': False, 'Badminton': True}, 'Rama': {'Tennis': True, 'Cricket': False, 'Badminton': False}, 'Rani': {'Tennis': False, 'Cricket': True, 'Badminton': True}}

print(exactly_two(p2))