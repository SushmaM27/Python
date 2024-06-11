import Pandas as pd
import os
#import unittets

csv_df = pd.read_csv('filepth+filename', encoding = 'ISO-8859-1', delimiter = '|' )

xl_df = pd.read_csv('filepth+filename', encoding = 'ISO-8859-1', engine= 'openpyxl')

difect_list = []

#get the the row and column count
csv_shape = csv_df.shape
xl_shape = xl_df.shape

if csv_shape[0] != xl_shape[0]:
	defect_list.append(['warning', 'Row count is not matching', csv_shape[0], xl_shape[0]])
if csv_shape[1] != xl_shape[1]:
	defect_list.append(['warning', 'Column count is not matching', csv_shape[1], xl_shape[1]])
	
#validate Column dtypes
expected_dtypes = {'machine_id': 'object', 'item_count': 'int64', 'date':'datetime', 'fault_items':'int64'}
Actual_dtypes = xl_df.dtypes.to_dict()

for key in list(expected_dtypes.keys()):
	try:
		if expected_dtypes[key] != Actual_dtypes[key]:
			defect_list.append(['error', 'Column Data types are not macthing', key, ''])
	except KeyError as ke:
		defect_list.append(['error', 'Column not found', key, ''])
		


# not null mandatory Columns

not_nullcols = ['machine_id']
for col in not_nullcols:
	len_of_null_rec = xl_df[col].isnull().shape()[0]
	if len_of_null_rec != 0:
		defect_list.append(['error', 'Not null column has null value', col, ''])
		

	
# compare data 
Create data 


fault_rec_df = csv_df.compare(xl_df, result_names=("csv", "xl"))
if fault_rec_df.shape[0] != 0:
    fault_rec_df.to_excel(file_path+filename, engine = 'openpyxl')
	defect_list.append(['error', 'Values Mismatching', file_path+filename, ''])
    
headers = ['type', 'description', 'err_value', 'expected']
    
falut_codes_df = pd.DataFrame(defect_list , columns = ['type', 'description', 'err_value', 'expected'])
falut_codes_df.to_excel(filepath+filename, engine = 'openpyxl')


