def oxford_comma(items):
    if len(items) == 1:
        print(items[0])
        return items[0]
    elif len(items) == 2:
        print(" and ".join(items))
        return " and ".join(items)
    else:
        joined_items = ", ".join(items[:-1]) + ", and " + items[-1]
    print(joined_items)
    return joined_items


oxford_comma(["fiddleheads", "okra"])
