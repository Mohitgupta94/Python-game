from random import randint
board=[]
new_row=['-','-']
position=[]
def add_row(n,new_row,board,position):  #adds n rows
	for i in range(n):
		a=randint(0,1)
		position.append(a)
		board.append(new_row)
		

def print_board(board):
	for row in board:
		print " ".join(row)

def play(board,position,new_row):
	user_guess=input()
	user_guess=user_guess-1
	if (user_guess==position[-1]):
		position.pop(-1)
		board.pop(-1)
		
	else:
		add_row(1,new_row,board,position)	

print ""
print ""
print "Welcome ! "
print "-----RULES-----"
print "There is a devil in each row, either at position 1 or 2"
print "Guess it's position in last row, entering either 1 or 2"
print "If you guess it right, you go one level up"
print "If you guess it wrong, another row containing a devil appears"
print "Happy playing :) :)"
print "START WITH YOUR FIRST GUESS"
print ""
print ""


add_row(5,new_row,board,position)
print_board(board)

while (len(board)>0):
	play(board,position,new_row)
	print ""
	print_board(board)

print "Congratulations! You won"
	
	
	
