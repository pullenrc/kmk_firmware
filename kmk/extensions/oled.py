import adafruit_ssd1306
import board
import busio

from kmk.extensions import Extension
from kmk.graphics import Graphics as Icon


class OLED(Extension):
    def __init__(self,width=[128],height=[64],scl=board.SCL,sda=board.SDA):
        self.enabled = True
        self.i2c_bus0 = None
        self.i2c_bus1 = None
        self.oleds = []
        self.oled_sda = sda
        self.oled_scl = scl
        self.oled_height = height
        self.oled_width = width
        self.oled_bus = None
        self.oled_count = len(self.oled_width)
        self.oled_addr = [0x31, 0x32]
        self.graphics = None
        self.current_key = ''
        self.prev_key = ''
        self.keylog_update = False
        self.prev_key = ''
        self.prev_layer_name = 'BASE'
        self.layer_names = []
        self.key_log = []
        self.prev_key_string = ''
        self.prev_key_log = []
        # mode badge handling
        self.prev_active_layer = []
        self.mode_badge = []
        self.prev_mode_badge = []
        self.prev_logo = []
        self.icon = Icon()
        self.init()

    def init(self):
        #self.i2c_bus0 = busio.I2C(self.oled_scl[0], self.oled_sda[0])
        self.i2c_bus0 = busio.I2C(self.oled_scl, self.oled_sda)
        for i in range(self.oled_count):
            self.oleds.append(
                adafruit_ssd1306.SSD1306_I2C(
                    #self.oled_width[i], self.oled_height[i], self.i2c_bus0
                    self.oled_width[i], self.oled_height[i], self.i2c_bus0
                )
            )
        self.draw_logo(self.oleds[0], self.icon.logos["Warhorse"])

    def __repr__(self):
        return #'LED({})'.format(self._to_dict())

    def _to_dict(self):
        return


    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):

        return

    def before_matrix_scan(self, sandbox):
        #self.draw_logo(self.oleds[0], self.icon.logos["Warhorse"])
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return

    def draw_badge(self, oled, mode_badge):
        for i in self.prev_mode_badge:
            oled.pixel(i[0] + 95, i[1], 0)

        for i in mode_badge:
            oled.pixel(i[0] + 95, i[1], 1)

        self.draw_layer_name(oled)
        oled.show()
        self.prev_mode_badge = mode_badge

    def draw_logo(self, oled, logo):
        # self.clear_oled(oled)
        for i in self.prev_logo:
            oled.pixel(i[0], i[1], 0)
        oled.show()

        for i in logo:
            oled.pixel(i[0], i[1], 1)
        oled.show()
        self.prev_logo = logo

    def draw_key(self, oled):
        # undraw last char
        oled.text(self.prev_key_string, 40, 18, 0)

        if len(self.key_log) < 9:
            self.key_log.append(self.current_key)
        else:
            self.key_log.pop(0)
            self.key_log.append(self.current_key)

        self.prev_key_string = ""
        # traverse in the string
        for ele in self.key_log:
            self.prev_key_string += ele

        # draw current char
        oled.text(self.prev_key_string, 40, 18, 1)
        oled.show()
        # set prev char
        self.prev_key_log = self.key_log
        self.prev_key = self.current_key

    def draw_layer_name(self, oled):
        # get center of display, must be int
        center = int(self.oled_width[0] / 2)
        # get length to middle of mode name
        mid = int(
            len(self.prev_layer_name) / 2 + len(self.prev_layer_name) % 2
        )

        # erase old mode name
        oled.text(self.prev_layer_name, center - (mid * 5), 0, 0)

        # get length of current mode name
        mid = int(
            len(self.layer_names[self.active_layers[0]]) / 2
            + len(self.layer_names[self.active_layers[0]]) % 2
        )

        # draw current mode name
        oled.text(
            self.layer_names[self.active_layers[0]], center - (mid * 5), 0, 1
        )

        # set prev mode name
        self.prev_layer_name = self.layer_names[self.active_layers[0]]



    def clear_oled(self, oled):
        # start with a blank screen
        oled.fill(0)
        # we just blanked the framebuffer.
        # to push the framebuffer onto the display, we call show()
        oled.show()


