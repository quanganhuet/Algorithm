import sys
from keras.datasets import cifar10
from keras.utils import to_categorical
from matplotlib import pyplot
from model import VGGFace

# load train and test dataset
def load_dataset():
    # load dataset
    (trainX, trainY), (testX, testY) = cifar10.load_data()
    # one hot encode target values
    trainY = to_categorical(trainY)
    testY = to_categorical(testY)
    return trainX, trainY, testX, testY


# scale pixels
def prep_pixels(train, test):
# convert from integers to floats
    train_norm = train.astype('float32')
    test_norm = test.astype('float32')
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    # return normalized images
    return train_norm, test_norm

def summarize_diagnostics(history):
# plot loss
    pyplot.subplot(211)
    pyplot.title('Cross Entropy Loss')
    pyplot.plot(history.history['loss'], color= 'blue', label= 'train' )
    pyplot.plot(history.history[ 'val_loss' ], color= 'orange' , label= 'test' )
    # plot accuracy
    pyplot.subplot(212)
    pyplot.title( 'Classification Accuracy' )
    pyplot.plot(history.history[ 'acc' ], color= 'blue' , label= 'train' )
    pyplot.plot(history.history[ 'val_acc' ], color= 'orange' , label= 'test' )
    # save plot to file
    filename = sys.argv[0].split('/')[-1]
    pyplot.savefig(filename + 'plot.png' )
    pyplot.close()

def main(args):
    # load dataset
    vgg = VGGFace()
    trainX, trainY, testX, testY = load_dataset()
    # prepare pixel data
    trainX, testX = prep_pixels(trainX, testX)
    vgg_face_1_block=  vgg.vgg_face_1_block()
    history = vgg_face_1_block.fit(trainX, trainY, epochs=100, batch_size=16, validation_data=(testX, testY), verbose=0)
    # evaluate model
    _, acc = vgg_face_1_block.evaluate(testX, testY, verbose=0)
    print('> %.3f' % (acc * 100.0))
    # learning curves
    summarize_diagnostics(history)


if __name__ == '__main__':
    main(1)