import subprocess

subprocess.run(["mkdir", "-v", "ostree"], check=True)

subprocess.run(["ostree", "--repo=ostree/repo", "init"], check=True)

subprocess.run(["mkdir", "-pv", "ostree/tree"], check=True)

with open("ostree/tree/hello.txt", 'w') as fo:
    fo.write("Hello, World!\n")

subprocess.run(["ostree", "--repo=ostree/repo", "commit", "--branch=foo", "ostree/tree"], check=True)

subprocess.run(["ostree", "--repo=ostree/repo", "refs"], check=True)

subprocess.run(["ostree", "--repo=ostree/repo", "checkout", "foo", "ostree/tree-checkout/"], check=True)

with open("ostree/tree-checkout/hello.txt", 'r') as fo:
    print(fo.readline())
