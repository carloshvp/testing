import sys

print(sys.version)

print("TESTING2!")
ThisIsAString = "strings everywehre"
print(ThisIsAString)
a = 1
b = 2
c = 4
print(a+b+c)


def add(a, b):
    """ This is some long description aka docstring. I am going to write some text to see what happens when it exceeds the limit. I can write really long sentences in the same line and see what happens.
    Now I am in a new line. This text should be used as description for the function.
    """
    return a+b


print(add.__doc__)


# Third additional change to see if the new commit is correctly linked in Github and correctly name shown
# Change one without push
# Second change
# Now we push
