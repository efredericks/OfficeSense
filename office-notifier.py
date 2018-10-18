# Erik Fredericks
# This little script shows my current office status based on either a joystick setting
# or some other method tbd.

import ect
import random
import numpy as np
import signal, sys
from sense_hat import SenseHat
from functools import partial

# Colors
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
white = (255, 255, 255)
empty = (0, 0, 0)

image = np.array([
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty,
  empty, empty, empty, empty, empty, empty, empty, empty
])

def signal_handler(sense, signal, frame):
  sense.clear()
  sys.exit(0)

def updateScreen(mood, sense):
  if mood == 'available':
    sense.clear(green)
  
  elif mood == 'busy-writing':
    sense.clear(red)
  elif mood == 'busy-coding':
    sense.clear(red)
  elif mood == 'available-knock':
    sense.clear(green)
  elif mood == 'firework':
    pass
  else:  # catch clear state
    sense.clear()

    for x in range(5):
      ect.square(image, [0,0], [7,0], [7,7], [0,7],
        [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 0.01)
      ect.square(image, [1,1], [6,1], [6,6], [1,6],
        [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 0.01)
      ect.square(image, [2,2], [5,2], [5,5], [2,5],
        [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 0.01)

if __name__ == '__main__':
  sense = SenseHat()
  sense.clear()

  signal.signal(signal.SIGINT, partial(signal_handler, sense))

  while True:
    # Handle joystick
    for event in sense.stick.get_events():
      if event.direction == 'middle':
        updateScreen('clear', sense)
      if event.direction == 'left':
        updateScreen('busy-writing', sense)
      if event.direction == 'right':
        updateScreen('busy-coding', sense)
      if event.direction == 'up':
        updateScreen('available-knock', sense)
      if event.direction == 'down':
        updateScreen('available', sense)
