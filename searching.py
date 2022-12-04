def linear_search(a,data):
    for i in data:
        if a==i:
            return True
        else:
            return False
print(linear_search(1,[2,3,4,5]))
print(linear_search(1,[1,2,3,4,5]))
