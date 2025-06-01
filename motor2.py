import nxt.locator
import nxt.motor

with nxt.locator.find() as b:
  mymotor = b.get_motor(nxt.motor.Port.B)
  mymotor.turn(25,360)
  mymotor.turn(-25,360)

