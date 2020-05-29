from matplotlib import pyplot as plt
import json

varData = {}
varData['categories'] = []

with open('categories.json') as json_file:
    data = json.load(json_file)
    for p in data['categories']:
        varData['categories'].append({
            'name': p['name'],
            'number': p['number']
        })

totalNumber = 0
for category in varData['categories']:
    totalNumber += int(category['number'])

print("Liczba wszystkich produktów: " + str(totalNumber))

lessThen = totalNumber*0.03
print(lessThen)

labels = []
numbers = []
otherLabels = []
numOfOthers = 0

for category in varData['categories']:
    if(int(category['number']) <= lessThen):
        otherLabels.append(category['name'])
        numOfOthers += int(category['number'])

    else:
        labels.append(category['name'])
        numbers.append(category['number'])

varData['categories'].append({
            'name': 'Inne',
            'number': str(numOfOthers)
        })
labels.append('Inne')
numbers.append(numOfOthers)


fig1, ax1 = plt.subplots()
patches = ax1.pie(numbers, labels=labels, radius=1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  #
fig1.suptitle('Porównanie dostępnych kategorii', fontsize=14, fontweight='bold')
ax1.set_title("Liczba wszystkich produktów: " + str(totalNumber))
ttl = ax1.title
ttl.set_position([.5, 1.05])
plt.show()