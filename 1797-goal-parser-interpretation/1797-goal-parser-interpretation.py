class Solution:
    def __init__(self):
        self.parse_commands = {
            '()': 'o',
            '(al)': 'al',
        }

    def interpret(self, command: str) -> str:
        result = command
        for key in self.parse_commands:
            result = result.replace(key, self.parse_commands[key])
        return result
