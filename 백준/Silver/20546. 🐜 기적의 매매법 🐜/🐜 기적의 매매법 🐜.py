money = int(input())
stocks = list(map(int, input().split()))

jun_stock = 0
jun_money = money
sung_stock = 0
sung_money = money

for stock in stocks:
    # 준현
    # 주식을 살 수 있을 경우
    if stock <= jun_money:
        # 최대한 매수
        jun_stock = jun_money // stock
        jun_money = jun_money % stock

# 성민
for i in range(len(stocks) - 4):
    # 3일 연속 하락 중
    if stocks[i] > stocks[i+1] > stocks[i+2]:
        # 전량 매수
        sung_stock += sung_money // stocks[i+3]
        sung_money = sung_money % stocks[i+3]

    # 3일 연속 상승 중
    if stocks[i] < stocks[i+1] < stocks[i+2]:
        # 전량 매도
        sung_money += stocks[i+3] * sung_stock
        sung_stock = 0

jun = jun_money + jun_stock * stocks[-1]
sung = sung_money + sung_stock * stocks[-1]

if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")
