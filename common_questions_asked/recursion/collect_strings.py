"""

Collect Strings

Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

Examples:
    obj = {
        "stuff": 'foo',
        "data": {
            "val": {
                "thing": {
                    "info": 'bar',
                    "moreInfo": {
                        "evenMoreInfo": {
                            "weMadeIt": 'baz'
                        }
                    }
                }
            }
        }
    }

    collectStrings(obj) # ['foo', 'bar', 'baz']

"""

obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}


def collectStrings(obj):
    collect_strings = []
    for key in obj:
        if type(obj[key]) is str:
            collect_strings.append(obj[key])
        elif type(obj[key]) is dict:
            collect_strings = collect_strings + collectStrings(obj=obj[key])
    return collect_strings


if __name__ == "__main__":
    result = collectStrings(obj=obj)
    print(result)
