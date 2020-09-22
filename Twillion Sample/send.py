from twilio.rest import Client

TWILIO_ACCOUNT_SID="ACb99b4b21ae84dd31d10024a17bd25d8e"
TWILIO_AUTH_TOKEN="a4fb0e3745010009fabcec5bffa7f41a"

client=Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
client.messages.create(
				to="+254704478977",
				from_="+12072227121",
				body="Khali test "
				)