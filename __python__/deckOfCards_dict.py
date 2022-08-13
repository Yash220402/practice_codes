from pprint import pprint as pp
deck = [{"value": i, "suit": c}
		for c in ["spades", "clubs", "hearts", "diamonds"]
		for i in range(2, 15)]
# pp(deck)

# WORKING WITH DICTIONARIES

d2 = deck.copy()  # copying dictionaries


l1 = [1, 2, [3, 4]]

l_copy = l1.copy()
l_deep = copy.deepcopy(1)

l1[0] = 100
l1[2][1] = 400 

print(l_copy, l_deep)