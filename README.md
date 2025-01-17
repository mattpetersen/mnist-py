# mnist-py

Lazily loads from `/tmp/mnist/` and caches the resulting numpy arrays. Downloads any missing MNIST files first.

## Installation

```bash
pip install mnist-py
```

## Usage

```python
from mnist import MNIST


mnist = MNIST()

# Train set is lazily loaded into memory and cached afterward
mnist.train_set.images  # (60000, 784)
mnist.train_set.labels  # (60000, 10)

# Test set is lazily loaded into memory and cached afterward
mnist.test_set.images   # (10000, 784)
mnist.test_set.labels   # (10000, 10)

# Yield minibatches from the shuffled train set
for images, labels in mnist.train_set.minibatches(batch_size=256):
    pass
```


## Image data

Images are rows, each of length 784, and with pixel values scaled to the range zero through one.

## Label data

Lables are one-hot rows each of length ten.

```python
[0 0 1 ... 0]  # 3
[0 0 0 ... 1]  # 9
```

## Example: Softmax Regression
```python
import numpy as np

from mnist import MNIST


def softmax(x: np.array) -> np.array:
    """Apply softmax independently to each row."""
    z = np.exp(x - x.max(1)[:, None])
    return z / z.sum(1)[:, None]


def main():
    learning_rate = 0.01
    batch_size = 256
    n_epochs = 4

    mnist = MNIST()

    weights = np.random.randn(784, 10) * np.sqrt(2 / 784)
    for _ in range(n_epochs):
        for images, labels in mnist.train_set.minibatches(batch_size):
            preds = softmax(images.dot(weights))
            error = images.T.dot(preds - labels)
            weights -= learning_rate * error

            acc = np.mean(preds.argmax(1) == labels.argmax(1))
            print(f'Train acc: {acc}')


if __name__ == '__main__':
    main()
```
