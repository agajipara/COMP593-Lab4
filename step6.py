def main():
    # Get the log file path from the command line
    log_path = get_file_path_from_cmd_line()

# TODO: Use filter_log_by_regex() to extract data from the gateway log per Step 6
    filtered_records, extracted_data = filter_log_by_regex(log_path, 'SRC=(.*?) DST=(.*?) LEN=(.*?) ')
    extracted_df = pd.DataFrame(extracted_data, columns=('Source IP', 'Desination IP', 'Length'))
    extracted_df.to_csv('data.csv', index=False)
    
    return