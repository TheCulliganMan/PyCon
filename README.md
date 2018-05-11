# PyCon

Notes and notebooks from pycon.

## Down the Rabbit Hole

### Reproducible data flows in Python

This will be extremely useful for all our work.


## Epiphanies

### Python's Quirks

Not that useful, but kind of interestings

## Network Analysis 101

### NetworkX + NXVis

Extremely useful. With many practical examples.  I think we need a graph database.  Bonus notebook three 
could be a lifesaver in Alex's project.

* NOTEBOOK 5!!!! BONUS NOTEBOOK 3 *

## Using Pandas For Better (Or Worse) 

You already know all of this.  If you don't somebody else in the group does.  Probably not worth your time.

## Thinking outside the GIL with AsyncIO and Multiprocessing

Facebook exascale storage people made a module that combines asyncio and multiprocessing for 8x performance 
gains against single threaded code and 5x gains against multiprocessed code.  It implements 
`map -> multiprocessing -> async.io --> reduce` to fully saturate a box. 
[Repo is here https://github.com/jreese/aiomultiprocess](https://github.com/jreese/aiomultiprocess).


## Performance Python: Seven Strategies for Optimizing your Numerical Code

