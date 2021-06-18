from pathlib import Path
import mypackage

PACKAGE_ROOT = Path(mypackage.__file__).resolve().parent

with open(PACKAGE_ROOT / 'VERSION') as f:
    __version__ = f.read().strip()