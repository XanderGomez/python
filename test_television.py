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
        self.tv_test.mute()
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_test.power()
        self.tv_test.mute()
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 1'
        self.tv_test.power()
        self.tv_test.volume_down()


    def test_channel_up(self):
        self.tv_test.power()
        self.tv_test.channel_up()
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = False, Channel = 1, Volume = 0'
        self.tv_test.power()
        self.tv_test.channel_up()
        assert self.tv_test.__str__() == 'Power = True, Channel = 2, Volume = 0'
        self.tv_test.channel_up()
        self.tv_test.channel_up()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_test.power()


    def test_channel_down(self):
        self.tv_test.power()
        self.tv_test.channel_up()
        self.tv_test.channel_down()
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_test.power()
        self.tv_test.channel_down()
        assert self.tv_test.__str__() == 'Power = True, Channel = 3, Volume = 0'
        self.tv_test.channel_up()

    def test_volume_up(self):
        self.tv_test.power()
        self.tv_test.volume_up()
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 1'
        self.tv_test.power()
        self.tv_test.volume_up()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv_test.volume_up()
        self.tv_test.mute()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_test.volume_up()
        self.tv_test.mute()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv_test.volume_down()
        self.tv_test.volume_down()
        self.tv_test.power()

    def test_tv_volume_down(self):
        self.tv_test.power()
        self.tv_test.volume_down()
        self.tv_test.power()
        assert self.tv_test.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_test.power()
        self.tv_test.volume_up()
        self.tv_test.volume_up()
        self.tv_test.volume_down()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_test.volume_up()
        self.tv_test.mute()
        self.tv_test.volume_down()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv_test.mute()
        self.tv_test.volume_down()
        self.tv_test.volume_down()
        assert self.tv_test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_test.power()
