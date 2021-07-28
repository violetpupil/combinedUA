from random import choice

from src.util import read_file

ios = read_file("./db/ios.txt").splitlines()
safari_build = read_file("./db/safari_build.txt").splitlines()
safari_version = read_file("./db/safari_version.txt").splitlines()
webkit = read_file("./db/webkit.txt").splitlines()
chrome = read_file("./db/chrome.txt").splitlines()
android = read_file("./db/android.txt").splitlines()


def get_ua_ios_safari():
    os = "(iPhone; CPU iPhone OS {} like Mac OS X)".format(choice(ios).replace(".", "_"))
    engine = "AppleWebKit/{} (KHTML, like Gecko)".format(choice(webkit))
    browser = "Version/{} Mobile/15E148 Safari/{}".format(choice(safari_version), choice(safari_build))
    return f"Mozilla/5.0 {os} {engine} {browser}"


def get_ua_ios_chrome():
    os = "(iPhone; CPU iPhone OS {} like Mac OS X)".format(choice(ios).replace(".", "_"))
    engine = "AppleWebKit/{} (KHTML, like Gecko)".format(choice(webkit))
    browser = "CriOS/{} Mobile/15E148 Safari/{}".format(choice(chrome), choice(safari_build))
    return f"Mozilla/5.0 {os} {engine} {browser}"


def get_ua_android_chrome():
    os = "(Linux; Android {}; M6 Note)".format(choice(android))
    engine = "AppleWebKit/{} (KHTML, like Gecko)".format(choice(webkit))
    browser = "Chrome/{} Mobile Safari/{}".format(choice(chrome), choice(safari_build))
    return f"Mozilla/5.0 {os} {engine} {browser}"


ua = [get_ua_ios_safari, get_ua_ios_chrome, get_ua_android_chrome]


def get_ua():
    f = choice(ua)
    return f()
