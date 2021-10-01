def processStrings(n, strs):
    return strs[0:n][::-1] + strs[n:n+n] + strs[-1*n:][::-1]
def main():
    n = int(input())
    strs = input()
    print(processStrings(n, strs))
main()