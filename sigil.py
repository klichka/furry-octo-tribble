from collections import OrderedDict
import re

def Sigil_Aid(phrase=u''):
	# Returns a String with all the vowels and other characters removed.
	# consonant_list = 'bcdfghjklmnpqrstvwxyz' Depreciated

	#word = re.sub('[^A-Z]+','',phrase.upper()) # UPPER CASE and Letters Only please!
	#word = "".join([l for l in word if l not in "AEIOU"]) # Remove Vowels

	word = re.sub('[^B-DF-HJ-NP-TV-Z]+','',phrase.upper()) # UPPER CASE No Vowels!
	word = "".join(OrderedDict.fromkeys(word)) # Remove Dupes!

	return word