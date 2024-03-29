# Imports
from random import *

from numpy import *
from sympy import *
from sympy.integrals.manualintegrate import manualintegrate
from pylatex import *
from latex2sympy2 import latex2sympy

# Enums
POWER_RULE = 0xa0
POWER_RULE_LINEAR = 0xa1
POWER_RULE_LN = 0xa2
POWER_RULE_LN_LINEAR = 0xa3
EXP_EULER = 0xe0
EXP_INTEGER = 0xe1
TRIGO = 0xb0
TRIGO_LINEAR = 0xb1

MODES = [
    POWER_RULE, POWER_RULE_LINEAR, POWER_RULE_LN, POWER_RULE_LN_LINEAR,
    EXP_EULER, EXP_INTEGER,
    TRIGO, TRIGO_LINEAR,
]

# Default configuration for question generator
DEFAULT_CONFIG = {
    "mode": POWER_RULE,
    "use_coefficient": True, # False: Only easy questions without coefficients
    "fractional_coefficient": False, # False: only integers will be used for coefficients
    "max_integer": 6, # Maximum integer to be used as digit
    "min_integer": 2, # Minimum integer to be used as digit
}

def __frac(num, den):
    return f"\\frac{{{num}}}{{{den}}}"

def __pow(base, pow, bracket=False):
    return f"({base})^{{{pow}}}" if bracket else f"{base}^{{{pow}}}"

def __ln_abs(a):
    return f"\\ln{{|{a}|}}"

def __sin(x, bracket=False):
    return f"\\sin({x})" if bracket else f"\\sin{{{x}}}"

def __cos(x, bracket=False):
    return f"\\cos({x})" if bracket else f"\\cos{{{x}}}"

def __coeff(config=DEFAULT_CONFIG):
    return str(randint(config["min_integer"], config["max_integer"]))

def __add_coeff(x, config=DEFAULT_CONFIG):
    i = __coeff(config)
    if not config["use_coefficient"]:
        return x
    use_frac = choice([config["fractional_coefficient"], False])
    return __frac(x, i) if use_frac else f"{i}{x}"

def __eqn(config=DEFAULT_CONFIG):
    linear = __add_coeff("x", config) + "+" + __coeff(config) \
        if config["use_coefficient"] else "x"
    if (config["mode"] == POWER_RULE):
        return __add_coeff(__pow("x", __coeff(config)), config)
    elif (config["mode"] == POWER_RULE_LINEAR):
        return __add_coeff(__pow(linear, __coeff(config), True), config)
    elif (config["mode"] == POWER_RULE_LN):
        return __frac(__coeff(config), "x") if config["use_coefficient"] \
        else __frac("1", "x")
    elif (config["mode"] == POWER_RULE_LN_LINEAR):
        return __frac(__coeff(config), linear) if config["use_coefficient"] \
        else __frac("1", linear)
    elif (config["mode"] == EXP_EULER):
        return __add_coeff(__pow("e", linear), config)
    elif (config["mode"] == EXP_INTEGER):
        return __pow(__coeff(config), linear)
    elif (config["mode"] == TRIGO):
        func = choice([__sin, __cos])
        return __add_coeff(func("x"), config)
    elif (config["mode"] == TRIGO_LINEAR):
        func = choice([__sin, __cos])
        return __add_coeff(func(linear, True), config)

def generate_definite_integral(config=DEFAULT_CONFIG):
    tex = __eqn(config)
    tex_ques = f"\\int {tex} \\,dx"

    x = Symbol("x")
    ans = manualintegrate(latex2sympy(tex), x)
    tex_ans = latex(ans, ln_notation=True) + "+C"
    return tex_ques, tex_ans