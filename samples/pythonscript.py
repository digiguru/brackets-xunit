#!/usr/bin/env python -u
# brackets-xunit: args=10
import time,sys
loops=5
if len(sys.argv)>1:
    loops=int(sys.argv[1])
start = time.time()
for i in range(loops):
    print("looping...%d" % (time.time()-start))
    time.sleep(1)
    
print("done")
sys.exit(10)