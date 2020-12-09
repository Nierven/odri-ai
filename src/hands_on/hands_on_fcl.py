# import pinocchio and the robot
from example_robot_data import load
import pinocchio

# import visualizer
from panda3d_viewer import Viewer, ViewerConfig
from pinocchio.visualize.panda3d_visualizer import Panda3dVisualizer

# load the robot and its initial configuration
robot = load('solo12')
model = robot.model
data = robot.data
q = robot.q0[:]
q[2] = 0.4 # place solo above the ground

# configure its collision model
robot.collision_model.addAllCollisionPairs()
print(len(robot.collision_model.collisionPairs))

# configure a Panda3D window
config = ViewerConfig()
config.set_window_size(800, 600)
config.show_axes(True)
config.show_floor(False)
config.enable_antialiasing(True, multisamples=4)

# open a GUI window
viewer = Viewer(window_title='solo12-pinocchio', config=config)
viewer.reset_camera(pos=(1,-1,1), look_at=(0,0,0))

# attach the robot to the visualizer
robot.setVisualizer(Panda3dVisualizer())
robot.initViewer(viewer=viewer) # attach to a viewer's scene
robot.loadViewerModel(group_name=model.name)

# display the robot
robot.display(q)

# wait for the user action
viewer.join()