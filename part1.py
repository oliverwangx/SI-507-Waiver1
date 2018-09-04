# these should be the only imports you need
import tweepy
import nltk
import json
import sys


consumer_key = 'TRkNj6jA3bN6wCd02Rm3Ce8kq'
consumer_secret = 'gj7XnD3fIjfRYovACEeUIWD3Ruw4R8Qc5xzESew34MpnEvckwi'
access_token = '868701000453967872-nCMrjSc7IpXD2dGPEp36kWXr8Q6SfMj'
access_secret = 'gJqPhFMaUpcM8kHskLYQyrmXNXE7r6BriLyzzVnRLFO4R'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.home_timeline).items(8):
#     print (status.text)


### under the python 2.7



num=int(sys.argv[2])
user=sys.argv[1]
public_tweets=api.user_timeline(id=user,count=num)

verbs=[]
verbs_num=[]
adj=[]
adj_num=[]
noun=[]
noun_num=[]

tf=0
ignore=["http", "https", "RT"]
text_list=[]
count=0
rt=0
for tweet in public_tweets[0:num]:
    if tweet.text[0:2]!="RT":
        tf=tweet.favorite_count+tf
        rt=tweet.retweet_count+rt
        count=count+1
    temp=json.dumps(tweet.text)
    tokens = nltk.Text(nltk.word_tokenize(temp))
    tweets_tagged = nltk.pos_tag(tokens)
    for word in tweets_tagged:
        if word[0][0].isalpha() and word[0] not in ignore:
            text_list.append(word)


wordCount_diction_vb= {}
wordCount_diction_nn= {}
wordCount_diction_jj= {}
for word in text_list:
    if word[1]=='VB':
        if word[0] in wordCount_diction_vb.keys():
            wordCount_diction_vb[word[0]] += 1
        else:
            wordCount_diction_vb[word[0]] = 1
    elif word[1]=='NN':
        if word[0] in wordCount_diction_nn.keys():
            wordCount_diction_nn[word[0]] += 1
        else:
            wordCount_diction_nn[word[0]] = 1
    elif word[1]=='JJ':
        if word[0] in wordCount_diction_jj.keys():
            wordCount_diction_jj[word[0]] += 1
        else:
            wordCount_diction_jj[word[0]] = 1






wordCount_diction_vb=sorted(wordCount_diction_vb.items(),key = lambda x:( -x[1],x[0]), reverse = False)
wordCount_diction_nn=sorted(wordCount_diction_nn.items(),key = lambda x: ( -x[1],x[0]), reverse = False)
wordCount_diction_jj=sorted(wordCount_diction_jj.items(),key = lambda x: ( -x[1],x[0]), reverse = False)


print ("USER: "+str(user))
print ("TWEETS ANALYZED: "+str(num))
print ("VERBS: "+str(wordCount_diction_vb[0][0])+'('+str(wordCount_diction_vb[0][1])+') '+\
str(wordCount_diction_vb[1][0])+'('+str(wordCount_diction_vb[1][1])+') '+\
str(wordCount_diction_vb[2][0])+'('+str(wordCount_diction_vb[2][1])+') '+\
str(wordCount_diction_vb[3][0])+'('+str(wordCount_diction_vb[3][1])+') '+\
str(wordCount_diction_vb[4][0])+'('+str(wordCount_diction_vb[4][1])+') ')

print ("NOUNS: "+str(wordCount_diction_nn[0][0])+'('+str(wordCount_diction_nn[0][1])+') '+\
str(wordCount_diction_nn[1][0])+'('+str(wordCount_diction_nn[1][1])+') '+\
str(wordCount_diction_nn[2][0])+'('+str(wordCount_diction_nn[2][1])+') '+\
str(wordCount_diction_nn[3][0])+'('+str(wordCount_diction_nn[3][1])+') '+\
str(wordCount_diction_nn[4][0])+'('+str(wordCount_diction_nn[4][1])+') ')

print ("ADJECTIVES: "+str(wordCount_diction_jj[0][0])+'('+str(wordCount_diction_jj[0][1])+') '+\
str(wordCount_diction_jj[1][0])+'('+str(wordCount_diction_jj[1][1])+') '+\
str(wordCount_diction_jj[2][0])+'('+str(wordCount_diction_jj[2][1])+') '+\
str(wordCount_diction_jj[3][0])+'('+str(wordCount_diction_jj[3][1])+') '+\
str(wordCount_diction_jj[4][0])+'('+str(wordCount_diction_jj[4][1])+') ')

print ( "ORIGINAL TWEETS: " +str(count))

print( "TIMES FAVORITED (ORIGINAL TWEETS ONLY): "+str(tf))

print ("TIMES RETWEETED (ORIGINAL TWEETS ONLY): "+str(rt))




# csvfile = open("noun_data.csv", "w+")
# try:
#     writer = csv.writer(csvfile)
#     writer.writerow(('Noun', 'Number'))
#     for i in range(5):
#         writer.writerow((wordCount_diction_nn[i][0],wordCount_diction_nn[i][1]))
# except IOError as e:
#     print(e)
# finally:
#     csvfile.close()


fo = open("noun_data.csv", "w")
#fo.write( "Python is a great language.\nYeah its great!!\n"    )
fo.write(("Noun, Number\n"))
for i in range(5):
    fo.write(str(wordCount_diction_nn[i][0])+','+str(wordCount_diction_nn[i][1])+'\n')
fo.close()