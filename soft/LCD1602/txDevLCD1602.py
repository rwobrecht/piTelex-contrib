#!/usr/bin/python3
"""
Telex Device - Control LCD Display Waveshare 16x2
"""
__author__      = "Rolf Obrecht (ro)"
__email__       = "rolf.obrecht@web.de"
__copyright__   = "Copyright 2026 ro"
__license__     = "GPL3"
__version__     = "0.0.1"


import os

import txCode
import txBase
import log
from datetime import datetime

import logging
l = logging.getLogger("piTelex." + __name__)

import LCD1602 # Copyright Waveshare?

def LOG(text:str, level:int=5):
    log.LOG('\033[5;30;43m<'+text+'>\033[0m', level)

#######

class TelexLCD1602(txBase.TelexBase):
    def __init__(self, **params):
        super().__init__()

        self.id = 'LCD'
        self.params = params

        self._LCD_WB_text = params.get('WB_text', 'Dialing...')
        self._LCD_A_text = params.get('A_text', 'Connected')
        self._LCD_incoming_dialnum_text = params.get('Incoming_text', 'Incoming call')
        self._LCD_Z_text = params.get('Z_text', 'Disconnected')
        self._LCD_ZZ_text = params.get('ZZ_text', 'Standby')

        self._LED_WB_brightness = params.get('WB_brightness', 30)
        self._LED_A_brightness = params.get('A_brightness', 30)
        self._LED_Z_brightness = params.get('Z_brightness', 15)
        self._LED_ZZ_brightness = params.get('ZZ_brightness', 5)

        self._lcd = LCD1602.LCD1602(16,2) 
        self._led = LCD1602.SN3193()

        self._mode = None
        self._dialnum = ''
        self._set_mode('ZZ','')                            # ZZ = sleeping


    # -----

    def exit(self):
        self._lcd.clear()
        self._led.set_mode(LCD1602.LED_NORMAL_MODE)
        self._led.set_brightness(0)
        del lcd

    # =====

    def read(self) -> str:
        return 
#        pass

    # -----

    def write(self, a:str, source:str):
        if len(a) != 1:
            self._check_commands(a[1:],source)
            return

        if a and self._mode == 'WB':
                # Display dialled number
                self._dialnum = self._dialnum + a
                self._lcd.setCursor(0,1)
                self._lcd.printout(self._dialnum)

    # =====

    def idle2Hz(self):
        pass

    # -----

    def idle20Hz(self):
        if self._lcd:
            if self._mode == 'ZZ':
                self._jetzt=datetime.now()
                self._lcd.setCursor(0, 0)
                self._lcd.printout(self._jetzt.strftime('%d.%m. %H:%M:%S'))


    # -----

    def idle(self):
        pass

    # =====



    #  === react to System commands (they start with \x1b)
    def _check_commands(self, a:str, source:str):

        if a in ('ZZ', 'Z', 'WB', 'A', 'AA'):
            self._set_mode(a,source)               

    

   # Set LCD Status Display 
    def _set_mode(self, mode:str, source:str):
        self._mode = mode
        if mode == 'WB':
            self._dialnum = ''
            self._led.set_brightness(self._LED_WB_brightness)
            self._lcd.clear()
            self._lcd.printout(self._LCD_WB_text)
            self._lcd.setCursor(0,1)
            self._lcd.cursor()

        if mode in ('A', 'AA'):
            if source == 'iTs':         #incoming call
                self._dialnum = self._LCD_incoming_dialnum_text 
            self._led.set_brightness(self._LED_A_brightness)
            self._lcd.clear()
            self._lcd.printout(self._LCD_A_text)
            self._lcd.setCursor(0,1)
            if ( self._dialnum == '000') or ( self._dialnum == ''): #local mode dialled or 'LT' pressed
                self._dialnum = 'local mode'
            elif self._dialnum == '009':                            #cmdline interface dialled
                self._dialnum = 'CmdLine interf.'
            self._lcd.printout(self._dialnum)
            self._lcd.nocursor()

        if mode == 'Z':
            self._led.set_brightness(self._LED_Z_brightness)
            self._lcd.clear()
            self._lcd.printout(self._dialnum)
            self._lcd.setCursor(0,1)
            self._lcd.printout(self._LCD_Z_text)
            self._lcd.nocursor()

        if mode == 'ZZ':
            self._dialnum = ''
            self._led.set_brightness(self._LED_ZZ_brightness)
            self._lcd.clear()
            self._lcd.setCursor(0,1)
            self._lcd.printout(self._LCD_ZZ_text)

    # -----


    # =====


#######

