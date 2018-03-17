with open('exam.txt') as f:
  exam_lines = f.readlines()
  
print(exam_lines)

print(len(exam_lines))

print(exam_lines[4])

last = exam_lines[-1]
print(last[5])

count = len(last)
print(count)

d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}

print(d['levelone'][2]['leveltwo'][2][1][0])


mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]

mylist = set(mylist)

print(len(mylist))