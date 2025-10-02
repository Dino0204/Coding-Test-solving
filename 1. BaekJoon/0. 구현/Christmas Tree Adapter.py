ampere = int(input())
watt, volt = map(int, input().split())

print(1) if watt / volt >= ampere else print(0)