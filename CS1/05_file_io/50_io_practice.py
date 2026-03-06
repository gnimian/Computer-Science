with open ('io_practice(text)','w') as f:
    s='hello mommy'
    f.write(s)
with open ('io_practice(text)','a') as f:
    f.write(' another line')
