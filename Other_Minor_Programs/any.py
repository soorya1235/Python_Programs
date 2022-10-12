string = "a=5\nb=10\nprint(a+b)"
codeobj = compile(string,'sumstring','exec')
exec(codeobj)
