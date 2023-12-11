import signal
from timeout_decorator import timeout

# Define your function
@timeout(1)  # Set the timeout to 5 seconds
def wrap_up():
    while True:
        pass

# signal.signal(signal.SIGALRM,lambda x,y:exit())
# signal.alarm(5)
# for i in range(3):
#     try:
#         wrap_up()
#     except TimeoutError:
#         print(f"Function timed out {i}")

# print("continuou")
# signal.alarm(0)

try:
    wrap_up()
except TimeoutError:
    print("Function timed out")

