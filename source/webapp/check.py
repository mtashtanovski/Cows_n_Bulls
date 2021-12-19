class Check:

    def __init__(self, user_numbers) -> None:
        self.user_numbers = user_numbers
        self.secret_numbers = [1, 2, 4, 9]

    def validation(self):
        if len(self.user_numbers) != 4:
            return 'The amount of integers should equal to 4!'

        if len(self.user_numbers) > len(set(self.user_numbers)):
            return 'The values should be unique!'

        for i in self.user_numbers:
            if i > 9 or i < 1:
                return 'Numbers must be greater than 1 and less than 10!'

    def get_result(self):
        bulls = 0
        cows = 0
        for i in range(len(self.secret_numbers)):
            if self.secret_numbers[i] == self.user_numbers[i]:
                bulls += 1
            elif self.secret_numbers[i] in self.user_numbers:
                cows += 1
        if bulls == 4:
            return 'You Won the game!'
        elif bulls or cows:
            return f"You got {bulls} bulls and {cows} cows!"
        else:
            return 'No identical numbers'
