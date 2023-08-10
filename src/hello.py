import os
import pathlib

import gi
gi.require_version("OSTree", "1.0")

from gi.repository import OSTree

OSTREE_REPO_MODE_BARE_USER = 2

pathlib.Path("ostree/tree").mkdir(parents=True,exist_ok=False)

ofd = os.open('ostree', os.O_RDONLY)
ostrepo = OSTree.Repo.create_at(ofd, "repo", OSTree.RepoMode(OSTREE_REPO_MODE_BARE_USER), None, None)

with open("ostree/tree/hello.txt", 'w') as fo:
    fo.write("Hello, World!\n")

ostrepo.prepare_transaction(None)
mutree = OSTree.MutableTree.new()
ostrepo.write_dfd_to_mtree(ofd, "tree", mutree, None, None)
mfile = ostrepo.write_mtree(mutree, None)
mcommit = ostrepo.write_commit(None, None, None, None, mfile[1], None)
print(mcommit[1])
ostrepo.transaction_set_ref(None, "foo", mcommit[1])
ostrepo.commit_transaction(None)

status, refs = ostrepo.list_refs()
print(list(refs.keys()))

ostrepo.checkout_at(None, ofd, "tree-checkout", refs["foo"], None )

with open("ostree/tree-checkout/hello.txt", 'r') as fo:
    print(fo.readline())
