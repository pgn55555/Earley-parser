from grammar import Grammar
from algorithm import EarleyParser

number_not_terminal, number_terminal, number_rules = list(map(int, input().split()))
input_grammar = Grammar(number_not_terminal, number_terminal, number_rules)

symbols_not_terminal = input()
input_grammar.add_not_terminal(symbols_not_terminal)
symbols_terminal = input()
input_grammar.add_terminal(symbols_terminal)

for i in range(number_rules):
    rule = input()
    input_grammar.add_rule(rule)

start = input()
input_grammar.add_start(start)

parser = EarleyParser()
parser.fit(input_grammar)

number_words = int(input())
words = ['' for i in range(number_words)]
for i in range(number_words):
    words[i] = input()

for word in words:
    if parser.predict(word):
        print("Yes")
    else:
        print("No")
