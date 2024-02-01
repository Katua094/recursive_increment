def loud(text):
    return text.upper()
def quet(text):
    return text.lower()

def hello(func):
    text=func("hello")
    print(text)

hello(quet)
