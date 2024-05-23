import os
from controllers import BaseController

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    def get_path(self,plot_id):
        plot_id = os .path.join(self.file_dir ,plot_id)


        return plot_id