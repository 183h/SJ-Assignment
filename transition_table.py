table = {
    "url": {
        "http://": "httpaddress",
        "ftp://": "ftpaddress",
        "telnet://": "telnetaddress",
        "mailto::": "mailtoaddress"
    },
    "httpaddress": {
        "http://": "http:// hostport httpaddress1"
    },
    "httpaddress1": {
        "http://": "/ path httpaddress2",
        "?": "? search",
        "$": "epsilon"
    },
    "httpaddress2": {
        "?": "? search",
        "$": "epsilon"
    },
    "ftpaddress": {
        "ftp://": "ftp:// login / path"
    },
    "telnetaddress": {
        "telnet://": "telnet:// login"
    },
    "mailtoaddress": {
        "mailto::": "mailto:: xalphas @ hostname"
    },
    "login": {
        "A-Z a-z": "user login1",
        "0 .. 9": "user login1",
        "@": "@ hostport"
    },
    "login1": {
        "@": "@ hostport",
        ":": ": password @ hostport"
    },
    "hostport": {
        "A-Z a-z": "hostname hostport1",
        "0 .. 9": "hostname hostport1"
    },
    "hostport1": {
        "?": "epsilon",
        ":": ": port",
        "/": "epsilon",
        "$": "epsilon"
    },
    "hostname": {
        "A-Z a-z": "xalphas hostname1",
        "0 .. 9": "xalphas hostname1"
    },
    "hostname1": {
        "?": "epsilon",
        ".": ". xalphas hostname1",
        ":": "epsilon",
        "/": "epsilon",
        "$": "epsilon"

    },
    "port": {
        "0 .. 9": "digits"
    },
    "path": {
        "?": "segment path1",
        "A-Z a-z": "segment path1",
        "0 .. 9": "segment path1",
        "$": "segment path1"

    },
    "path1": {
        "?": "epsilon",
        "/": "/ segment path1",
        "$": "epsilon"
    },
    "search": {
        "A-Z a-z": "xalphas search1",
        "0 .. 9": "xalphas search1"
    },
    "search1": {
        "+": "+ xalphas search1",
        "$": "epsilon"
    },
    "user": {
        "A-Z a-z": "xalphas",
        "0 .. 9": "xalphas"
    },
    "password": {
        "A-Z a-z": "xalphas",
        "0 .. 9": "xalphas"
    },
    "segment": {
        "?": "epsilon",
        "/": "epsilon",
        "A-Z a-z": "xalpha segment",
        "0 .. 9": "xalpha segment",
        "$": "epsilon"
    },
    "xalphas": {
        "A-Z a-z": "xalpha xalphas1",
        "0 .. 9": "xalpha xalphas1"
    },
    "xalphas1": {
        "A-Z a-z": "xalphas",
        "0 .. 9": "xalphas",
        "?": "epsilon",
        "@": "epsilon",
        ":": "epsilon",
        ".": "epsilon",
        "/": "epsilon",
        "+": "epsilon",
        "$": "epsilon"
    },
    "xalpha": {
        "A-Z a-z": "alpha",
        "0 .. 9": "digit"
    },
    "digits": {
        "0 .. 9": "digit digits1",
    },
    "digits1": {
        "?": "epsilon",
        "/": "epsilon",
        "0 .. 9": "digits",
        "$": "epsilon"
    },
    "alpha": {
        "A-Z a-z": "A | .. | Z | a | .. | z"
    },
    "digit": {
        "0 .. 9": "0 | .. | 9"
    },
    "http://": {
        "http://": "POP"
    },
    "?": {
        "?": "POP"
    },
    "ftp://": {
        "ftp://": "POP"
    },
    "telnet://": {
        "telnet://": "POP"
    },
    "mailto::": {
        "mailto::": "POP"
    },
    "@": {
        "@": "POP"
    },
    ":": {
        ":": "POP"
    },
    ".": {
        ".": "POP"
    },
    "/": {
        "/": "POP"
    },
    "+": {
        "+": "POP"
    },
    "A-Za-z": {
        "A-Za-z": "POP"
    },
    "0..9": {
        "0..9": "POP"
    },
    "epsilon": {
        "epsilon": "ACCEPT"
    },
}