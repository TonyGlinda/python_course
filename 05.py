# 打印久久乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print('%d*%d=%d' % (col, row, col*row), end='\t')  # \t制表符使文本在垂直方向上对齐。
        col += 1
    print('')
    row += 1
