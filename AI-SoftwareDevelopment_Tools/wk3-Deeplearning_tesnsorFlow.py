# Import TensorFlow. TensorFlow provides the deep learning framework and Keras API for building models.
import tensorflow as tf
# Build a Sequential model, which is a linear stack of layers.
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np # numerical operations

# 1. Load MNIST Dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to range [0,1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Add channel dimension (CNN expects 4D input)
x_train = np.expand_dims(x_train, -1)   # shape: (60000, 28, 28, 1)
x_test = np.expand_dims(x_test, -1)

# 2. Build CNN Model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D((2,2)),

    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# 3. Train the Model
history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

# 4. Evaluate the model on the Test Set
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest Accuracy: {test_acc * 100:.2f}%")

# 5. Visualize Predictions on 5 Sample Test Images
num_images = 5
sample_images = x_test[:num_images]
sample_labels = y_test[:num_images]

predictions = model.predict(sample_images)
predicted_classes = np.argmax(predictions, axis=1)

plt.figure(figsize=(10, 3))
for i in range(num_images):
    plt.subplot(1, num_images, i+1)
    plt.imshow(sample_images[i].reshape(28, 28), cmap="gray")
    plt.title(f"Pred: {predicted_classes[i]}\nTrue: {sample_labels[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()
