#world cup sweepstake
#Written by Stuart Bowe
import random
import smtplib


random.seed()
#List of teams in the world cup
teams = ['Algeria', 'Argentina', 'Australia', 'Belgium', 'Bosnia-Herzegovina', 'Brazil (host)', 'Cameroon', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Ecuador', 'England', 'France', 'Germany', 'Ghana', 'Greece', 'Honduras', 'Iran', 'Italy', 'Ivory Coast', 'Japan', 'Mexico', 'Netherlands', 'Nigeria', 'Portugal', 'Russia', 'South Korea', 'Spain', 'Switzerland', 'Uruguay', 'U.S']
#Put everyone's names here
Names = ['**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**', '**redacted**']

random.shuffle(Names)

random.shuffle(teams)
writestring = ''
for name in Names:
    rand1 = random.randint(0,len(teams)-1)

    writestring = writestring + name + ' will be supporting: ' + teams[rand1] + ' and '
    del teams[rand1]

    rand2 = random.randint(0,len(teams)-1)

    writestring = writestring + teams[rand2] + '\n'
    del teams[rand2]

#Outputs the results as a .txt file
result = open('Sweepstake results.txt','w')
result.write(writestring)
result.close()


#This section was designed to send the result as an email to prevent fraud
#but I'll be buggered if I can get it to work
'''
fp = open(result, 'rb')
msg = MIMEText(fp.read())
fp.close

msg['Subject'] = 'World cup sweepstake'
msg['From'] = 'stuart.bow***redacted***@gmail.com'
msg['To'] = 'ppx***redacted***@nottingham.ac.uk'

s = smtplib.SMTP('localhost')
'''
