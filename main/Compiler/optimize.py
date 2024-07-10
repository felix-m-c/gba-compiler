REMOVE_COMMENTS         = False
REMOVE_EMPTY_LINES      = False
UPPERCASE_REGISTERS     = True


def optimizeAsm(asm:list[list[str]]):
    if REMOVE_EMPTY_LINES:
        asm = list(filter(lambda x: x!=[], asm))
    if REMOVE_COMMENTS:
        asm = list(filter(lambda x: (x==[] or not x[0].startswith(";;")), asm))
    if UPPERCASE_REGISTERS:
        for i, line in enumerate(asm):
            for j, x in enumerate(line):
                if x in ['a', 'c', 'b', 'e', 'd', 'hl', 'de', 'bc']:
                    asm[i][j]=x.upper()
                
    return asm