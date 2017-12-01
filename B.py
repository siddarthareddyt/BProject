import numpy as np
from PIL import Image

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

def convert(path):
    print path
    image = Image.open(path)
    grey = image.convert('1')
    imageArr = np.array(grey, dtype=bool)
    imgIntArr = imageArr.astype(int)

    cols = len(imgIntArr[0])
    rows = len(imgIntArr)

    newArr = blockshaped(imgIntArr, 8, 8)

    k = 0
    for lineBlock in newArr:
        print "["
        for i in range(0, len(lineBlock)):
            col = lineBlock[:,i]
            revCol = list(reversed(col))
            colString = [str(n) for n in revCol]
            binaryString = ''.join(colString)
            hexValue = hex(int(binaryString, 2))
            print hexValue + ","
        print "], "
        k+=1
        if k == 16:
            print "-------------------------------------------------"
            k = 0






def main():
    convert("Artboard.png")

if __name__ == "__main__":
    main()