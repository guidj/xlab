import unittest

from pylab.etc import slidingwindow


class TestSlidingWindow(unittest.TestCase):

    def test_window_assignment(self):
        window_size, advance, events = 20, 10, {
            0: [10],
            1: [10],
            10: [20, 10],
            13: [20, 10],
            19: [20, 10],
            20: [30, 20, 10],
            27: [30, 20, 10],
            31: [40, 30, 20]
        }

        for event_timestamp in events:
            self.assertEquals(events[event_timestamp],
                              slidingwindow.compute_windows(window_size, advance, event_timestamp))

        window_size, advance, events = 40, 15, {
            0: [15],
            1: [15],
            15: [30, 15],
            29: [30, 15],
            44: [45, 30, 15],
            50: [60, 45, 30],
            67: [75, 60, 45],
            81: [90, 75, 60]
        }

        for event_timestamp in events:
            self.assertEquals(events[event_timestamp],
                              slidingwindow.compute_windows(window_size, advance, event_timestamp))

        window_size, advance, events = 20, 20, {
            0: [20],
            1: [20],
            10: [20],
            13: [20],
            15: [20],
            19: [20],
            20: [40],
            27: [40],
            29: [40],
            31: [40],
            44: [60],
            50: [60],
            67: [80],
            81: [100]
        }

        for event_timestamp in events:
            self.assertEquals(events[event_timestamp],
                              slidingwindow.compute_windows(window_size, advance, event_timestamp))

if __name__ == "__main__":
    unittest.main()
