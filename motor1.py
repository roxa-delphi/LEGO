import time

import nxt.locator
import nxt.motcont
import nxt.motor

with nxt.locator.find() as b:
  print(b.get_device_info())

  mc = nxt.motcont.MotCont(b)

  def wait() :
    while not mc.is_ready(nxt.motor.Port.B) or not mc.is_ready(nxt.motor.Port.C):
      time.sleep(0.5)

  mc.start()

  mc.cmd((nxt.motor.Port.B, nxt.motor.Port.C), 100,720)
  wait()

  mc.cmd((nxt.motor.Port.B, nxt.motor.Port.C), -100,720)
  wait()

  mc.stop()


