# Import classes from your brand new package
#import Animals
#Animals.Birds
#Animals folder will be searched from sys.path 

#import sys
#sys.path.append("folder path of module/package folder")

from Animals import Mammals
from Animals import Birds
 
# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()











"""
installing module in Python
>pip install module_name
"""
