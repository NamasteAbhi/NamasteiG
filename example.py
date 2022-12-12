from NamasteiG import Instagram

#For Login IG Account
UserName=''
PassWord=''
IG=Instagram(UserName,PassWord)
IG.Login()

#For Scrape Victim Followers
#Category Is username, pk, full_name And More
Category='username'
VictimUserId=''
data=IG.Scrape_Followers(VictimUserId,Category)
print(data)

#More Features Comming Soon And Tell Me Which Types Of Features You Want To Add In This Library
# Drop Your Suggestion Here => https://t.me/namastehackersgroup