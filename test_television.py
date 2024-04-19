import pytest
from television import *


class Test():
    def setup_method(self):
        self.tv_test = Television()


    def teardown_method(self):
        del self.tv_test

    def test_init(self):
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 0'


    def test_power(self):
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_test.power()


    def test_mute(self):
        self.tv_test.power()
        self.tv_test.volume_up()
        self.tv_test.mute()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_test.mute()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 1'

    def test_channel_up(self):
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 0'

