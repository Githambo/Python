from twilio.rest import Client

TWILIO_ACCOUNT_SID="your TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="Your TWILIO_AUTH_TOKEN"

mytwillio_number="your twilio number"
sms="Your message"

client=Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
client.messages.create(
				to='input number[s]'
				from_=mytwillio_number,
				body=sms
				)