# Check that the packages are installed.
import sys

from pkgutil import iter_modules


def check_import(packagename):
    if packagename in (name for _, name, _ in iter_modules()):
        return True
    else:
        return False


packages = [
    "networkx",
    "numpy",
    "matplotlib",
    "hiveplot",
    "pandas",
    "jupyter",
    "nxviz",
    "community",
]

for p in packages:
    assert check_import(p), "{0} not present. Please install via pip or conda.".format(
        p
    )

assert sys.version_info.major >= 3, "Please install Python 3!"

# Credit: @zmilicc for requesting this.
print("All checks passed. Your environment is good to go!")


unrequitted_friendships = []
# Fill in your answer below.

import itertools

unrequitted_friendships = [
    edge
    for edge, *_ in itertools.combinations(G.edges(), 1)
    if (G.has_edge(*edge) and not G.has_edge(*reversed(edge)))
]


assert len(unrequitted_friendships) == 124
