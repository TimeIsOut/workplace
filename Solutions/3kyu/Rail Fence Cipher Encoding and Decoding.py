def encode_rail_fence_cipher(string, n, for_solving=False):  # Little remark: using flag for decoding func.
    array = [[""] * len(string) for _ in range(n)]  # Drawing the rails.
    checking, catch = 0, 1
    for i, k in zip(string, range(len(string))):  # Writing data for our rails with the rule.
        array[checking][k] = i
        if checking == n - 1 and catch == 1:
            catch = -1
        elif checking == 0 and catch == -1:
            catch = 1
        checking += catch
    string = ''.join([''.join(i) for i in array]) # Joining strings.
    if for_solving is True:  # Key for the decoding (raw rails data).
        return array
    return string


def decode_rail_fence_cipher(string, n):
    map = encode_rail_fence_cipher(string, n, True)  # For map only.
    count = 0
    for i in map:  # Re-drawing the rails.
        for j in range(len(i)):
            if i[j] != "":
                i[j] = string[count]
                count += 1
    map = [list(''.join(i)) for i in map]  # Joining strings to remove empty indexes.
    list_checking, catch, answer, f = [0] * n, 0, "", 1
    print(map)
    for _ in range(len(string)):  # Reading strings in the rails' order.
        answer += map[catch][list_checking[catch]]
        list_checking[catch] += 1
        if catch == 0 and len(answer) > 1:
            f = 1
        elif catch == n - 1 and answer:
            f = -1
        catch += f
    return answer