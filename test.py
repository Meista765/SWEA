def triDiffCheck(num1, num2):
    # 0, 1, 2의 개수
    digit_cnt_1 = [0, 0, 0]
    digit_cnt_2 = [0, 0, 0]

    while num1 and num2:
        num1, rem1 = divmod(num1, 10)
        num2, rem2 = divmod(num2, 10)
        digit_cnt_1[rem1] += 1
        digit_cnt_2[rem2] += 1

    gap_zero = False
    gap_one = False
    gap_minusOne = False

    for i in range(3):
        diff = digit_cnt_1[i] - digit_cnt_2[i]
        if diff == 0:
            gap_zero = True
        elif diff == 1:
            gap_one = True
        elif diff == -1:
            gap_minusOne = True

    return gap_zero & gap_one & gap_minusOne

print(triDiffCheck(112, 102))