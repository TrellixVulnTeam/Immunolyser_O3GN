import sys
import os
from subprocess import call

task_id = sys.argv[1]

for sample in os.listdir('/immunolyser-data/data/{}'.format(task_id)):
    for replicate in os.listdir('/immunolyser-data/data/{}/{}'.format(task_id,sample)):
        
        if replicate[-3:] == 'txt':
            call(['python2', 'app/tools/seq2logo-2.1/Seq2Logo.py', '-f', '/immunolyser-data/data/{}/{}/{}'.format(task_id, sample, replicate), '-o', '{}/{}/{}/seqlogos/{}'.format('app/static/images', task_id, sample, replicate[:-4]), '--format', '[JPEG]', '-t', '{}'.format(replicate[:-4]), '-S', '2', '-I', '2'])
