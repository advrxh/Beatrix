import os


class Beatrix:
    token = os.getenv("TOKEN")
    admin_id = os.getenv("ADMIN")
    downloads_dir = os.getenv("DOWNLOADS")
    binge_box_dir = os.getenv("BINGE_BOX")