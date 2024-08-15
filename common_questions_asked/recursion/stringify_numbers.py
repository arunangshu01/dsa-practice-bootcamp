"""

Stringify Numbers

Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and
converts them to strings. Recursion would be a great way to solve this!

Examples:
    obj = {
        "num": 1,
        "test": [],
        "data": {
            "val": 4,
            "info": {
                "isRight": True,
                "random": 66
            }
        }
    }

    stringifyNumbers(obj)

    {
        'num': '1',
        'test': [],
        'data': {'val': '4', 'info': {'isRight': True, 'random': '66'} }
    }

"""

obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}


def stringifyNumbers(obj):
    new_obj = obj
    for key in new_obj:
        if type(new_obj[key]) is int:
            new_obj[key] = str(new_obj[key])
        if type(new_obj[key]) is dict:
            new_obj[key] = stringifyNumbers(obj=new_obj[key])
    return new_obj


if __name__ == "__main__":
    result = stringifyNumbers(obj=obj)
    print(result)
