from flask_restful import Resource, fields, marshal_with
from flask import send_file
import io

from common.device_maker import CameraDevice
from common.image_collector import Collector

class Preview(Resource):
    def get(self):
        cd = CameraDevice()
        c = Collector()
        byte_stream = c.get_frame(c.preview_queue, "preview")

        if isinstance(byte_stream, str):
            return {'status': 'error', 'info': 'no image!'}, 400
        else:
            return send_file(io.BytesIO(byte_stream), attachment_filename="preview.png", mimetype="image/jpeg")
