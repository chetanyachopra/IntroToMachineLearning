from sklearn import tree
features=[[140, 1], [150, 1], [130,0], [170,1], [180, 1], [110,0]]
labels=['orange','orange','apple','apple','apple','orange']

classifier=tree.DecisionTreeClassifier()
classifier=classifier.fit(features,labels)

print(classifier.predict([140,0]))

