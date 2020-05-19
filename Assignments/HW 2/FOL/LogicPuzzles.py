T = int(input())
for i in range(T):
    nb = []
    ip_str = input()
    nb_a = ip_str.split()
    N = int(nb_a[0])
    B = int(nb_a[1])
    arr = []
    ip_str = input().split()
    for j in range(N):
        arr.append(int(ip_str[j]))
    arr.sort()
    count = 0
    sum = 0
    for j in range(N):
        if sum+arr[j] <= B:
            sum += arr[j]
            count += 1
        else:
            break
    print("Case #" + str(i+1) + ": " + str(count))





# T = int(input())
# for i in range(T):
#     N = int(input())
#     mat = []
#     for j in range(N):
#         row = []
#         strT= input().split()
#         for k in range(N):
#             row.append(int(strT[k]))
#         mat.append(row)
#     rowCount = 0
#     colCount = 0
#     trace = 0
#     for j in range(N):
#         rowSet = set()
#         for k in range(N):
#             rowSet.add(mat[j][k])
#             if j == k:
#                 trace += mat[j][k]
#         if (len(rowSet) < N):
#             rowCount += 1
#
#     for k in range(N):
#         colSet = set()
#         for j in range(N):
#             colSet.add(mat[j][k])
#         if (len(colSet) < N):
#             colCount += 1
#     print("Case #" + str(i + 1) + ": " + str(trace) + " " + str(rowCount) + " " + str(colCount))
