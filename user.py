# coding:UTF-8 
import pandas as pd
import numpy as np
import random
import math
df = pd.read_csv('/home/liuchenlu/python/JD/data/JData/JData_User.csv',encoding='gbk')
n=df.__len__()

#################### parameter set  ########
age1=u'15岁以下'
age2=u'16-25岁'
age3=u'26-35岁'
age4=u'36-45岁'
age5=u'46-55岁'
age6=u'56岁以上'
age7=u'-1'

user=[]

for i in range(0,n):
	#age=df['age'][i]
	
	#deal with the age

	if df['age'][i]==age1:
		
		df['age'][i]=1
	if df['age'][i]==age2:
		#print 'haha'
		df['age'][i]=2
	if df['age'][i]==age3:
		#print 'haha'
		df['age'][i]=3
	if df['age'][i]==age4:
		#print 'haha'
		df['age'][i]=4
	if df['age'][i]==age5:
		#print 'haha'
		df['age'][i]=5
	if df['age'][i]==age6:
		#print 'haha'
		df['age'][i]=6
	# if the bank is -1 or NULL,rand select the num from 1-6

	if df['age'][i]==age7 or math.isnan(df['age'][i]):
		#print 'haha'
		rd_age=random.randint(1,6)
		df['age'][i]=rd_age

	#deal with the sex

	if df['sex'][i]==2 or math.isnan(df['sex'][i]):
		rd_age=random.randint(0,1)
		df['sex'][i]=rd_age

	
	fea1=np.array(df.ix[i,['user_id','age','sex','user_lv_cd','user_reg_tm']])
	#print fea1
	if i==0:
		fea=fea1;
	else:
		fea=np.vstack((fea,fea1))
	
# print type(fea)
# print fea[1]


np.savez('/python/data/user_fea.npz',fea=fea)
# #print user
# print df.ix[0,['age','sex','user_lv_cd']]


############### how to use the  npz #########

# user=load('F:/data/small_JD/user_fea.npz')

# user['fea'][1] 这样就返回每一行的特征


