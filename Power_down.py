import os
from logging import shutdown

# shutdown declaration

shut_down = ["shutdown", "-f", "-s", "-t", "15"]
# shut down function
def shutdown(self):
    import subprocess
    subprocess.call(shut_down)


# restart declaration
re_boot = ["shutdown", "-f", "-r", "-t", "30"]
# restart function
def restart(self):

    import subprocess
    subprocess.call(re_boot)

