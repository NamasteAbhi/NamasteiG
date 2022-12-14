from NamasteiG import Instagram

#For Login IG Account
UserName=''
PassWord=''
IG=Instagram(UserName,PassWord)
IG.Login()

#For Scrape Victim Followers
VictimUserId=''
data=IG.Scrape_Followers(VictimUserId)
print(data)

#For Scrape Victim Followings
VictimUserId=''
data=IG.Scrape_Followings(VictimUserId)
print(data)


#More Features Comming Soon And Tell Me Which Types Of Features You Want To Add In This Library
# Drop Your Suggestion Here => https://t.me/namastehackersgroup
