
def is_triangle(a,b,c):
    if a + b < c:
        print("NO")
    elif a + c < b:
        print("NO")
    elif b + c < a:
        print("NO")
    else:
        print("YES")
