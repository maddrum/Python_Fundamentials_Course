K = input()
N = input()
M = input()
days = 0
try:
    K = float(K)
    N = float(N)
    M = float(M)
except:
    print("INVALID INPUT")
    quit()
diff = 10 * N - M
if diff <= 0 or N == 0:
    print("NO BIKE FOR YOU")
    quit()
tenDaysNum = K // diff
K -= tenDaysNum * diff
days = int(tenDaysNum) * 10
while K > 0:
    days += 1
    K -= N
print(days)
