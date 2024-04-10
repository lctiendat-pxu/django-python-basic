import math

def cong(a, b):
  """Tính tổng hai số a và b."""
  return a + b

def nhan(a, b):
  """Tính tích hai số a và b."""
  return a * b

def mu(a, b):
  """Tính a mũ b."""
  return a ** b

def can_bac_2(a):
  """Tính căn bậc 2 của a."""
  return math.sqrt(a)

def acos(a):
  """Tính acos của a."""
  return math.cos(a)

def giai_ptb2(a, b, c):
  """Giải phương trình bậc 2 ax^2 + bx + c = 0."""
  delta = b ** 2 - 4 * a * c
  if delta < 0:
    return "Phương trình vô nghiệm."
  elif delta == 0:
    return "Phương trình có nghiệm kép x = {}".format(-b / (2 * a))
  else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return "Phương trình có hai nghiệm x1 = {} và x2 = {}".format(x1, x2)
