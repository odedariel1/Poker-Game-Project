def _decorator(func):
    def notice_player_set(args, **kwargs):
        print("Decorator: The Players Are Getting Sets!!")
        func(args, **kwargs)

    return notice_player_set