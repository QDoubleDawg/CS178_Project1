import boto3
from botocore.exceptions import ClientError
#had to look up the syntax for exceptions! link: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html
# This impliments everything wiht CRUD; making my table CRUD compliant!!!!!! yipeeeeeeeeeeeee

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users')


def create_user():
    username = input("Username: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    

    try:
        table.put_item(Item={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,

        })
        print("User created!")
    except ClientError as e:
        print("Error:", e.response['Error']['Message'])

# I only needed to get the user, i had no reason to keep the get all users implimentation; changed dirctions for my prject so i changed it to get a single user
def get_user(username):
    try:
        response = table.get_item(Key={"username": username})
        return response.get("Item")
    
    except ClientError as e:
        print("Error fetching user:", e.response['Error']['Message'])
        return None



def update_user_password():
    username = input("Username: ")
    email = input("Email: ")
    new_password = input("New password: ")


    response = table.get_item(Key={'username': username})
    user = response.get('Item')

    if not user:
        print("User not found.")
        return

    if user['email'] != email:
        print("Email doesn’t match.")
        return
    
    user['password'] = new_password
    table.put_item(Item=user)

    print("Password updated!")


def delete_user():
    username = input("Username: ")
    email = input("Email: ")

    user = table.get_item(Key={'username': username}).get('Item')

    if not user:
        print("User not found.")
        return

    if user['email'] != email:
        print("Email does not match.")
        return

    table.delete_item(Key={'username': username})
    print("User deleted.")
