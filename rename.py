import os
paths = ['../journalist-archive/stories/azmirror/', '../journalist-archive/stories/downtowndevil/']
prefix = 'story_'
suffix = '.html'

count = 0
for path in paths:
    for filename in enumerate(os.listdir(path)):
        src = path + filename
        dst = path + prefix + str(count) + suffix
        count = count + 1
        os.rename(src, dst)

print('renaming complete')