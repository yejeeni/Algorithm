color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

register = color.index(input()) * 10 + color.index(input())

print(register * 10 ** color.index(input()))