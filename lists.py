shoplist = ["apples", "oranges", "bananas", "cheese"]
print(shoplist[0:3])
shoplist.append("mere")
print(shoplist)
shoplist[0] = "cherries"
print(shoplist)

del shoplist[1]
print(shoplist)

print(len(shoplist))
