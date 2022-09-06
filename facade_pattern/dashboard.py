from facade_pattern.fog_lamp_light import FogLampLight
from facade_pattern.hand_brake_light import HandBrakeLight


class Dashboard:
    def __init__(self):
        self.lights = {"handbrake": HandBrakeLight(), "fog": FogLampLight()}

    def show(self):
        for light in self.lights.values():
            light.status_check()