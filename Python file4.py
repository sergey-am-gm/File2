grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score = {}
students = sorted(list(students))
for i in range(len(students)):
    average_score[students[i]] = sum(grades[i])/len(grades[i])
print(average_score)
# Как-бы циклы мы ещё не проходили, но как по другому не придумал,
# только если вручную перебирать индексы от 0 до 4  ?






