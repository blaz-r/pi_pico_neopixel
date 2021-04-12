# pi_pico_neopixel
a library for using ws2812b and sk6812 leds (aka neopixels) with Raspberry Pi Pico

![example](https://github.com/blaz-r/pi_pico_neopixel/blob/main/pico_rgbw_rgb.jpg)

You'll first need to save the neopixel.py file to your device (for example, open it in Thonny and go file > save as and select MicroPython device. Give it the same name). Once it's there, you can import it into your code. 

You create an object with the parameters number of LEDs, state machine ID, GPIO number and mode (RGB or RGBW) in that order. So, to create a strip of 10 leds on state machine 0 and GPIO 0 in RGBW mode you use:

```
pixels = ws2812b.ws2812b(10, 0, 0, "RGBW")
```

This class has many methods, two main ones being show() which sends the data to the strip, and set_pixel which sets the color values for a particular LED. The parameters are LED number, red, green, blue or a tuple of form (red, green blue) with the colors taking values between 0 and 255.

At the moment, this isn't working with the interpreter, so you have to run it from a file. Looks like it's running just too slow to keep up with the PIO buffer from the interpreter. The key methods are set_pixel(n (r,g,b)), set_pixel_line(p1, p2, (r, g, b)) which sets a row of pixels from pixel p1 to pixel p2 (inclusive), and fill((r,g,b)) which fills all the pixels with the color r, g, b.
If you want to use the library for RGBW, each function works the same just with last parameter being "white": set_pixel(num, (r, g, b, w))

```
pixels.set_pixel(5, (10, 0, 0))
pixels.set_pixel_line(5, 7, (0, 10, 0))
pixels.fill((20, 5, 0))

rgb1 = (0, 0, 50, 0)
rgb2 = (50, 0, 0, 250)
pixels.set_pixel(42, (0, 50, 0))
pixels.set_pixel_line(5, 7, rgb1)
pixels.set_pixel_line_gradient(0, 13, rgb1, rgb2)
```

Library is extended verison of https://github.com/blaz-r/pico_python_ws2812b, originaly forked from https://github.com/benevpi/pico_python_ws2812b.