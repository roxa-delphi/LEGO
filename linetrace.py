import nxt.locator
import nxt.sensor
import nxt.sensor.generic
import nxt.motcont
import nxt.motor

with nxt.locator.find() as b:
  sens = b.get_sensor(nxt.sensor.Port.S3, nxt.sensor.generic.Color)
  mc   = nxt.motcont.MotCont(b)
  mc.start()

  while (1) :
    col = sens.get_color()
    #print("color : %d" %(col.value))

    if col.value == 1 :
      mc.set_output_state(nxt.motor.Port.B,  0, 0)
      mc.set_output_state(nxt.motor.Port.C, 50, 0)
    else :
      mc.set_output_state(nxt.motor.Port.B, 50, 0)
      mc.set_output_state(nxt.motor.Port.C,  0, 0)


mc.stop()

