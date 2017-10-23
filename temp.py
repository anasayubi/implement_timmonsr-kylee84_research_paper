from collections import Counter

tokens = ['hey', 'there', ',', 'there']
tokensCount = Counter(tokens)
print('there' in tokensCount)
print(tokensCount)
print(tokensCount['there'])