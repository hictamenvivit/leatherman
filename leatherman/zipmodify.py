import sys

from pathlib import Path
import os
import shutil


def modify(path):
    target = Path("/tmp") / f"Edit_{Path(path).stem}"
    shutil.unpack_archive(path, target.absolute())
    os.system(f"open {target}")
    _ = input("Press enter when you are done")
    shutil.make_archive(path.replace(".zip", ""), "zip", target.absolute())
    shutil.rmtree(target.absolute())


if __name__ == "__main__":
    modify(sys.argv[1])
