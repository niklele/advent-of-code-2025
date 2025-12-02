from day2.day2 import Range
class TestRange():

    def test_is_invalid(self):
        r = Range(11,22)

        assert r.is_invalid(11)
        assert r.is_invalid(22)

        for i in range(12,22):
            assert r.is_invalid(i) == False

    def test_find_invalid_ids(self):
        # Zero invalid IDs
        r = Range(15, 17)
        assert len(r.find_invalid_ids()) == 0

        # Two invalid IDs
        r = Range(11, 22)
        invalid_ids = r.find_invalid_ids()

        assert len(invalid_ids) == 2
        assert 11 in invalid_ids
        assert 22 in invalid_ids