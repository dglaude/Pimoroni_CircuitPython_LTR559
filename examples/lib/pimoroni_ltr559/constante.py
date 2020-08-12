# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Philip Howard, written for Pimoroni Ltd
#
# SPDX-License-Identifier: MIT
"""
`pimoroni_circuitpython_ltr559`
================================================================================

Library for the LTR559 Proximity/Presence/Light Sensor


* Author(s): Philip Howard

Implementation Notes
--------------------

**Hardware:**

Written to support Pimoroni's LTR559 breakout and Enviro+ FeatherWing.

* Pimoroni LTR559 Breakout Garden Breakout:
  https://shop.pimoroni.com/products/ltr-559-light-proximity-sensor-breakout

* Pimoroni Enviro+ FeatherWing:
  https://shop.pimoroni.com/products/enviro-plus-featherwing

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

* Adafruit's Register library:
  https://github.com/adafruit/Adafruit_CircuitPython_Register
"""
from micropython import const

__version__ = "0.0.1"
__repo__ = "https://github.com/pimoroni/Pimoroni_CircuitPython_LTR559.git"


### _LTR559_I2C_ADDR = const(0x23)
### _LTR559_PART_ID = const(0x09)
### _LTR559_REVISION_ID = const(0x02)

### _LTR559_REG_ALS_CONTROL = const(0x80)
### _LTR559_REG_PS_CONTROL = const(0x81)
### _LTR559_REG_PS_LED = const(0x82)
### _LTR559_REG_PS_N_PULSES = const(0x83)
### _LTR559_REG_PS_MEAS_RATE = const(0x84)
### _LTR559_REG_ALS_MEAS_RATE = const(0x85)
### _LTR559_REG_PART_ID = const(0x86)
### _LTR559_REG_MANUFACTURER_ID = const(0x87)
### _LTR559_REG_ALS_DATA_CH1 = const(0x88)
_LTR559_REG_ALS_DATA_CH0 = const(0x8A)
### _LTR559_REG_ALS_PS_STATUS = const(0x8C)
### _LTR559_REG_PS_DATA_CH0 = const(0x8D)
### _LTR559_REG_PS_DATA_SAT = const(0x8E)
### _LTR559_REG_INTERRUPT = const(0x8F)
### _LTR559_REG_PS_THRESHOLD_UPPER = const(0x90)
### _LTR559_REG_PS_THRESHOLD_LOWER = const(0x92)
### _LTR559_REG_PS_OFFSET = const(0x94)
### _LTR559_REG_ALS_THRESHOLD_UPPER = const(0x97)
### _LTR559_REG_ALS_THRESHOLD_LOWER = const(0x99)
### _LTR559_REG_INTERRUPT_PERSIST = const(0x9E)

LTR559_INTERRUPT_MODE_OFF = const(0b00)
LTR559_INTERRUPT_MODE_PS = const(0b01)
LTR559_INTERRUPT_MODE_ALS = const(0b10)

### LTR559_LED_FREQ_30KHZ = const(0b000)
LTR559_LED_FREQ_40KHZ = const(0b001)
LTR559_LED_FREQ_50KHZ = const(0b010)
LTR559_LED_FREQ_60KHZ = const(0b011)
LTR559_LED_FREQ_70KHZ = const(0b100)
LTR559_LED_FREQ_80KHZ = const(0b100)
LTR559_LED_FREQ_90KHZ = const(0b110)
LTR559_LED_FREQ_100KHZ = const(0b111)

LTR559_LED_DUTY_25 = const(0b00)
LTR559_LED_DUTY_50 = const(0b01)
LTR559_LED_DUTY_75 = const(0b10)
### LTR559_LED_DUTY_100 = const(0b11)

LTR559_LED_CURRENT_5MA = const(0b000)
LTR559_LED_CURRENT_10MA = const(0b001)
LTR559_LED_CURRENT_20MA = const(0b010)
### LTR559_LED_CURRENT_50MA = const(0b011)
LTR559_LED_CURRENT_100MA = const(0b100)

LTR559_PS_INTEGRATION_TIME_100MS = const(0b000)
LTR559_PS_INTEGRATION_TIME_50MS = const(0b001)
LTR559_PS_INTEGRATION_TIME_200MS = const(0b010)
LTR559_PS_INTEGRATION_TIME_400MS = const(0b011)
LTR559_PS_INTEGRATION_TIME_150MS = const(0b100)
LTR559_PS_INTEGRATION_TIME_250MS = const(0b101)
LTR559_PS_INTEGRATION_TIME_300MS = const(0b110)
LTR559_PS_INTEGRATION_TIME_350MS = const(0b111)

### LTR559_PS_RATE_50MS = const(0b000)
LTR559_PS_RATE_100MS = const(0b001)
LTR559_PS_RATE_200MS = const(0b010)
LTR559_PS_RATE_500MS = const(0b011)
LTR559_PS_RATE_1000MS = const(0b100)
LTR559_PS_RATE_2000MS = const(0b101)

LTR559_ALS_GAIN_1X = const(0b000)
LTR559_ALS_GAIN_2X = const(0b001)
### LTR559_ALS_GAIN_4X = const(0b010)
LTR559_ALS_GAIN_8X = const(0b011)
LTR559_ALS_GAIN_48X = const(0b110)
LTR559_ALS_GAIN_96X = const(0b111)

### LTR559_ALS_RATE_50MS = const(0b000)
LTR559_ALS_RATE_100MS = const(0b001)
LTR559_ALS_RATE_200MS = const(0b010)
LTR559_ALS_RATE_500MS = const(0b011)
LTR559_ALS_RATE_1000MS = const(0b100)
LTR559_ALS_RATE_2000MS = const(0b101)

LTR559_ALS_INTEGRATION_TIME_100MS = const(0b000)
### LTR559_ALS_INTEGRATION_TIME_50MS = const(0b001)
LTR559_ALS_INTEGRATION_TIME_200MS = const(0b010)
LTR559_ALS_INTEGRATION_TIME_400MS = const(0b011)
LTR559_ALS_INTEGRATION_TIME_150MS = const(0b100)
LTR559_ALS_INTEGRATION_TIME_250MS = const(0b101)
LTR559_ALS_INTEGRATION_TIME_300MS = const(0b110)
LTR559_ALS_INTEGRATION_TIME_350MS = const(0b111)
