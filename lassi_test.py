import lassie
import micawber

# res = lassie.fetch('https://www.youtube.com/watch?v=5zeol3wcOwg')
# print(res)


providers = micawber.bootstrap_basic()
# todo: only good on youtube
res = providers.request('https://www.youtube.com/watch?v=5zeol3wcOwg')
print(res)