score = []
score.extend(['85', '90', '78', '92', '88'])
print(score)

score.insert(2, '80')
print("inserted 80 at index 2", score)

score.remove("92")
print(score)

score.sort()
print("sorted in ascending",score)

score.reverse()
print("reversed list",score)

print("maximum score", max(score))
print("minimum score", min(score))

for i in score:
    if i == "90":
        print("Is 90 Present: ",True)


print("total number of score",len(score))

print("first 3 scores",score[:3])

print("remove last score",score[-1])

score[2] = 95
print("replacing index 2 with 95:",score)

copied_score = score.copy()
print("copied score",copied_score)