from grammar import Grammar, Rule
from situation import Situation

class EarleyParser:
    def earley_scan(self, index_token: int,
                    token: str) -> None:
        for situation in self.rules_step[index_token - 1][token]:
            new_situation = Situation(situation.rule,
                                      situation.point_in_rule + 1,
                                      situation.index_subtree)
            self.rules_step[index_token][
                new_situation.get_next_symbol()].add(new_situation)

    def earley_complete(self, index_token: int) -> None:
        new_situations = list()
        for situation1 in self.rules_step[index_token]['$']:
            index_subtree = situation1.index_subtree
            for situation2_symbol in self.grammar.not_terminal:
                for situation2 in self.rules_step[index_subtree][situation2_symbol]:
                    new_point_in_rule = situation2.point_in_rule + 1 if situation2.rule.right != '' else 0
                    new_situation = Situation(situation2.rule,
                                    new_point_in_rule,
                                    situation2.index_subtree)
                    new_situations.append(new_situation)
        
        for new_situation in new_situations:
            self.rules_step[index_token][
                new_situation.get_next_symbol()].add(new_situation)

    def earley_predict(self, index_token: int) -> None:
        new_situations = list()
        for situation_symbol in self.grammar.not_terminal:
            for rule in self.grammar.rules:
                if situation_symbol == rule.left:
                    new_situation = Situation(rule, 0, index_token)
                    new_situations.append(new_situation)
        
        for new_situation in new_situations:
            self.rules_step[index_token][
                new_situation.get_next_symbol()].add(new_situation)

    def len_steps(self, i: int) -> int:
        length = 0
        for step in self.rules_step[i].values():
            length += len(step)
        return length

    def fit(self, input_grammar: Grammar) -> None:
        self.grammar = input_grammar
        self.key_list = set()
        self.key_list.update(self.grammar.not_terminal)
        self.key_list.update(self.grammar.terminal)
        self.key_list.add('$')

    def predict(self, word: str) -> bool:
        self.rules_step = [
            {key: set() for key in self.key_list} for i in range(len(word) + 1)]
        self.rules_step[0][self.grammar.start].add(
            Situation(Rule("S'", self.grammar.start), 0, 0))
        length_last_rules_step = 0

        while length_last_rules_step != self.len_steps(0):
            length_last_rules_step = self.len_steps(0)
            self.earley_complete(0)
            self.earley_predict(0)
        
        for index_token in range(len(word)):
            step = index_token + 1
            self.earley_scan(step, word[index_token])
            length_last_rules_step_j = 0
            while length_last_rules_step_j != self.len_steps(step):
                length_last_rules_step_j = self.len_steps(step)
                self.earley_complete(step)
                self.earley_predict(step)
        
        if Situation(Rule("S'", self.grammar.start), 1, 0) in self.rules_step[-1]['$']:
            return True
        else:
            return False
