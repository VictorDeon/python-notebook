from matplotlib import pyplot as plt
import cv2


def show(img, color=True):
    """
    Redimensionar a imagem e mostrar no codigo.
    """

    if color:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.rcParams['figure.figsize'] = (50, 50)
    plt.imshow(img)
    plt.axis("off")
    plt.show()