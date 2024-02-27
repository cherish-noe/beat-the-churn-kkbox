from src.data_prep import load_raw_data

member_file_path = './data/members_v3.csv'
member_df = load_raw_data(member_file_path)
print(member_df.head())