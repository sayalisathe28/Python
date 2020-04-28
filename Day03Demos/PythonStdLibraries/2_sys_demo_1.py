

"""sys. stdin  sys.stdout sys.stderr"""

import sys
#sys.stdout is by default pointing to screen
#let's change it to a file object

sys.stdout = open("hello.txt","w")
print "AAAAAAAAAAAAAAAAaa"  #instead of printing on console, it will print inside file hello.txt 
sys.stdout.close()



























'''
stdin
stdout
stderr
#!/usr/bin/env python

 f1 = open("hello.txt","w")
 f1.write("Hello !!!")
'''
