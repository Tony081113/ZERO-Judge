#ZERO-Judge a009

#輸入
n = str(input())
nn = ''

#處理1
n = list(n)  # 將字串轉換為列表以便修改

#處理2
for i in range(len(n)):
    a = ord(n[i])
    a -= 7
    n[i] = chr(a)

#處理3
for i in range(len(n)):
    nn += n[i]

#輸出
print(nn)