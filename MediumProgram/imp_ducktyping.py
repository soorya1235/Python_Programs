class atom:

    def execute(self):
        print("Atom")

class pycharm:

    def execute(self):
        print("compiling")
        print("running")


class laptop:

    def code(self,ide):
        ide.execute()

class myeditor:

    def code(self,ide):
        ide.execute()

ide = pycharm()
lap1 = laptop()
lap1.code(ide)


a1 = atom()
atom1 = myeditor()
atom1.code(a1)