## Context Manager Examples - Advanced Usecase. 
## yield without argument is semantically equivalent to yield None

from contextlib import contextmanager
import sys

@contextmanager
def redirected(**kwds):
    stream_names = ["stdin", "stdout", "stderr"]
    old_streams = {}
    try:
        for sname in stream_names:
            stream = kwds.get(sname, None)
            if stream is not None and stream != getattr(sys, sname):
                old_streams[sname] = getattr(sys, sname)
                setattr(sys, sname, stream)
        yield
    finally:
        for sname, stream in old_streams.items():
            setattr(sys, sname, stream)

with redirected(stdout=open("/tmp/uw-py220-log-context-mgr.txt", "w")):
     # these print statements will go to /tmp/log.txt
     print ("Test entry 1")
     print ("Test entry 2")
# back to the normal stdout
print ("Back to normal stdout again")