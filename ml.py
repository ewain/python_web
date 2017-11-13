#TEST con predizione e controllo accuratezza
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

XT = np.array([[-1, -2], [-2, -3], [-3, 4], [1, 1.5], [2.5, 1], [3, 2.5]])
YT = np.array([1, 1, 1, 1, 1, 2])

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB(priors=None)
print("previsione ", clf.predict([[-10.8, -11]]))
print("predizione 2 ", clf.predict([[5, 5]]))
print ("---ATT---")
#predi = clf.predict([[-10.8, -11]])
#print ("pred ", predi)

#gli passo le features (X) e lui cerca di indovinare le labels (Y)
predi2 = clf.predict(XT)
print ("predi2 ", predi2)
#Esempio corrente: ('predi2 ', array([1, 1, 2, 2, 2, 2]))

#confronto le label ottenute dalla predizione con quelle corrette del mio campione
#CONSIDERAZIONE: più c'è differenza di "logica" tra le coppie X,Y e le coppie XT,YT e peggio funziona il mio apprendimento
 #CONSIDERAZIONE: più c'è differenza di "logica matematica" tra le coppie X,Y e le coppie XT,YT e peggio funziona il mio apprendimento
accuracy = accuracy_score(predi2, YT)
print ("accuracy: ", accuracy)

#clf_pf = GaussianNB()
#clf_pf.partial_fit(X, Y, np.unique(Y))
#GaussianNB(priors=None)
#print("predizione 2 ", clf_pf.predict([[-2, -1]]))
print('-------FINE-------')