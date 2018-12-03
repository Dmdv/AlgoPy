# Example of data annotations


def maxvalue(max_value):
    def wrap_function(func):

        def replace_target_function(self, value):
            assert value <= max_value
            return func(self, value)

        replace_target_function.__name__ = func.__name__
        return replace_target_function

    return wrap_function


if __name__ == '__main__':
    pass
