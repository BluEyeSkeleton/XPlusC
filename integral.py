# Imports
from numpy import *
from scipy.integrate import *;
from sympy import Symbol, integrate
from pylatex import *
from latex2sympy2 import latex2sympy, latex2latex

def parse(val):
  """
  Parse float value into constant symbol if any
  Returns
  -------
  str
    Value in string type
  """
  if (val == e): return "e"
  if (val == pi): return "\\pi"
  return str(val)

class BaseIntegral:
  """Base integral class, only use this as parent class for inheritance purposes"""
  def __init__(self, tex):
    """
    Initializes the integral instance
    Parameters
    ----------
    fx : str
      Mathematic expression of f(x) in LaTeX string format
    """
    self.tex = tex

  def init(self):
    pass

  def integrand(self, x):
    """
    Method representation of f(x)
    Returns
    -------
    float
      Method representation of f(x)
    """
    pass

  def evaluate(self):
    """Evaluates the expression"""
    pass

  def toLaTeXStr(self):
    """
    Returns integral in LaTeX string format
    Returns
    -------
    str
      Integral in LaTeX string format
    """
    pass

class DefiniteIntegral(BaseIntegral):
  """Definite integral class"""
  def __init__(self, tex, a, b):
    """
    Initializes the definite integral instance
    
    Parameters
    ----------
    tex : str
      Mathematic expression of f(x) in LaTeX string format
    a : float
      Lower limit
    b : float
      Upper limit
    """
    self.fx = latex2sympy(tex)
    self.a = a
    self.atex = parse(a)
    self.b = b
    self.btex = parse(b)
    super().__init__(tex)

  def integrand(self, x):
    """
    Method representation of f(x)
    Returns
    -------
    float
      Method representation of f(x)
    """
    return eval(self.fx, {"x": x})
  
  def evaluate(self):
    """
    Evaluates the expression
    Returns
    -------
    float
      The solution of the integral in decimals
    """
    return quad(self.integrand, self.a, self.b)
  
  def toLaTeXString(self):
    """
    Returns integral in LaTeX string format
    Returns
    -------
    str
      Integral in LaTeX string format
    """
    return f"\\int_{self.atex}^{self.btex} {self.tex} \\,dx"
  
class IndefiniteIntegral(BaseIntegral):
  """Indefinite integral class"""
  def __init__(self, fx):
    """
    Initializes indefinite integral expression
    Parameters
    ----------
    fx : str
      Mathematic expression of f(x)
    """
    self.x = Symbol("x")
    super().__init__(fx)

  def init(self):
    pass

  def integrand(self):
    """Method expression for f(x)"""
    return eval(self.fx, {"x": self.x})
  
  def evaluate(self):
    """Evaluate the expression"""
    return integrate(self.integrand(), self.x)