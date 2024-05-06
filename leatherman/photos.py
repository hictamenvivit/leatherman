import os


def handle_folder():
    try:
        os.mkdir("raw")
    except:
        pass

    for x in os.listdir("."):
        if x.endswith(".JPG"):
            os.rename(x, x.replace(".JPG", ".jpg"))
        if x.endswith(".RW2"):
            os.rename(x, f"raw/{x}")
