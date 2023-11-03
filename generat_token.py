import jwt

# Your payload data
payload = {
    "user_id": "123456",
    "username": "exampleuser"
}

# Your secret key (keep this secret!)
secret_key = "your_secret_key"

# Generate the JWT token
token = jwt.encode(payload, secret_key, algorithm="HS256")

print(token)
