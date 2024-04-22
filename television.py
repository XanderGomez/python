class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        '''
        This function initializes the variables which will be used in the functions below

        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self) -> None:
        '''
        This function turns the tv on if it is off, and it turns it off if it is on
        
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute(self) -> None:
        '''
        
        This function mutes the tv if it is unmuted and unmutes it if it's muted.

        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False
    def channel_up(self) -> None:
        '''
        This function increases the current channel of the television by 1, unless it's at the max channel, in which case it goes to the minimum channel

        '''
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        '''
        This function decreases the current channel of the television by 1, unless it's at the min channel, in which case it goes to the maximum channel
        
        '''
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self) -> None:
        '''
        
        This function increases the volume by one, unless it's at the max volume, in which case the volume remains the same

        '''
        if self.__status == True:
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self) -> None:
        '''

        This function decreases the volume by one, unless it's at the min volume, in which case the volume remains the same

        '''
        if self.__status == True:
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self) -> str:
        
        '''

        This function returns the power, channel, and volume of the television when a print statement is issued. If the channel is muted, volume returns as 0
        
        '''
        
        if self.__muted == False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {MIN_VOLUME}'


