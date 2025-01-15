from matplotlib import pyplot
from keras.datasets import cifar10
import numpy as np

# Load dataset
(trainX, trainy), (testX, testy) = cifar10.load_data()

# Summarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
print('Test: X=%s, y=%s' % (testX.shape, testy.shape))

# Find and display the total number of unique labels
unique_labels = np.unique(trainy)
print('Total number of unique labels:', len(unique_labels))
print('Labels:', unique_labels)

# Plot first few images
pyplot.figure(figsize=(10, 10))  # Create a larger figure to accommodate the grid
for i in range(9):
    pyplot.subplot(3, 3, i + 1)  # 3x3 grid
    pyplot.imshow(trainX[i])
    pyplot.axis('off')  # Hide axes for better visualization

pyplot.tight_layout()  # Adjust layout to prevent overlap
pyplot.show()