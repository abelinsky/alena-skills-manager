class AsmException(Exception):
    def __repr__(self):
        s = self.__str__().rstrip("\n")
        if "\n" in s:
            s = s.replace("\n", "\n\t") + "\n"
        return f"{self.__class__.__name__}({s})"
