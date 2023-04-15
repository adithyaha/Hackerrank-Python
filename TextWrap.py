

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    wrapped_string='\n'.join(wrapped)
    return wrapped_string

