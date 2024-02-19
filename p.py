import os
import glob
import pandas as pd

os.chdir('C:\\Users\\Ariake\\Desktop\\20230214\\log\\20svnn\\net-excel')

ext= 'csv'
allfile= [i for i in glob.glob('*.{}'.format(ext))]

combine= pd.concat([pd.read_csv(f) for f in allfile])
combine.to_csv('net-combine-n.csv', index=False, encoding='utf-8-sig')