bNEW = '╩'
bESW - '╦'
bNES = '╠'
bNSW = '╣'
bNS = '║'
bEW = '═'
bNE = '╝'
bNW = '╚'
bSW = '╗'
bES = '╔'
bNESW = '╬'

# B & L
bEWlS = '╤'
bNlEW = '╨'
bEWlN = '╧'
bSlEW = '╥'
bNlE = '╙'
bElN = '╘'
bElS = '╒'
bSlE = '╓'
bNSlEW = '╫'
bEWlNS = '╪'
bElNS = '╞'
bNSlE = '╟'
bWlNS = '╡'

# L
lNW = '┘'
lWS = '┐'
lNESW = '┼'
lSW = '┐'
lNE = '└'
lNEW = '┴'
lES = '┌'
lESW = '┬'
lNES = '├'
lEW = '─'
lNS = '│'
lNSE = '┤'

bl = ' '
# short for bar line blank or just blank
########################
example

top_width = 10
top_bar_width = bEW*top_width
title = 'Example'
title_length = len(title)
extra = title_length - top_width

def console_menu():
  print(bES + top_bar_width + bSW)
  print(bNS + title + extra + bNS)
  print(bNE + top_bar_width + bNW)
  
console_menu()
