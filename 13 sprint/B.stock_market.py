n = 6
input_str = '7 1 5 3 6 4'
input_str2 = '1 2 3 4 5'
input_str3 = '1 12 12 16 1 8'
input_str5 = '1 29 22 65 82 83 5 10 22 76 93 29 97 26 81 62 5 36 25 41 6 65 1 10 41 91 78 13 85 43 93 10 36'

prices = [int(i) for i in input_str5.split()]

print(prices)

cash = 0
i = 1
today = prices[0]
tomorrow = prices[1]
last_price = 0
if today < tomorrow:
    cash -= today
    last_price = today
else:
    cash -= tomorrow
    last_price = tomorrow
    i += 1

print('cash:', cash)
flag = 0
while i != (len(prices)):
    today = prices[i - 1]
    tomorrow = prices[i]
    print('today:', today, 'tomorrow:', tomorrow)
    if today < tomorrow and flag:
        cash -= today
        print('buy', cash)
        i += 1
        flag = 0
        continue
    elif today > tomorrow and not flag:
        cash += today
        flag = 1
        print('sale', cash)
    i += 1

if not flag:
    cash += tomorrow
    print('sale', cash)

print(cash)
