words = ["abc","xyz"]

def cap(w):
    return w.upper()

print "Original words list = ",words
upper_words1 = map(cap,words)
print "Capitialised words list1 = ",upper_words1

upper_words2 = map(lambda x: x.upper(),words)
print "Capitialised words list2 = ",upper_words2
