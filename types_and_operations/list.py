# The Python list object is the most general sequence provided by the language. Lists arepositionally ordered collections of arbitrarily typed objects, and they have no fixed size.They are also mutable—unlike strings, lists can be modified in place by assignment tooffsets as well as a variety of list method calls. Accordingly, they provide a very flexibletool for representing arbitrary collections—lists of files in a folder, employees in acompany, emails in your inbox, and so on.

# A list of three different-type objects
items = [123, 'spam', 1.23]

# Number of items in the list
len(items)

# index by position
items[0]

# slice a list returns a new list
items[0:1]

# concat
items + [1, 2]

# repeate
items * 2

# add item in end of the lis
items.append('item')

# print(items)

# create an array from 0 to 99
# print(list(range(100)))