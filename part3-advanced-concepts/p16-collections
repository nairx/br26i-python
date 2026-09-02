# from collections import Counter
# lottery_winners = ["John","Cathy","John","Amy","John","Amy"]
# mycounter = Counter(lottery_winners)
# #print(mycounter)
# # print(mycounter.most_common(1))
# print(mycounter.most_common(2))

# from collections import namedtuple
# Price = namedtuple('Price',["Product1","Product2","Product3"])
# p=Price(100,120,140)
# print(p)
# print(p.Product1)

# from collections import defaultdict
# score = defaultdict(int) # float str
# score["John"]=50 
# score["Amy"]=90
# # print(score["John"])
# print(score["Mike"])

from collections import deque 
numbers = deque([2,4,5])
# numbers.append(9)
# print(numbers)
# numbers.appendleft(9)
# print(numbers)
# numbers.extend([7,8,9])
# print(numbers)
# numbers.extendleft([7,8,9])
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.popleft()
# print(numbers)

# print(numbers)
# numbers.rotate(1)
# print(numbers[0])
# numbers.rotate(1)
# print(numbers[0])

# from collections import ChainMap
# court1 = {"Nadal":5,"Novak":3}
# court2 = {"Roger":9}
# court3 = {"Osaka":7,"Sharapova":3}
# players = ChainMap(court1,court2,court3)
# print(players)
# for player,points in players.items():
#     print(player,points)

# from collections import UserList  #UserDict
# class MyList(UserList):
#     def pop(self,s=None):
#         raise RuntimeError("Deletion not allowed")
# L =  MyList([1,2,3,4])
# L.pop()

from collections import UserString
class MyStr(UserString):
    def upper(self,s=None):
        return self.data.lower()

s = MyStr("Hello")

print(s.upper())