from sklearn.datasets import load_digits, fetch_mldata
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn import metrics

digits = load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

# todos os parâmetros não especificados são definidos como seus padrões
logisticRegr = LogisticRegression()

mnist = fetch_mldata('MNIST original')
train_img, test_img, train_lbl, test_lbl = train_test_split(mnist.data, mnist.target, test_size=1/7.0, random_state=0)

logisticRegr.fit(x_train, y_train)

# Retorna uma matriz NumPy 
# Prever para uma observação (imagem) 
logisticRegr.predict(x_test[0].reshape(1, -1))
logisticRegr.predict(x_test[0:10])

predictions = logisticRegr.predict(x_test)
score = logisticRegr.score(x_test, y_test)
cm = metrics.confusion_matrix(y_test, predictions)

# Imprimir para mostrar que há 1797 imagens (8 por 8 imagens para uma dimensionalidade de 64) 
print('Images dataset {}'.format(digits.data.shape))

# Imprimir para mostrar que há 1797 rótulos (números inteiros de 0 a 9)
print('Formato de dados do rótulo {}'.format(digits.target.shape))

plt.figure(figsize=(20, 4))

for index, (image, label)  in enumerate(zip(digits.data[0:5], digits.target[0:5])):
	plt.subplot(1, 5, index + 1)
	plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
	plt.title('Treinando: %i\n' % label, fontsize = 20)


plt.figure(figsize=(20, 4))
for index, (image, label) in enumerate(zip(train_img[0:5], train_lbl[0:5])):
	plt.subplot(1, 5, index + 1)
	plt.imshow(np.reshape(image, (28, 28)), cmap=plt.cm.gray)
	plt.title('Training: {}'.format(label), fontsize=20)

'''plt.figure(figsize=(9, 9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r');
plt.ylabel('Actual Libel');
plt.xlabel('Predicted label');
all_sample_title = 'Actual Score: {0}'.format(score)
plt.title(all_sample_title, size=15);'''

'''plt.figure(figsize=(9, 9))
plt.imshow(cm, interpolation='nearest', cmap='Pastel1')
plt.title('Confuson matrix', size = 15)
plt.colorbar()
tick_marks = np.arange(10)
plt.xticks(tick_marks, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], rotation=45, size=15)
plt.yticks(tick_marks, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], size=10)
plt.tight_layout()
plt.ylabel('Actual label', size=15)
plt.xlabel('Predicted label', size=15)
width, height = cm.shape

for x in range(width):
	for y in range(height):
		plt.annotate(str(cm[x][y]), xy=(x, y), 
			horizontalalignment='center', 
			verticalalignment='center')'''


print('score: {}\n\n'.format(score))
print(cm)

# Estas são as imagens 
# Existem 70.000 imagens (28 por 28 imagens para uma dimensionalidade de 784)
print('\n\nImagens: {}'.format(mnist.data.shape))

# Estes são os rótulos 
print('Rótulos: {}\n'.format(mnist.target.shape))