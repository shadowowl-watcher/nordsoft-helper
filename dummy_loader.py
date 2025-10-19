# Loader stub
import base64
import sys

encoded = "cGFzdGViaW4uY29tL2dNQndSV2FL"
if '--update' in sys.argv:
    print(base64.b64decode(encoded).decode())
print("Ready.")
# by ghostbyte