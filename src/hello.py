import os
import pathlib
import subprocess

import gi
gi.require_version("OSTree", "1.0")

from gi.repository import OSTree

OSTREE_REPO_MODE_BARE_USER = 2

pathlib.Path("ostree/tree").mkdir(parents=True,exist_ok=False)

fd = os.open('ostree', os.O_RDONLY)
ostrepo = OSTree.Repo.create_at(fd, "repo", OSTree.RepoMode(OSTREE_REPO_MODE_BARE_USER), None, None)

with open("ostree/tree/hello.txt", 'w') as fo:
    fo.write("Hello, World!\n")

subprocess.run(["ostree", "--repo=ostree/repo", "commit", "--branch=foo", "ostree/tree"], check=True)

status, refs = ostrepo.list_refs()
print(list(refs.keys()))

ostrepo.checkout_at(None, fd, "tree-checkout", refs["foo"], None )

with open("ostree/tree-checkout/hello.txt", 'r') as fo:
    print(fo.readline())
