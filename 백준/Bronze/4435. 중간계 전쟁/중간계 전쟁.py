t = int(input())


for i in range(t):
    Hobbit, Man, Elf, Dwarf, Eagle, Wizard = map(int, input().split())
    score_g = Hobbit*1 + Man * 2 + Elf * 3 + Dwarf * 3 + Eagle * 4 + Wizard * 10
    
    Orc, Man, Warg, Goblin, Uruk_hai, Troll, Wizard = map(int, input().split())
    score_s = Orc * 1 + Man * 2 + Warg * 2 + Goblin * 2 + Uruk_hai * 3 + Troll * 5 + Wizard * 10

    print("Battle {}: ".format(i+1), end="")
    if score_g > score_s:
        print("Good triumphs over Evil")
    elif score_g < score_s:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")