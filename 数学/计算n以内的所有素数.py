def calPrimes(n):
    notPrimes = [False] * (n + 1)
    count = 0
    for i in range(2, n):
        if notPrimes[i]:
            continue
        count += 1
        for j in range(i*i, n, i):
            notPrimes[j] = True
    return count

# public int countPrimes(int n) {
#     boolean[] notPrimes = new boolean[n + 1];
#     int count = 0;
#     for (int i = 2; i < n; i++) {
#         if (notPrimes[i]) {
#             continue;
#         }
#         count++;
#         // 从 i * i 开始，因为如果 k < i，那么 k * i 在之前就已经被去除过了
#         for (long j = (long) (i) * i; j < n; j += i) {
#             notPrimes[(int) j] = true;
#         }
#     }
#     return count;
# }

if __name__ == '__main__':
    print(calPrimes(10))
