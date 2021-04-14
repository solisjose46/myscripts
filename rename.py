import os
paths = ['../madeline-ackley/stories/azmirror/', '../madeline-ackley/stories/downtowndevil/']
prefix = 'madeline_ackley_'
suffix = '.html'

for path in paths:
    for count, filename in enumerate(os.listdir(path)):
        src = path + filename
        dst = path + prefix + str(count) + suffix
        os.rename(src, dst)