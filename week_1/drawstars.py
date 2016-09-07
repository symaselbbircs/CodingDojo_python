def count_stars(num):
    response = ""
    for i in range(0,num):
        response += "*"
    return response

def draw_stars(a):
    for val in a:
        print count_stars(val)

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)
