##    https://www.hackerrank.com/challenges/apple-and-orange/problem

##    The problem description provided is long and has a diagram to accompany
##    it. So go to the link above to read it for yourself.
##
##    In my own words, the problem is as follows:
##
##        Given locations for a house, an apple tree, an orange tree and the locations
##        for numerous individual apples and oranges that have fallen to the ground, 
##        determine how many fell on the house.

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the length of the longest list provided
#   The algo is straight forward.  Iterate through the apple locations and calculate
#   if they fell on the house with simple checks.  Repeat for oranges.
#   Remember the locations of the apples and oranges provded are relative to
#   the tree from which they fell, so their absolute position relative to the house
#   must be calculated.

def countApplesAndOranges(start, end, apple_tree, orange_tree, apples, oranges):

    apples_hit_house = 0
    oranges_hit_house = 0

    for apple in apples:

        location = apple_tree + apple

        if location >= start and location <= end:

            apples_hit_house += 1

    for orange in oranges:

        location = orange_tree + orange

        if location >= start and location <= end:

            oranges_hit_house += 1
            
    print(apples_hit_house)
    print(oranges_hit_house)
    
    return None
