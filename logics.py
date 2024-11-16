import pandas as pd
import numpy as np
import os
from collections import Counter


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
    cap_dataframe = cap_dataframe.dropna(subset=['customer_id', 'order_id', 'MOTT'], how='all')
    prepd_cap_count= len(cap_dataframe)
    cap_dataframe.to_csv("./prepd/prepared_cap.csv",index=False)
    return f"{original_count}:{remove_dup_count}:{prepd_cap_count}"

def rma_prep(rmafile):
    rma_dataframe= pd.read_csv(rmafile, sep='\t', skiprows=0)
    original_countr= len(rma_dataframe)
    rma_dataframe.drop_duplicates(subset=['customer_id','annos'],keep='first',inplace=True)
    remove_dup_countr =len(rma_dataframe)
    rma_dataframe= rma_dataframe.loc[rma_dataframe['status']!='A']
    rma_dataframe= rma_dataframe.loc[rma_dataframe['status']!='F']
    rma_dataframe = rma_dataframe.dropna(subset=['customer_id', 'order_id', 'annos'], how='all')
    prepd_rma_countr = len(rma_dataframe)
    rma_dataframe.to_csv("./prepd/prepared_rma.csv",index=False)
    return f"{original_countr}:{remove_dup_countr}:{prepd_rma_countr}" 

import pandas as pd

def cap_assign(agent_list):
    
    df = pd.read_csv('prepd/prepared_cap.csv')
    
   
    df['login'] = np.nan
    
    
    num_tasks = len(df)
    num_agents = len(agent_list)
    
    
    tasks_per_agent = num_tasks // num_agents
    remainder = num_tasks % num_agents
    
    
    agent_task_list = agent_list * tasks_per_agent
    agent_task_list += agent_list[:remainder]
    
    
    np.random.shuffle(agent_task_list)
    
    
    df['login'] = agent_task_list

    
    anno_counts = Counter(df['MOTT'])
    anno_per_agent = {agent: [] for agent in agent_list}

    
    sorted_annos = sorted(anno_counts.items(), key=lambda x: x[1], reverse=True)
    for anno, count in sorted_annos:
        
        agent_with_fewest = min(anno_per_agent, key=lambda agent: len(set(anno_per_agent[agent])))
        anno_per_agent[agent_with_fewest].append(anno)

    
    for agent in agent_list:
        anno_assigned = set(anno_per_agent[agent])
        df.loc[df['login'] == agent, 'Assigned MOTT'] = ", ".join(anno_assigned)
    columns = ['login'] + [col for col in df.columns if col != 'login']
    df = df[columns]
    
    
    df.to_excel('./assigned/assigned_CAP_tasks.xlsx', index=False)
    
    return f"{len(agent_list)}|{[f"{x}  :  {len(df.loc[df['login']==x])}  :  {round(len(df.loc[df['login']==x])/23,2)} hours" for x in agent_list]}"


def rma_assign(agent_list):
    
    df = pd.read_csv('prepd/prepared_rma.csv')
    
    
    df['login'] = np.nan
    
    
    num_tasks = len(df)
    num_agents = len(agent_list)
    
    
    tasks_per_agent = num_tasks // num_agents
    remainder = num_tasks % num_agents
    
    
    agent_task_list = agent_list * tasks_per_agent
    agent_task_list += agent_list[:remainder]
    
    
    np.random.shuffle(agent_task_list)
    
    
    df['login'] = agent_task_list

    
    anno_counts = Counter(df['annos'])
    anno_per_agent = {agent: [] for agent in agent_list}

    
    sorted_annos = sorted(anno_counts.items(), key=lambda x: x[1], reverse=True)
    for anno, count in sorted_annos:
        
        agent_with_fewest = min(anno_per_agent, key=lambda agent: len(set(anno_per_agent[agent])))
        anno_per_agent[agent_with_fewest].append(anno)

    
    for agent in agent_list:
        anno_assigned = set(anno_per_agent[agent])
        df.loc[df['login'] == agent, 'Assigned Annos'] = ", ".join(anno_assigned)
    columns = ['login'] + [col for col in df.columns if col != 'login']
    df = df[columns]
   
    df.to_excel('./assigned/assigned_RMA_tasks.xlsx', index=False)
    
    return f"{len(agent_list)}|{[f"{x}  :  {len(df.loc[df['login']==x])}  :  {round(len(df.loc[df['login']==x])/23,2)} hours" for x in agent_list]}"