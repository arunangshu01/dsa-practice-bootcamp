def open_russian_doll(doll):
    if doll == 0:
        raise ValueError("There are no dolls to be opened.")
    elif doll == 1:
        print("All dolls are opened.")
    else:
        print(f"Doll: {doll} has been opened.")
        open_russian_doll(doll=(doll - 1))


if __name__ == "__main__":
    try:
        doll1, doll2 = 4, 0
        open_russian_doll(doll=doll1)
        open_russian_doll(doll=doll2)
    except Exception as e:
        print(e.__str__())
