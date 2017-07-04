import random 

w = []
x = []
sums = []
answers = []
theta = random.random()
counter = 0 

while counter < 50:
    w.append(random.random())
    x.append(random.randint(0, 1))
    counter += 1

counter = 0

while counter < 50:
    sums.append(x[counter] * w[counter])
    counter += 1

counter = 0 
while counter < 50:
    if sums[counter] > theta:
        answers.append(1)
    else: 
        answers.append(0)
    counter += 1
    
print(answers)




