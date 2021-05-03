#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    words = dir(hidden_4)
    for name in words:
        if name[0] == "__":
            print(name)
