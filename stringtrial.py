strings = "hello"
whole = 20
floats = 7.0

if strings == "hello":
    print('corect')

if isinstance(strings, str):
    print('even correct')

if isinstance (whole, int) and whole == 20:
    print('well done')
if isinstance (floats, float) and floats == 7.0:
    print("good %f " % floats) 
