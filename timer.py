import re
import sys
import time

from workflow import Workflow3
from workflow.notify import notify, validate_sound

def main(wf):
    request = get_request(wf.args[0])
    if request is None:
        notify("Timer not created", "Invalid request %s" % wf.args[0])
        return

    set_timer(request)

def get_request(args): # returns (timer name, duration, unit (h, m, or s))
    match = re.match("(.+) (\d{1,3})([hms])", args)
    return None if match is None else (match.group(1), match.group(2), match.group(3))

def set_timer(request):

    name = request[0]
    duration = int(request[1])
    unit = request[2]

    seconds = get_seconds(duration, unit)

    time.sleep(seconds)

    notify("%s" % name, "set %s%s ago" % (duration, unit), "Purr")

def get_seconds(duration, unit):
    if unit == 's':
        return duration
    elif unit == 'm':
        return duration * 60
    elif unit == 'h':
        return duration * 60 * 60
    else:
        raise Exception("Unsupported unit: %s" % unit)

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))

