from random import choice

from util import read_file

ios = read_file("./db/ios.txt").splitlines()
safari_build = read_file("./db/safari_build.txt").splitlines()
safari_version = read_file("./db/safari_version.txt").splitlines()
webkit = read_file("./db/webkit.txt").splitlines()


def get_ua():
    os = "(iPhone; CPU iPhone OS {} like Mac OS X)".format(choice(ios).replace(".", "_"))
    engine = "AppleWebKit/{} (KHTML, like Gecko)".format(choice(webkit))
    browser = "Version/{} Mobile/15E148 Safari/{}".format(choice(safari_version), choice(safari_build))
    return f"Mozilla/5.0 {os} {engine} {browser}"
