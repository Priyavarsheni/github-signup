def signup(username, password):
    if not username:
        return "Username is required"
    if len(password) < 6:
        return "Password must be at least 6 characters"
    if not username.isalnum():
        return "Username must contain only letters and numbers"
    return "Signup successful"

print(signup("priya", "123456"))
