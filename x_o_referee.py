def checkio(game_result):
    result = ''
    # Check for rows and cols
    for i in range(0,3):
        if(game_result[0][i]== game_result[1][i] == game_result[2][i]):
            if(game_result[0][i] != '.'):
                result = game_result[0][i]
                break
        elif(game_result[i][0]== game_result[i][1] == game_result[i][2]):
            if(game_result[i][0] != '.'):
                result = game_result[i][0]
                break
        else:
            result = "D"
    # Check for diagonal
    if(game_result[0][0]== game_result[1][1] == game_result[2][2]) or (game_result[0][2]== game_result[1][1] == game_result[2][0]):
        if(game_result[1][1] != '.'):
            result = game_result[1][1]
    # No results?Draw.
    if result=='':
        result = "D"
    return result
