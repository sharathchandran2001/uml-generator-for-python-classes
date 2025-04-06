import sys

class SequenceOn:
    autonumber = True
    init_done = False
    output_file = 'sequence.txt'

    def __init__(self, participant=""):
        if not SequenceOn.init_done:
            if SequenceOn.autonumber:
                self._write_to_file("autonumber")
            SequenceOn.init_done = True

        callee_frame = sys._getframe(1)
        self.__funcName = callee_frame.f_code.co_name

        if 'self' in callee_frame.f_locals:
            self.__className = callee_frame.f_locals['self'].__class__.__name__
        else:
            self.__className = participant

        caller_frame = sys._getframe(2)
        if 'self' in caller_frame.f_locals:
            self.__caller = caller_frame.f_locals['self'].__class__.__name__
        else:
            self.__caller = ""

        activate = "++" if self.__caller != self.__className else ""
        self._write_to_file(f'{self.__caller} -> {self.__className} {activate} :{self.__funcName}')

    def __del__(self):
        if hasattr(self, '__caller') and self.__caller != self.__className:
            self._write_to_file(f'{self.__caller} <-- {self.__className} -- ')

    def note(self, msg):
        self._write_to_file(f'note over {self.__className}:{msg}')

    def _write_to_file(self, message):
        with open(SequenceOn.output_file, 'a') as f:
            print(message)
            f.write(message + '\n')

class SequenceOff:
    def __init__(self, participant=""):
        pass
    def __call__(self, msg):
        pass
    def note(self, msg):
        pass

if __name__ == "__main__":

    class B:
        def __init__(self):
            pass

        def funcB1(self):
            s = SequenceOn()

        def funcB2(self):
            s = SequenceOn()
            s.note("calling private method")
            self.__funcB22()

        def __funcB22(self):
            s = SequenceOn()

    class A:
        def __init__(self):
            pass
        def funcA(self):
            s = SequenceOn()
            b = B()
            b.funcB1()
            b.funcB2()

    a = A()
    a.funcA()