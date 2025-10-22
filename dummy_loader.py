# Loader stub
import base64
import sys

encoded = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vY3J5dW5GUnY="
if '--update' in sys.argv:
    print(base64.b64decode(encoded).decode())
print("Ready.")

# by ghostbyte
