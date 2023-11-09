email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawe@sgh.waw.'
email4 = 'pawesgh.waw.'
email5 = 'pawesgh.waw.@.'

email_list = [email1, email2, email3, email4, email5]

def validate_email(email):
    #TODO - verify email....
    # True if ok, False otherwise
    at_pos = email.find('@')
    #print(at_pos)
    if at_pos > 0:
        return True
    else:
        return False


for em in email_list:
    print('{}: {}'.format(em, validate_email(em)))