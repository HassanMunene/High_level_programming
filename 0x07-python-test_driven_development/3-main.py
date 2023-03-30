#!/usr/bin/python3

say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Hassan", "Munene")
say_my_name("Munene", "Awanzi")
say_my_name("Lawrence", "Omondi")
say_my_name("Bob")

try:
    say_my_name(12, "white")
except Exception as e:
    print(e)
