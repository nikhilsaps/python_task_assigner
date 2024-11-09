import pandas as pd
import os


def clear_prepd():
    if os.path.exists("./prepd/") and os.path.isdir("./prepd/"):
        for item in os.listdir("./prepd/"):
            item_path = os.path.join("./prepd/",item)
            print(item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
            except Exception as e:
                print(f"Error while deleting the file{item_path}:{e}")
        print("all file removed and no old data")
    else:
        print(f"Folder does not exist or is not a directory")

def cap_prep(capfile):
    cap_dataframe= pd.read_csv(capfile)
    original_count= len(cap_dataframe)
    cap_dataframe.drop_duplicates(subset=['customer_id','MOTT'],keep='first',inplace=True)
    remove_dup_count =len(cap_dataframe)
    cap_dataframe= cap_dataframe.loc[cap_dataframe["conceded_order_id"].isna()]
    prepd_cap_count= len(cap_dataframe)
    cap_dataframe.to_csv("./prepd/prepared_cap.csv",index=False)
    return f"{original_count}:{remove_dup_count}:{prepd_cap_count}"

def rma_prep(rmafile):
    rma_dataframe= pd.read_csv(rmafile)
    original_countr= len(rma_dataframe)
    rma_dataframe.drop_duplicates(subset=['customer_id','annos'],keep='first',inplace=True)
    remove_dup_countr =len(rma_dataframe)
    rma_dataframe= rma_dataframe.loc[rma_dataframe['status']!='A']
    rma_dataframe= rma_dataframe.loc[rma_dataframe['status']!='F']
    prepd_rma_countr = len(rma_dataframe)
    rma_dataframe.to_csv("./prepd/prepared_rma.csv")
    return f"{original_countr}:{remove_dup_countr}:{prepd_rma_countr}" 


def cap_assign(logins):  
    tasks = pd.read_csv('prepd/prepared_cap.csv') 
    print(logins)
    investigators = pd.DataFrame([x for x in logins.split(",")], columns=["login"])
    grouped_tasks = tasks.groupby('MOTT')['order_id'].apply(list).reset_index()
    assigned_tasks = []
    investigator_workload = {login: {'order_count': 0, 'mott_count': 0} for login in investigators['login']}
    for _, group in grouped_tasks.iterrows():
        mott = group['MOTT']
        order_ids = group['order_id']
        for order_id in order_ids:
            least_loaded_investigator = min(investigator_workload.items(), 
                                             key=lambda x: (x[1]['order_count'], x[1]['mott_count']))
            login = least_loaded_investigator[0]
            task_row = tasks[tasks['order_id'] == order_id].iloc[0]
            assigned_tasks.append({
                **task_row.to_dict(), 
                'login': login          
            })
            investigator_workload[login]['order_count'] += 1
            investigator_workload[login]['mott_count'] += 1
    assigned_df = pd.DataFrame(assigned_tasks)
    cols = ['login'] + [col for col in assigned_df.columns if col != 'login']
    assigned_df = assigned_df[cols]
    assigned_df.to_csv('./assigned/assigned_CAP_tasks.csv', index=False)
    return f"{len(investigators)}"


def rma_assign(logins):  
    tasks = pd.read_csv('prepd/prepared_rma.csv') 
    print(logins)
    investigators = pd.DataFrame([x for x in logins.split(",")], columns=["login"])
    grouped_tasks = tasks.groupby('annos')['order_id'].apply(list).reset_index()
    assigned_tasks = []
    investigator_workload = {login: {'order_count': 0, 'annos': 0} for login in investigators['login']}
    for _, group in grouped_tasks.iterrows():
        annos = group['annos']
        order_ids = group['order_id']
        for order_id in order_ids:
            least_loaded_investigator = min(investigator_workload.items(), 
                                             key=lambda x: (x[1]['order_count'], x[1]['annos']))
            login = least_loaded_investigator[0]
            task_row = tasks[tasks['order_id'] == order_id].iloc[0]
            assigned_tasks.append({
                **task_row.to_dict(), 
                'login': login          
            })
            investigator_workload[login]['order_count'] += 1
            investigator_workload[login]['annos'] += 1
    assigned_df = pd.DataFrame(assigned_tasks)
    cols = ['login'] + [col for col in assigned_df.columns if col != 'login']
    assigned_df = assigned_df[cols]
    assigned_df.to_csv('./assigned/assigned_RMA_tasks.csv', index=False)
    return f"{len(investigators)}"


# def rma_assign():  
#     tasks = pd.read_csv('prepd/prepared_rma.csv') 
#     investigators = pd.read_csv('login.csv') 
#     grouped_tasks = tasks.groupby('annos')['order_id'].apply(list).reset_index()
#     assigned_tasks = []
#     investigator_workload = {login: {'order_count': 0, 'annos': 0} for login in investigators['login']}
#     for _, group in grouped_tasks.iterrows():
#         annos = group['annos']
#         order_ids = group['order_id'] 
#         for order_id in order_ids:
#             least_loaded_investigator = min(investigator_workload.items(), 
#                                          key=lambda x: (x[1]['order_count'], x[1]['annos']))
#             login = least_loaded_investigator[0]
#             assigned_tasks.append({
#                 'order_id': order_id,
#                 'annos': annos,
#                 'login': login
#             })
#             investigator_workload[login]['order_count'] += 1
#             investigator_workload[login]['annos'] += 1
#     assigned_df = pd.DataFrame(assigned_tasks)
#     assigned_df.to_csv('./assigned/assigned_RMA_tasks.csv', index=False)