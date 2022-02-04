
import mujoco_py 
import os
import math

mj_path = '/home/gabs/Rover4We/'
xml_path = os.path.join(mj_path, 'rover4We-field.xml')
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim) 
t = 0
while True:
    sim.data.ctrl[0] = math.cos(t) *  0.29
    sim.data.ctrl[1] = math.sin(t * 0.01)
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break