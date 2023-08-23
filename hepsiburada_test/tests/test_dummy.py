
import pytest


@pytest.mark.usefixtures("init_driver")
class TestDummy():


    def test_dummy_func(self):
        print("Im dummy test line")
        self.driver.get("https://google.com")
        import pdb; pdb.set_trace()
