email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawe@sgh.waw.'
email4 = 'pawesgh.waw.'
email5 = 'pawesgh.waw.@'

email_list = [email1, email2, email3, email4, email5]

def validate_email(email):
    #TODO - verify email....
    # True if ok, False otherwise
    at_pos = email.find('@')
    #if email[-1]=='@' or email[-1]=='.':
    if email[-1] in ['@', '.']:
        return False
    #print(at_pos)
    if at_pos < 1:
        return False

    return True


for em in email_list:
    print('{}: {}'.format(em, validate_email(em)))