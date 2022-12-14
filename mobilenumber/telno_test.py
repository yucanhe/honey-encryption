# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunctionAPI.py, and DTE.py
# work together.

from telno import *
from DTE import *
import os
from random import randint

''' Create prefixes dictionary 'prefix': [numRandom, cardLength, probWeight]
i.e. 
prefixes = {
    '5235**': [2, 8, 100],
    '123456': [0, 8, 1]
}
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

telno_example = '13000000023'
secret_key = 2048101736616812280
#guess_key =  2048101736616812280
guess_key =  5496328831800304765

# Create probability fxns
id_fxns = TelNOProbabilityFxns()


# Use DTE on identification example
seed = encode(telno_example, id_fxns)
ciphertext = secret_key ^ seed
decipher_seed = guess_key ^ ciphertext


print "MOBILE NUMBER TO BE ENCRYPED: "+telno_example
print ""
print "HEX(SEED): "+str(hex(seed))
print "CIPHERTEXT: "+str(ciphertext)
print "HEX(GUESSED_SEED): "+str(hex(decipher_seed))
print ""

message = decode(decipher_seed, id_fxns)
print "decoded by the guessed seed, returned MESSAGE: "+message

message = decode(seed, id_fxns)
print "decoded by a right seed, returned MESSAGE: "+message
