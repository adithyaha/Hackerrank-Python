def mutate_string(string, position, character):
    stringlist = list(string)
    stringlist[int(position)] = character
    stringnew="".join(stringlist)
    return stringnew
