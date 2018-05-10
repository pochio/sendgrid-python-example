import sendgrid
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey="SENDGRID_API_KEY")

mail = Mail()
mail.from_email = Email("example+from@example.jp")
mail.add_content(Content("text/plain", "Hello World!"))

## リプライ先を指定したい場合
#mail.reply_to = Email("hogehoge@example.jp")

## メールヘッダから To を隠蔽したい場合
#mail.add_header(Header("To:", ""))

to_addrs = ["example+to@example.jp"]
cc_addrs = ["example+cc@example.jp"]
bcc_addrs = ["example+bcc@example.jp"]

personalization = Personalization()
personalization.subject = "Hello World!"

for addr in to_addrs:
    personalization.add_to(Email(addr))

if len(cc_addrs) != 0:
    for addr in cc_addrs:
        personalization.add_cc(Email(addr))

if len(bcc_addrs) != 0:
    for addr in bcc_addrs:
        personalization.add_bcc(Email(addr))

mail.add_personalization(personalization)

try:
    response = sg.client.mail.send.post(request_body=mail.get())
except Exception as e:
    print(e)

print(response.status_code)
print(response.body)
print(response.headers)

