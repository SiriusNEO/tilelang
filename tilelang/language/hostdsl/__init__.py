"""HostDSL for tl programs.

@T.prim_func
def func():
    # Host part of kernel

    # Device part of kernel, split by kernel launch
    with T.Kernel(...)
        ...
"""
