statuses = {        #   status description      input values designation                input values type           output values designation                           output values type

    "toc"   : 0,    # type of connection        (app/remote):                           bool
}

ltypes = {
    "san"   : 1,    # set app name              ("*"):                                  string
    "sad"   : 2,    # set app description       ("*"):                                  string
    "mgr"   : 3,    # message get request       (count)                                 int                         [(id, app name, message), ...]                      [int, string, any], ...
    "arc"   : 4,    # add remote client         (address, short name)                   string, string              (id)                                                int
    "ms"    : 5,    # message send              (id/short name, app name, message)      int/string, string, any
    "grc"   : 6,    # get remote client         (id/short name)                         int/string                  (address, short name, id)
}

# def is_local(sockname):
#     if type(sockname) == str:
#         return True
#     else:
#         if "::" in sockname[0]:
#             return True
#         else:
#             return True