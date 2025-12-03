from src.day1 import Safe


class TestDay1:
    def test_safe_single_rotations(self):
        safe = Safe()
        safe.rotate_left(40)
        assert safe.curr == 10

        safe.rotate_right(1)
        assert safe.curr == 11

        safe.rotate_right(20)
        assert safe.curr == 31

        safe.rotate_left(10)
        assert safe.curr == 21

    # @pytest.mark.skip()
    def test_safe_at_zero(self):
        safe = Safe()

        # Rotate left 50 and end at 0, increment 0s
        safe.rotate_left(50)
        assert safe.curr == 0
        assert safe.zeros == 1

        # Rotate right 40 and end at 40
        safe.rotate_right(40)
        assert safe.curr == 40
        assert safe.zeros == 1

        # Rotate right 50 and end at 0, increment 0s
        safe.rotate_right(60)
        assert safe.curr == 0
        assert safe.zeros == 2

        # Rotate left 70 and end at 30
        safe.rotate_left(70)
        assert safe.curr == 30
        assert safe.zeros == 2

        # Rotate left 30 and end at 0, increment 0s
        safe.rotate_left(30)
        assert safe.curr == 0
        assert safe.zeros == 3

    def test_safe_cross_zero(self):
        safe = Safe()

        # Rotate right 100 and end at 50, increment 0s
        safe.rotate_right(100)
        assert safe.curr == 50
        assert safe.zeros == 1

        # Rotate left 100 and end at 50, increment 0s
        safe.rotate_left(100)
        assert safe.curr == 50
        assert safe.zeros == 2

        # Rotate right 200 and end at 50, increment 0s
        safe.rotate_right(200)
        assert safe.curr == 50
        assert safe.zeros == 4

        # Rotate left 200 and end at 50, increment 0s
        safe.rotate_left(200)
        assert safe.curr == 50
        assert safe.zeros == 6

    def test_safe_example(self):
        safe = Safe()

        safe.rotate_left(68)
        assert safe.curr == 82
        assert safe.zeros == 1

        safe.rotate_left(30)
        assert safe.curr == 52
        assert safe.zeros == 1

        safe.rotate_right(48)
        assert safe.curr == 0
        assert safe.zeros == 2

        safe.rotate_left(5)
        assert safe.curr == 95
        assert safe.zeros == 2

        safe.rotate_right(60)
        assert safe.curr == 55
        assert safe.zeros == 3

        safe.rotate_left(55)
        assert safe.curr == 0
        assert safe.zeros == 4

        safe.rotate_left(1)
        assert safe.curr == 99
        assert safe.zeros == 4

        safe.rotate_left(99)
        assert safe.curr == 0
        assert safe.zeros == 5

        safe.rotate_right(14)
        assert safe.curr == 14
        assert safe.zeros == 5

        safe.rotate_left(82)
        assert safe.curr == 32
        assert safe.zeros == 6
