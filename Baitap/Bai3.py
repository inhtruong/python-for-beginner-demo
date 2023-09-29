'''
  Viết một chương trình Python tách username và domain của email. Chương trình sẽ yêu cầu người dùng nhập email và in ra username, domain của email đó.
'''

email = input("Enter your email: ")

at_index = email.find("@")

if at_index != -1:
    username = email[:at_index]
    domain = email[at_index + 1:]

    print("Username: ", username)
    print("Domain: ", domain)
else:
    print("Invalid email")