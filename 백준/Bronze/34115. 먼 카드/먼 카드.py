n = int(input())
cards = list(map(int, input().split()))

cards_set = set(cards)

max = 0
for card in cards_set:
    idx = cards.index(card)

    count = 0
    for i in range(idx+1, len(cards)):
        if cards[i] != card:
            count += 1
        elif cards[i] == card:
            break
    
    if count > max:
        max = count

print(max)