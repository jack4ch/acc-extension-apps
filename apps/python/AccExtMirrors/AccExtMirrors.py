try:
    import ac
    import acsys
    import traceback
except ImportError:
    pass

app = 0
mirror = 0
timer = 0
debug = 0
roles = "NLCR"
isPatch = 1

def acMain(ac_version):
    global app, debug, mirrorrole, mirrorindex, toggleMonButton, fovValue, isPatch
    try:
        app = ac.newApp("Shaders Patch Mirrors")
        ac.setTitle(app, "Mirrors")
        ac.setSize(app, 144, 188)

        debug = ac.addLabel(app, "")
        ac.setPosition(debug, 16, 164)

        mirrorrole = ac.addLabel(app, "")
        ac.setPosition(mirrorrole, 44, 40)

        mirrorindex = ac.addLabel(app, "")
        ac.setPosition(mirrorindex, 54, 46)
        ac.setFontSize(mirrorindex, 12)

        fovLabel = ac.addLabel(app, "FOV")
        ac.setPosition(fovLabel, 102, 164)

        fovValue = ac.addLabel(app, "")
        ac.setPosition(fovValue, 108, 112)

        fovUpButton = ac.addButton(app, "+")
        ac.setPosition(fovUpButton, 104, 88)
        ac.setSize(fovUpButton, 24, 24)
        ac.setFontSize(fovUpButton, 14)
        ac.addOnClickedListener(fovUpButton, fovUpMirror)

        fovDownButton = ac.addButton(app, "-")
        ac.setPosition(fovDownButton, 104, 136)
        ac.setSize(fovDownButton, 24, 24)
        ac.setFontSize(fovDownButton, 14)
        ac.addOnClickedListener(fovDownButton, fovDownMirror)

        toggleMonButton = ac.addButton(app, "m")
        ac.setPosition(toggleMonButton, 104, 40)
        ac.setSize(toggleMonButton, 24, 24)
        ac.setFontSize(toggleMonButton, 14)
        ac.addOnClickedListener(toggleMonButton, toggleMonMirror)

        prevButton = ac.addButton(app, "-")
        ac.setPosition(prevButton, 16, 40)
        ac.setSize(prevButton, 24, 24)
        ac.setFontSize(prevButton, 14)
        ac.addOnClickedListener(prevButton, prevMirror)

        nextButton = ac.addButton(app, "+")
        ac.setPosition(nextButton, 64, 40)
        ac.setSize(nextButton, 24, 24)
        ac.setFontSize(nextButton, 14)
        ac.addOnClickedListener(nextButton, nextMirror)

        leftButton = ac.addButton(app, "L")
        ac.setPosition(leftButton, 16, 112)
        ac.setSize(leftButton, 24, 24)
        ac.setFontSize(leftButton, 14)
        ac.addOnClickedListener(leftButton, leftMirror)

        rightButton = ac.addButton(app, "R")
        ac.setPosition(rightButton, 64, 112)
        ac.setSize(rightButton, 24, 24)
        ac.setFontSize(rightButton, 14)
        ac.addOnClickedListener(rightButton, rightMirror)

        upButton = ac.addButton(app, "U")
        ac.setPosition(upButton, 40, 88)
        ac.setSize(upButton, 24, 24)
        ac.setFontSize(upButton, 14)
        ac.addOnClickedListener(upButton, upMirror)

        downButton = ac.addButton(app, "D")
        ac.setPosition(downButton, 40, 136)
        ac.setSize(downButton, 24, 24)
        ac.setFontSize(downButton, 14)
        ac.addOnClickedListener(downButton, downMirror)
    except:
        isPatch = 0
        acTrace()
    return "AccExtMirrors"

def leftMirror(*args):
    try:
        ac.ext_mirrorLeft()
    except:
        acTrace()

def rightMirror(*args):
    try:
        ac.ext_mirrorRight()
    except:
        acTrace()

def upMirror(*args):
    try:
        ac.ext_mirrorUp()
    except:
        acTrace()

def downMirror(*args):
    try:
        ac.ext_mirrorDown()
    except:
        acTrace()

def prevMirror(*args):
    try:
        ac.ext_mirrorPrev()
    except:
        acTrace()

def nextMirror(*args):
    try:
        ac.ext_mirrorNext()
    except:
        acTrace()

def fovUpMirror(*args):
    try:
        ac.ext_mirrorFovUp()
    except:
        acTrace()

def fovDownMirror(*args):
    try:
        ac.ext_mirrorFovDown()
    except:
        acTrace()

def toggleMonMirror(*args):
    try:
        ac.ext_mirrorToggleMon()
    except:
        acTrace()

def acTrace():
    isPatch=0

def acUpdate(delta_t):
    global timer, isPatch
    timer += delta_t
    if timer > 0.25 and isPatch==1:
        if isPatch==1:
            timer = 0.0
            try:
                params = ac.ext_mirrorParams()
                ac.setText(mirrorrole, roles[int(params[3])])
                index = int(params[4])
                if index > 0:
                    ac.setText(mirrorindex, str(index))
                else:
                    ac.setText(mirrorindex, "")

                ac.setText(fovValue, str(int(params[1])))
                if params[0] == True:
                    ac.setText(toggleMonButton, "M")
                else:
                    ac.setText(toggleMonButton, "m")
            except:
                acTrace()
        else:
            ac.setText(debug,'Shaders Patch not active')

def acShutdown(*args):
    return
