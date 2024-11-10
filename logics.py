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
    rma_dataframe= pd.read_csv(rmafile)
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
    # Read the CSV file
    df = pd.read_csv('prepd/prepared_cap.csv')
    
    # Initialize columns for agents and unique annos tracking
    df['login'] = np.nan
    
    # Get the total number of tasks and agents
    num_tasks = len(df)
    num_agents = len(agent_list)
    
    # Calculate the maximum and minimum number of tasks each agent can receive
    tasks_per_agent = num_tasks // num_agents
    remainder = num_tasks % num_agents
    
    # Create a list of agents with nearly equal task distribution
    agent_task_list = agent_list * tasks_per_agent
    agent_task_list += agent_list[:remainder]
    
    # Shuffle the agent list for random distribution (optional)
    np.random.shuffle(agent_task_list)
    
    # Add the tasks to each agent
    df['login'] = agent_task_list

    # Now distribute the 'annos' values equally
    # Group by 'annos' to count how many unique annos each agent is assigned
    anno_counts = Counter(df['MOTT'])
    anno_per_agent = {agent: [] for agent in agent_list}

    # Distribute unique annos to agents while trying to balance the unique count
    sorted_annos = sorted(anno_counts.items(), key=lambda x: x[1], reverse=True)
    for anno, count in sorted_annos:
        # Find the agent with the least unique annos and assign this anno to them
        agent_with_fewest = min(anno_per_agent, key=lambda agent: len(set(anno_per_agent[agent])))
        anno_per_agent[agent_with_fewest].append(anno)

    # Update the dataframe with the unique annos for each agent
    for agent in agent_list:
        anno_assigned = set(anno_per_agent[agent])
        df.loc[df['login'] == agent, 'Assigned MOTT'] = ", ".join(anno_assigned)
    
    # Save the updated dataframe to a new CSV or return it
    df.to_csv('./assigned/assigned_CAP_tasks.csv', index=False)
    
    return f"{len(agent_list)}|{[f"{x}  :  {len(df.loc[df['login']==x])}  :  {round(len(df.loc[df['login']==x])/23,2)} hours" for x in agent_list]}"


def rma_assign(agent_list):
    # Read the CSV file
    df = pd.read_csv('prepd/prepared_rma.csv')
    
    # Initialize columns for agents and unique annos tracking
    df['login'] = np.nan
    
    # Get the total number of tasks and agents
    num_tasks = len(df)
    num_agents = len(agent_list)
    
    # Calculate the maximum and minimum number of tasks each agent can receive
    tasks_per_agent = num_tasks // num_agents
    remainder = num_tasks % num_agents
    
    # Create a list of agents with nearly equal task distribution
    agent_task_list = agent_list * tasks_per_agent
    agent_task_list += agent_list[:remainder]
    
    # Shuffle the agent list for random distribution (optional)
    np.random.shuffle(agent_task_list)
    
    # Add the tasks to each agent
    df['login'] = agent_task_list

    # Now distribute the 'annos' values equally
    # Group by 'annos' to count how many unique annos each agent is assigned
    anno_counts = Counter(df['annos'])
    anno_per_agent = {agent: [] for agent in agent_list}

    # Distribute unique annos to agents while trying to balance the unique count
    sorted_annos = sorted(anno_counts.items(), key=lambda x: x[1], reverse=True)
    for anno, count in sorted_annos:
        # Find the agent with the least unique annos and assign this anno to them
        agent_with_fewest = min(anno_per_agent, key=lambda agent: len(set(anno_per_agent[agent])))
        anno_per_agent[agent_with_fewest].append(anno)

    # Update the dataframe with the unique annos for each agent
    for agent in agent_list:
        anno_assigned = set(anno_per_agent[agent])
        df.loc[df['login'] == agent, 'Assigned Annos'] = ", ".join(anno_assigned)
    
    # Save the updated dataframe to a new CSV or return it
    df.to_csv('./assigned/assigned_RMA_tasks.csv', index=False)
    
    return f"{len(agent_list)}|{[f"{x}  :  {len(df.loc[df['login']==x])}  :  {round(len(df.loc[df['login']==x])/23,2)} hours" for x in agent_list]}"