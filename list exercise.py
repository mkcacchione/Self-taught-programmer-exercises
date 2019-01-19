Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> music= ["taylor Swift", "lil waynne", "post malone", "kid cuddy", "fetty"]
>>> music
['taylor Swift', 'lil waynne', 'post malone', 'kid cuddy', 'fetty']
>>> music[4]="john lennon"
>>> music
['taylor Swift', 'lil waynne', 'post malone', 'kid cuddy', 'john lennon']
>>> music[1]="lil uzi vert"
>>> music
['taylor Swift', 'lil uzi vert', 'post malone', 'kid cuddy', 'john lennon']
>>> print(music)
['taylor Swift', 'lil uzi vert', 'post malone', 'kid cuddy', 'john lennon']
>>> music.append("fetty")
>>> music
['taylor Swift', 'lil uzi vert', 'post malone', 'kid cuddy', 'john lennon', 'fetty']
>>> item=music.pop()
>>> item
'fetty'
>>> music
['taylor Swift', 'lil uzi vert', 'post malone', 'kid cuddy', 'john lennon']
>>> music[0]
'taylor Swift'
>>> music[4]
'john lennon'
>>> colors=["purple", "orange", "green"]
>>> colors
['purple', 'orange', 'green']
>>> guess=input("guess a color:")
guess a color:"yellow"
>>> if guess in colors
SyntaxError: invalid syntax
>>> if guess in colors:
	print("you guessed correctly")
else:
	print("wrong, guess again")

	
wrong, guess again
>>> guess=input("guess a color:")
guess a color:"purple"
>>> if guess in colors:
	print("you guessed correctly!")
else:
	print("wrong, guess again")

	
wrong, guess again
>>> 
