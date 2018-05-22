from random import choice

def password(tamanho):
	carac = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVXZW1234567890_!@#$%&?'
	senha = ''
	for char in xrange(tamanho):
		senha += choice(carac)
	return senha

print password(12)
