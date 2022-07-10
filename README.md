# pi_pico_neopixel
a library for using ws2812b and sk6812 leds (aka neopixels) with Raspberry Pi Pico

![example](https://github.com/blaz-r/pi_pico_neopixel/blob/main/pico_rgbw_rgb.jpg)

### Detailed documentation can be found on [Wiki page](https://github.com/blaz-r/pi_pico_neopixel/wiki).

## Quick start guide

You'll first need to save the neopixel.py file to your device (for example, open it in Thonny and go file > save as and select MicroPython device. Give it the same name). Once it's there, you can import it into your code. 

## Initialization

You create an object with the parameters number of LEDs, state machine ID, GPIO number and mode (RGB or RGBW) in that order. So, to create a strip of 10 leds on state machine 0 and GPIO 0 in RGBW mode you use:

```
from neopixel import Neopixel

pixels = Neopixel(10, 0, 0, "RGBW")
```

Mind that you can use whichever order of RGB / RGBW you want (GRB, WRGB, GRB, RGWB ...). This only represents order of data sent to led-strip, all functions still work with RGBW order. Exact order of leds should be on package of your led-strip. (My BTF-lights sk6812 has GRBW).

## Usage

This class has many methods, two main ones being show() which sends the data to the strip, and set_pixel which sets the color values for a particular LED. The parameters are LED number and a tuple of form (red, green blue) or (red, green, blue, white) with the colors taking values between 0 and 255.

At the moment, this isn't working with the interpreter, so you have to run it from a file. Looks like it's running just too slow to keep up with the PIO buffer from the interpreter. The key methods are set_pixel(n (r,g,b)), set_pixel_line(p1, p2, (r, g, b)) which sets a row of pixels from pixel p1 to pixel p2 (inclusive), and fill((r,g,b)) which fills all the pixels with the color r, g, b.
If you want to use the library for RGBW, each function works the same just with last parameter being "white": set_pixel(num, (r, g, b, w))

## Examples

```
pixels.set_pixel(5, (10, 0, 0))
pixels.set_pixel_line(5, 7, (0, 10, 0))
pixels.fill((20, 5, 0))

rgbw1 = (0, 0, 50, 0)
rgbw2 = (50, 0, 0, 250)
pixels.set_pixel(42, (0, 50, 0, 0))
pixels.set_pixel_line(5, 7, rgbw1)
pixels.set_pixel_line_gradient(0, 13, rgbw1, rgbw2)
```

For new settings to take effect you write:
```
pixels.show()
```

For more examples, check [examples folder](https://github.com/blaz-r/pi_pico_neopixel/tree/main/examples) and [documentation](https://github.com/blaz-r/pi_pico_neopixel/wiki).

## HSV colors

Library also supports HSV colors. For example you can look at [smoothRinbow.py](https://github.com/blaz-r/pi_pico_neopixel/blob/main/examples/smoothRainbow.py).
To use HSV colors, call colorHSV(hue, sat, val) function with hue, saturation and value as parameters. The function returns rgb tuple that you can then use in all other functions.

Hue should be between 0 and 65535. When it becomes larger it just rolls over (65536 -> 0). Saturation and value must be in range from 0 to 255. 255 saturation means just hue, and 255 value is maximum brightness. For more info about HSV colors you can check out [Adafruit NeoPixel library documentation](https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use) and scroll down to HSV section.

```
color = pixels.colorHSV(32000, 255, 200)
pixels.fill(color)
pixels.show()
```

Library is extended verison of https://github.com/blaz-r/pico_python_ws2812b, originally forked from https://github.com/benevpi/pico_python_ws2812b.
