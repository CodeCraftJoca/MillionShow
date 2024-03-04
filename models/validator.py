class Validator:


    def is_valid_integer(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False


    def is_valid_difficulty(user_input):
        return user_input in {'1', '2', '3'}
    # Example of usage:
