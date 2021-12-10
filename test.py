import EventDB as edb
from random import choices
def main():
    emp = []
    event_test = [eve for eve in edb.bad_events]
    prob = [.24, .01, .01, .01, .1, .02, .02, .02, .02]
    for _ in range(10):
        emp.append("".join((choices(event_test, prob))))
    print(emp)
main()