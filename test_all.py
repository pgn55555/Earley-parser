from grammar import Grammar
from algorithm import EarleyParser

def test_sample():
    grammar = Grammar(1, 2, 2)
    grammar.add_not_terminal('S')
    grammar.add_terminal('ab')
    grammar.add_rule('S-> aSbS')
    grammar.add_rule('S -> ')
    grammar.add_start('S')
    parser = EarleyParser()
    parser.fit(grammar)
    
    assert parser.predict('aababb')
    assert not parser.predict('aabbba')

def test_simple_letter():
    grammar = Grammar(1, 2, 1)
    grammar.add_not_terminal('S')
    grammar.add_terminal('ab')
    grammar.add_rule('S -> a')
    grammar.add_start('S')
    parser = EarleyParser()
    parser.fit(grammar)
    
    assert parser.predict('a')
    assert not parser.predict('b')

def test_simple_grow():
    grammar = Grammar(1, 1, 2)
    grammar.add_not_terminal('S')
    grammar.add_terminal('a')
    grammar.add_rule('S -> aS')
    grammar.add_rule('S ->')
    grammar.add_start('S')
    parser = EarleyParser()
    parser.fit(grammar)
    
    assert parser.predict('a')
    assert parser.predict('aa')
    assert parser.predict('aaaaaaaaaaaaaaaaaaaaa')

def test_multiple_not_terminals():
    grammar = Grammar(2, 2, 4)
    grammar.add_not_terminal('SP')
    grammar.add_terminal('ab')
    grammar.add_rule('S -> PS')
    grammar.add_rule('P -> a')
    grammar.add_rule('S -> ')
    grammar.add_rule('P -> bb')
    grammar.add_start('S')
    parser = EarleyParser()
    parser.fit(grammar)
    
    assert parser.predict('abb')
    assert parser.predict('aaaabb')
    assert not parser.predict('abbb')
    assert parser.predict('abbbb')
    assert parser.predict('bba')
    assert not parser.predict('b')

def test_double_letters():
    grammar = Grammar(4, 2, 7)
    grammar.add_not_terminal('SABC')
    grammar.add_terminal('ab')
    grammar.add_rule('A -> aaSb')
    grammar.add_rule('C -> aSbSa')
    grammar.add_rule('B -> bSaa')
    grammar.add_rule('S -> ')
    grammar.add_rule('S -> AS')
    grammar.add_rule('S -> BS')
    grammar.add_rule('S -> CS')
    grammar.add_start('S')
    parser = EarleyParser()
    parser.fit(grammar)
    
    assert not parser.predict('abb')
    assert parser.predict('aaaabb')
    assert parser.predict('aab')
    assert parser.predict('aabaabaabbaa')
    assert parser.predict('bbabbaaaaaaa')
    assert not parser.predict('a')

def test_brackets():
    grammar = Grammar(1, 2, 3)
    grammar.add_not_terminal('S')
    grammar.add_terminal('()')
    grammar.add_rule('S -> ')
    grammar.add_rule('S -> SS')
    grammar.add_rule('S -> (S)')
    grammar.add_start('S')
    parser = EarleyParser()
    parser.fit(grammar)
    
    assert parser.predict('()')
    assert not parser.predict('())')
    assert parser.predict('()()()')
    assert parser.predict('(())()((()))')
    assert not parser.predict(')(')
    assert not parser.predict('(()()))')
