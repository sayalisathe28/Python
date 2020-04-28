"""
list = re.findall()

"""

import re

s1="Welcome to PSL, PSL in pune. psl"

matchlist = re.findall("psl",s1,re.I)
print "Match Found content = ",matchlist #['PSL', 'PSL', 'psl']

print "-------------------------------------------"

words=["abc","123aaa","xyz","ABC","123"]
alphabetical_words = [w for w in words if w.isalpha()] #["abc","xyz","ABC"]
print "Original words = ",words
print "alphabetical words = ",alphabetical_words

print "-------------------------------------------"
alphabetical_words = [w for w in words if re.search("^[a-zA-Z]+$",w)!=None]
print "alphabetical words = ",alphabetical_words

print "-------------------------------------------"
s1=["sayalisathe98@gmail.com","say"]
alphabetical_words = [w for w in s1 if re.search("^([a-zA-Z0-9]+)@([a-zA-Z]+)\.([a-z]+)$",w)!=None]
print "alphabetical words = ",alphabetical_words
