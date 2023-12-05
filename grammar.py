class Rule:
    def __init__(self, left : str, right : str) -> None:
        self.left = left
        self.right = right


class Grammar:
    def __init__(self, number_not_terminal: int,
                 number_terminal: int, number_rules: int) -> None:
        self.number_not_terminal = number_not_terminal
        self.number_terminal = number_terminal
        self.number_rules = number_rules
        self.rules = list()

    def input_error(self) -> None:
        raise ValueError("Incorrect input")

    def add_not_terminal(self, input_string: str) -> None:
        if len(input_string) != self.number_not_terminal or \
            input_string.upper() != input_string:
            self.input_error()
        self.not_terminal = set(input_string)
    
    def add_terminal(self, input_string: str) -> None:
        if len(input_string) != self.number_terminal:
            self.input_error()
        self.terminal = set(input_string)
    
    def add_rule(self, input_string: str) -> None:
        rule = input_string.split("->")
        if len(rule) != 2:
            self.input_error()
        self.rules.append(Rule(rule[0].strip(), rule[1].strip()))
    
    def add_start(self, input_string: str) -> None:
        if input_string not in self.not_terminal:
            self.input_error()
        self.start = input_string
