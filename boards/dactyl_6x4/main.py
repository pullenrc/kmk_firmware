import board

from kb_rp2040 import KMKKeyboard

from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.keys import KC
from kmk.extensions.oled import OLED
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType


keyboard = KMKKeyboard()

# custom keys used for encoder actions
Zoom_in = KC.LCTRL(KC.EQUAL)
Zoom_out = KC.LCTRL(KC.MINUS)

split = Split()
oled = OLED([128],[32],board.SCL,board.SDA)
layers_ext = Layers()

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

#  for use in the encoder extension
encoder_map = [
    [
        (
            KC.VOLU,
            KC.VOLD,
            2,
        ),  #  Only 1 encoder is being used, so only one tuple per layer is required
    ],
    [
        (Zoom_in, Zoom_out, 1),
    ],
    [
        (_______, _______, 1),  #  no action taken by the encoder on this layer
    ],
]

encoder_ext = EncoderHandler([board.TX], [board.D4], encoder_map)
encoder_ext.encoders[0].is_inverted = True
keyboard.modules = [layers_ext, split, encoder_ext]
keyboard.extensions = [oled]
#
# custom keys
NEW = KC.LCTL(KC.N)
NEW_DIR = KC.LCTL(KC.LSFT(KC.N))
CAD = KC.LCTL(KC.LALT(KC.DEL))
RES = KC.LCTL(KC.LSFT(KC.ESC))
FE = KC.LGUI(KC.E)
LT1_DEL = KC.LT(1, KC.DEL)
LT2_ENT = KC.LT(2, KC.ENT)
SAVE_AS = KC.LCTL(KC.LSFT(KC.S))
PSCR = KC.LGUI(KC.PSCR)
SNIP = simple_key_sequence(
    (
        KC.LGUI,
        KC.MACRO_SLEEP_MS(25),
        KC.S,
        KC.N,
        KC.I,
        KC.P,
        KC.MACRO_SLEEP_MS(25),
        KC.ENT,
    )
)

# programming layer keys
UINT = simple_key_sequence(
    (
        KC.U,
        KC.I,
        KC.N,
        KC.T,
    )
)
INT = simple_key_sequence(
    (
        KC.I,
        KC.N,
        KC.T,
    )
)
DOUBLE = simple_key_sequence(
    (
        KC.D,
        KC.O,
        KC.U,
        KC.B,
        KC.L,
        KC.E,
    )
)
BOOL = simple_key_sequence(
    (
        KC.B,
        KC.O,
        KC.O,
        KC.L,
    )
)
BYTE = simple_key_sequence(
    (
        KC.B,
        KC.Y,
        KC.T,
        KC.E,
    )
)
SBYTE = simple_key_sequence(
    (
        KC.S,
        KC.B,
        KC.Y,
        KC.T,
        KC.E,
    )
)
CHAR = simple_key_sequence(
    (
        KC.C,
        KC.H,
        KC.A,
        KC.R,
    )
)
GETSET = simple_key_sequence(
    (
        KC.LBRC,
        KC.SPC,
        KC.G,
        KC.E,
        KC.T,
        KC.SCLN,
        KC.SPC,
        KC.S,
        KC.E,
        KC.T,
        KC.SCLN,
        KC.SPC,
        KC.RBRC,
    )
)
PUBLIC = simple_key_sequence(
    (
        KC.P,
        KC.U,
        KC.B,
        KC.L,
        KC.I,
        KC.C,
    )
)
DEBUGWL = simple_key_sequence(
    (
        KC.LSFT(KC.D),
        KC.E,
        KC.B,
        KC.U,
        KC.G,
        KC.DOT,
        KC.LSFT(KC.W),
        KC.R,
        KC.I,
        KC.T,
        KC.E,
        KC.LSFT(KC.L),
        KC.I,
        KC.N,
        KC.E,
        KC.LSFT(KC.N9),
    )
)
PRINT = simple_key_sequence(
    (
        KC.P,
        KC.R,
        KC.I,
        KC.N,
        KC.T,
    )
)


keyboard.keymap = [
    [  #QWERTY
        KC.CAPS,   KC.Q,      KC.W,      KC.E,      KC.R,        KC.T,           KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,       KC.PSLS,
        KC.TAB,    KC.A,      KC.S,      KC.D,      KC.F,        KC.G,           KC.H,      KC.J,      KC.K,      KC.L,      KC.SCLN,    KC.QUOT,
        KC.ESC,    KC.Z,      KC.X,      KC.C,      KC.V,        KC.B,           KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,    FE,
        KC.LALT,   KC.LSFT,   KC.LCTL,   KC.BSPC,   KC.MO(1),    KC.MO(3),      KC.MO(3),   KC.MO(2),  KC.SPC,    KC.ENT,    KC.RSFT,    KC.RGUI,
    ],
    [  #LOWER
        KC.BSLS,   KC.NO,     KC.HOME,     KC.UP,      KC.END,    NEW_DIR,            KC.N5,      KC.N6,      KC.N7,       KC.N8,      KC.N9,     KC.BSLS,
        KC.F2,     KC.NO,     KC.LEFT,     KC.DOWN,    KC.RGHT,   KC.HASH,        KC.N0,      KC.N1,      KC.N2,       KC.N3,      KC.N4,     KC.QUOT,
        KC.LSFT,   KC.NO,     KC.NO,       KC.NO,      KC.TAB,    KC.UNDS,        KC.MINS,    KC.PPLS,    KC.MINS,     KC.PAST,    KC.PSLS,   KC.LBRC,
        _______,   _______,   _______,     _______,    _______,   _______,        _______,    _______,    _______,     KC.EQUAL,    _______,    _______,
    ],
    [  #RAISE
        KC.BSLS,   KC.NO,      KC.NO,      KC.LCBR,   KC.RCBR,    KC.AT,          INT,        GETSET,     KC.UP,     KC.NO,     KC.NO,     KC.NO,
        KC.TAB,    KC.NO,      KC.NO,      KC.LPRN,   KC.RPRN,    KC.DLR,         BOOL,       KC.LEFT,    KC.DOWN,   KC.RGHT,   KC.NO,     KC.NO,
        KC.LSFT,   KC.NO,      KC.NO,      KC.LBRC,   KC.RBRC,    KC.PERC,        UINT,       DOUBLE,     KC.NO,     KC.NO,     KC.NO,     KC.NO,
        _______,   _______,    _______,    _______,   _______,    _______,        _______,    _______,    _______,   _______,   _______,   _______,
    ],
    [  #ADJUST
        KC.BSLS,   KC.NO,      KC.NO,      KC.LCBR,    KC.RCBR,    KC.AT,          INT,        GETSET,     KC.UP,     KC.NO,      KC.NO,     KC.NO,
        KC.TAB,    KC.NO,      KC.NO,      KC.LPRN,    KC.RPRN,    KC.DLR,         BOOL,       KC.LEFT,    KC.DOWN,   KC.RGHT,    KC.NO,     KC.NO,
        KC.LSFT,   KC.NO,      KC.NO,      KC.LBRC,    KC.RBRC,    KC.PERC,        UINT,       DOUBLE,     KC.NO,     KC.NO,      KC.NO,     KC.NO,
        _______,   _______,    _______,    _______,    _______,    _______,        _______,    _______,    _______,   _______,    _______,   _______,
    ]
]

if __name__ == '__main__':
    keyboard.go()
