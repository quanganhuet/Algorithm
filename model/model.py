from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import SGD

class VGGFace:
    def __init__(self, input_shape=(32, 32, 3), optimizer=None):
        print("Init VGGG")
        self.input_shape = input_shape
        self.optimizer = optimizer if optimizer else SGD(learning_rate=0.001, momentum=0.9)

    def _add_conv_block(self, model, filters, num_layers):
        """Add a block of Conv2D layers followed by MaxPooling2D."""
        for _ in range(num_layers):
            model.add(Conv2D(filters, (3, 3), activation='relu', 
                             kernel_initializer='he_uniform', padding='same'))
        model.add(MaxPooling2D((2, 2)))

    def _build_model(self, blocks):
        """Build a VGG-like model based on the number of convolutional blocks."""
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', 
                         padding='same', input_shape=self.input_shape))
        
        for block in blocks:
            self._add_conv_block(model, *block)

        # Add the output layer
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.compile(optimizer=self.optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def vgg_face_1_block(self):
        """Create a model with 1 convolutional block."""
        return self._build_model([(32, 2)])  # One block with 2 Conv2D layers (32 filters)

    def vgg_face_2_block(self):
        """Create a model with 2 convolutional blocks."""
        return self._build_model([(32, 2), (64, 2)])  # Two blocks: (32 filters, 2 layers) & (64 filters, 2 layers)

    def vgg_face_3_block(self):
        """Create a model with 3 convolutional blocks."""
        return self._build_model([(32, 2), (64, 2), (128, 2)])  # Three blocks with increasing filters

# Example usage
vgg = VGGFace()
model_1_block = vgg.vgg_face_1_block()
model_2_block = vgg.vgg_face_2_block()
model_3_block = vgg.vgg_face_3_block()

print(model_1_block.summary())
print(model_2_block.summary())
print(model_3_block.summary())
