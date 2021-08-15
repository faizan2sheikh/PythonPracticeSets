try:
    1+x
except Exception:
    print(1)
except ValueError:
    print(2)

# ValueError except block must be placed before Exception block, otherwise it would not have any effect on code because even if try block raises a ValueError it'll be catered by Exception block.