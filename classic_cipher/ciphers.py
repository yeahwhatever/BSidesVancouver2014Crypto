# -*- coding: utf-8 -*-
from random import shuffle, choice
from itertools import starmap, cycle 

'''
This is a "caesar cipher" or "subsitution cipher", which is one of the oldest methods of enciphering. You can often find 
this being used in puzzles for kids as they're relatively simple and can be done on paper.

From Wikipedia: (http://en.wikipedia.org/wiki/Substitution_cipher):

	Substitution of single letters separately simple substitution—can be demonstrated by writing out the 
	alphabet in some order to represent the substitution. This is termed a substitution alphabet. The 
	cipher alphabet may be shifted or reversed (creating the Caesar and Atbash ciphers, respectively) or 
	scrambled in a more complex fashion, in which case it is called a mixed alphabet or deranged 
	alphabet. Traditionally, mixed alphabets may be created by first writing out a keyword, removing 
	repeated letters in it, then writing all the remaining letters in the alphabet in the usual order.

'''
class caesar_cipher():
	def __init__(s, message):
		s.alpha = [ x for x in 'abcdefghijklmnopqrstuvwxyz' ]
		s.string = message.lower() # For the cipher to be effective, you have to work with the same case because confusion
		s._create_keys()
		s._encipher()

	# Creates a random assortment of keys for substitution
	def _create_keys(s):
		alpha_shuffle = s.alpha
		shuffle(alpha_shuffle) # I really dislike how shuffle works but whatever :)
		s.keys = { sorted(s.alpha)[x]:alpha_shuffle[x] for x in xrange(0, len(s.alpha)) }

	# Let's make this "super secret" message
	def _encipher(s):
		s.output = []
		for char in s.original():
			if char in s.alpha:
				char = s.keys[char]
			s.output.append(char)
		s.output = ''.join(s.output)

	# Done as a method to verify that the cipher is working as expected
	def _decipher(s):
		reverse_keys = { cipher: real for real, cipher in s.keys.iteritems() } # Just reverse the key list
		s.deciphered = []
		for char in s.output:
			if char in s.alpha:
				char = reverse_keys[char]
			s.deciphered.append(char)
		s.deciphered = ''.join(s.deciphered)

	def original(s):
		return s.string

	def enciphered(s):
		return s.output

	def deciphered(s):
		s._decipher() # Deciphering isn't done automatically unlike the enciphering process
		return s.deciphered

'''
This is very much similar to the Caesar cipher from before except it uses numbers and shuffles them around.

As in 'A' is '1', 'B' is '2' etc. It then multiplies each value by the key length and adds the length value 
of the key as well.

Unlike the other cipher it does remove other non-alphabetical characters. This was done to kind of bring 
home why you don't do your own crypto. :)
'''
class number_cipher():
	def __init__(s, key, message):
		s.message = message.lower()
		s.alpha = [ x for x in 'abcdefghijklmnopqrstuvwxyz' ]
		s.key = key
		s.numbers = [ '%d' % ((x + len(s.key)) * len(s.key)) for x in xrange(0, len(s.alpha)) ]
		s._create_keys()
		s._filter()
		s._encipher()

	def _create_keys(s):
		number_shuffle = s.numbers
		shuffle(number_shuffle)
		s.keys = { sorted(s.alpha)[x]:number_shuffle[x] for x in xrange(0, len(s.alpha)) }

	def _filter(s):
		s.message = filter(lambda _: _.isalpha(), s.message.lower())

	def _encipher(s):
		s.output = ' '.join([ s.keys[char] for char in s.message ])

	def _decipher(s):
		reverse_keys = { cipher: real for real, cipher in s.keys.iteritems() }
		s.deciphered = ' '.join([ reverse_keys[value].upper() for value in s.output.split() ])

	def enciphered(s):
		return s.output

	def deciphered(s):
		s._decipher()
		return s.deciphered

'''
This is code for using a "Vigenère cipher".

As detailed on Wikipedia (http://en.wikipedia.org/wiki/Vigenère_cipher):

	The Vigenère cipher is a method of encrypting alphabetic text by using a series of different 
	Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic 
	substitution.

	The Vigenère cipher has been reinvented many times. The method was originally described by 
	Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso; however, 
	the scheme was later misattributed to Blaise de Vigenère in the 19th century, and is now 
	widely known as the "Vigenère cipher".

Some of the code was lifted from Rosetta Code:
http://rosettacode.org/wiki/Vigenère_cipher#Python

No need to reinvent the wheel when the above does the job effectively.
'''
class vigenere_cipher():
	def __init__(s, cipherkey, message):
		s.key = cipherkey.upper()
		s.message = message
		s._filter()
		s._encipher()

	# Removes non-alphabet characters
	def _filter(s):
		s.message = filter(lambda _: _.isalpha(), s.message.upper())

	# Stars the enciphering process
	def _encipher(s):
		s.enciphered = ''.join(starmap(s._enc, zip(s.message, cycle(s.key)))) 

	def _decipher(s):
		s.deciphered = ''.join(starmap(s._dec, zip(s.message, cycle(s.key)))) 

	# Encodes a character
	def _enc(s, c, k): 
		return chr(((ord(k) + ord(c)) % 26) + ord('A'))

	# Decodes a character
	def _dec(s, c, k):
		return chr(((ord(c) - ord(k)) % 26) + ord('A')) 

	def encipher(s):
		return s.enciphered

	def decipher(s):
		s._decipher()
		return s.deciphered

class xor_cipher():
	def __init__(s, cipherkey, message):
		s.key = ord(cipherkey)
		s.message = message
		s._filter()
		s.enciphered = s._encipher(s.message)
	
	# Removes non-alphabet characters
	def _filter(s):
		s.message = filter(lambda _: _.isalpha(), s.message.upper())
	
	def _encipher(s, m):
		return ''.join(chr(ord(x) ^ s.key) for x in m)
	
	def encipher(s):
		return s.enciphered

	def decipher(s):
		s.deciphered = s._encipher(s.enciphered)
		return s.deciphered

