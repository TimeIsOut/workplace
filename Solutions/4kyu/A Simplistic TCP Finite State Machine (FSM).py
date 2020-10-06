def traverse_TCP_states(events):
    dic = {'APP_PASSIVE_OPEN': [['CLOSED', 'LISTEN']], 'APP_ACTIVE_OPEN': [['CLOSED', 'SYN_SENT']],
           'RCV_SYN': [['LISTEN', 'SYN_RCVD'], ['SYN_SENT', 'SYN_RCVD']], 'APP_SEND': [['LISTEN', 'SYN_SENT']],
           'APP_CLOSE': [['LISTEN', 'CLOSED'], ['SYN_RCVD', 'FIN_WAIT_1'], ['SYN_SENT', 'CLOSED'], ['ESTABLISHED', 'FIN_WAIT_1'], ['CLOSE_WAIT', 'LAST_ACK']],
           'RCV_ACK': [['SYN_RCVD', 'ESTABLISHED'], ['FIN_WAIT_1', 'FIN_WAIT_2'], ['CLOSING', 'TIME_WAIT'], ['LAST_ACK', 'CLOSED']],
           'RCV_SYN_ACK': [['SYN_SENT', 'ESTABLISHED']], 'RCV_FIN': [['ESTABLISHED', 'CLOSE_WAIT'], ['FIN_WAIT_1', 'CLOSING'], ['FIN_WAIT_2', 'TIME_WAIT']],
           'RCV_FIN_ACK': [['FIN_WAIT_1', 'TIME_WAIT']], 'APP_TIMEOUT': [['TIME_WAIT', 'CLOSED']]}
    state = "CLOSED"
    for i in events:
        f = 0
        for j in dic[i]:
            if j[0] == state:
                state = j[1]
                f = 1
                break
        if not f:
            return "ERROR"
    return state