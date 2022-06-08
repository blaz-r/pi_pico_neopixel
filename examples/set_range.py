# Example showing use of 'slice setting'
import time
from neopixel import Neopixel


numpix = 60
K = 3

strip = Neopixel(numpix, 0, 0, "GRB")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# set the first K to red, next K to green, next K to blue;
# and the rest to R,G,B,R,B  ... and then spin it.

# reduce K, if numpix is < K*3+1
K = min(K,(numpix-1)//3)

strip.brightness(80)

strip[:] = blue   # all to blue first...
# now fill in the red & green...
strip[:K] = red
strip[K:2*K] = green
strip[3*K::3] = red
strip[3*K+1::3] = green

strip.show()

# show it for 5 seconds...
time.sleep(5.0)

# spin it...

while(True):
    strip.rotate_right()
    strip.show()
    time.sleep(0.5)

