from twilio.rest import Client
client = Client("AC74319e794ee429aa7104381c0f74397f",
                "882e5530386dc3e7fa972e373f289484")

msg = client.messages.create(
    to="+14704020092",
    from_="+19147304906",
    body="hello makabaka",
)
print(f"create a new message: {msg.sid}")

# delete all messages in your account WARNING
# for msg in client.messages.list():
#    print(f"deleting {msg.body}")
#    msg.delete()
