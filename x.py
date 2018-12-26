import requests
import os
import webbrowser

ID = int(input('URLのvideoの後ろにある、現在のIDを入力してください。\n例→　http://www.xvideos.com/video1234567/ \nだったら[1234567]\nID:'))
hit = int(input('検索件数を入力してください。※50件以上はマズイと思う\n検索件数:'))
i = 0
with open('./videolist.html','w') as file:#videolistの初期化、特に何もしないのでpass
    pass

for i in range(hit):
    url = ('http://www.xvideos.com/video'+ str(ID+i)+'/')
    url = requests.get(url)

    if url.status_code == 404:#もしない場合はその直前のIDを記録
        current_ID = ('http://www.xvideos.com/video'+ str(ID+i-1)+'/')
        hit +=1
        with open('newest_ID.html','w') as file:
            file.write(current_ID)
    else:
        html=('<iframe src="https://www.xvideos.com/embedframe/' + str(ID+i) + '"' + ' frameborder=0 width=510 height=400 scrolling=no allowfullscreen=allowfullscreen></iframe>')#動画自動生成
        with open('./videolist.html','a') as file:#'a'は追記モード、ファイルがない場合は新規作成
            file.write(html+str('\n'))
    i += 1
    print('残り'+str(hit-i+1))

path = os.path.abspath('videolist.html')
web = 'file:///'+path
print(web)
webbrowser.open_new(web)
