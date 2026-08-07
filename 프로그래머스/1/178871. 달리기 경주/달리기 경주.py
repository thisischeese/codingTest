def solution(names, callings):
    # 선수 : 순서 
    players = {names[i]:i for i in range(len(names))}
    # 순서 : 선수 -> idx가 이미 순서 역할 수행 
    orders = names[:]
    
    for player in callings:
        # 현재 순서 정보 조회 
        order = players[player]
        prev_player = orders[order-1]
        
        # 순서 정보 변경 
        orders[order-1] = player 
        orders[order] = prev_player
        
        # 선수 정보 변경 
        players[player] = order-1 
        players[prev_player] = order 

    return orders