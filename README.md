# BLCN - Bar &amp; Line Cardinal-Clockwise Notation
by Donald J. Guiles

May 2 2022

---
## Preface 

Symbol Reference 

		bNEW  = '╩'	bESW   = '╦'	bNES   = '╠'	bNSW  = '╣'	bNS   = '║'	bEW   = '═'

		bNE   = '╝'	bNW    = '╚'	bSW    = '╗'	bES   = '╔'	bNESW = '╬'	bEWlS = '╤'

		bNlEW = '╨'	bEWlN  = '╧'	bSlEW  = '╥'	bNlE  = '╙'	bElN  = '╘'	bElS  = '╒'	

		bSlE  = '╓'	bNSlEW = '╫'	bEWlNS = '╪'	bElNS = '╞'	bNSlE = '╟'	bWlNS = '╡'	

		lNW   = '┘'	lWS    = '┐'	lNESW  = '┼'	lSW   = '┐'	lNE   = '└'	lNEW  = '┴'	

		lES   = '┌'	lESW   = '┬'	lNES   = '├'	lEW   = '─'	lNS   = '│'	lNSE  = '┤'


 ## 1. Introduction - How to write and read shorthand notation
 
 	
   Bar and Line Cardinal Clockwise Notation attempts to simplify the symbol and character
map for the lined and Double-lined Charcters by using the Clockwise Cardinal Naming Algorithm.
Clockwise Cardinal Naming Algorithm is self-explanatory. However, i will attempt to explain it 
in the simpliest way possible. Starting with the name. 
	
	Clockwise - The flow of direction that lines in relation to symbols are described from the center.
	
	Cardinal  - Cardinal directions are used to help notate the direction (from center, then from north) 
			the line or bar is travelling.
	
	Naming    - Assigning variables to those equations
	
	Algorithm - How it is achieved from beginning to end
	
So Starting from the top... The flow of bars then lines in a symbol from the center, in North East South West clockwise notation.

---

Here are some Examples
If the variable is 
	
	bEWlNS

then the symbol looks like this...


	╪ 

What does bEWlNS stand for? 

	b 	E	W	l	N	S
	bar	East	West 	line	North	South

That is the physical description and variable name for the symbol ╪

Not only is BLCN flow indicative, but it makes reverse-engineering a symbol easy, without looking at a character map.
	

	
What about complex symbols like '╫'?

	"bar travels North South line travels East West"
		
			bNSlEW
			
---
## 2. Variables
[b] lowercase bravo
b = bar

bar or "double bar" 
	
	b is the symbol notation for a line with two lines in place of one. '═' not '-'
	
l = lowercase lima


l = line or | or -- or 'single line':

	[l] is the symbol varaible for a line with one line in place of one  '-' not '═'

---
 ## 3. Equation

If a symbol has any double bars or bars any bars the variable starts with b:

	bNEW = '╩'  "bar North East West"

		note that the directionals start at North [N] and goes clockwise 90 degrees, if you want the bar to continue
		that direction you need to denote the direction as you go clockwise around the compass.

If the symbol contains ONLY lines in the symbol then the variable starts with a l:
	
	lNS = |   "line North South"

If the symbol contains bars and lines, start with bars then move to lines b(directionals)l(directionals):

	bEWlN = "bar East West line North"  ==    ╧ 

Here is the logical thought flow of calculating the symbol out:

The [b]ar goes [N]orth [E]ast [S]outh [W]est, so the symbol is >> bNESW

	BLCN = { b[N][E][S][W] } + { ¬l[¬N][¬E][¬S][¬W] }

		bN + bE + bS + bN = B
		lN + lE + lS + lN = L
			 B  ==  B
			 L  ==  L
		     B  == ¬L
		    ¬B  ==  L
		     B  !=  L

       { bNu + bEz + bSy + bWz } + { lNu + lEx + lSy + lWz } 
       	
       	if [ x = 1 ] then  [ y = 0 ]

       		check: [ x = 0 ] and  [ y = 0 ]

       										= 0 pass

       			if [ bNu = 1 ] then [ lNu = 0 ];
       			if [ lNy = 1 ] then [ bNy = 0 ];

------------------------------------------------------------------------------
>## 4. Examples:

	  b[¬N][E][S][W] = l[N][¬E][¬S][¬W]
	    
      BLCN is bESWlN
      
    b[¬N][¬E][S][W] = l[N][E][¬S][¬W]
      
      BLCN is bSWlNE
      
    b[¬N][¬E][¬S][W] = l[N][E][S][¬W]
    
      BLCN is bWlNES
      
    b[¬N][¬E][¬S][¬W] = l[N][E][S][W]
      
      BLCN is lNESW
 
 ## Application
 
 Python use of BLCN to easily create Symbol based console art or structure.
 
 see PyBLCN
 
