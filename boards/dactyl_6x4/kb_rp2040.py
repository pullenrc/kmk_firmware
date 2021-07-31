import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.D25,
        board.D24,
        board.A3,
        board.A2,
        board.A1,
        board.A0,
    )
    row_pins = (board.SCK, board.MOSI, board.MISO, board.RX)
    diode_orientation = DiodeOrientation.ROWS
    data_pin = board.D13
    i2c = board.I2C

    coord_mapping = []
    #coord_mapping.extend(ic(0, x) for x in range(12))
    #coord_mapping.extend(ic(1, x) for x in range(12))
    #coord_mapping.extend(ic(2, x) for x in range(12))

    # And now, to handle R3, which at this point is down to just six keys
    #coord_mapping.extend(ic(3, x) for x in range(3, 9))
