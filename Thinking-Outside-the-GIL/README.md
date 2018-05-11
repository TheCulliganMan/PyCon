# Thinking Outside the GIL async.io and Multiprocessing
## John Reese -- Facebook -- exabyte scale storage

### Takeaways:

1. Switch to Python 3
  * ~45% memory savings
  * ~20% runtime reduction


Use multiprocessing primitives + event loop per process, queues for work and results

Newer versions of python3 use spawn instead of fork.  This means we could be getting memory savings already with the 3.6.4 versions. 

# Github
https://github.com/jreese/aiomultiprocess

# IT IS ON PIP!!!

```bash
pip install aiomultiprocess
```