># BLCN
Bar &amp; Line Cardinal-Clockwise Notation

## Symbols
---

---
 ## Introduction
 
 	
   Bar and Line Cardinal Clockwise Notation attempts to simplify the symbol and character
map for the lined and Double-lined Charcters by using the Clockwise Cardinal Naming Algorithm.
	
Starting at the center of this plus Symbol, first notice if it uses any double bars, it does not.
	Second check to see if it uses lines. It does. write the letter 'l'. Which directions from the center
	do the lines travel? Starting at north and moving clockwise we get North East South West.
	Therefore, this symbols notation is lNESW, shorthand for line from center North East South West.
	
What about complex symbols like '╫'?

	Double bar travels North South line travels East West
		
			BLCN = bNSlEW
			
---
## Variables
[b] lowercase bravo
b = bar

bar or "double bar" 
	
	b is the symbol notation for a line with two lines in place of one. '═' not '-'
	
l = lowercase lima


l = line or | or -- or 'single line':

	[l] is the symbol varaible for a line with one line in place of one  '-' not '═'

---
 ## Equation

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
>## Examples:

	  b[¬N][E][S][W] = l[N][¬E][¬S][¬W]
	    
      BLCN is bESWlN
      
    b[¬N][¬E][S][W] = l[N][E][¬S][¬W]
      
      BLCN is bSWlNE
      
    b[¬N][¬E][¬S][W] = l[N][E][S][¬W]
    
      BLCN is bWlNES
      
    b[¬N][¬E][¬S][¬W] = l[N][E][S][W]
      
      BLCN is lNESW
