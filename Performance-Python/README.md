# Performance Python: Seven Strategies for Optimizing Your Numerical Code
## [Jake Vanderplas](https://github.com/jakevdp)


## Takeaways

1. Python is much slower than fortran.
  * What do you do when things are slow
    1. Line profileing `lprun | %line_profiler`
    2. Vectorization (numpy) 
        * when you loop over numbers best do it in numpy.
        * overhead is per array rather than per array item
        * use numpy everywhere
    3. Specialized Data Structures
        * Tools:
            1. pandas
            2. scipy.spacial.cKDTree
            3. xarray (multidimentional pandas) # We need to check this one out.
    4. Cython :
        * Turns python into C...
        * About 100x faster than python
        * At the expense of code readability...
    5. Numba
        * JIT LLVM bytecode
        * Just add some decorators!
        * Heavy dependency chain, and possible errors. 
    6. DASK + DASKML (Takes more time on small datasets, enables high memory compute)
        * Mirrors numpy + pandas API
        * For when your data is just too big.
        * np.array => dask.array => cluster / local / whatever
    7. USE EXISTING CODE!!!
        * If you are creating an implementation of an algorithm chances are it is implemented somewhere.
        * The community is python's strength!
        
