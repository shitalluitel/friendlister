import facebook
import pyperclip

token = input("Enter user access token: ")
friends = []
get_name = ""

graph = facebook.GraphAPI(access_token=token, version='2.7')
data = graph.request('/me/taggable_friends?limit=10000')
for x in data['data']:
    friends.append(x['name'])

print(len(friends))

for name in friends:
    get_name += '@' + name + ' '

final_list = get_name.split()
count = 0
str = ''
for i in final_list:
    if count == 30:
        pyperclip.copy(str)
        str = ''
        count = 0
        print("Enter 'n' to continue: ")
        if input().lower() != 'n':
            pyperclip.copy(str)
            exit()
        continue
    str += i + ' '
    print(i)
    count += 1

