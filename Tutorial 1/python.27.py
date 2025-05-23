import cmath 
def quadratic_roots(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    
    return root1, root2

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

root1, root2 = quadratic_roots(a, b, c)

print(f"The roots of the quadratic equation are: {root1} and {root2}")
