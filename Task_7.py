# import libraries here


def main():
  '''
  Kodunuzu buraya yazin.
  '''
  import math
  sh = float(input("lenth: "))
  n = int(input("Number of sides: "))
  a = (sh*n**2)/(4*math.tan((math.pi))/sh)
  print(f'Area: {a:.6f}')

if __name__ == "__main__":
  main()
