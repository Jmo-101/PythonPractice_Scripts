import csv
import boto3

def write_iam_policies_to_csv(iam_policies_dict, output_csv_file):
    iam_client = boto3.client('iam')
    
    with open(output_csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Policy Name', 'PolicyId', 'Arn']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for policy_name, policy_arn in iam_policies_dict.items():
            policy_response = iam_client.get_policy(PolicyArn=policy_arn)
            policy_id = policy_response['Policy']['PolicyId']
            
            writer.writerow({'Policy Name': policy_name, 'PolicyId': policy_id, 'Arn': policy_arn})