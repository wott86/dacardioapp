import matplotlib.pyplot as plt


def get_image(coords, file_like, format='png'):
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.savefig(file_like, format=format)
