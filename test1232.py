
from apscheduler.schedulers.tornado import TornadoScheduler
sched = TornadoScheduler
c = sched.get_jobs()
print(c)