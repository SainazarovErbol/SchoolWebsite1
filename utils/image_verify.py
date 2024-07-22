from PIL import Image


class NoImageException(Exception):
    pass


def image_verify(file):
    try:
        img = Image.open(file)
        img.verify()
    except (IOError, SyntaxError):
        raise NoImageException("Invalid image file")
