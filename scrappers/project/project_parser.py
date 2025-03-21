import re

PROJECT_PARSER = {
    "title": {
        "selector": ".container>h1>span", 
        "parser": None
    },
    "subtitle": {
        "selector": ".container div div h2", 
        "parser": None
    },
    "container": {
        "selector": ".container div div p", 
        "parser": None
    },
    "researcher": {
        "selector": ".container>div+div>div>p",
        "parser": lambda text: text.replace("<>", "").strip(),
    },
    "type": {
        "selector": ".container>div+div>div+div>div>div>ul>li",
        "parser": lambda text: text.split(":")[-1].strip(),
    },
    "funder": {
        "selector": ".container>div+div>div+div>div>div>ul>li+li",
        "parser": lambda text: text.split(":")[-1].strip(),
    },
    "reference": {
        "selector": ".container>div+div>div+div>div>div>ul>li+li+li",
        "parser": lambda text: text.split(":")[-1].strip(),
    },
    "start_date": {
        "selector": ".container>div+div>div+div>div>div+div>ul>li",
        "parser": lambda text: text.split(":")[-1].strip(),
    },
    "end_date": {
        "selector": ".container>div+div>div+div>div>div+div>ul>li+li",
        "parser": lambda text: text.split(":")[-1].strip(),
    },
    "total_granted": {
        "selector": ".container>div+div>div+div>div>div+div>ul>li+li+li",
        "parser": lambda text: re.sub(r"[^\d,]", "", text).strip(),
    },
}
