#nCrの計算rとnを順番に手入力

glb  = 0
glb2 = 0

def function_r(r):   #選ぶ個数
      result = 1
      if r == 0:
            return result
      for num in range(1, r + 1):
            result *= num
      global glb2
      glb2 += result
      return glb2

print("選ぶ個数を入力")
b  = input()
b2 = int(b)
function_r(b2)
      
def function_n(n):   #母数
      result = 1
      global b2
      global glb
      if n == 0:
            return result
      for num in range(n-b2+1, n + 1):
        result *= num
      glb += result
      return glb

print("母数を入力")
a  = input()
a2 = int(a)
function_n(a2)

glb3 = glb / glb2
print(glb3)

glb  = 0
glb2 = 0
