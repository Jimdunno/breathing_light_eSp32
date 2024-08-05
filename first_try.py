from machine import Pin, PWM
import time

led2 = PWM(Pin(2))
led2.freq(1000)

while True: # Control the repetition of the light pulse

    # From off gradually to on
    for i in range(0, 1024):
        led2.duty(i)
        time.sleep_ms(2)

    # From on gradually to off
    for i in range(1023, -1, -1):
        led2.duty(i)
        time.sleep_ms(2)



