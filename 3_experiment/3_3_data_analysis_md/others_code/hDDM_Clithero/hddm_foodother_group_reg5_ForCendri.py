
###HDDM SCRIPT: JOHN CLITHERO###
###UPDATED: 23 March 2016###

import hddm
import pandas as pd
import numpy as np
import os,sys
import matplotlib.pyplot as plt

###paths###
date_var = '160315' 
exp_dir = '/Users/jac54747/Dropbox/Projects/Pomona/FoodOther/' #make sure this is correct
data_dir = os.path.join(exp_dir, 'Data/CSV_data/')
analysis_dir = os.path.join(exp_dir,'Analysis','HDDM')
date_analysis_dir = os.path.join(analysis_dir,date_var)
if os.path.isdir(date_analysis_dir) == False:
    os.mkdir(date_analysis_dir)
group_analysis_dir = os.path.join(date_analysis_dir,'Group')
if os.path.isdir(group_analysis_dir) == False:
    os.mkdir(group_analysis_dir)
group_reg5_analysis_dir = os.path.join(group_analysis_dir,'GroupReg5')
if os.path.isdir(group_reg5_analysis_dir) == False:
    os.mkdir(group_reg5_analysis_dir)
group_reg5_posterior_analysis_dir = os.path.join(group_reg5_analysis_dir,'Posteriors')
if os.path.isdir(group_reg5_posterior_analysis_dir) == False:
    os.mkdir(group_reg5_posterior_analysis_dir)
    
                
###group model###
num_samples = 11000
num_reg_samples = 11000
num_burn = 1000
num_subs = 38 #full sample
group_csv = 'foodother_Xsub_n' + str(num_subs) + '_hddm.csv'
group_csv_path = os.path.join(data_dir,group_csv)
group_data = hddm.load_csv(group_csv_path)

##separate regressors for rating on trial type##
self_index = group_data.type == 1 
sim_index = group_data.type == 2
diff_index = group_data.type == 3
group_data['TasteSelf'] = 0
group_data['TasteSim'] = 0
group_data['TasteDiff'] = 0
group_data['HealthSelf'] = 0
group_data['HealthSim'] = 0
group_data['HealthDiff'] = 0
group_data.loc[self_index,'TasteSelf'] = group_data.loc[self_index,'TasteRating']
group_data.loc[self_index,'HealthSelf'] = group_data.loc[self_index,'HealthRating']
group_data.loc[sim_index,'TasteSim'] = group_data.loc[sim_index,'TasteRating']
group_data.loc[sim_index,'HealthSim'] = group_data.loc[sim_index,'HealthRating']
group_data.loc[diff_index,'TasteDiff'] = group_data.loc[diff_index,'TasteRating']
group_data.loc[diff_index,'HealthDiff'] = group_data.loc[diff_index,'HealthRating']
##convert other choices to affect self choices##
group_data['SimOnSelf'] = group_data['SimRating'] - 2.5 #make negative for no choices
group_data['DiffOnSelf'] = group_data['SimRating'] - 2.5 #make negative for no choices
group_data.loc[sim_index,'SimOnSelf'] = 0 #make zero on all non-self trials
group_data.loc[diff_index,'SimOnSelf'] = 0 #make zero on all non-self trials
group_data.loc[sim_index,'DiffOnSelf'] = 0 #make zero on all non-self trials
group_data.loc[diff_index,'DiffOnSelf'] = 0 #make zero on all non-self trials

#confidence#
group_data['confidence'] = 0
yes_index = group_data.choice == 4
no_index = group_data.choice == 1 
group_data.loc[yes_index,'confidence'] = 1 #more likely to say yes
group_data.loc[no_index,'confidence'] = -1 #more likely to say no
group_data['confidenceSelf'] = 0
group_data['confidenceSim'] = 0
group_data['confidenceDiff'] = 0
group_data.loc[self_index,'confidenceSelf'] = group_data.loc[self_index,'confidence']
group_data.loc[sim_index,'confidenceSim'] = group_data.loc[sim_index,'confidence']
group_data.loc[diff_index,'confidenceDiff'] = group_data.loc[diff_index,'confidence']

###drop RT that are too fast###
#need to do this last since other params require history#
rt_thresh_lb = 0.200 #200 ms lower threshold
group_data = group_data[group_data['rt'] > rt_thresh_lb]
group_data = group_data.reset_index() #reset index

##reg5##
reg_model_num = 5
v_reg = 'v ~ TasteSelf + HealthSelf + TasteSim + HealthSim + TasteDiff + HealthDiff'
a_reg = 'a ~ C(type)'
reg = [v_reg,a_reg]
model_group_reg5 = hddm.HDDMRegressor(group_data,reg,include='z',informative=False,keep_regressor_trace=True) #use patsy
model_group_reg5_traces = os.path.join(group_reg5_analysis_dir,'traces_reg5.db')
model_group_reg5.sample(num_reg_samples,burn=num_burn,dbname=model_group_reg5_traces,db='pickle')
#print#
model_group_reg5_name = 'stats_print_all_model_group_n' + str(num_subs) + '_reg' + str(reg_model_num) + '.csv'
model_group_reg5_out_path = os.path.join(group_reg5_analysis_dir,model_group_reg5_name)
model_group_reg5.print_stats(fname=model_group_reg5_out_path)
#stats#
model_group_reg5_stats = model_group_reg5.gen_stats()
model_group_reg5_stats_name = 'stats_all_group_n' + str(num_subs) + '_reg' + str(reg_model_num) + '_stats.csv'
model_group_reg5_stats_out_path = os.path.join(group_reg5_analysis_dir,model_group_reg5_stats_name)
model_group_reg5_stats.to_csv(model_group_reg5_stats_out_path)
dic_reg5 = model_group_reg5.dic
#save reg5#
model_group_reg5_sname = 'model_group_reg' + str(reg_model_num) + '_n' + str(num_subs)
model_group_reg5_path = os.path.join(group_reg5_analysis_dir,model_group_reg5_sname)
model_group_reg5.save(model_group_reg5_path)

##save posterior plots for reg4##
model_group_reg5.plot_posteriors(save=True,path=group_reg5_posterior_analysis_dir)
plt.close('all')

###PPC###
group_reg_ppc_analysis_dir = os.path.join(group_reg5_analysis_dir,'PPC')
if os.path.isdir(group_reg_ppc_analysis_dir) == False:
    os.mkdir(group_reg_ppc_analysis_dir)
group_model = model_group_reg5 #to keep it simple below
##generate ppc data##
##probably takes a while to generate for large number of samples##
num_samples = 100
ppc_data = hddm.utils.post_pred_gen(group_model,samples= num_samples)
ppc_data_name = date_var + '_ppc_data_model_group_reg' + str(reg_model_num) + '_n' + str(num_subs) + '_ns' + str(num_samples) + '.csv'
ppc_data_path = os.path.join(group_reg_ppc_analysis_dir,ppc_data_name)
ppc_data.to_csv(ppc_data_path)
##ppc_load = pd.read_csv(ppc_data_path,index_col=[0,1,2])
#ppc stats#
ppc_compare = hddm.utils.post_pred_stats(group_data, ppc_data)
#save to csv#
ppc_compare_name = date_var + '_ppc_stats_all_hddm_group_model_reg' + str(reg_model_num) + '_n' + str(num_subs) + '_ns' + str(num_samples) + '.csv'
ppc_compare_path = os.path.join(group_reg_ppc_analysis_dir,ppc_compare_name)
ppc_compare.to_csv(ppc_compare_path) #to read use index_col=[0] in read_csv
#save separate summary to csv#
ppc_mse_choice = ppc_compare.loc['accuracy']['MSE']
ppc_mse_rt_ub = ppc_compare.loc['mean_ub']['MSE'] #upper barrier
ppc_mse_rt_lb = ppc_compare.loc['mean_lb']['MSE'] #lower barrier (negative RT)
ppc_mh_choice = ppc_compare.loc['accuracy']['mahalanobis']
ppc_mh_rt_ub = ppc_compare.loc['mean_ub']['mahalanobis'] #upper barrier
ppc_mh_rt_lb = ppc_compare.loc['mean_lb']['mahalanobis'] #lower barrier (negative RT)
mse_array = np.array([ppc_mse_choice,ppc_mse_rt_ub,ppc_mse_rt_lb])
mh_array = np.array([ppc_mh_choice,ppc_mh_rt_ub,ppc_mh_rt_lb])
index_array = ['accuracy','mean_ub','mean_lb']
df_ppc_stats = pd.DataFrame(mse_array)
df_ppc_stats = df_ppc_stats.rename(columns = {0:'MSE'})
df_ppc_stats['mahalanobis'] = mh_array
df_ppc_stats.index = index_array
df_ppc_stats.index.name = 'stat'
df_ppc_stats_name = date_var + '_ppc_stats_summary_hddm_group_model_reg' + str(reg_model_num) + '_n' + str(num_subs) + '_ns' + str(num_samples) + '.csv'
df_ppc_stats_path = os.path.join(group_reg_ppc_analysis_dir,df_ppc_stats_name)
df_ppc_stats.to_csv(df_ppc_stats_path) #to read use index_col=[0] in read_csv

del model_group_reg5
