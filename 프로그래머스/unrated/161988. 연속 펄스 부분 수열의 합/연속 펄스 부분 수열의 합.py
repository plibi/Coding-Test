def solution(sequence):
    answer = 0
    
    seq_len = len(sequence)
    seq_1 = [s if i % 2 == 0 else -s for i, s in enumerate(sequence)]  # [1, -1, ...]
    seq_2 = [-s if i % 2 == 0 else s for i, s in enumerate(sequence)]  # [-1, 1, ...]
    
    dp1 = [0 for __ in range(seq_len)]
    dp2 = [0 for __ in range(seq_len)]
    dp1[0] = seq_1[0]
    dp2[0] = seq_2[0]
    for i in range(1, seq_len):
        dp1[i] = max(0, dp1[i-1]) + seq_1[i]
        dp2[i] = max(0, dp2[i-1]) + seq_2[i]

    return max(max(dp1), max(dp2))