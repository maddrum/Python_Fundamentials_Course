def modifier(state_in, fiction_in):
    modify_state = state_in
    modify_fiction = fiction_in
    len_fiction = len(modify_fiction)
    while len_fiction != 0:
        len_fiction = len(modify_fiction)
        modify_state = modify_state.replace(modify_fiction, "")
        modify_fiction = modify_fiction[1:-1]
    return modify_state


while True:
    state = input().strip()
    if state == "collapse":
        break
    fiction = input().strip()
    result = modifier(state, fiction)
    if result:
        print(result)
    else:
        print("(void)")
