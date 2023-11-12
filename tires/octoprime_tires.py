from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears

    def needs_service(self):
        return sum(self.tire_wears) >= 3
