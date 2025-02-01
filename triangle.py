#Ryan Feroz 
#SSW567 HW00b

def classify_triangle(a, b, c):
        #Sorts the sides to ensure a <= b <= c for easier right triangle check
        sides = sorted([a, b, c])
        a, b, c = sides
        
        #Checks valid triangle
        if a + b <= c:
            return "Invalid Triangle"
        
        #Determines the type of triangle
        if a == b == c:
            triangle_type = "Equilateral"
        elif a == b or b == c or a == c:
            triangle_type = "Isosceles"
        else:
            triangle_type = "Scalene"
        
        #Checks right triangle
        if a**2 + b**2 == c**2:
            triangle_type += " Right"
        
        return triangle_type
    
#Input:
if __name__ == "__main__":
    test_cases = [(3, 4, 5), (7, 7, 7), (2, 2, 3), (7, 24, 25), (10, 10, 14), (1, 2, 3)]
    for sides in test_cases:
        print(f"Triangle {sides}: {classify_triangle(*sides)}")
