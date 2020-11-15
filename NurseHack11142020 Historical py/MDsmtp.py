#Fake SMTP Server

import mdmail

FormSender = "Yuchen <wang.yuchen@dhs.sg>"

sender = "Yuchen Wang <ywang@connexall.com>"
receiver = FormSender

subject = "Notes 401B 14Nov2020"

message = """

# Patient Notes

* Patient Observation notes #1
* Patient Observation notes cont

## This is a sample numbered list

1. Vent setting
2. Vital Signs 
4. ABG

*that* **is** all.
"""

smtp = {
  'host': 'smtp.mailtrap.io',
  'port': 2525,
  'tls': False,
  'ssl': False,
  'user': '865682b2d753ed',
  'password': '5a2d3de0b5287e',
}

mdmail.send(message, subject=subject, from_email=sender, to_email=receiver, smtp=smtp)


    