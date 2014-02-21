# -*- coding: utf-8 -*-
'''
Simple script making use of the classic ciphers written for BSides Vancouver 2014
'''

import sys
from classic_cipher import ciphers as c

# Don't let me be snarky. :)
if len(sys.argv) > 1:
	string = ' '.join(sys.argv[1:])
else:
	string = 'Hey! You need to specify a message in order to do anything here! Just append a message at command execution.' 

key = 'security' # This key is universal for the demo.

print
print 'BSides Vancouver 2014 Crypto Challenge'
print 'Key being used where appropriate for demo: "%s"' % key
print
print 'If you see this code before BSides, consider it an early surprise. :)'
print

print 'Original string:'
print string
print

print 'Caesar cipher (uses randomly generated substitution):'
cc = c.caesar_cipher(string)
print 'Encrypted: %s' % cc.enciphered()
print 'Decrypted: %s' % cc.deciphered()
print

print 'Number-based Caesar cipher (number-based substitution with key):'
nc = c.number_cipher(key, string)
print 'Encrypted: %s' % nc.enciphered()
print 'Decrypted: %s' % nc.deciphered()
print

print
print 'Vigenère cipher (uses the key but forced to upper-case):'
vc = c.vigenere_cipher(key, string)
crypted = vc.encipher()
print 'Encrypted: %s' % crypted
vc = c.vigenere_cipher(key, crypted)
print 'Decrypted: %s' % vc.decipher()
print