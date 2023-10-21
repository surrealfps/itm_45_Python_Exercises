'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member="joaquin",to_member="chums",social_graph={
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            relationship_status = " is friends with"
        else:
            relationship_status = " is followed by"
    else:
        if from_member in social_graph[to_member]["following"]:
                relationship_status = " is a follower of"
        else:
                relationship_status = " has no relationship with"
    print("User " + from_member + relationship_status + " the user " + to_member)
    return


def tic_tac_toe(board=[
['X','X','O'],
['O','X','O'],
['X','','O'],
]):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    grid = len(board)
    row = 0
    column = 0
    for a in board:
        sumset_horizontal = set(board[row])
        if len(sumset_horizontal)==1:
            print(str(sumset_horizontal), " is the winner")
            return
        row += 1
    if len(set([board[x][x] for x in range(3)])) == 1:
        print(str(set([board[x][x] for x in range(3)])) + " is the winner")
        return
    if len(set([board[3-1-y][y] for y in range(3)])) == 1:
        print(str(set([board[y][y] for y in range(3)])) + " is the winner")
        return
    vertical_board = [z for z in zip(*board)]
    for b in board:
        sumset_vertical = set(vertical_board[column])
        if len(sumset_vertical)==1:
            print(str(sumset_vertical), " is the winner")
            return
        column += 1
    return("There is no winner")

def eta(first_stop="upd",second_stop="admu",route_map = {
    ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    a = 0
    legs = list(route_map.keys())
    count = len(legs)
    while a<count:
        if (str(first_stop),legs[a][1]) in legs:
            tmp_stop1 = str(first_stop + "," + legs[a][1])
            travel_time += route_map[(first_stop,legs[a][1])]["travel_time_mins"]
            break
        a += 1
    if a>=count-1:
        b = 0
    else:
        b = a+1
    c = 0
    if (first_stop,second_stop) in legs:
        return("Estimated Time of Arrival: " + str(travel_time) + " mins")
    else:
        while c<count:
            if (legs[b][0],second_stop) in route_map.keys():
                tmp_stop2 = str(legs[b])
                travel_time += route_map[(legs[b])]["travel_time_mins"]
                break
            else:
                tmp_stop2 = str(legs[b])
                travel_time += route_map[(legs[b])]["travel_time_mins"]
            b += 1
            c += 1
            if b>=count:
                b=0
    print("Estimated Time of Arrival: " + str(travel_time) + " mins")
