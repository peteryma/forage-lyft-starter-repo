import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-11-11")
        last_service_date = date.fromisoformat("2019-11-11")
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-11-11")
        last_service_date = date.fromisoformat("2022-11-11")
        battery = SpindlerBattery(current_date, last_service_date)
        
        self.assertFalse(battery.needs_service())
