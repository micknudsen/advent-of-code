import unittest


class TestCode(unittest.TestCase):
    def test_rectangle(self) -> None:

        reactangle = Rectangle(height=1000, width=1000)

        # The reactangle starts out with no lights on
        self.assertEqual(reactangle.count_lights_on(), 0)

        # Turn on all lights
        reactangle.turn_on(x1=0, y1=0, x2=999, y2=999)
        self.assertEqual(reactangle.count_lights_on(), 1_000_000)

        # Toggle first line of lights
        reactangle.toggle(x1=0, y1=0, x2=999, y2=0)
        self.assertEqual(reactangle.count_lights_on(), 999_000)

        # Turn off middle four lights
        reactangle.turn_off(x1=499, y1=499, x2=500, y2=500)
        self.assertEqual(reactangle.count_lights_on(), 998_996)
