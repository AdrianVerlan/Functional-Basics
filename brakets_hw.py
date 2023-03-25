def wrap_brackets( text ):
  return "(" + text + ")"

def square_brackets(text):
  return "[[["+ text + "]]]"

def caracter(text):
  return "<<<"+ text + ">>>"

print(caracter(square_brackets(wrap_brackets("1234"))))