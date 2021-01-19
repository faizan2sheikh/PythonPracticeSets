def proc(n):
    if n < 1:
        return 1
    else:
        return proc(n/2)

#a.
proc(0)
#b.
proc(1)
#c.
proc(2)
#d.
proc(3)
#e.
proc(5)
#f.
proc(10)