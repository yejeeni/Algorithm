import sys

hg_dict = {
    'a': 'aespa',
    'b': 'baekjoon',
    'c': 'cau',
    'd': 'debug',
    'e': 'edge',
    'f': 'firefox',
    'g': 'golang',
    'h': 'haegang',
    'i': 'iu',
    'j': 'java',
    'k': 'kotlin',
    'l': 'lol',
    'm': 'mips',
    'n': 'null',
    'o': 'os',
    'p': 'python',
    'q': 'query',
    'r': 'roka',
    's': 'solvedac',
    't': 'tod',
    'u': 'unix',
    'v': 'virus',
    'w': 'whale',
    'x': 'xcode',
    'y': 'yahoo',
    'z': 'zebra'
}

s = sys.stdin.readline().strip()

result = []
idx = 0

while True:
    idx_word = s[idx] # 지금 s의 첫글자
    # 첫글자와 일치하는 hg 단어 찾기
    hg_word = hg_dict.get(idx_word)

    # s의 지금 단어
    now_word = s[idx:len(hg_word)+idx]
    # 가 hg 사전에 있는지
    if hg_word == now_word:
        # 있다면 hg 단어 맞음
        result.append(idx_word)
        idx += len(hg_word)
    else:
        print("ERROR!")
        break

    if idx >= len(s):
        print("It's HG!")
        print("".join(result))
        break
