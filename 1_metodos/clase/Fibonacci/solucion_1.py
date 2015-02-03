fib = 1
fib2 = 2
fn = 0
suma = 0

while fn <=4000000:
    fn = fib2
    if fn % 2 == 0:
        suma += fn
    fn = fib + fib2
    fib = fib2
    fib2 = fn

print suma 

