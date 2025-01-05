DEPOSIT = 1
WITHDRAWAL = 2
LOAN = 3
LOAN_PAID = 4
TRANSFER_RECEIVE = 5
TRANSFER_SEND = 6

TRANSACTION_TYPE = (
    (DEPOSIT, 'Deposite'),
    (WITHDRAWAL, 'Withdrawal'),
    (LOAN, 'Loan'),
    (LOAN_PAID, 'Loan Paid'),
    (TRANSFER_RECEIVE,'Transfer Receive'),
    (TRANSFER_SEND,'Transfer Send'),
)


from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_transaction_email(user, amount, subject, template):
        context_user_info = {
            'user':user,
            'amount':amount
        }
        body = render_to_string(template,context_user_info)

        email = EmailMultiAlternatives(
            subject=subject,
            body='',
            from_email= 'ReFresh Bank <noreply@example.com>',
            to=[user.email],
        )
        email.attach_alternative(body, "text/html")
        email.send()

def money_transfer_email(title,send_account, receive_account, transaction, template):
        context = {
            'sender':send_account,
            'recipient':receive_account,
            'transaction':transaction,
            'title' : title
        }
        email = send_account.user.email
        if context['title'] != 'Send':
                email = receive_account.user.email
         
        body = render_to_string(template,context)

        email = EmailMultiAlternatives(
            subject="Transfar Money",
            body='',
            from_email= 'ReFresh Bank <noreply@example.com>',
            to=[email],
        )
        email.attach_alternative(body, "text/html")
        email.send()