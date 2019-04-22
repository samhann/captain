

from collections import defaultdict, Counter
import random
import sys

# This is the length of the "state" the current character is predicted from.
# For Markov chains with memory, this is the "order" of the chain. For n-grams,
# n is STATE_LEN+1 since it includes the predicted character as well.
STATE_LEN = 3
model = defaultdict(Counter)

with open(sys.argv[1], "r") as file:
    print('reading...')
    contents = file.read().replace('\n',' ').replace('"','')
    words = contents.split(' ')

    print('Learning model...')
    for i in range(len(words) - STATE_LEN):
        state = ' '.join(words[i:i + STATE_LEN])
        next = words[i + STATE_LEN]
        model[state][next] += 1

    print('Sampling...')
    state = random.choice(list(model))
    out = [state]
    for i in range(400):
        out.extend(random.choices(list(model[state]), model[state].values()))
        state = state.split(' ')[1] + ' '+ state.split(' ')[2] + ' '+ out[-1]
    print(' '.join(out))
