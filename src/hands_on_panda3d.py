from panda3d_viewer import Viewer, ViewerConfig

config = ViewerConfig()
config.set_window_size(320, 240)
config.enable_antialiasing(True, multisamples=4)

viewer = Viewer()

viewer.append_group('root')
viewer.append_box('root', 'box_node', size=(1, 1, 1))
viewer.append_sphere('root', 'sphere_node', radius=0.5)

viewer.set_material('root', 'box_node', color_rgba=(0.7, 0.1, 0.1, 1))
viewer.set_material('root', 'sphere_node', color_rgba=(0.1, 0.7, 0.1, 1))

viewer.move_nodes('root', {
    'box_node': ((0, 0, 0.5), (1, 0, 0, 0)),
    'sphere_node': ((0, 0, 1.5), (1, 0, 0, 0))})

viewer.reset_camera(pos=(4, 4, 2), look_at=(0, 0, 1))
viewer.save_screenshot(filename='box_and_sphere.png')

viewer.join()