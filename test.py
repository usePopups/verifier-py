import verifier
import json


if verifier.verify('meet@hooktap.in', 'e005b9d6242eee960b34257203a23d42ac9df09a673c422aa9a9a9bb3e2f4032'):
    print("Hurray! Email is right!")
else:
    print("Oh! Email is not real")
