'''
    Bring Python's various filesystem, file, and path-related functionality
    under one roof.

    Open questions:

        - File descriptors, probably no
        - chroot?
        - l- functions to not follow links?
        - Unix dev files?  obscure
        - pathconf?
        - supports api is a bit odd?
        - scandirs and/or walk?

        - Unpack os.path functions?  Handy but lengthy.
        - Unpack file related shutil functions?  Or leave as submodule.
'''
# Path manipulation
import os.path as path
from pathlib import Path

# File manipulation from the os module:
from os import (
    access,
        F_OK,
        R_OK,
        W_OK,
        X_OK,

    chdir,
    #~ chflags,  # include stat flags?
    chmod,
    chown,
    #~ chroot,
    devnull,
    getcwd,
    getcwdb,

    fspath, fsencode, fsdecode,         # fs path codec
    #~ lchflags, lchmod, lchown, lstat,  # dont' follow links

    link,
    listdir,
    makedirs,
    mkdir,
    mkfifo,
    #~ mknod, major, minor, makedev,  # devices, not common?
    #~ pathconf,
    readlink,

    remove,
    rename,
    renames,
    replace,

    # these don't match:
    rmdir,
    removedirs as rmdirs,

    scandir,
    stat,
    statvfs,
    symlink,
    sync,
    truncate,
    utime,

    #~ supports_dir_fd,  # unsure
    #~ supports_effective_ids,
    #~ supports_fd,
    #~ supports_follow_symlinks,

    #~ walk, fwalk,  # use scandir?

    # extended attrs
    getxattr,
    listxattr,
    removexattr,
    setxattr,
        XATTR_SIZE_MAX,
        XATTR_CREATE,
        XATTR_REPLACE
)

# Shell convenience functions
import shutil as util
from shutil import (

    copy2 as copy,
    copytree,
    rmtree,
    move,
)
