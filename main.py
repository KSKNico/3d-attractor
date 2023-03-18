import moderngl_window as mglw

class Main(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (640, 360)
    aspect_ratio = 16 / 9
    title = "3D Attractor"
    resizable = False
    samples = 8

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Do initialization here

    def render(self, time, frametime):
        # This method is called every frame
        pass

# Blocking call entering rendering/event loop
mglw.run_window_config(Main)