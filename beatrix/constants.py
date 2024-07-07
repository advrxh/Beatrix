import os


class Beatrix:
    token = os.getenv("TOKEN")
    admin_id = os.getenv("ADMIN")
    downloads_dir = os.getenv("DOWNLOADS")
    binge_box_dir = os.getenv("BINGE_BOX")
    cache_dir = os.getenv("CACHE")
    zoom_executable = os.getenv("ZOOM")
    qbit_port = int(os.getenv("QBITPORT"))
