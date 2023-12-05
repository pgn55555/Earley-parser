from grammar import Rule

class Situation:
    def __init__(self, rule: Rule, point_in_rule: int,
                index_subtree: int) -> None:
        self.rule = rule
        self.point_in_rule = point_in_rule
        self.index_subtree = index_subtree

    def __eq__(self, other) -> bool:
        return self.rule.left == other.rule.left and\
               self.rule.right == other.rule.right and\
               self.point_in_rule == other.point_in_rule and\
               self.index_subtree == other.index_subtree

    
    def __hash__(self) -> int:
        pass
        return hash((self.rule.left,
                     self.rule.right,
                     self.point_in_rule,
                     self.index_subtree))
    
    def get_next_symbol(self) -> str:
        if self.point_in_rule == len(self.rule.right):
            return '$'
        return self.rule.right[self.point_in_rule]
