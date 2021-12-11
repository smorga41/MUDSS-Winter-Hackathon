#Enter date in "yyyy-mm-dd" format

import requests
from bs4 import BeautifulSoup
import pandas as pd

date=input("enter date: ")

country_dict={"us":"United States","gb":"United Kingdom","ae":"UAE","ar":"Argentina","at":"Austria","au":"Australia","be":"belgium","bg":"Bulgaria","bo":"Bolivia","br":"Brazil","ca":"Canada","ch":"Switzerland","cl":"Chile","co":"Colombia","cr":"Costa Rica","cz":"Czech Republic","de":"Germany","dk":"Denmark","do":"Dominican Republic","ec":"Ecuador","ee":"Estonia","eg":"Egypt","es":"Spain","fi":"Finland","fr":"France","gr":"Greece","gt":"Guatemala","hk":"Hong Kong","hn":"Honduras","hu":"Hungary","id":"Indonesia","ie":"Ireland","il":"Israel","in":"India","is":"Iceland","it":"Italy","jp":"Japan","kr":"Republic of Korea","lt":"Lithuania","lu":"Luxembourg","lv":"Latvia","ma":"Morocco","mx":"Mexico","my":"Malaysia","ni":"Nicaragua","nl":"Netherlands","no":"Norway","nz":"New Zealand","pa":"Panama","pe":"Peru","ph":"Philippines","pl":"Poland","pt":"Portugal","py":"Paraguay","ro":"Romania","ru":"Russian Federation","sa":"Saudi Arabia","se":"Sweden","sg":"Singapore","sk":"Slovakia","sv":"El Salvador","th":"Thailand","tr":"Turkey","tw":"Taiwan","ua":"Ukraine","uy":"Uruguay","vn":"Vietnam","za":"South Africa"}

for country in country_dict.keys():
    positions=[]
    track_names=[]
    artists=[]
    streams=[]
    song_links=[]


    url="https://spotifycharts.com/regional/"+country+"/daily/"+date

    headers={'User-agent': 'Mozilla/5.0'}

    re=requests.get(url, headers=headers)

    soup=BeautifulSoup(re.content, 'html.parser')
    links= soup.find_all('a',href=True)
    artists_names=soup.find_all('span')
    for i in range(5,len(links)-5):
        song_links.append(links[i]['href'])
    for i in soup.find_all('td', {"class":"chart-table-position"}):
        positions.append(i.text)

    for i in soup.find_all('strong'):
        track_names.append(i.text)

    for i in range(1,len(artists_names)):
        artists.append(artists_names[i].text)

    for i in soup.find_all('td',{"class":"chart-table-streams"}):
        streams.append(i.text)


    dffinal= pd.DataFrame(list(zip(positions,track_names,artists,streams,song_links)),columns=["Positions","Track Name","Artist","Streams","URL"])
    dffinal.to_csv(str(country)+str(date)+".csv",sep=',')