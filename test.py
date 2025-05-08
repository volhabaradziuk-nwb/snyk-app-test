user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "';"
execute_query(query)


user_input = input("Enter expression: ")
result = eval(user_input)
