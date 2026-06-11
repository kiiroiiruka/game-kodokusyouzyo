import pgzrun#普段
import winsound
import random
WIDTH =700
HEIGHT=490
TITLE="RPG ゲーム名[孤独少女に問いかけた]　  ※画面一番右上の X を押して終了してもセーブデーターは消えません→"
#on[1]=3←セリフ出す　　　　　　　　	#on[3]=n←n番目のストーリーシーン流す
#ii[3]＝n←セリフ出すときｎ段落出す
music=[0,0,0,0]
item=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#アイテムを保持してるかしてないかの判定
on=[1,0,0,0,2,-1]# 1-1アイテム欄1-2セーブ欄1-3テキスト欄 2　-を廊下　＋教室　＋999+大きい部屋　on[4]階数　on[3]シーンon[5]敵
time=[60,-1,180]
i=[0,0,0,0,30,0,5,0,0,0,0,0,0,0]
z=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#アイテム欄のアイテムの座標
zz=[0,0,0,0,0,0,0,0,0,0,0]#セーブ欄のセーブデーターの座標
savee=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#初期状態のデータ
saveee=[0,0]#初期状態のデータ
save1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
save11=[0,0]
save2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
save22=[0,0]
save3=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
save33=[0,0]
save4=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
save44=[0,0]
stoppppp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#初期状態のデータ
gyara=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
gyaraa=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#初期状態のデータ
data=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#ゲーム中はここにデーターが入る#data1マップ data2進み具合　
q=Actor('q',topleft=(0,0))
qq1=Actor('qq',topleft=(-20,-10))
qq2=Actor('qq',topleft=(-20,90))
qq3=Actor('qq',topleft=(-20,190))
qq4=Actor('qq',topleft=(-20,290))
setumei2=Actor('setumei2',topleft=(280,380))
setumei3=Actor('setumei3',topleft=(400,410))
iii=[0,0,0,0,0,0,0,0]#[0]で霊鬼階段移動２でプレイ時間3でアイテムのある場所
ii=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,1,0,0,0,0]#ii[3]テキストの段落数#ii[4]マップ動くかキャラクターが動くか
#ii[7]とii[8]でマップ移動時のプレイヤー座標 ii[9]でセーブストッパー10 11 12同様12は今保持しているアイテム数
#ii[13]でセリフが最終段落か判断#ii[14]でセリフ中にプレイヤーを表示するか#ii[15]ストーリー進めるストッパー
#ii[16]ロック画面#ii[17]ロック画面の数字1桁ii[18]ロック画面の数字2桁ii[19]ロック画面の数字3桁ii[20]ロック画面の数字4桁ii[21]ロック画面の数字5桁
#ii[22]とii[23]でキャラクターの表情ii[24]で会話スキップストッパー#ii[25]で敵のモーションii[26]ii[27]ii[28]ii[29]敵の出現ii[30]1ii[31]プレイ時間
#ii[32]#ii[33]#ii[34]#ii[35]セーブデーターのプレイ時間ii[36]
so=[0,0,1,0,0,0,0,0,0]#0どの効果音ならすか1当たり判定2シーンの段落3ロック画面のストッパー4アイテム元の位置に戻す、再びとるとき56
teki=[0,0,0,0,0,0]
saigo=Actor('saigo')
nn=Actor('nn',topleft=(0,330))
home=Actor('home',topleft=(0,0))
home2=Actor('home2',topleft=(0,0))
start=Actor('start',topleft=(5,25))
tuduki=Actor('tuduki',topleft=(5,135))
setumei=Actor('setumei',topleft=(5,245))
modoru=Actor('modoru',topleft=(5,375))
gyarari=Actor('gyarari',topleft=(5,355))#gyarariinokabegami
gyarariinokabegami=Actor('gyarariinokabegami',topleft=(0,0))
roudo=[Actor('roudo',topleft=(0,0)),Actor('roudo1',topleft=(0,0)),Actor('roudo2',topleft=(0,0)),Actor('roudo3',topleft=(0,0))]
n=Actor('n',topleft=(0,340))
over=Actor('over',topleft=(0,0))#gameover
A2F=Actor('kannnai',topleft=(0,0))#館内マップ
n1=Actor('n',topleft=(0,340))
m1=Actor('m1m',topleft=(0,0))
c=Actor('a2',topleft=(350,300))
cc=Actor('cc',topleft=(350,300))
kabe=Actor('kabe',topleft=(0,340))
kabe1=Actor('kabe2',topleft=(350,300))
kabe3=Actor('kabe3',topleft=(350,300))#出口1
kabe4=Actor('kabe3',topleft=(350,300))#出口2
kabe5=Actor('kabe3',topleft=(350,300))#出口3
kabe6=Actor('kabe3',topleft=(350,300))#出口4
kabe7=Actor('kabe5',topleft=(350,300))#出口4
kabe8=Actor('kabe5',topleft=(350,300))#出口5
kabe9=Actor('kabe5',topleft=(350,300))#出口6
maaku1=Actor('maaku1',topleft=(350,300))#キャラクターの反応
maaku1n1=Actor('maaku1n1',topleft=(350,300))#キャラクターの反応
maaku1n2=Actor('maaku1n2',topleft=(350,300))#キャラクターの反応
maaku1n3=Actor('maaku1n3',topleft=(350,300))#キャラクターの反応
maaku2=Actor('maaku2',topleft=(350,300))#キャラクターの反応
maaku3=Actor('maaku3',topleft=(350,300))#キャラクターの反応
am6=Actor('am6',topleft=(140,310))#キャラクター（主人公）
am7=Actor('am7',topleft=(430,310))#キャラクター（主人公）
am2=Actor('am2',topleft=(500,70))#キャラクター（主人公）
am4=Actor('am4',topleft=(500,70))#キャラクター（主人公）
am5=Actor('am5',topleft=(500,70))#キャラクター（主人公）
am3=Actor('am3',topleft=(500,70))#キャラクター（主人公）
g1=Actor('am1',topleft=(500,70))#キャラクター（主人公）
ccc=Actor('a22',topleft=(350,300))#歩いているモーション
cccc=Actor('a222',topleft=(350,300))#歩いているモーション
c1=Actor('a5',topleft=(350,300))#歩いているモーション
c1c=Actor('a55',topleft=(350,300))#歩いているモーション
c1cc=Actor('a555',topleft=(350,300))#歩いているモーション
c2=Actor('a3',topleft=(350,300))#歩いているモーション
c2c=Actor('a33',topleft=(350,300))#歩いているモーション
c2cc=Actor('a333',topleft=(350,300))#歩いているモーション
c3=Actor('a4',topleft=(350,300))#歩いているモーション
c3c=Actor('a44',topleft=(350,300))#歩いているモーション
c3cc=Actor('a444',topleft=(350,300))#歩いているモーション
R=Actor('w',topleft=(0,70))#暗号ロックパネル
R1=Actor('w',topleft=(116,70))#暗号ロックパネル
R2=Actor('w',topleft=(232,70))#暗号ロックパネル
R3=Actor('w',topleft=(348,70))#暗号ロックパネル
R4=Actor('w',topleft=(464,70))#暗号ロックパネル
R5=Actor('w1',topleft=(0,70))#暗号ロックパネル押しているとき
map1=Actor('map1',topleft=(0,70))#一番最初のマップ
map11=Actor('map11',topleft=(0,70))#一番最初のマップ
map2=Actor('map2',topleft=(0,0))#マップ3
map3=Actor('map3',topleft=(0,0))#マップ3
map4=Actor('map4',topleft=(0,0))#マップ4
map5=Actor('map5',topleft=(0,0))#マップ5
map6=Actor('map6',topleft=(0,0))#マップ6
murasaki=Actor('5-1',topleft=(0,0))#マップ6
tosyo=Actor('tosyo',topleft=(0,340))#部屋（図書室）
rouka=Actor('rouka',topleft=(0,340))#部屋（本館教室前廊下）
rouka1=Actor('rouka1f',topleft=(0,340))#部屋（本館教室前廊下）
rouka4=Actor('rouka4f',topleft=(0,340))#部屋（本館教室前廊下）
huku=Actor('huku',topleft=(0,340))#部屋（服飾デザイン）
huku2=Actor('huku',topleft=(40,0))
tosyo2=Actor('tosyo',topleft=(0,-90))
soubi=Actor('soubi',topleft=(0,340))#部屋（総合ビジネス）
soubi2=Actor('無題618_20230825110719',topleft=(0,340))
sikai=Actor('sikai',center=(450,365))#視界エフェクト

osita=Actor('osita',center=(450,365))#ボタンクリック
pc=Actor('pc',topleft=(0,0))
pc1=Actor('pc1',center=(100,400))#ボタンクリック
pc2=Actor('pc2',center=(340,400))#ボタンクリック
gouseikabegami=Actor('test(q)',topleft=(0,0))
dekinai1=Actor('dekisouninai',center=(350,100))
dekinai2=Actor('dekisouninai',center=(350,100))
nae=Actor('nae',topleft=(500,70))#キャラクター（主人公）
zetu=Actor('zetu',topleft=(500,70))#キャラクター（主人公）
wara=Actor('wara',topleft=(500,70))#キャラクター（主人公）
saigob=Actor('saigob',topleft=(0,0))
kagi=[Actor('kagi1',topleft=(0,0)),Actor('kagi1',center=(350,100)),Actor('kagi2',center=(350,200)),Actor('kagi3',center=(350,300))]
gousei=[Actor('pc3',topleft=(0,0)),Actor('pc3',topleft=(0,0)),Actor('pc3',topleft=(0,0)),Actor('pc3',topleft=(0,0)),Actor('pc3',topleft=(0,0))
        ,Actor('pc5',topleft=(0,0)),Actor('pc5',topleft=(0,0)),Actor('pc4',topleft=(250,320)),0,0,0,0,0,Actor('gousei',bottomleft=(0,480))]
basyo=[0,0,0,0,0]#○○箇所押したら
kyou=[Actor('kyousitu3',topleft=(0,0)),Actor('kyousitu4',topleft=(0,0)),Actor('kyousitu5',topleft=(0,0)),
      Actor('kyousitu6',topleft=(0,0)),Actor('syoukou',topleft=(0,0)),Actor('kyousitu7',topleft=(0,0)),Actor('kyousitu0',topleft=(0,0)),Actor('kyousitu-2',topleft=(0,0))]

sakuma=[Actor('hi14',topleft=(20,40)),Actor('hi15',topleft=(20,40)),Actor('hi16',topleft=(20,40)),
        Actor('hi17',topleft=(20,40)),Actor('hi18',topleft=(20,40)),Actor('hi19',topleft=(20,40)),
        Actor('hi20',topleft=(20,40)),Actor('hi21',topleft=(20,40)),Actor('hi22',topleft=(20,40))]

enogu=[Actor('kyousitu-1',topleft=(0,0)),Actor('kyousitu-1(2)',topleft=(0,0)),Actor('kyousitu-1(3)',topleft=(0,0)),
       
       Actor('kyousitu-1(4)',topleft=(0,0)),Actor('kyousitu-1(5)',topleft=(0,0)),Actor('kyousitu-1(6)',topleft=(0,0)),Actor('kyousitu-1(7)',topleft=(0,0))]
hito=[Actor('hito0',topleft=(20,40)),Actor('hito1',topleft=(20,40)),Actor('hito2',topleft=(20,40)),
      Actor('hito3',topleft=(20,40)),Actor('hito4',topleft=(20,40)),Actor('hito5',topleft=(20,40)),Actor('hito6',topleft=(20,40)),Actor('hito7',topleft=(20,40)),
      Actor('hito8',topleft=(20,40)),Actor('hito9',topleft=(20,40)),Actor('hito10',topleft=(20,40)),Actor('hito11',topleft=(20,40))]

hirou=[0,Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),
       Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),Actor('item1'),]
       
heya=[Actor('0-3',topleft=(0,0)),Actor('0-3-2',topleft=(0,0)),Actor('0-4',topleft=(0,0)),Actor('0-4-2',topleft=(0,0)),Actor('3f-2',topleft=(0,0)),Actor('4f-2',topleft=(0,0)),
      Actor('3f-1',topleft=(0,0)),Actor('4f-1',topleft=(0,0)),Actor('1f-1',topleft=(0,0)),Actor('3f1',topleft=(0,0)),Actor('4f1',topleft=(0,0)),Actor('1f2',topleft=(0,0)),
      Actor('3f2',topleft=(0,0)),Actor('4f2',topleft=(0,0)),Actor('1f3',topleft=(0,0)),Actor('3f3',topleft=(0,0)),Actor('4f3',topleft=(0,0)),Actor('4',topleft=(0,0)),
      Actor('5',topleft=(0,0)),Actor('-5-1',topleft=(0,0)),Actor('-5-2',topleft=(0,0)),Actor('-5-4',topleft=(0,0)),Actor('-6-4',topleft=(0,0)),Actor('7',topleft=(0,0)),
      Actor('7-2',topleft=(0,0)),Actor('7-3',topleft=(0,0)),Actor('7-4',topleft=(0,0)),Actor('9-1',topleft=(0,0)),Actor('9-2',topleft=(0,0)),Actor('9-3',topleft=(0,0)),Actor('9-4',topleft=(0,0))]
pasu=[Actor('rokku1',topleft=(0,0)),Actor('rokku2',topleft=(0,0))]             
reiki=[0,Actor('re1',topleft=(0,0)),Actor('re2',topleft=(0,0)),Actor('re3',topleft=(0,0)),Actor('re4',topleft=(0,0)),Actor('re5',topleft=(0,0))]  
ka=[0,0,"",0,0,0,0,0,0,0,0,0,0,0,0]#0は壁にぶつかってるかぶつかっていないか1はキー入力した値#3は？#4と5はキーボードの文字数指定6はバグ削除789.10,11,12１４階で段追われる
maplist=[Actor('on0',topleft=(0,0)),Actor('on1',topleft=(0,0)),Actor('on2',topleft=(0,0)),
         Actor('on3',topleft=(0,0)),Actor('on4',topleft=(0,0)),Actor('on5',topleft=(0,0)),
         Actor('on6',topleft=(0,0)),Actor('on7',topleft=(0,0)),Actor('on8',topleft=(0,0)),Actor('on9',topleft=(0,0)),
         Actor('on-1',topleft=(0,0)),Actor('on-2',topleft=(0,0)),Actor('on-5',topleft=(0,0)),Actor('on-6',topleft=(0,0)),Actor('on999',topleft=(0,0))]
tekilist=[Actor('kabann',topleft=(300,350)),Actor('teki',topleft=(0,0)),Actor('teki',topleft=(0,0)),
         Actor('teki',topleft=(0,0)),Actor('teki',topleft=(0,0)),Actor('obake',topleft=(0,0)),]
tai=[Actor('tai0',topleft=(0,0)),Actor('tai1',topleft=(0,0)),Actor('tai2',topleft=(0,0)),Actor('tai3',topleft=(0,0)),Actor('tai4',topleft=(0,0))]
items=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#セーブストッパー２
stop1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#セーブストッパー２
stop2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#セーブストッパー２
stop3=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#セーブストッパー２
stop4=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#セーブストッパー２
serihu=[0,0,0,0]
reset=[Actor('reset',midbottom=(444,490)),Actor('yes',midbottom=(216,310)),Actor('no',midbottom=(484,310))]
savek=[Actor('a5',topleft=(350,300)),Actor('a5',topleft=(350,300)),Actor('a5',topleft=(350,300)),Actor('a5',topleft=(350,300))]
siinn=[Actor('siinn',bottomleft=(93,472)),Actor('siinn2',topleft=(0,0)),1,Actor('siinn4',topleft=(0,420)),Actor('siinn3',topright=(700,420)),0]
u=[0]
siinn2=[0,Actor('siinn11',topleft=(0,0)),Actor('siinn11-2',topleft=(0,0)),Actor('siinn12',topleft=(0,0)),Actor('siinn12-2',topleft=(0,0)),Actor('siinn13',topleft=(0,0))
        ,Actor('siinn13-2',topleft=(0,0)),Actor('siinn14',topleft=(0,0)),Actor('siinn14-2',topleft=(0,0)),Actor('siinn15',topleft=(0,0)),Actor('siinn15-2',topleft=(0,0))
        ,Actor('siinn16',topleft=(0,0)),Actor('siinn16-2',topleft=(0,0)),Actor('siinn17',topleft=(0,0)),Actor('siinn17-2',topleft=(0,0)),Actor('siinn18',topleft=(0,0))
        ,Actor('siinn18-2',topleft=(0,0)),Actor('siinn19',topleft=(0,0)),Actor('siinn19-2',topleft=(0,0)),Actor('siinn20',topleft=(0,0)),Actor('siinn20-2',topleft=(0,0))]
map_data=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#体育館2F
          [1,0,0,0,0,1,0,0,0,0,1,0,3,0,1],
          [1,0,1,1,0,0,0,1,0,1,0,1,1,0,1],
          [1,0,1,1,1,1,0,1,0,0,0,0,0,0,1],
          [1,0,1,0,0,0,1,1,0,1,1,0,1,0,1],
          [1,0,0,1,0,0,1,0,1,0,1,1,1,0,6],
          [1,1,0,1,1,0,0,0,1,0,1,0,1,0,1],
          [1,0,0,1,0,1,1,0,0,0,1,0,0,0,1],
          [1,0,1,1,0,0,1,0,1,1,0,0,1,0,1],
          [1,0,0,1,0,1,0,0,1,0,0,1,0,0,1],
          [1,1,0,1,0,1,0,1,0,1,0,0,0,1,1],
          [1,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [1,0,1,7,1,1,0,1,0,1,1,0,1,1,1],
          [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
          [1,1,1,1,5,1,1,4,1,1,1,1,1,1,1]]

map_end1=[[-1,1,4,1,4,1,4,1,4,1,5,1,4,1,1],#最後のところ
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,0,0,1,1,0,1,1,0,1,0,1],
          [1,0,0,1,0,0,1,0,1,0,1,1,1,0,1],
          [1,1,0,1,1,0,0,0,1,0,1,0,1,0,1],
          [1,0,0,1,0,1,1,0,0,0,1,0,0,0,1],
          [1,0,1,1,0,0,1,0,1,1,0,0,1,0,1],
          [1,0,0,1,0,1,0,0,1,0,0,1,0,0,1],
          [1,1,0,1,0,1,0,1,0,1,0,0,0,1,1],
          [1,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [1,0,1,0,1,1,0,1,0,1,1,0,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_data9=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#体育館=1F
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,0,0,3,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,6],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,7,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,5,1,1,4,1,1,1,1,1,1,1]]
map_data10=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#体育館=3F
          [1,7,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,1,1,1,1,3,1,1,1,1,0,0,1],
          [1,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,6],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,1,1,1,1,1,1,1,1,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,5,1,1,4,1,1,1,1,1,1,1]]
map_data12=[[-1,1,1,1,1,1,1,8,1,1,1,1,1,1,1],#体育館=4F
          [1,0,0,1,0,0,0,0,0,0,1,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,9,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,6],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
          [1,0,0,1,0,0,1,7,1,0,0,1,0,0,1],
          [1,0,0,1,1,1,1,3,1,1,1,1,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,5,1,1,4,1,1,1,1,1,1,1]]

map_data3=[[-1,1,1,1,1,4,1],#渡り廊下
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1], 
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,1,1,3,1,1,1]]

map_end2=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#最後のところ２
           [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1],
           [1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1],
           [1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,1],
           [1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,3],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_data4=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#渡り廊下
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
           [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
           [6,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1],
           [5,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
           [1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1]]

map_data5=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#図書館
           [1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
           [4,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1],
           [1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1],
           [1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,5,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,3],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_data6=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#服飾
           [1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
           [4,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,3],
           [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
           [1,0,0,0,0,0,0,0,0,5,1,6,1,0,1,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_data7=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#総合ビジネス
           [1,0,0,0,0,0,0,0,0,0,1,6,5,0,1,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1],
           [1,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1],
           [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1],
           [4,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,3],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
map_data8=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
           [1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1],
           [1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1],
           [1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_end3=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#最後3
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map0_data=[[-1,1,1,1,1,1,1,1,1,1,1,1,1,1],#最後の部屋
           [3,0,0,0,5,0,0,0,0,0,0,0,4,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
map_data11=[[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]]
map2_data=[[-10,-39,-38,-37,-36,-35,-34,-33,-32,-31],#体躯倉庫１
           [-11,11,12,13,14,15,16,17,18,-30],
           [-12,21,22,23,24,25,26,27,28,-29],
           [-13,31,32,33,34,35,36,37,38,-28],
           [-14,41,42,43,44,45,46,47,48,-27],
           [-15,51,52,53,54,55,56,57,58,-26],
           [-16,-17,-18,-19,-20,-21,-22,-23,-24,-25]]
sgyara=[Actor('sgyara',bottomright=(690,315)),Actor('sgyara1',topleft=(0,0)),Actor('sgyara2',topleft=(0,0)),Actor('sgyara3',topleft=(0,0)),Actor('sgyara4',topleft=(0,0)),0,0]
kgyara=[Actor('kgyara',bottomright=(690,381)),Actor('kgyara1',topleft=(0,0)),Actor('kgyara2',topleft=(0,0)),Actor('kgyara3',topleft=(0,0)),Actor('kgyara4',topleft=(0,0)),Actor('kgyara5',topleft=(0,0)),0,Actor('gyarariinimodoru',topleft=(500,0)),Actor('kgyara6',topleft=(0,0))]#6でどこまで出てきたか
lim=[Actor('obake'),0,0,0]#３でお化け出ないようにするストッパー
owari=Actor('owari',topleft=(0,0))
tgyara=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pgyara=[0,0,0,0]
#on[0]=0
with open("save1.txt","r") as file:
     save1=[line.strip() for line in file]
with open("save11.txt","r") as file:
     save11=[line.strip() for line in file]
with open("save2.txt","r") as file:
     save2=[line.strip() for line in file]
with open("save22.txt","r") as file:
     save22=[line.strip() for line in file]
with open("save3.txt","r") as file:
     save3=[line.strip() for line in file]
with open("save33.txt","r") as file:
     save33=[line.strip() for line in file]
with open("save4.txt","r") as file:
     save4=[line.strip() for line in file]
with open("save44.txt","r") as file:
     save44=[line.strip() for line in file]

with open("stop1.txt","r") as file:
     stopp=[line.strip() for line in file]
     for ttt in range(26):
          stop1[ttt]=int(stopp[ttt])
with open("stop2.txt","r") as file:
     stopp=[line.strip() for line in file]
     for ttt in range(26):
          stop2[ttt]=int(stopp[ttt])
with open("stop3.txt","r") as file:
     stopp=[line.strip() for line in file]
     for ttt in range(26):
          stop3[ttt]=int(stopp[ttt])
with open("stop4.txt","r") as file:
     stopp=[line.strip() for line in file]
     for ttt in range(26):
          stop4[ttt]=int(stopp[ttt])


with open("item.txt","r") as file:#複数読み込む
     tgyara=[line.strip() for line in file]
gyara[0]=int(tgyara[0])
gyara[1]=int(tgyara[1])
gyara[2]=int(tgyara[2])
gyara[3]=int(tgyara[3])
gyara[4]=int(tgyara[4])
gyara[5]=int(tgyara[5])
gyara[6]=int(tgyara[6])
gyara[7]=int(tgyara[7])
gyara[8]=int(tgyara[8])
gyara[9]=int(tgyara[9])
gyara[10]=int(tgyara[10])
gyara[11]=int(tgyara[11])
gyara[12]=int(tgyara[12])
gyara[13]=int(tgyara[13])
gyara[14]=int(tgyara[14])
gyara[15]=int(tgyara[15])
gyara[16]=int(tgyara[16])
gyara[17]=int(tgyara[17])
gyara[18]=int(tgyara[18])
gyara[19]=int(tgyara[19])
gyara[20]=int(tgyara[20])
gyara[21]=int(tgyara[21])
gyara[22]=int(tgyara[22])
gyara[23]=int(tgyara[23])
gyara[24]=int(tgyara[24])
gyara[25]=int(tgyara[25]) 
with open("game.txt","r") as file:#複数読み込む
     pgyara[0]=file.readline()
sgyara[6]=int(pgyara[0])
with open("kyara.txt","r") as file:#一つ読み込む
     pgyara[1]=file.readline()
kgyara[6]=int(pgyara[1])
with open("story.txt","r") as file:#一つ読み込む
     pgyara[2]=file.readline()
siinn2[0]=int(pgyara[2])
with open("time.txt","r") as file:#一つ読み込む
     pgyara[3]=file.readline()
iii[2]=int(pgyara[3])
#on[2]=7
#data[2]=11
#on[4]=2
#item[2]=1
#item[3]=1
#奈々子
#item[5]=0
#gyara[1]=1
#gyara[2]=1
#gyara[3]=1
#gyara[4]=1
#kgyara[0]=2
#on[2]=0
#item[2]=1
#item[3]=1
#item[16]=1
#on[4]=1#1階

#音葉
#ii[17]=4
#ii[18]=5
#ii[19]=6
#ii[20]=8
#ii[21]=9
#i[4]=30
#data[2]=8
#on[4]=2
#on[2]=8


#on[2]=-1
#海斗
#on[3]=14

#on[4]=4
#on[3]=15

#item[1]=0
#item[2]=1
#item[3]=1
#item[4]=0
#item[5]=1
#data[2]=13
#on[2]=-2
#on[4]=1
##on[2]=8
#on[4]=2
#data[2]=10
#3階から
#item[2]=1
#item[3]=1
#data[2]=24
#on[4]=3
#on[2]=1
#on[2]=2
#data[2]=8
#on[0]=0
#on[4]=1
#on[2]=1
#item[11]=1
#item[2]=1
#item[3]=1
#data[2]=37

ending=[Actor('ending',topleft=(0,0)),0]
tyuuto=[Actor('tyuuto',bottomleft=(45,465)),Actor('tyuutoriarumap',topleft=(0,0))]
ninngenn=[Actor('ninngenn',topleft=(400,-100)),Actor('ninngenn2',topleft=(400,0)),Actor('tk1',topleft=(400,-50))
          ,Actor('tk3',topleft=(300,0)),Actor('tk5',topleft=(300,0)),Actor('tk6',topleft=(300,0)),Actor('tk7',topleft=(300,0)),Actor('tk2',topleft=(400,-50))]
sakuma2=[Actor('sakuma',topleft=(500,40)),Actor('sakuma1',topleft=(500,40)),Actor('sakuma2',topleft=(500,40)),Actor('sakuma3',topleft=(500,40)),Actor('sakuma4',topleft=(500,40)),Actor('sakuma5',topleft=(500,40)),0]
kotarou=[Actor('kotarou',topleft=(20,20)),Actor('kotarou1',topleft=(20,20)),Actor('kotarou2',topleft=(20,20)),Actor('kotarou3',topleft=(20,20)),Actor('kotarou4',topleft=(20,20)),Actor('kotarou5',topleft=(20,20)),Actor('kotarou6',topleft=(20,20)),Actor('kotarou7',topleft=(20,20))]
                                                                                                                 
hinnto=[Actor('hinnto0',topleft=(200,250)),Actor('hinnto1',topleft=(200,250)),Actor('hinnto2',topleft=(200,250)),
        Actor('hinnto-2',topleft=(200,250)),Actor('hinnto-1',topleft=(200,250)),Actor('hinnto-5',topleft=(200,250)),
        Actor('hinnto-6',topleft=(200,250)),Actor('hinnto7',topleft=(200,250)),Actor('hinnto8',topleft=(200,250)),]
item2=[0,Actor('item0',topleft=(0,0)),Actor('item2',topleft=(0,0)),0,Actor('item4',topleft=(0,0)),Actor('item5',topleft=(0,0)),
         Actor('item6',topleft=(0,0)),Actor('item7',topleft=(0,0)),Actor('item8',topleft=(0,0)),Actor('item9',topleft=(0,0)),
         Actor('item10',topleft=(0,0)),Actor('item11',topleft=(0,0)),Actor('item12',topleft=(0,0)),Actor('item13',topleft=(0,0)),0,
         Actor('item15',topleft=(0,0)),0,0,Actor('item18',topleft=(0,0)),0,0]
class k2:
     def __init__(self,a,b,c):
         self.k=Actor('kotarouc',center=(800,200))
         self.x=a
         self.y=b
         self.e=10
         self.i=0
         self.o=c
         if a==430:
             self.k=Actor('kotarouc',center=(800,270))
     def draw(self):
         if self.o<ii[3]<=self.y or self.o==1000:
             self.k.draw()
         if self.x<self.k.x+self.e and ii[3]<=self.y:
             self.k.x-=2
         if on[2]==8 and on[4]==3:
             self.k.x=400
         if on[2]==8 and on[4]==2 and ii[3]==7:
             if self.e>self.i:
                 self.i+=1
                 self.k.x+=3
         if (so[2]==4 or so[2]==6)and on[2]==999:
             self.k.x=430
         if self.o==1000:
             self.k.x=430

class k3:
    def __init__(self,x,c):
         self.k=Actor('otohac',center=(300,200))
         self.y=x
         self.a=c
    def draw(self):
        if self.a<=ii[3]<=self.y:
            self.k.draw()
kotarou7=k2(430,0,1000)
kotarou8=k2(550,20,7)
otohac=k3(28,3)
otohac2=k3(25,5)
otohac3=k3(21,4)
kotarou4=k2(430,29,0)
kotarou5=k2(430,8,0)
kotarou6=k2(430,23,11)
kotarou3=k2(400,21,2)
kotarou2=k2(400,25,4)
kotarou1=k2(400,24,3)
class k4:
    def __init__(self):
         self.nanako=Actor('nanakoc',center=(367,270))
         self.kaito=Actor('kaitoc',center=(367,130))
    def draw(self):
        if 6<=ii[3]<=33:
             self.nanako.draw()
             self.kaito.draw()
kaitonanako=k4()
class k:
    def __init__(self,a):
        self.t=a
        if a==300:
            self.k=Actor('otohac',center=(-100,a))
        if a==650:
            self.k=Actor('nanakoc',center=(350,a))
        if a==-60:
            self.k=Actor('kaitoc',center=(480,a))
    def draw(self):
        if self.t==300:
            if on[2]==2:
                if 21>ii[3]>2:
                    if self.k.x<150:
                        self.k.x+=2
                else:
                    if self.k.x>-100:
                        self.k.x-=2
            if on[2]==-1:
                self.k.y=155
                if 18>ii[3]>1:
                    if self.k.x<480:
                        self.k.x+=2
                else:
                    if self.k.x>-100:
                        self.k.x-=3
            if on[2]==8:
                self.k.y=300
                if 46>ii[3]>4:
                    if self.k.x<290:
                        self.k.x+=2
                else:
                    if self.k.x>-100:
                        self.k.x-=3
            if on[2]==999:
                self.k.y=330
                if self.k.x<290:
                        self.k.x+=2
        if self.t==650:
            if self.k.y>400:
                self.k.y-=2
        if self.t==-60:
            if 35>ii[3]>4:
                if self.k.y<250:
                    self.k.y+=2
            else:
                if self.k.y>-100:
                    self.k.y-=2
        self.k.draw()
            
k1=k(300)#音葉
k2=k(650)#奈々子
k3=k(-60)#海斗
v=[0]#最後のラストシーン用のストッパー変数
class hyouzi:
    def __init__(self,a):
        self.txt=a
    def draw(self):
        screen.draw.text(self.txt,(320,300),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=60)
listkey=[hyouzi("A"),hyouzi("B"),hyouzi("C"),hyouzi("D"),hyouzi("E"),hyouzi("F"),hyouzi("G"),hyouzi("H"),hyouzi("I"),hyouzi("J"),hyouzi("K")
        ,hyouzi("L"),hyouzi("M"),hyouzi("N"),hyouzi("O"),hyouzi("P"),hyouzi("Q"),hyouzi("R"),hyouzi("S"),hyouzi("T"),hyouzi("U")
        ,hyouzi("V"),hyouzi("W"),hyouzi("X"),hyouzi("Y"),hyouzi("Z")]
class hyouzi2:
    def __init__(self):
        self.akai=Actor('eee',center=(350,240))#視界エフェクト
        self.akai2=Actor('eee',center=(350,240))#視界エフェクト
        self.v=0
        self.g=1
    def draw(self):
        self.v+=1
        self.akai2.draw()
        if self.v%30==0:
            self.g=self.g*-1
        if self.g<0 and (on[1]==0 or 3<on[1]<8):
            self.akai.draw()
            screen.draw.text("マップの移動を繰り返せば\n巻くことが可能!",(0,20),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
hyouzi2=hyouzi2()
class game:
    def __init__(self,a):
        self.i=a
        self.h=[Actor('a3(1)',center=(350,150)),Actor('a33(1)',center=(350,150)),Actor('a3(1)',center=(350,150)),Actor('a333(1)',center=(350,150))]
        self.r=[Actor('a4(1)',center=(350,150)),Actor('a44(1)',center=(350,150)),Actor('a4(1)',center=(350,150)),Actor('a444(1)',center=(350,150))]
        self.a5=Actor('a5(1)',center=(350,150))
        self.heya=[Actor('heya1',topleft=(0,-150)),Actor('heya2',topleft=(320,-150)),Actor('heya3',topright=(380,-150))
                   ,Actor('heya4',topleft=(320,-150)),Actor('heya5',topright=(380,-150)),Actor('heya6',topleft=(320,-150))]
        self.doa=[Actor('kabe2'),Actor('kabe2'),0]#いき０戻り１アドレス2
        self.w=a
        self.ww=a
        self.back=[Actor('game',topleft=(0,-150)),Actor('sikai',center=(450,365-100))]
        self.time=[1,100,300]
        self.takara=["ない","ない","ない","ない",4]
        self.reba=[Actor('botann'),Actor('botann'),0,0,0,0,Actor('takara')]
        self.mini=Actor('minigame',topleft=(0,-150))
    def draw(self):
        if  on[1]==14:
            self.back[0].draw()
            self.doa[0].draw()
            self.doa[1].draw()
            self.heya[self.doa[2]].draw()
            if self.doa[2]==0:#ボタンを押す
                if self.reba[2]==1:#
                    self.reba[6].topright=self.heya[0].midright
                    self.reba[6].x=self.heya[0].x-100
                    self.reba[6].draw()
                    if self.reba[6].colliderect(self.a5)and self.takara[3]=="ない":
                        screen.draw.text("\n\n\n[Dキーで宝を取る]",(0,20),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="YELLOW",fontsize=20)#
                    if keyboard.d and self.reba[6].colliderect(self.a5):
                            self.takara[3]="a"
                            self.reba[2]=0
                            sounds.koukaonn1.play()
            if self.doa[2]==1:#ボタンを押す
                self.reba[0].topleft=self.heya[1].center
                self.reba[0].draw()
                if self.reba[0].colliderect(self.a5)and keyboard.d and self.i==30 and self.takara[4]!=0:#ボタンを押す
                     self.reba[5]=1
                     self.i=0
                     sounds.koukaonn7.play()
            if self.doa[2]==2:#ボタンを押す
                self.reba[0].center=self.heya[2].center
                self.reba[0].draw()
                if self.reba[0].colliderect(self.a5)and keyboard.d and self.i==30 and self.takara[4]!=0:#ボタンを押す
                     self.reba[3]=1
                     self.i=0
                     sounds.koukaonn7.play()
            if self.doa[2]==3:
                if self.reba[4]==1:#
                    self.reba[6].topright=self.heya[3].center
                    self.reba[6].x=self.heya[3].x-200
                    self.reba[6].draw()
                    if self.reba[6].colliderect(self.a5)and self.takara[1]=="ない":
                        screen.draw.text("\n\n\n[Dキーで宝を取る]",(0,20),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="YELLOW",fontsize=20)#
                    if keyboard.d and self.reba[6].colliderect(self.a5):
                            self.takara[1]="a"
                            self.reba[4]=0
                            sounds.koukaonn1.play()
            if self.doa[2]==4:#ボタンを押す
                self.reba[0].center=self.heya[4].center
                self.reba[0].draw()
                if self.reba[0].colliderect(self.a5)and keyboard.d and self.i==30 and self.takara[4]!=0:#ボタンを押す
                     self.reba[4]=1#
                     self.i=0
                     sounds.koukaonn7.play()
                if self.reba[3]==1:
                        self.reba[6].topright=self.heya[4].center
                        self.reba[6].x=self.heya[4].x-200
                        self.reba[6].draw()
                        if self.reba[6].colliderect(self.a5)and self.takara[2]=="ない":
                            screen.draw.text("\n\n\n[Dキーで宝を取る]",(0,20),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="YELLOW",fontsize=20)#
                        if keyboard.d and self.reba[6].colliderect(self.a5):
                            self.takara[2]="a"
                            self.reba[3]=0
                            sounds.koukaonn1.play()
            if self.doa[2]==5:
                self.reba[0].center=self.heya[5].center
                self.reba[0].draw()
                if self.reba[0].colliderect(self.a5)and keyboard.d and self.i==30 and self.takara[4]!=0:#ボタンを押す
                     self.reba[2]=1
                     self.i=0
                     sounds.koukaonn7.play()
                if self.reba[5]==1:#
                        self.reba[6].topright=self.heya[5].center
                        self.reba[6].x=self.heya[5].x-200
                        self.reba[6].draw()
                        if self.reba[6].colliderect(self.a5)and self.takara[0]=="ない":
                            screen.draw.text("\n\n\n[Dキーで宝を取る]",(0,20),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="YELLOW",fontsize=20)#
                        if keyboard.d and self.reba[6].colliderect(self.a5):
                            self.takara[0]="a"
                            sounds.koukaonn1.play()
                            self.reba[5]=0
            if keyboard.right:
               self.r[self.ww].draw()
               self.heya[self.doa[2]].x-=3
               if self.doa[0].x<self.a5.x and self.doa[1].x<self.a5.x:
                   self.heya[self.doa[2]].x+=3
            if keyboard.left: 
               self.h[self.ww].draw()
               self.heya[self.doa[2]].x+=3
               if self.doa[0].x>self.a5.x and self.doa[1].x>self.a5.x:
                   self.heya[self.doa[2]].x-=3
            if (not (keyboard.right or keyboard.left))or (keyboard.right and keyboard.left):
                self.a5.draw()
            self.back[1].draw()
            if self.reba[0].colliderect(self.a5):
                screen.draw.text("\n\n\n[Dキーでボタンを押す]",(0,20),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="YELLOW",fontsize=20)#
            if self.doa[0].colliderect(self.a5)or self.doa[1].colliderect(self.a5):
                screen.draw.text("\n\n\n[Dキーで扉の先へ行く]",(0,20),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="YELLOW",fontsize=20)#
            if self.doa[2]==0:
                screen.draw.text("場所：暗黙の廊下",(0,20),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)#部屋のアド
            if self.doa[2]==1:
                screen.draw.text("場所：学校の廊下",(0,20),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)#部屋のアド
            if self.doa[2]==2:
                screen.draw.text("場所：屋敷の廊下",(0,20),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)#部屋のアド
            if self.doa[2]==3:
                screen.draw.text("場所：牢屋の廊下",(0,20),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)#部屋のアド
            if self.doa[2]==4:
                screen.draw.text("場所：森の廊下",(0,20),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)#部屋のアド
            if self.doa[2]==5:
                screen.draw.text("場所：城の廊下",(0,20),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)#部屋のアド
            screen.draw.text("残り時間"+str( self.time[1])+"秒",(self.time[2],20),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30,gcolor="GREEN")#タイム
            if  self.time[1]<30:
                screen.draw.text("残り時間"+str( self.time[1])+"秒",(self.time[2],20),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)#タイム
            screen.draw.text("┌--ー宝ー--┐\n"+"  宝①→"+self.takara[0]+"\n  宝②→"+self.takara[1]+"\n  宝③→"+self.takara[2]+"\n  宝④→"+self.takara[3]+"\n└--ー--ー--┘",(540,20),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=23)
            if  self.takara[0]=="a":#見つけて手に取ったらaを入れる
                 self.takara[4]-=1
                 self.takara[0]="ある"
            if  self.takara[1]=="a":#見つけて手に取ったらaを入れる
                 self.takara[4]-=1
                 self.takara[1]="ある"
            if  self.takara[2]=="a":#見つけて手に取ったらaを入れる
                 self.takara[4]-=1
                 self.takara[2]="ある"
            if  self.takara[3]=="a":#見つけて手に取ったらaを入れる
                 self.takara[4]-=1
                 self.takara[3]="ある"
            screen.draw.text("宝の残り"+str( self.takara[4])+"個",(550,150),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",gcolor="WHITE",fontsize=25)#
            screen.draw.text("↑ーーーミニゲームプレイ中ーーー↑",(5,380),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=40)
            screen.draw.text("          Aキーでミニゲーム途中終了",(10,430),fontname='a.ttc',owidth=0.3,color="ORANGE",fontsize=30)
            screen.draw.text("ミニゲームクリア条件(時間内に4つお宝を見つけよう)",(0,270),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=26)
            screen.draw.text("※矢印キーでプレイヤーを操作(今回は横移動のみ)",(0,295),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
            if self.takara[4]==0:
                self.mini.draw()
                screen.draw.text("ゲームが自動で終了するまで残り"+str( self.time[1])+"秒",(self.time[2]-200,20),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30,gcolor="GREEN")#タイム
                if  self.time[1]<30:
                    screen.draw.text("ゲームが自動で終了するまで残り"+str( self.time[1])+"秒",(self.time[2]-200,20),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)#タイム
            screen.draw.text("===================================",(0,-10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("=============================GAME==",(0,305),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("                             GAME",(0,305),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="ORANGE",fontsize=40)

    def update(self):
        if  on[1]==14:
            if self.time[0]%60==0:
                self.time[1]-=1
                if on[1]==14:
                    sounds.koukaonn4.play()
                self.time[2]=320
            self.time[0]+=1
            if self.time[2]>300:
                self.time[2]-=1
            if self.doa[2]%2==0:
                self.doa[0].midleft=self.heya[self.doa[2]].midleft
                self.doa[1].midright=self.heya[self.doa[2]].midright
            if self.doa[2]%2==1 or self.doa[2]%2==-1:
                self.doa[1].midleft=self.heya[self.doa[2]].midleft
                self.doa[0].midright=self.heya[self.doa[2]].midright
            if self.doa[2]==0:#最大最小のときは扉出さない！！！
                self.doa[1].y=10000
            if self.doa[2]==5:
                self.doa[0].y=10000
            if self.i<30:
                self.i+=1
            if self.doa[0].colliderect(self.a5):
                if keyboard.d and self.i==30 and self.takara[4]!=0:
                    self.doa[2]+=1#部屋進む
                    self.i=0
                    sounds.koukaonn1.play()
            if self.doa[1].colliderect(self.a5) and self.takara[4]!=0:
                if keyboard.d and self.i==30:
                    self.doa[2]-=1#部屋戻る
                    self.i=0
                    sounds.koukaonn1.play()
            if (keyboard.right or keyboard.left)and not(keyboard.right and keyboard.left):#押されてる
                self.w+=1
                if self.w%10==0:
                    self.ww+=1#カウント
                    if self.ww==4:
                        self.ww=0
            if not (keyboard.right or keyboard.left):#どっちも押されていない
                self.w=0
                self.ww=0
            if self.time[1]==0 and on[1]==14 or keyboard.a and on[1]==14:
                if  serihu[1]!=1:
                    on[1]=0
                    i[4]=0
                    self.time[1]=100
                if  serihu[1]==1 and self.time[1]<=103:
                    on[0]=6
                    on[1]=0
                    serihu[1]=0
                    serihu[2]=0
                
game=game(0)
class game2:
     def __init__(self,a):
        self.sukoa = 0 #左上に表示されるスコアの値の変数
        self.damtime= 0#ダメージ受けている間か、間じゃないか確認するやつ
        self.dd = []#敵がランダムに出てくれるようにここから敵画像ここから引っ張って来る
        self.gg = []#玉出すための入れ物
        self.g=0 #g=60で割って1秒間に１回球が出てくれるようにしてくれる
        self.kenn = Actor('無題617_20230824200038',topleft=(0,0))#kenn=プレイヤー
        self.daiya2 = Actor('無題617_20230824200119',topleft=(0,0))#kenn=プレイヤー
        self.dame = 6#←HP変数をdameにしHPを１０に
        self.q=0
        self.hai = Actor('botann.png',topleft=(1000,-500))#背景
        self.a=0#ダメージで揺れる
        self.b=0#ダメージで揺れるときの動き
        self.c=1#スピード上げるための変数
        self.d=1#
        self.t=60#　T÷60の秒数ごとに敵が出現
        self.mini=Actor('minigame2',topleft=(0,-150))
     def draw(self):
        if on[1]==15:
            self.mini.draw()
            #screen.fill((70,10,100))##画面の背景の色を調整
            self.hai.draw()
            screen.draw.text("↑ーーーミニゲームプレイ中ーーー↑",(5,380),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=40)
            screen.draw.text("          Aキーでミニゲーム途中終了",(10,430),fontname='a.ttc',owidth=0.3,color="ORANGE",fontsize=30)
            if self.damtime > 0: 
                self.daiya2.y=self.kenn.y
                self.daiya2.x=self.kenn.x 
                self.daiya2.draw()
            else:
                self.kenn.draw()

            for self.i,obj in enumerate(self.dd):#enumerateでojjのFOR文を何個目に取り出したかの数字とセットで出力→「０；とら　１；かめ　２；犬」※iはなくても動く
                obj.draw()
            #    screen.draw.text(str(i),(obj.x,obj.y))#DDから何個目に取り出したかの数（i）の数を出てきた敵のそばに表示
                
            for self.i in self.gg:#ddに入れたTEKIの画像をiに入れる
                self.i.draw()
            if	self.dame>0:
                if self.dame==1:
                    screen.draw.text("HP:"+str(self.dame),(250,20),owidth=1.5,color="RED",fontsize=40)
                else:
                    screen.draw.text("HP:"+str(self.dame),(250,20),owidth=1.5,color="LIGHT BLUE",fontsize=40)
                screen.draw.text("SCORE:"+str(self.sukoa),(0,20),owidth=1.5,color="YELLOW",fontsize=40)#←画像と画像が重なったときにプログラムで下に画像出力された画像が表示されるので、隠れないように下に書いてる
                #                              ↑
                #+strで””の中のSCOREの右に（　　　）内の値を表示してくれる
                screen.draw.text("ミニゲームクリア条件(50隻打ち倒せ)",(355,20),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=20)
                screen.draw.text("※矢印キーで操作：spaceキーで玉発射",(0,295),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
            if self.dame<1 or keyboard.a:
                screen.draw.text("GAME OVER",(100,50),owidth=1.5,color="RED",fontsize=100)
                screen.draw.text("Aでゲーム終了",(350,250),owidth=1.5,color="RED",fontsize=50,fontname='a.ttc')
                if  keyboard.a:
                     if  serihu[1]!=1:
                        on[1]=0
                        i[4]=0
                     if  serihu[1]==1:
                            on[0]=6
                            on[1]=0
                            serihu[1]=0
                            serihu[2]=0
            if self.sukoa >= 50:#スコアが50まで行ったらクリア
                if self.dame>0:
                    screen.draw.text("GAME CLEAR!!!",(70,50),owidth=1.5,color="YELLOW",fontsize=100)
                    screen.draw.text("  パスワードの12～19文字目はBIZINESU",(0,150),owidth=1.5,color="YELLOW",fontsize=35,fontname='a.ttc')
                    screen.draw.text("Aでゲーム終了",(350,250),owidth=1.5,color="YELLOW",fontsize=50,fontname='a.ttc')
                    if  keyboard.a:
                        if  serihu[1]!=1:
                            on[1]=0
                            if data[2]==32:
                                data[2]=33
                        if  serihu[1]==1:
                            on[0]=6
                            on[1]=0
                            serihu[1]=0
                            serihu[2]=0
            screen.draw.text("===================================",(0,-10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("=============================GAME==",(0,305),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("                             GAME",(0,305),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="ORANGE",fontsize=40)
     def update(self):
        if on[1]==15:
            if self.dame>0 and self.sukoa<50:#ddにTEKIの画像入れて右の（）内の座標から表示させる
                if self.g % self.t == 0:     #   　↓　　 ↓ｘ座　　↓ｙ座
                    self.dd.append(Actor('無題617_20230824200100',(WIDTH,random.randrange(230)+50)))
                self.g+= 1
                ##print(g)#←画面外にまだ敵がいるかを確認用、なくてもゲームは動く
                for self.ddd in self.dd:#ddに入っている玉がなくなる までF ORぶんが続く
                    for self.ggg in self.gg:#←②
                        if self.ddd.colliderect(self.ggg):#dddとgggのどれかがぶつかった時
                            self.dd.remove(self.ddd)#removeでぶつかったと玉を配列から消す、消すので画面から消える
                            self.gg.remove(self.ggg)
                            self.sukoa += 1
                            self.d     += 1
                            sounds.koukaonn3.play()
                            break#IF起動したらブレイクが発動する仕組みで②のFOF文に入りなおす※
                for obj in self.dd:
                    if self.kenn.colliderect(obj):#kennとobjがぶつかっているかいないか
                        sounds.koukaonn3.play()
                        if self.damtime==0:#==0でてきにぶつかったときにダメージを受け中でない普通の状態のとき
                            self.dame -= 1                        
                            self.damtime = 60#←これだとダメージ中はダメージ受ける
                        #damtime = 120#ダメージ中もダメージうけない
                if self.damtime > 0:
                    self.damtime -=1
                    self.a=self.a+1
                    if self.a % 5==0:#ダメージ受けたときに揺れる処理
                       self.b+=1
                    if self.b%2==0:
                        self.kenn.y-=3
                    if self.b%2==1:
                        self.kenn.y+=3
                if self.q != 0:
                    self.q=self.q-1
                
                if keyboard.down:
                    if self.kenn.y <280:
                        self.kenn.y +=4
                if keyboard.up:
                    if self.kenn.y >50:
                        self.kenn.y -=4
                if keyboard.left:
                    if self.kenn.x >50:
                        self.kenn.x -=4
                if keyboard.right:
                    if self.kenn.x <645:
                        self.kenn.x +=4
                if self.d % 6 == 0:#もしスコアが5上がったら、敵の移動スピードを+2加速させる
                    self.d=1
                    self.c=self.c+1.5
                if self.sukoa==30:
                    self.t=45
                for obj in self.gg:
                    obj.x +=10

                for obj in self.dd:
                    obj.x -=self.ｃ#敵のスピード
                    if obj.x<0 :#OBJの中の敵が右から左に画面を通りすぎたか判断
                        self.dd.remove(obj)#ラグらないように敵削除
                if self.hai.x>=-500:
                    self.hai.x -=1.75
                if self.hai.x<-500:
                    self.hai.x=1300
      
            if  keyboard.space:
                if self.q==0:#球を０．５秒感覚で連射制限をする
                    self.gg.append(Actor('cc.png',(self.kenn.x+30,self.kenn.y)))
                    sounds.koukaonn4.play()
                    self.q=30
            
class game3:
     def __init__(self,a):
         self.c = Actor('a5(1).png',center=(350,170))#kenn=プレイヤー
         self.map = Actor('minigame3.png',topleft=(0,-200))#kenn=プレイヤー
         self.m = Actor('minigame2',topleft=(0,-150))#kenn=プレイヤー
         self.i=[0,0]
     def draw(self):
         if on[1]==16:
            self.m.draw()
            screen.draw.text("GAME CLEAR!!!",(70,50),owidth=1.5,color="YELLOW",fontsize=100)
            screen.draw.text("  パスワードの5～13文字目はGAMEKURIA",(0,150),owidth=1.5,color="YELLOW",fontsize=35,fontname='a.ttc')
            screen.draw.text("Aでゲーム終了",(350,200),owidth=1.5,color="YELLOW",fontsize=50,fontname='a.ttc')
            self.map.draw()
            for y in range(4):
                for x in range(260):
                    kabe.topleft=((self.map.x)+(70*x),(self.map.y)+(70*y)-20)#←キャラクターが動く場合はm1.はいらない
                    kabe.draw()
                    if map_data11[y][x]==1:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe1.topleft=((self.map.x)+(70*x),(self.map.y)+(70*y)-20)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(self.c):#壁にぶつかったら止まる
                            self.i[1]=1
            self.c.draw()
            if self.i[1]==1:#壁にぶつかったら止まる
                    screen.draw.text("GAME OVER",(70,100),owidth=1.5,color="RED",fontsize=100)
                    screen.draw.text("Aでゲーム終了",(350,200),owidth=1.5,color="RED",fontsize=50,fontname='a.ttc')
            screen.draw.text("start→-----------------------------------------→goal",(0,22),fontname='a.ttc',owidth=0.3,color="ORANGE",gcolor="WHITE",fontsize=25)
            screen.draw.text("↑",(-1*(self.map.x/25),40),fontname='a.ttc',owidth=0.3,color="RED",fontsize=40)
            screen.draw.text("ミニゲームクリア条件(迫ってくる壁を上下に移動して、よけろ)",(0,270),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=20)
            screen.draw.text("※矢印キーでジャンプ(今回は上下↑↓のみ)",(0,295),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
            screen.draw.text("===================================",(0,-10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("=============================GAME==",(0,305),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("                             GAME",(0,305),fontname='a.ttc',owidth=0.3,color="WHITE",gcolor="ORANGE",fontsize=40)
            screen.draw.text("↑ーーーミニゲームプレイ中ーーー↑",(5,380),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=40)
            screen.draw.text("          Aキーでミニゲーム途中終了",(10,430),fontname='a.ttc',owidth=0.3,color="ORANGE",fontsize=30)
     def update(self):
         if on[1]==16 and self.i[1]==0:
             self.map.x-=5
             if self.i[0]==0:
                 if keyboard.up:
                     self.i[0]=60
                     sounds.koukaonn2.play()
                 if keyboard.down:
                     self.i[0]=-60
                     sounds.koukaonn2.play()
             if self.i[0]>0:
                 self.i[0]-=1
                 if self.i[0]>=30:
                     self.c.y-=4
                 if self.i[0]<30:
                     self.c.y+=4
             if self.i[0]<0:
                 self.i[0]+=1
                 if self.i[0]>-30:
                     self.c.y-=4
                 if self.i[0]<=-30:
                     self.c.y+=4
         if keyboard.a and on[1]==16:
                 if  serihu[1]!=1:
                     i[4]=0
                     on[1]=0
                 if  serihu[1]==1:
                     on[0]=6
                     on[1]=0
                     serihu[1]=0
                     serihu[2]=0
#def on_key_down(key,unicode):
#    ka[2]+=str(unicode)

game2=game2(0)
game3=game3(0)
class video:
     def __init__(self,a,aw,e,aww,text,iiii,iro):#a初速度#aw画像
         self.c = aw
         self.x=  aw.x
         self.y=  aw.y
         self.v = 0.0
         self.a = a
         self.t = 0.0
         self.g = 9.8
         self.i = 0.0
         self.e=e
         self.muki=-1#うえ向き
         self.asiba=Actor('cc',center=(aw.x,aw.y+40))
         self.aa=30
         self.tobu=aww#ジャンプ画像
         self.ab=[0,0,0,0]
         self.text=text
         self.sai=iiii
         self.iro=iro
     def draw(self):
        if (on[1]==0 or 3<on[1]<8):
            self.ab[0]=self.c.x
            self.ab[1]=self.c.y
            self.ab[2]=self.asiba.x
            self.ab[3]=self.asiba.y
            self.asiba.x+=m1.x
            self.c.x+=m1.x
            self.asiba.y+=m1.y
            self.c.y+=m1.y
            self.tobu.topleft=self.c.topleft#ジャンプ画像
            self.tobu.draw()#ジャンプ画像
            self.c.x=self.ab[0]
            self.c.y=self.ab[1]
            screen.draw.text(self.text,(self.tobu.x-35,self.tobu.y-60),fontname='a.ttc',owidth=0.3,color=self.iro,gcolor="WHITE",fontsize=self.sai)
            self.asiba.x=self.ab[2]
            self.asiba.y=self.ab[3]
     def update(self):
            if self.asiba.colliderect(self.c) and self.e==1 and self.aa==0:
                     self.t= 0.0
                     self.c.center=(self.x,self.y)
                     self.v = 0.0
                     self.i = 0.0
            if self.aa>0 and self.e==1:
                self.aa-=1
            (self.v)=(self.a)-(self.g*self.t)#v=a-gt
            (self.c.y)+=(self.v)*self.muki#v
            self.i+=1.0
            self.t=self.i/60.0
#[初速度(振れ幅),座標,0でジャンプしない１でジャンプする,ジャンプさせるがそう,ジャンプさせる吹き出し,文字のサイズ,色]

#move1=video(6.0,Actor('kabe'),1,Actor('sirusi'),"階段")#テスト
move1=video(6.0,Actor('kabe',topleft=(0,200)),1,Actor('sirusi'),"階段",30,"BLUE")#テスト
item1move=video(5.0,Actor('kabe',topleft=(224,780)),1,Actor('sirusi1'),"どこかの部屋のカギ",20,"LIGHT GREEN")#
item2move=video(5.0,Actor('kabe',topleft=(265,0)),1,Actor('sirusi1'),"\n\n\n     どこかの通路のカギ",20,"LIGHT GREEN")#
item4move=video(5.0,Actor('kabe',topleft=(157,360)),1,Actor('sirusi1'),"メモ帳",20,"LIGHT GREEN")#テスト
item5move=video(5.0,Actor('kabe',topleft=(842,370)),1,Actor('sirusi1'),"\n\n\n     デザイン科のカギ",20,"LIGHT GREEN")#テスト
item6move=video(5.0,Actor('kabe',topleft=(100,70)),1,Actor('sirusi1'),"黄色い\n絵の具",20,"LIGHT GREEN")#テスト
item7move=video(5.0,Actor('kabe',topleft=(294,280)),1,Actor('sirusi1'),"青い絵の具",20,"LIGHT GREEN")#テスト
item8move=video(5.0,Actor('kabe',topleft=(715,500)),1,Actor('sirusi1'),"赤い絵の具",20,"LIGHT GREEN")#テスト
item9move=video(5.0,Actor('kabe',topleft=(190,200)),1,Actor('sirusi1'),"長い棒",20,"LIGHT GREEN")#テスト
item10move=video(5.0,Actor('kabe',topleft=(47,99)),1,Actor('sirusi1'),"懐中電灯",20,"LIGHT GREEN")#テスト
item11move=video(5.0,Actor('kabe',topleft=(50,0)),1,Actor('sirusi1'),"\n\n\n     被覆室のカギ",20,"LIGHT GREEN")#テスト
item12move=video(5.0,Actor('kabe',topleft=(60,140)),1,Actor('sirusi1'),"曲がった棒",20,"LIGHT GREEN")#テスト
item13move=video(5.0,Actor('kabe',topleft=(84,10)),1,Actor('sirusi1'),"ゴミ箱",20,"LIGHT GREEN")#テスト
item15move=video(5.0,Actor('kabe',topleft=(50,0)),1,Actor('sirusi1'),"\n\n\n     ロープ",20,"LIGHT GREEN")#テスト
item18move=video(5.0,Actor('kabe',topleft=(145,200)),1,Actor('sirusi1'),"紫のカギ",20,"LIGHT GREEN")#テスト
class tennmetu:
    def __init__(self):
        self.p=0
    def draw(self):
        if self.p<60:
            self.p+=1
        if self.p>30: 
            screen.draw.text(" Dキーで確かめる",(-15,453),fontname='a.ttc',owidth=6,gcolor="WHITE",color="GREEN",fontsize=25)
        if self.p>=60:
            self.p=0
tennmetu=tennmetu()
def draw():
    if time[1]!=-1:
        if time[0]!=0:
            time[0]-=1
        if time[0]==0:
            time[0]=60
            time[1]-=1
    if tekilist[5].colliderect(c)and on[5]>=0:
            time[1]=0
            on[5]=-1
    if time[1]==0:
        on[1]=10
        so[0]=7
        i[0]=0
        ii[27]=1
        ii[17]=0#暗号リセット
        ii[18]=0#暗号リセット
        ii[19]=0#暗号リセット
        ii[20]=0#暗号リセット
        ii[21]=0#暗号リセット
        ii[3]=0
    screen.clear()
    if i[4]<30:#←どのon[]==1にもかかわってくる
        i[4]+=1
    if i[13]>0:#←どれだけ音止めておくか
        i[13]-=1
    if on[2]!=ii[8]:#マップ移動時のプレイヤーの初期座標設定
        so[0]=2#音
        if on[2]>ii[8]:#移動
         ii[7]=0
        if on[2]<ii[8]:#移動
         ii[7]=2
        ii[8]=on[2]
#チュートリアル###########################
    if data[2]<0:
        if data[2]==-98:
             music[0]=13
        on[2]=-100
        if data[2]==-100 and on[1]!=3:
            on[1]=3
            ii[3]=4
        if -99==data[2]:
            if keyboard.up:
                iii[4]=1
            if keyboard.down:
                iii[5]=1
            if keyboard.left:
                iii[6]=1
            if keyboard.right:
                iii[7]=1
        if iii[4]==1 and iii[5]==1 and iii[6]==1 and iii[7]==1 and i[4]==30 and data[2]==-99:
            on[1]=3
            ii[3]=6
        
#エンドシーン####################################################データ４４～５４の間
    if on[2]==-100:#チュートリアル
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or  map2_data[y][x]==21:#←横壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                    if map2_data[y][x]==-28:#←横壁
                         kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                         kabe3.draw()
                         if kabe3.colliderect(cc):#壁にぶつかったら止まる
                             so[1]=1
                             if data[2]==-98:
                                 on[1]=3
                                 ii[3]=21
                                 c.x-=10

                if map2_data[y][x]==31:#←横壁
                         kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                         kabe4.draw()
                if kabe4.colliderect(cc) and on[1]!=3 and data[2]==-97 and keyboard.d and i[4]==30:
                                 on[1]=3
                                 ii[3]=8
        tyuuto[1].draw()
                                 

    if on[1]!=10:
        if 44<=data[2]<=54:
            music[0]=7
            if siinn2[0]<=19:#ゲームストーリーギャラリー
                    siinn2[0]=20
        if 48==data[2]:
                time[1]=18
        if data[2]==44 or 46==data[2]:
                time[1]=15
        if data[2]==50:
                time[1]=10
        if data[2]==52:
                time[1]=35
        if 54==data[2]:
                time[1]=13
        if 56==data[2]:
                time[1]=-1
        if 44<=data[2]<=45:#指示+逃げる部屋1
            on[2]=100
            if data[2]==44 and on[1]!=3:#初期位置
                    on[1]=3
                    ii[3]=4
                    c.topleft=(550,350)
        if 46<=data[2]<=47:#指示+逃げる部屋2
            on[2]=101
            if data[2]==46 and on[1]!=3:#初期位置
                    on[1]=3
                    ii[3]=1
                    c.topleft=(70,70)
        if 48<=data[2]<=49:#指示+逃げる部屋3
            on[2]=102
            if data[2]==48 and on[1]!=3:#初期位置
                    on[1]=3
                    ii[3]=1
                    c.topleft=(350,300)
                    m1.topleft=(-345,-630)
        if 50<=data[2]<=51:#指示+逃げる部屋4
            on[2]=103
            if data[2]==50 and on[1]!=3:#初期位置
                    on[1]=3
                    ii[3]=1
                    c.topleft=(70,70)
        if 52<=data[2]<=53:#指示+逃げる部屋5
            on[2]=104
            if data[2]==52 and on[1]!=3:#初期位置
                    on[1]=3
                    ii[3]=1
                    m1.topleft=(230,170)
                    c.topleft=(350,300)
                    time[1]=30
        if 54<=data[2]<=55:#指示+逃げる部屋6
            on[2]=105
            if data[2]==54 and on[1]!=3:#初期位置
                    on[1]=3
                    ii[3]=1
                    m1.topleft=(220,230)
                    c.topleft=(350,300)
    if on[2]==100:
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or 42<=map2_data[y][x]<=48 or 21<=map2_data[y][x]<=27:#←横壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if map2_data[y][x]==-11:#←横壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if kabe3.colliderect(cc)and data[2]==45:
                    data[2]=46
                    
    if on[2]==101:
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or (map2_data[y][x]%10==2 and map2_data[y][x]<50)or (map2_data[y][x]%10==7 and 20<map2_data[y][x]<50)or (map2_data[y][x]%10==5 and 10<map2_data[y][x]<30)or 43<=map2_data[y][x]<=46:#←横壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if map2_data[y][x]==-37:#←横壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if kabe3.colliderect(cc)and data[2]==47:
                    data[2]=48
    if on[2]==102:
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(15):
            for x in range(15):
                    kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe.draw()
                    if map_end1[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_end1[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_end1[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                        if kabe4.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1    
                    if kabe3.colliderect(cc)and data[2]==49:
                        data[2]=50
    if on[2]==103:
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or (map2_data[y][x]%10==2 and  not 30<map2_data[y][x]<40)or 23<=map2_data[y][x]<=25 or 43<=map2_data[y][x]<=45 or (map2_data[y][x]%10==7 and map2_data[y][x]<50):#←横壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if map2_data[y][x]==-19 or map2_data[y][x]==-37:#←横壁
                    kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
                if map2_data[y][x]==-32:
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if kabe3.colliderect(cc)and data[2]==51:
                    data[2]=52
    if on[2]==104:
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(8):
            for x in range(25):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map_end2[y][x]==1:#←横壁
                    kabe1.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if map_end2[y][x]==3:#←横壁
                    kabe3.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if kabe3.colliderect(cc)and data[2]==53:
                     data[2]=54
    if on[2]==105:
        lim[3]=1#お化け出ないマップ
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(3):
            for x in range(25):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map_end3[y][x]==1:#←横壁
                    kabe1.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if map_end3[y][x]==3:#←横壁
                    kabe3.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if kabe3.colliderect(cc) and data[2]==55:#クリアしたら起こるシーン１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１１
                         data[2]=56#←クリアシーン
                         on[2]=500
                         v[0]=0#めんどくさくて付け足した変数；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；；
    if on[2]==500:
        if siinn2[0]<=20:#ゲームストーリーギャラリー
                    siinn2[0]=21
        lim[3]=1#お化け出ないマップ
        if v[0]==300:
            on[3]=21
            m1.topleft=(0,0)
        v[0]+=1
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(3):
            for x in range(25):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                if map_end3[y][x]==-1:#←横壁
                    if v[0]>300:
                        owari.topleft=(m1.x+70*x-335,m1.y+70*y-610)#←キャラクターが動く場合はm1.はいらない
                        owari.draw()
        if so[2]==14:
                    ii[4]=1
#エンドシーン####################################################

                         
#on[2]マップ系#0床１壁３～６出口　7黒いスペース
#体育館#######################################
    if on[2]==0:
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==2:
            music[0]=2
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==1:
            music[0]=6
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==3:
            music[0]=10
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(15):
            for x in range(15):
                if on[4]==2:
                    kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe.draw()
                    if map_data[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe6.draw()
                    if map_data[y][x]==7:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe7.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe7.draw()
                    if map_data[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        map1.topleft=(m1.x+70*x,m1.y+70*y)
                        map11.topleft=(m1.x+70*x,m1.y+70*y)
                if on[4]==1:
                    kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe.draw()
                    if map_data9[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data9[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data9[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data9[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data9[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe6.draw()
                    if map_data9[y][x]==7:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe7.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe7.draw()
                    if map_data9[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        kyou[6].topleft=(m1.x+70*x,m1.y+70*y)
                if on[4]==3:
                    kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe.draw()
                    if map_data10[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data10[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data10[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data10[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data10[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe6.draw()
                    if map_data10[y][x]==7:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe7.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe7.draw()
                    if map_data10[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        heya[0].topleft=(m1.x+70*x,m1.y+70*y)
                        heya[1].topleft=(m1.x+70*x,m1.y+70*y)
                if on[4]==4:
                    kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe.draw()
                    if map_data12[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data12[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data12[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data12[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data12[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe6.draw()
                    if map_data12[y][x]==7:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe7.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe7.draw()
                    if map_data12[y][x]==8:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe8.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe8.draw()
                    if map_data12[y][x]==9:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe9.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe9.draw()
                    if map_data12[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        heya[2].topleft=(m1.x+70*x,m1.y+70*y)
                        heya[3].topleft=(m1.x+70*x,m1.y+70*y)
        if on[4]==2:
            map1.draw()#マップデザイン表示
            if data[2]>=5:
                map11.draw()
        #マップ移動↓
        if on[4]==1:
            kyou[6].draw()
        if on[4]==3:
            heya[0].draw()
            if data[2]>=30:
                heya[1].draw()
        if on[4]==4:
            heya[2].draw()
            if data[2]>=40:
                heya[3].draw()
        if kabe4.colliderect(cc):
            if on[4]==2:
                if item[1]==1:
                    on[2]=(on[2]-1)#移動先on[2]==0
                    c.topleft=(70,70)#移動した際のプレイヤーORマップの初期位置
                    lim[3]=0#お化け出る
                if item[1]==0:#鍵持ってないときは押し返される
                    so[1]=1
                    screen.draw.text("カギがかかっていて\n     通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
            if on[4]!=2:
                    on[2]=(on[2]-1)#移動先on[2]==0
                    c.topleft=(70,70)#移動した際のプレイヤーORマップの初期位置
                    lim[3]=0#お化け出る
        if kabe5.colliderect(cc):
             on[2]=(on[2]-2)#移動先
             c.topleft=(560,100)
             m1.topleft=(0,0)
             lim[3]=0#お化け出る"
        if kabe8.colliderect(cc) and data[2]>=42 and on[4]==4:
            on[2]=999#移動先#最後の場所
            m1.topleft=(200,220)
            on[1]=7
            i[4]=0
            lim[3]=1#お化け出ない
        if kabe8.colliderect(cc) and data[2]<42 and on[4]==4:
             so[1]=1
             screen.draw.text("先に本を読んでみよう",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
        if kabe6.colliderect(cc):
            if on[4]==2:
                if item[2]==1 and data[2]>5:
                    on[2]=(on[2]+1)#移動先
                    c.topleft=(70,70)
                    lim[3]=1#お化け出ないマップ
                if item[2]!=1:#鍵持ってないときは押し返される
                    so[1]=1
                    if data[2]>5:
                        screen.draw.text("カギがかかっていて\n     通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
            if on[4]!=2:
                    m1.topleft=(0,0)
                    on[2]=(on[2]+1)#移動先
                    lim[3]=1#お化け出ないマップ
                    c.topleft=(70,70)
        if kabe7.colliderect(cc) and on[4]==4:
            if data[2]<40:
                so[1]=1
                screen.draw.text("ロックがかかっていて\n     通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
        #マップ移動↑
#体育館倉庫１#######################################
    if on[2]==-1:
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==2:
            music[0]=2
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==1:
            music[0]=6
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==3:
            music[0]=10
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or (map2_data[y][x]==18 and (on[4]==1 or on[4]==2)):#←横壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if (map2_data[y][x]>0 and map2_data[y][x]%10==3 and 10<map2_data[y][x]<40 or 36<=map2_data[y][x]<=38)  and (on[4]==1 or on[4]==2):#←縦壁(最後のandは範囲を示す)orのほうは横壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                         so[1]=1
                if map2_data[y][x]==-39:
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if map2_data[y][x]==28:
                    kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe5.draw()
                if map2_data[y][x]==48:
                    kabe6.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe6.draw()
        if on[4]==3:
            heya[6].draw()
        if on[4]==4:
            heya[7].draw()
        if on[4]==1:
            if item[6]==1 and item[7]==0 and item[8]==0:#黄色だけ
               enogu[1].draw()
            if item[6]==1 and item[7]==1 and item[8]==0:#黄色青
               enogu[5].draw()#緑
            if item[6]==0 and item[7]==1 and item[8]==0:#青
               enogu[2].draw()
            if item[6]==0 and item[7]==0 and item[8]==1:#赤
               enogu[0].draw()
            if item[6]==1 and item[7]==0 and item[8]==1:#オレンジ
               enogu[3].draw()
            if item[6]==0 and item[7]==1 and item[8]==1:#紫
               enogu[4].draw()
            if item[6]==0 and item[7]==0 and item[8]==0:#白
               enogu[6].draw()
        if on[4]==2:
             map3.draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=0
            lim[3]=1#お化け出る
            c.topleft=(350,300)
            m1.topleft=(-215,-630)
#最後の場所###########################################################
    if on[2]==999:
        lim[3]=1#お化け出ないマップ
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=0
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(3):
            for x in range(14):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map0_data[y][x]==1:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map0_data[y][x]==3:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if map0_data[y][x]==4:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe4.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
                if map0_data[y][x]==5:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe5.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe5.draw()
                if map0_data[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        saigo.midleft=((m1.x+70*x)+70,(m1.y+70*y)+100)
                        saigob.midleft=((m1.x+70*x)+70,(m1.y+70*y)+100)
        saigo.draw()
        if on[3]==20 and so[2]>=3:
            saigob.draw()
        if kabe3.colliderect(cc):
            on[2]=0
            lim[3]=1#お化け出ない
            c.topleft=(350,300)
            m1.topleft=(-200,200)
            on[1]=5
            i[4]=0
#体育館倉庫2#######################################
    if on[2]==-2:
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==2:
            music[0]=2
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==1:
            music[0]=6
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==3:
            music[0]=10
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if on[4]==2:
                    if map2_data[y][x]==-32:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe3.draw()
                    if map2_data[y][x]==11:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe4.draw()
                    if map2_data[y][x]==14:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
                if on[4]==1:
                    if 22<=map2_data[y][x]<=26:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                    if map2_data[y][x]==-32:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe3.draw()
                    if map2_data[y][x]==12:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe4.draw()
                    if map2_data[y][x]==21:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
                    if map2_data[y][x]==32:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe6.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe6.draw()
                if on[4]==3:
                    if map2_data[y][x]==-32:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe3.draw()
                    if map2_data[y][x]==11:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe4.draw()
                if on[4]==4:
                    if map2_data[y][x]==-32:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe3.draw()
                    if map2_data[y][x]==11:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe4.draw()
        if on[4]==2:
            map2.draw()
        if on[4]==1:
            kyou[7].draw()
        if on[4]==3:
            heya[4].draw()
        if on[4]==4:
            heya[5].draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=0
            lim[3]=1#お化け出ない
            c.topleft=(350,300)
            m1.topleft=(15,-630)
            if on[4]==1 and on[5]>=0:
                m1.topleft=(-45,-630)
#教室#######################################
    if on[2]==99999999999999:
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1から左はいらない
                kabe.draw()
                if map_data[y][x]==1:
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1から左はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                          so[1]=1           
########################################
#食道前廊下#######################################
    if on[2]==1:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==2:
            music[0]=2
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==1:
            music[0]=6
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==3:
            music[0]=10
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-29:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                    if ii[7]==2:
                         c.topleft=(70*x-100,70*y)#右(70*x+100,70*y)　左(70*x-100,70*y)　上(70*x,70*y-100)　下(70*x,70*y+100)
                         ii[7]=1
                if map2_data[y][x]==-15:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
                    if ii[7]==0:
                         c.topleft=(70*x+100,70*y)#右(70*x+100,70*y)　左(70*x-100,70*y)　上(70*x,70*y-100)　下(70*x,70*y+100)
                         ii[7]=1
                if on[4]==2:
                    if map2_data[y][x]==14:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
                    if map2_data[y][x]==11:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe6.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe6.draw()
                    if map2_data[y][x]==27:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe7.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe7.draw()
                    if map2_data[y][x]==17:
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                               so[1]=1
                if on[4]==3:
                    if map2_data[y][x]==21:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                    if map2_data[y][x]==31:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
                if on[4]==4:
                    if map2_data[y][x]==17:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                    if map2_data[y][x]==27:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
        if on[4]==1:
            heya[8].draw()
        if on[4]==3:
            heya[9].draw()
        if on[4]==4:
            heya[10].draw()
        if on[4]==2:
            map4.draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=(on[2]+1)
        if kabe4.colliderect(cc):
            if on[4]!=1:
                on[2]=(on[2]-1)
                c.topleft=(350,300)
                m1.topleft=(-630,-70)
                lim[3]=0#お化け出る
            if on[4]==1 and data[2]>12 and item[5]==1:
                on[2]=(on[2]-1)
                c.topleft=(350,300)
                m1.topleft=(-630,-70)
                lim[3]=0#お化け出る
            if on[4]==1 and (item[5]==0 or data[2]<=12):
                    so[1]=1
                    screen.draw.text("   カギがかかっていて\n        通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
#実習棟廊下①廊下#######################################
    if on[2]==2:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==2:
            music[0]=2
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==1:
            music[0]=6
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==3:
            music[0]=10
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or (map2_data[y][x]==33 and on[4]==2):#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                    if map2_data[y][x]==-28:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe3.draw()
                        if ii[7]==2:
                         c.topleft=(70*x-100,70*y)#右(70*x+100,70*y)　左(70*x-100,70*y)　上(70*x,70*y-100)　下(70*x,70*y+100)
                         ii[7]=1
                    if map2_data[y][x]==-13:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe4.draw()
                        if ii[7]==0:
                         c.topleft=(70*x+100,70*y)#右(70*x+100,70*y)　左(70*x-100,70*y)　上(70*x,70*y-100)　下(70*x,70*y+100)
                         ii[7]=1
                if on[4]==2:#デザイン科前廊下#######################################2階                    
                    if map2_data[y][x]==18:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
                    if map2_data[y][x]==16:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe6.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe6.draw()
                    if map2_data[y][x]==43:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe7.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe7.draw()
        if on[4]==1:
            heya[11].draw()
        if on[4]==3:
            heya[12].draw()
        if on[4]==4:
            heya[13].draw()        
        if on[4]==2:
            map5.draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=(on[2]+1)
            lim[3]=1#お化けない
            c.topleft=(350,300)
            m1.topleft=(-95,-630)
        if kabe4.colliderect(cc):
            lim[3]=0#お化け出る
            on[2]=(on[2]-1)
            c.topleft=(350,300)
            m1.topleft=(-95,-630)
#2階実習棟渡り廊下前#######################################
    if on[2]==3:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==2:
            music[0]=2
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==1:
            music[0]=6
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==3:
            music[0]=10
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-24:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                    if ii[7]==2:
                         c.topleft=(70*x,70*y-100)#右(70*x+100,70*y)　左(70*x-100,70*y)　上(70*x,70*y-100)　下(70*x,70*y+100)
                         ii[7]=1
                if map2_data[y][x]==58:
                    kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe5.draw()                
                if map2_data[y][x]==-13:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
                    if ii[7]==0:
                         c.topleft=(70*x+100,70*y)#右(70*x+100,70*y)　左(70*x-100,70*y)　上(70*x,70*y-100)　下(70*x,70*y+100)
                         ii[7]=1
        #マップ移動↓
        if on[4]==1:
            heya[14].draw()
        if on[4]==3:
            heya[15].draw()
        if on[4]==4:
            heya[16].draw()    
        if on[4]==2:
            map6.draw()
        if kabe3.colliderect(cc) and time[1]==-1:
            if data[2]>=9:
                on[2]=(on[2]+1)
                c.topleft=(350,300)
                m1.topleft=(-50,200)
                lim[3]=1#お化け出ない
            if data[2]<=8:#鍵持ってないときは押し返される
                so[1]=1
                if data[2]==8:
                    screen.draw.text("通れない",(c.x-40,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
        if kabe4.colliderect(cc):
            on[2]=(on[2]-1)
            lim[3]=0#お化け出る
            c.topleft=(350,300)
            m1.topleft=(-95,-630)
#2階渡り廊下#######################################
    if on[2]==4:
        if on[1]!=3 and on[3]==0:
            music[0]=4
        if on[1]!=3 and on[3]==0 and time[1]==-1 and on[4]==4:
            music[0]=8
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(12):
            for x in range(7):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map_data3[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                    kabe1.draw()
                    if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                        so[1]=1              #←壁にぶつかったら止まる時加える２文
                if map_data3[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                    kabe3.draw()
                if map_data3[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                    kabe4.draw()
                if map_data3[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                    heya[17].topleft=(m1.x+70*x,m1.y+70*y)
        #マップ移動↓
        heya[17].draw()
        if kabe3.colliderect(cc) and on[4]!=4:
            on[2]=(on[2]+1)#移動先on[2]==0
            lim[3]=0#お化け出る
            c.topleft=(380,70)#移動した際のプレイヤーORマップの初期位置
        if kabe3.colliderect(cc) and on[4]==4:
            so[1]=1
        if kabe4.colliderect(cc):
            on[2]=(on[2]-1)#移動先
            lim[3]=0#お化け出る
            c.topleft=(70,70)
        #マップ移動↑
#2階本館渡り廊下前#######################################
    if on[2]==5:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-21:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if map2_data[y][x]==-35:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
                if map2_data[y][x]==-30:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe5.draw()
                if map2_data[y][x]==-15:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe6.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe6.draw()
                if map2_data[y][x]==14:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe7.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe7.draw()
        if on[4]==1 or on[4]==3:
            heya[18].draw()
        if on[4]==4:
            murasaki.draw()#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        if on[4]==2:
            kyou[5].draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=(on[2]+1)
            lim[3]=0#お化け出る
            c.topleft=(350,300)
            m1.topleft=(-950,40)
            on[1]=4
            i[4]=0
        if kabe4.colliderect(cc):
            if on[4]!=4:
                lim[3]=0#お化け出る
                on[2]=(on[2]-1)
                m1.topleft=(85,-400)
                c.topleft=(350,300)
            if on[4]==4:
                if item[18]==1:
                 on[2]=(on[2]-1)
                 lim[3]=0#お化け出る
                 m1.topleft=(85,-400)
                 c.topleft=(350,300)
                if item[18]==0:
                    so[1]=1
                    screen.draw.text("カギがかかっていて\n     通れない",(c.x-100,c.y+40),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
        if kabe5.colliderect(cc):
            on[2]=9
            on[1]=6
            i[4]=0
            lim[3]=0#お化け出る
            c.topleft=(550,200)
        if kabe6.colliderect(cc):
            on[2]=(on[2]-on[2]*2)
            m1.topleft=(0,0)
            lim[3]=0#お化け出る
            ii[4]=0
#科学室当たりの教室#######################################
    if on[2]==-5:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        if ii[4]==0:
            c.topleft=(550,350)
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-26:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
               # if on[4]==3:
                   # if map2_data[y][x]==38:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                      #  kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                      #  kabe5.draw()
                if on[4]==3:
                    if map2_data[y][x]>0 and((21<=map2_data[y][x]<=27)or(31<=map2_data[y][x]<=37) or (41<=map2_data[y][x]<=47)):#←縦壁(最後のandは範囲を示す)orのほうは横壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                    if map2_data[y][x]==53:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                            kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                            kabe5.draw()
                if on[4]==1 or on[4]==2:
                    if map2_data[y][x]!=56 and map2_data[y][x]>20 and ((map2_data[y][x]%10==2)or(map2_data[y][x]%10==4)or(map2_data[y][x]%10==6)):#←縦壁(最後のandは範囲を示す)orのほうは横壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
        if on[4]==1:
            heya[19].draw()
        if on[4]==2:
            heya[20].draw()
        if on[4]==4:
            heya[21].draw()
        if on[4]==3:
            kyou[3].draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            lim[3]=0#お化け出る
            on[2]=(on[2]+on[2]*-2)
            c.topleft=(100,350)
#2階廊下#######################################
    if on[2]==6:
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(6):
            for x in range(25):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map_data4[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                    kabe1.draw()
                    if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                        so[1]=1              #←壁にぶつかったら止まる時加える２文
                if map_data4[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                    kabe3.draw()
                if map_data4[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                    kabe4.draw()
                if map_data4[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                    rouka.topleft=(m1.x+70*x,m1.y+70*y)
                    rouka1.topleft=(m1.x+70*x,m1.y+70*y)
                    rouka4.topleft=(m1.x+70*x,m1.y+70*y)
                if map_data4[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                if map_data4[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                if map_data4[y][x]==7:#←←←←←←←←←←←←←マップ種類＆壁
                    kabe7.topleft=(m1.x+70*x,m1.y+70*y)
        rouka.draw()
        if on[4]==1:
            rouka1.draw()
        if on[4]==4:
            rouka4.draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=(on[2]+1)#移動先on[2]==0
            m1.topleft=(0,0)
            c.topleft=(380,70)#移動した際のプレイヤーORマップの初期位置
            lim[3]=0#お化け出る
        if kabe4.colliderect(cc):
            on[2]=(on[2]-1)#移動先
            ii[4]=1
            lim[3]=0#お化け出る
            c.topleft=(380,310)
            on[1]=4
            i[4]=0
        if kabe5.colliderect(cc):
            lim[3]=0#お化け出る
            if data[2]>10:
                 if on[4]==1:
                     so[1]=1
                 if on[4]>1:
                    on[4]=(on[4]-1)#1つ下の階へ
                    m1.topleft=(250,80)
                    on[1]=7
                    i[4]=0
                    so[0]=1
            if data[2]<=10:
                so[1]=1
                screen.draw.text("先に２階を探索しよう",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
        if kabe6.colliderect(cc):
            lim[3]=0#お化け出る
            if data[2]>10:
                if on[4]==4:
                    so[1]=1
                if on[4]<4:
                    on[4]=(on[4]+1)#1つ上の階へ
                    m1.topleft=(250,-10)
                    on[1]=7
                    i[4]=0
                    so[0]=1
            if data[2]<11:
                so[1]=1
                screen.draw.text("先に２階を探索しよう",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
        if kabe7.colliderect(cc):
            lim[3]=0#お化け出る
            if on[4]==1:
                if item[5]==1:
                    on[2]=(on[2]-on[2]*2)
                if item[5]==0:
                    so[1]=1
                    screen.draw.text("カギがかかっていて\n     通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
            c.topleft=(100,350)
            if on[4]!=1:
                m1.topleft=(0,0)
                on[2]=(on[2]-on[2]*2)
#物理室当たりの教室#######################################
    if on[2]==-6:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-15:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe3.draw()
                if on[4]==2 or on[4]==3:
                    if map2_data[y][x]==31:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe4.draw()
                    if map2_data[y][x]==31:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe5.draw()
                    if map2_data[y][x]>0 and (11<=map2_data[y][x]<=17 or 21<=map2_data[y][x]<=27 or 43<=map2_data[y][x]<=47 or 53<=map2_data[y][x]<=57):#←縦壁(最後のandは範囲を示す)orのほうは横壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                if on[4]==1:
                    if map2_data[y][x]>0 and (21<=map2_data[y][x]<=28 and map2_data[y][x]%2==0 or 41<=map2_data[y][x]<=48 and map2_data[y][x]%2==0):#←縦壁(最後のandは範囲を示す)orのほうは横壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                    if map2_data[y][x]==58:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                            kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                            kabe5.draw()
        if on[4]==4:
            heya[22].draw()    
        if on[4]==2:
            kyou[0].draw()
        if on[4]==3:
            kyou[1].draw()
        if on[4]==1:
            kyou[2].draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            lim[3]=0#お化け出る
            m1.topleft=(-1300,200)
            on[2]=(on[2]+on[2]*-2)
            c.topleft=(350,300)
        #マップ移動
#2階本館図書室前#######################################
    if on[2]==7:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-26:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if map2_data[y][x]==-35:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
                if map2_data[y][x]==11:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe5.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe5.draw()
                if on[4]==4:
                    if (map2_data[y][x]%10==6 or map2_data[y][x]%10==7 or map2_data[y][x]%10==8) and map2_data[y][x]<50:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                        kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                        kabe1.draw()
                        if kabe1.colliderect(cc):#壁にぶつかったら止まる
                            so[1]=1
                    

        if on[4]==1:
            heya[23].draw()
        if on[4]==2:
            heya[24].draw()
        if on[4]==3:
            heya[25].draw()
        if on[4]==4:
            heya[26].draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            lim[3]=0#お化け出る
            if on[4]==2:
                on[2]=(on[2]+1)
                c.topleft=(350,300)
            if (on[4]==3 and item[11]==1) or (on[4]==4 and item[17]==1)or on[4]==1:
                on[2]=(on[2]+1)
                c.topleft=(350,300)
            if (on[4]==3 and item[11]==0) or (on[4]==4 and item[17]==0):
                so[1]=1
                screen.draw.text("カギがかかっていて\n     通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
            m1.topleft=(230,120)
            if  on[4]==4:
                    m1.topleft=(230,-150)
            if  on[4]==1:
                    m1.topleft=(230,120)
        if kabe4.colliderect(cc):
            lim[3]=0#お化け出る
            on[2]=(on[2]-1)
            m1.topleft=(150,0)
            c.topleft=(350,300)
#図書室#######################################
    if on[2]==8:
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=0    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(8):
            for x in range(25):
                kabe.topleft=(m1.x+70*x,m1.y+70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if on[4]==2:
                    if map_data5[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data5[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data5[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data5[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data5[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        tosyo.topleft=(m1.x+70*x,m1.y+70*y)
       
                if on[4]==3:
                    if map_data6[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data6[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data6[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data6[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data6[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe6.draw()
                    if map_data6[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        huku.topleft=(m1.x+70*x,m1.y+70*y)
                if on[4]>3:
                    if map_data7[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data7[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data7[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data7[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data7[y][x]==6:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe6.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe6.draw()
                    if map_data7[y][x]==7:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe7.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe7.draw()
                    if map_data7[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        soubi.topleft=(m1.x+70*x,m1.y+70*y)
                        soubi2.topleft=(m1.x+70*x,m1.y+70*y)
                if on[4]<2:
                    if map_data8[y][x]==1:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe1.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe1.draw()
                        if kabe1.colliderect(cc):#←壁にぶつかったら止まる時加える２文
                            so[1]=1              #←壁にぶつかったら止まる時加える２文
                    if map_data8[y][x]==3:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe3.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe3.draw()
                    if map_data8[y][x]==4:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe4.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe4.draw()
                    if map_data8[y][x]==5:#←←←←←←←←←←←←←マップ種類＆壁
                        kabe5.topleft=(m1.x+70*x,m1.y+70*y)
                        kabe5.draw()
                    if map_data8[y][x]==-1:#←←←←←←←←←←←←←マップ種類＆壁
                        kyou[4].topleft=(m1.x+70*x,m1.y+70*y)
        if on[4]==3:
            huku.draw()#部屋
        if on[4]==2:
            tosyo.draw()#部屋
        if on[4]>3:
            soubi.draw()#部屋
        if on[4]<2:
            kyou[4].draw()#部屋 
        #マップ移動↓
        if kabe3.colliderect(cc):
            on[2]=(on[2]+1)#移動先on[2]==0
            c.topleft=(100,270)#移動した際のプレイヤーORマップの初期位置
            lim[3]=0#お化け出る
        if kabe4.colliderect(cc):
            lim[3]=0#お化け出る
            ii[4]=1
            on[2]=(on[2]-1)#移動先
            c.topleft=(540,350)
        #マップ移動
#図書室入り口#######################################
    if on[2]==9:
        m1.topleft=(0,0)
        if on[1]!=3 and on[3]==0 and time[1]==-1:
            music[0]=4
        m1.draw()  #map+そのマップ内の障害物
        ii[4]=1    #動き方0だとマップが動く１だとキャラクターが動く
        for y in range(7):
            for x in range(10):
                kabe.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                kabe.draw()
                if map2_data[y][x]<0 or 21<=map2_data[y][x]<=28:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe1.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe1.draw()
                    if kabe1.colliderect(cc):#壁にぶつかったら止まる
                        so[1]=1
                if map2_data[y][x]==-28:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe3.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe3.draw()
                if map2_data[y][x]==-14:#←←←←←←←←←←←←←←←←←←←←←←←←マップ種類×壁
                    kabe4.topleft=(70*x,70*y)#←キャラクターが動く場合はm1.はいらない
                    kabe4.draw()
        if on[4]==1:
            heya[27].draw()
        if on[4]==2:
            heya[28].draw()
        if on[4]==3:
            heya[29].draw()
        if on[4]==4:
            heya[30].draw()
        #マップ移動↓
        if kabe3.colliderect(cc):
            lim[3]=0#お化け出る
            on[2]=5
            c.topleft=(550,70)
            on[1]=6
            i[4]=0
        if kabe4.colliderect(cc):
            lim[3]=0#お化け出る
            if on[4]==2:#としょしつ
                on[2]=(on[2]-1)
                c.topleft=(350,300)
                m1.topleft=(-1250,-140)
                c.topleft=(350,300)
            if on[4]==1:#昇降口
                on[2]=(on[2]-1)
                c.topleft=(350,300)
                m1.topleft=(-1320,120)
                c.topleft=(350,300)
            if (on[4]==3 and item[11]==1) or (on[4]==4 and item[17]==1):
                c.topleft=(350,300)
                on[2]=(on[2]-1)
                if on[4]==3:
                    c.topleft=(350,300)
                    m1.topleft=(-1330,140)
                if  on[4]==4:
                    m1.topleft=(-1250,-150)
            if (on[4]==3 and item[11]==0) or (on[4]==4 and item[17]==0):
                so[1]=1
                screen.draw.text("   カギがかかっていて\n        通れない",(c.x-100,c.y-70),fontname='a.ttc',owidth=0.3,color="RED",gcolor="ORANGE",fontsize=18)
    if serihu[0]==1 and on[2]==8:
             if on[4]==2:
                 screen.clear()
                 tosyo2.draw()
             if on[4]==3:
                 screen.clear()
                 huku2.draw()
    if -2<=on[2]<=4 and on[4]==4:#お化け出現防ぐストッパー！！
        lim[3]=1
    if -2<=on[2]<=-1 and on[4]==2:#お化け出現防ぐストッパー！！
        lim[3]=1
    if items[6]!=1 and on[2]==-2 and on[4]==1 or serihu[0]==1:#お化け出現防ぐストッパー！！
        lim[3]=1
    if so[1]==1:
        ka[0]+=1
        if on[1]==4:#逆上移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
            if ii[4]==1:
                c.y+=3
            if ii[4]==0:
                m1.y-=3
        if on[1]==5:#逆下移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
            if ii[4]==1:
                c.y-=3
            if ii[4]==0:
                m1.y+=3
        if on[1]==6:#逆左移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
            if ii[4]==1:
                c.x+=3
            if ii[4]==0:
                m1.x-=3
        if on[1]==7:#逆右移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
            if ii[4]==1:
                c.x-=3
            if ii[4]==0:
                m1.x+=3
        so[1]=0
    if ka[0]==3:#ぶつかっているときも敵が近づいてくるように
        ka[0]=0
        if ii[4]==0:
            if tekilist[0].x>c.x:
                tekilist[0].x-=3
            if tekilist[0].x<c.x:
                tekilist[0].x+=3
            if tekilist[0].y>c.y:
                tekilist[0].y-=3
            if tekilist[0].y<c.y:
                tekilist[0].y+=3      
    if 3<=on[1]<=8:#アニメーション・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        if ii[22]<10 or 20<ii[22]<30:
            if on[1]==4:#↑
                c.draw()
            if on[1]==6:#←
                c2.draw()
            if on[1]==7:#→
                c3.draw()
            if on[1]==5:#↓
                c1.draw()
        if 10<=ii[22]<=20:
            if on[1]==4:#↑
                ccc.draw()
            if on[1]==6:#←
                c2c.draw()
            if on[1]==7:#→
                c3c.draw()
            if on[1]==5:#↓
                c1c.draw()
        if ii[22]>=30:
            if on[1]==4:#↑
                cccc.draw()
            if on[1]==6:#←         
                c2cc.draw()
            if on[1]==7:#→
                c3cc.draw()
            if on[1]==5:#↓
                c1cc.draw()
        if ii[4]==1:
            ccc.topleft=c.topleft
            cccc.topleft=c.topleft
            c1.topleft=c.topleft
            c1c.topleft=c.topleft
            c1cc.topleft=c.topleft
            c2.topleft=c.topleft
            c2c.topleft=c.topleft
            c2cc.topleft=c.topleft
            c3.topleft=c.topleft
            c3c.topleft=c.topleft
            c3cc.topleft=c.topleft
        if ii[4]==0:
            c.topleft=(350,300)
            ccc.topleft=(350,300)
            cccc.topleft=(350,300)
            c1.topleft=(350,300)
            c1c.topleft=(350,300)
            c1cc.topleft=(350,300)
            c2.topleft=(350,300)
            c2c.topleft=(350,300)
            c2cc.topleft=(350,300)
            c3.topleft=(350,300)
            c3c.topleft=(350,300)
            c3cc.topleft=(350,300)
        if (on[1]==3 or on[1]==8) and serihu[0]==0:
            c1.draw()
    if on[1]==0 or 3<on[1]<8:
        if i[4]==30:
            ii[22]=0
        if on[1]==0:
            c1.draw()
    if ii[22]<40 and 3<on[1]<8:
        ii[22]+=1
    if ii[22]>=40 and 3<on[1]<8:
        ii[22]=0
    if on[1]!=14 and on[2]!=500:
        if on[4]==4 and on[2]==8 and (on[1]==0 or 3<on[1]<8):
             soubi2.draw()
        sikai.draw()
        if on[5]>=0:
            hyouzi2.draw()
    if on[0]==0:#プレイ時間カウント
        ii[30]+=1
        if ii[30]==3600:
            if ii[31]<999:
                ii[31]+=1
                if iii[2]<999:
                    iii[2]+=1
            ii[30]=0
    if on[0]>0:#←スタート画面の時・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        on[1]=0#←スタート画面の時はゲームを操作できないようにする
        i[4]=0
        if 7>=on[0]>=4:#←ギャラリーBGM
             music[0]=5
             if siinn[5]<30:
                siinn[5]+=1
        if not 7>=on[0]>=4:#←続きからゲーム始めた際にBGMがホーム画面のBGMに変わらないようにするためのストッパー
            music[0]=1
        if on[0]==1:
            home.draw()
            start.draw()
            tuduki.draw()
            setumei.draw()
            gyarari.draw()
            osita.draw()
            reset[0].draw()
        if on[0]!=1:
            home2.draw()
        if on[0]==3:#操作説明
            modoru.bottomright=(690,480)
            sikai.draw()
            setumei2.draw()
            setumei3.draw()
            c3c.center=(200,417)
            c3c.draw()
            screen.draw.text("[このゲームの操作説明]",(0,10),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
            screen.draw.text("矢印キー(↑↓→←)でプレイヤーを操作し、移動できます",(20,165),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            screen.draw.text("ゲームプレイ中は画面右上に目標というものが表示されたり\nするのでそれに従ってマップを探索してください！！！",(20,190),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=23)
            screen.draw.text("このゲームでは新しいアイテムをゲットするたびにセーブ\nすることができます。文章をスキップしてしまうとセーブ\nポイントを逃してしまう場合があるので気をつけましょう!",(20,240),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=25)
            screen.draw.text("ゲームプレイ中はどのキーを押せばゲームを操作できるのかが\n画面のはじのほうに表示されます(※矢印キーをのぞく)\nゲームをプレイする際は参考にすることを強くオススメします",(20,50),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
            screen.draw.text("(↑※そのキーの説明が表示されている間はキーが反応しますが\n表示が消えている間は反応しないので注意しましょう!!!!!!!)",(20,110),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=18)
            screen.draw.text("マップは扉などに衝突することで移動が可能です\n(※カギがないと移動できない場所もあるので注意!!)",(20,330),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
            screen.draw.text("\n\n\n\n                    --→",(20,330),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=20)
            screen.draw.text("\n\n\n\n\n\n 衝突!　　 ↑扉の印の例↑2つ",(200,330),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",fontsize=20)
            screen.draw.text("　　    扉などに衝突することで移動",(20,330),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=20)
            screen.draw.text("\n\n\n\n\n\n 衝突!",(200,330),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=20)
            screen.draw.text("\n\n\n\n\n       　　1つ目　　二つ目",(200,330),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=20)
            tyuuto[0].draw()
        if on[0]==4:#
            gyarariinokabegami.draw()
            sgyara[0].draw()
            kgyara[0].draw()
            siinn[0].draw()
            screen.draw.text("ゲーム内全アイテム20個",(320,40),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",gcolor="YELLOW",fontsize=30)
            screen.draw.text("このゲームの総プレイ時間:"+str(iii[2])+"分",(30,410),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="LIGHT BLUE",fontsize=30)
            screen.draw.text("・         ・         ・",(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・         ・",(0,130),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・         ・",(0,170),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・         ・",(0,210),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・         ",(0,250),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・         ",(0,290),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・         ",(0,330),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            screen.draw.text("・         ・",(0,370),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[1]==0:
                screen.draw.text("・？？？？ ・",(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[2]==0:
                screen.draw.text("・？？？？ ・",(0,130),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[3]==0:
                screen.draw.text("・？？？？ ・",(0,170),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[4]==0:
                screen.draw.text("・？？？？ ・",(0,210),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[5]==0:
                screen.draw.text("・？？？？ ・",(0,250),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[6]==0:
                screen.draw.text("・？？？？ ・",(0,290),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[7]==0:
                screen.draw.text("・？？？？ ・",(0,330),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[8]==0:
                screen.draw.text("・？？？？ ・",(0,370),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[9]==0:
                screen.draw.text("・    　　 ・？？？？",(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[10]==0:
                screen.draw.text("・    　　 ・？？？？",(0,130),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[11]==0:
                screen.draw.text("・    　　 ・？？？？",(0,170),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[12]==0:
                screen.draw.text("・    　　 ・？？？？",(0,210),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[13]==0:
                screen.draw.text("・    　　 ・？？？？",(0,250),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[14]==0:
                screen.draw.text("・    　　 ・？？？？",(0,290),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[15]==0:
                screen.draw.text("・    　　 ・？？？？",(0,330),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[16]==0:
                screen.draw.text("・    　　 ・？？？？",(0,370),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[17]==0:
                screen.draw.text("・         ・   　　　・？？？？",(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[18]==0:
                screen.draw.text("・         ・         ・？？？？",(0,130),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[19]==0:
                screen.draw.text("・         ・         ・？？？？",(0,170),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[20]==0:
                screen.draw.text("・         ・         ・？？？？",(0,210),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[21]==0:
                screen.draw.text("・         ・         ",(0,250),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[22]==0:
                screen.draw.text("・         ・         ",(0,290),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[23]==0:
                screen.draw.text("・         ・         ",(0,330),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=40)
            if gyara[1]==1:
                screen.draw.text("どこかの部屋のカギ",(26,90+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[2]==1:
                screen.draw.text("どこかの通路のカギ",(26,130+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[3]==1:
                screen.draw.text("　　館内の地図",(26,170+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[4]==1:
                screen.draw.text("　　何かのメモ",(26,210+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[5]==1:
                screen.draw.text(" デザイン科のカギ",(26,250+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[6]==1:
                screen.draw.text("　 黄色い絵の具",(26,290+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[7]==1:
                screen.draw.text("　　青い絵の具",(26,330+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[8]==1:
                screen.draw.text("　　赤い絵の具",(26,370+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[9]==1:
                screen.draw.text("     長い棒",(250,90+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[10]==1:
                screen.draw.text("    懐中電灯",(250,130+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[11]==1:
                screen.draw.text("   被覆室のカギ",(250,170+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[12]==1:
                screen.draw.text("   曲がった棒",(250,210+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[13]==1:
                screen.draw.text("     ゴミ箱",(250,250+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[14]==1:
                screen.draw.text("     バケツ",(250,290+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[15]==1:
                screen.draw.text("     ロープ",(250,330+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[16]==1:
                screen.draw.text(" ロープ付きバケツ",(250,370+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[17]==1:
                screen.draw.text(" ビジネス科のカギ",(470,90+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[18]==1:
                screen.draw.text("    紫のカギ",(470,130+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[19]==1:
                screen.draw.text("    ハンマー",(470,170+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[20]==1:
                screen.draw.text("  霊よけのお守り",(470,210+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[21]==1:
                screen.draw.text("二つ目のお守り",(470,250+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[22]==1:
                screen.draw.text("三つ目のお守り",(470,290+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
            if gyara[23]==1:
                screen.draw.text("四つ目のお守り",(470,330+10),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)            
    if on[0]==5:#
        if kgyara[6]==0:
            kgyara[1].draw()
        if kgyara[6]==1:
            kgyara[2].draw()
        if kgyara[6]==2:
            kgyara[3].draw()
        if kgyara[6]==3:
            kgyara[8].draw()
        if kgyara[6]==4:
            kgyara[4].draw()
        if kgyara[6]==5:
            kgyara[5].draw()
        kgyara[7].draw()
    if on[0]==6:#
        if sgyara[6]==0:
            sgyara[1].draw()
        if sgyara[6]==1:
            sgyara[2].draw()
        if sgyara[6]==2:
            sgyara[3].draw()
        if sgyara[6]==3:
            sgyara[4].draw()
        kgyara[7].draw()
    if on[0]==7:
        siinn[1].draw()
        if siinn2[0]==0:
                #screen.draw.text("「ああああああああああああああ  「あああああああああああああ  \n  ああああああああああああああ」  あああああああああああああ」",(30,75),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=20)
                screen.draw.text("[？？？？？？？？？？？] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==1:
            c3c.topleft=(475,65)
            if siinn2[0]>=1:
                siinn2[1].draw()
                screen.draw.text("[　　　　始まり　　　　] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=2:
                siinn2[2].draw()
                screen.draw.text("[　　　　始まり　　　　] 　[ そんなこともあったな ]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==2:
            c3c.topleft=(495,65)
            if siinn2[0]>=3:
                siinn2[3].draw()
                screen.draw.text("[     宝探しゲーム     ] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=4:
                siinn2[4].draw()
                screen.draw.text("[     宝探しゲーム     ] 　[　　音葉との出会い　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==3:
            c3c.topleft=(510,65)
            if siinn2[0]>=5:
                siinn2[5].draw()
                screen.draw.text("[　　　霊鬼の出現　　　] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=6:
                siinn2[6].draw()
                screen.draw.text("[　　　霊鬼の出現　　　] 　[　　幽霊との出会い　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==4:
            c3c.topleft=(525,65)
            if siinn2[0]>=7:
                siinn2[7].draw()
                screen.draw.text("[　　　　邪魔者　　　　] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=8:
                siinn2[8].draw()
                screen.draw.text("[　　　　邪魔者　　　　] 　[　　 告げたくない 　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==5:
            c3c.topleft=(540,65)
            if siinn2[0]>=9:
                siinn2[9].draw()
                screen.draw.text("[　　　出口の有無　　　] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=10:
                siinn2[10].draw()
                screen.draw.text("[　　　出口の有無　　　] 　[　 私の優しいお友達　 ]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==6:
            c3c.topleft=(555,65)
            if siinn2[0]>=11:
                siinn2[11].draw()
                screen.draw.text("[　　 無意味な希望　　 ] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=12:
                siinn2[12].draw()
                screen.draw.text("[　　 無意味な希望　　 ] 　[　 　初めての希望 　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==7:
            c3c.topleft=(570,65)
            if siinn2[0]>=13:
                siinn2[13].draw()
                screen.draw.text("[ シューティングゲーム ] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=15:
                siinn2[14].draw()
                screen.draw.text("[ シューティングゲーム ] 　[　　　諦めないで　　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==8:
            c3c.topleft=(585,65)
            if siinn2[0]>=16:
                siinn2[15].draw()
                screen.draw.text("[　 　　戻れない 　　　] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=17:
                siinn2[16].draw()
                screen.draw.text("[　 　　戻れない 　　　] 　[　　　　裏切り　　　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==9:
            c3c.topleft=(600,65)
            if siinn2[0]>=18:
                siinn2[17].draw()
                screen.draw.text("[壁除けアクションゲーム] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=19:
                siinn2[18].draw()
                screen.draw.text("[壁除けアクションゲーム] 　[　　　 帰る意味 　　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==10:
            c3c.topleft=(615,65)
            if siinn2[0]>=20:
                siinn2[19].draw()
                screen.draw.text("[　　最後の鬼ごっこ　　] 　[？？？？？？？？？？？]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
            if siinn2[0]>=21:
                siinn2[20].draw()
                screen.draw.text("[　　最後の鬼ごっこ　　] 　[　　さよならと脱出　　]",(30,392),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="ORANGE",fontsize=25)
        if siinn[2]==1:
            kgyara[7].draw()
        if siinn[2]!=1:
            siinn[3].draw()
            screen.draw.text("  １ページ目の右上に表示されているギャラリ\n　ー画面に戻るボタンを押せばギャラリー画面\n　ヘ戻る事が可能です。(最初の1/10ページ目)",(316,0),fontname='a.ttc',owidth=0.3,gcolor="LIGHT BLUE",color="GRAY",fontsize=18)
        if siinn[2]!=10:
            siinn[4].draw()
        screen.draw.text("↑マウスでクリックしてページ移動↑",(177,465),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="LIGHT BLUE",fontsize=20)
        screen.draw.text("ゲームストーリーギャラリー",(7,70),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="LIGHT GREEN",fontsize=30)
        screen.draw.text("進み具合",(408,70),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=17)
        screen.draw.text("start→-------------→goal",(423,85),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
        c3c.draw()
        screen.draw.text(str(siinn[2])+"/10 ページ目",(0,0),fontname='a.ttc',owidth=4,gcolor="WHITE",color="YELLOW",fontsize=45)
    if on[0]==8:
         sikai.draw()
         screen.draw.text("[※セーブデーター、ギャラリーがすべて初期状態に戻ります]",(-4,130),fontname='a.ttc',owidth=3,color="RED",fontsize=25)
         screen.draw.text("[リセット後記録は復元できません!本当にリセットしますか?]",(-4,160),fontname='a.ttc',owidth=3,color="RED",fontsize=25)
         screen.draw.text("本当にリセットしますか？",(110,50),fontname='a.ttc',owidth=4,color="WHITE",fontsize=40)
         screen.draw.text("（※リセットには0秒～数秒程かかります!）",(0,0),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=20)
         reset[2].draw()
         reset[1].draw()
     #   sgyara[2].draw()
      #  sgyara[3].draw()
       # sgyara[4].draw()
        #sgyara[5].draw()
        #sgyara[6].draw()
    if on[1]==11:#GAME中断・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        if data[2]!=56:
            modoru.center=(350,245)
            modoru.draw()
            screen.draw.text("本当にゲームを中断しますか？",(150,20),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            screen.draw.text("※セーブしていない場合は、続きから始めることができません",(0,120),fontname='a.ttc',owidth=0.3,color="RED",fontsize=25)
            if i[4]==30:
                screen.draw.text("wでゲームに戻る",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if data[2]==56:
            screen.clear()
            modoru.center=(350,245)
            modoru.draw()
            screen.draw.text("GAME CLEAR!",(58,30),fontname='a.ttc',owidth=4,color="YELLOW",gcolor="RED",fontsize=100)
            screen.draw.text(" 最後までプレイしてくれて\n        ありがとう!",(148,360),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
            with open("item.txt","w") as file:
               for wwww in gyara:
                    file.write(str(wwww)+"\n")
            with open("time.txt","w") as file:#１行書き込み
                    file.write(str(iii[2]))
            with open("kyara.txt","w") as file:
                    file.write(str(kgyara[6]))
            with open("game.txt","w") as file:
                    file.write(str(sgyara[6]))
            with open("story.txt","w") as file:#１行書き込み
                    file.write(str(siinn2[0]))
           
    if on[1]==12:#MAP開く・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        if on[2]==0:
            maplist[0].draw()
        if on[2]==1:
            maplist[1].draw()
        if on[2]==2:
            maplist[2].draw()
        if on[2]==3:
            maplist[3].draw()
        if on[2]==4:
            maplist[4].draw()
        if on[2]==5:
            maplist[5].draw()
        if on[2]==6:
            maplist[6].draw()
        if on[2]==7:
            maplist[7].draw()
        if on[2]==8:
            maplist[8].draw()
        if on[2]==9:
            maplist[9].draw()
        if on[2]==-1:
            maplist[10].draw()
        if on[2]==-2:
            maplist[11].draw()
        if on[2]==-5:
            maplist[12].draw()
        if on[2]==-6:
            maplist[13].draw()
        screen.draw.text(str(on[4]),(550,75),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=100)
        if on[2]==999:
            maplist[14].draw()
        if i[4]==30:
            screen.draw.text("←Aで戻る",(0,450),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
#アイテムゲットしてセーブ・・・・・・・・・・・・・・・・・・・・・・・・・・・・
    if ii[10]<26:  
       if ii[3]==0:#セーブするかしないか表示前にスキップした時は表示されないようにする
             ii[9]=0
       if item[ii[10]]!=0:
           ii[11]+=1
       ii[10]+=1
       if ii[10]>=26:#アイテム個数10個、数えたときの処理※ゲーム内でゲットするアイテムが10以上の時はもっとでかい数にする必要あり
        ii[10]=0#←カウント数リセット
        if ii[12] < ii[11]:#←アイテムが増えた時
         ii[9]=1#アイテムゲットしたときだけセーブできるようにするための、ストッパー発動
        ii[12]=ii[11]#受け渡し
        ii[11]=0#←アイテム数リセット
        if ii[12] > 5 and ii[9]==1:#←アイテムが増えた時
            ii[9]=0
    if on[1]==18:#アイテムの位置・・・・・・・・・・・・・・・・・・・・・・・・
        q.draw()
        screen.draw.text("[どの部屋で拾ったITEMなのか？について↓]",(47,0),fontname='a.ttc',owidth=5,color="LIGHT BLUE",gcolor="BLUE",fontsize=30)
        if iii[3]!=3 and iii[3]!=14 and iii[3]!=16 and iii[3]!=17 and iii[3]!=19 and iii[3]!=20:
            screen.draw.text("マ\nッ\nプ\nの\n青  ➡  \n色\nの\n部\n屋",(100,247),fontname='a.ttc',owidth=3,gcolor="BLUE",color="LIGHT BLUE",fontsize=22)
        if iii[3]!=3 and iii[3]!=14 and iii[3]!=16 and iii[3]!=17 and iii[3]!=19 and iii[3]!=20:
            screen.draw.text("アイテムを\n拾った場所 ➡\n",(53,140),fontname='a.ttc',owidth=3,color="WHITE",fontsize=20)
            screen.draw.text("┌────────┐\n│ITEMをもとの位置│\n│に戻す時は、現在│\n│画面に表示されて│\n│いる階数や、部屋│\n│の位置、ITEMがあ│\n│った場所などの情│\n│報を参考にして、│\n│元々ITEMが置いて│\n│あった所に戻ろう│\n│!!歩いてその場所│\n│についたら、以前│\n│アイテムを拾った│\n│時に,Dを押して調│\n│べた所と同じ場所│\n│を!!!再びDで調べ│\n│ると!,もとの位置│\n│に戻せる！面倒だ│\n│と思うが頑張って│\n│くれ！BY作者より│\n└────────┘",(495,37),fontname='a.ttc',owidth=3,gcolor="GREEN",color="WHITE",fontsize=20)
            screen.draw.text("\n\n(緑の矢印の所)",(53,150),fontname='a.ttc',owidth=3,gcolor="GREEN",color="WHITE",fontsize=20)
        if iii[3]==1:
            hinnto[0].draw()
            item2[1].midbottom=hinnto[0].midtop
            item2[1].draw()
            screen.draw.text("2F",(210,255),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==2:
            hinnto[3].draw()
            item2[2].midbottom=hinnto[3].midtop
            item2[2].draw()
            screen.draw.text("2F",(210,255),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==3:
            screen.draw.text("もらったITEMなのでもとの位\n置に戻すことができない",(155,90),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            #hinnto[2].draw()
        if iii[3]==4:
            hinnto[8].draw()
            item2[4].midbottom=hinnto[8].midtop
            item2[4].draw()
            screen.draw.text("2F",(210,255),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==5:
            hinnto[8].draw()
            item2[5].midbottom=hinnto[8].midtop
            item2[5].draw()
            screen.draw.text("1F",(210,255),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",fontsize=30)
        if iii[3]==6:
            hinnto[3].draw()
            item2[6].midbottom=hinnto[3].midtop
            item2[6].draw()
            screen.draw.text("1F",(210,255),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",fontsize=30)
        if iii[3]==7:
            hinnto[0].draw()
            item2[7].midbottom=hinnto[0].midtop
            item2[7].draw()
            screen.draw.text("1F",(210,255),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",fontsize=30)
        if iii[3]==8:
            hinnto[0].draw()
            item2[8].midbottom=hinnto[0].midtop
            item2[8].draw()
            screen.draw.text("1F",(210,255),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",fontsize=30)
        if iii[3]==9:
            hinnto[5].draw()
            item2[9].midbottom=hinnto[5].midtop
            item2[9].draw()
            screen.draw.text("3F",(210,255),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=30)
        if iii[3]==10:
            hinnto[1].draw()
            item2[10].midbottom=hinnto[1].midtop
            item2[10].draw()
            screen.draw.text("3F",(210,255),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=30)
        if iii[3]==11:
            hinnto[7].draw()
            item2[11].midbottom=hinnto[7].midtop
            item2[11].draw()
            screen.draw.text("3F",(210,255),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=30)
        if iii[3]==12:
            hinnto[6].draw()
            item2[12].midbottom=hinnto[6].midtop
            item2[12].draw()
            screen.draw.text("3F",(210,255),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=30)
        if iii[3]==13:
            hinnto[0].draw()
            item2[13].midbottom=hinnto[0].midtop
            item2[13].draw()
            screen.draw.text("3F",(210,255),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=30)
        if iii[3]==14:
            #hinnto[8].draw()
            screen.draw.text("合成してゲットしたITEMなの\nでもとの位置に戻すことがで\nきない",(150,90),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==15:
            hinnto[3].draw()
            item2[15].midbottom=hinnto[3].midtop
            item2[15].draw()
            screen.draw.text("3F",(210,255),fontname='a.ttc',owidth=0.3,color="PINK",fontsize=30)
        if iii[3]==16:
            #hinnto[8].draw()
            screen.draw.text("合成してゲットしたITEMなの\nでもとの位置に戻すことがで\nきない",(150,90),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==17:
            #hinnto[0].draw()
            screen.draw.text("水の中から救いあげてゲット\nしたITEMなのでもとの位置に\n戻すことができない",(150,90),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==18:
            hinnto[8].draw()
            item2[18].midbottom=hinnto[8].midtop
            item2[18].draw()
            screen.draw.text("4F",(210,255),fontname='a.ttc',owidth=0.3,color="PURPLE",fontsize=30)
        if iii[3]==19:
             screen.draw.text("もらったITEMなのでもとの位\n置に戻すことができない",(155,90),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if iii[3]==20:
             screen.draw.text("もらったITEMなのでもとの位\n置に戻すことができない",(155,90),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if i[4]==30:
            screen.draw.text("←SキーでITEM欄に戻る",(0,450),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
    if on[1]==1:#アイテム欄・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        q.draw()
        am6.draw()
        am7.draw()
        if data[2]>10:
            screen.draw.text("\n┌────┐\n│アイテム│\n│名の右に│\n│ある水色│\n│のボタン│\n│をマウス│\n│でクリッ│\n│クすると│\n│元の位置│\n│が見れる│\n└────┘",(595,275),fontname='a.ttc',owidth=3,gcolor="WHITE",color="YELLOW",fontsize=18)
        if on[4]==3 and on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc))and data[2]>=24:
                gouseikabegami.draw()
                gousei[13].draw()
        if i[4]==30:
            screen.draw.text("sで戻る",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[4]==3 and on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc))and data[2]>=24:
                screen.draw.text("合成したい二つのアイテムを選択してください",(0,410),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",fontsize=30)
                screen.draw.text("sで戻る　　　(↑マウスでクリックして選択↑)",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if i[0]<25:
          i[0]+=1
    #手持ちのアイテムあるパターン↓               
        if item[1]==1 and i[0]==1:
             z[1]=i[1]
             i[1]+=1
        if item[2]==1 and i[0]==2:
             z[2]=i[1]
             i[1]+=1
        if item[3]==1 and i[0]==3:
             z[3]=i[1]
             i[1]+=1
        if item[4]==1 and i[0]==4:
             z[4]=i[1]
             i[1]+=1
        if item[5]==1 and i[0]==5:
             z[5]=i[1]
             i[1]+=1
        if item[6]==1 and i[0]==6:
             z[6]=i[1]
             i[1]+=1
        if item[7]==1 and i[0]==7:
             z[7]=i[1]
             i[1]+=1
        if item[8]==1 and i[0]==8:
             z[8]=i[1]
             i[1]+=1
        if item[9]==1 and i[0]==9:
             z[9]=i[1]
             i[1]+=1
        if item[10]==1 and i[0]==10:
             z[10]=i[1]
             i[1]+=1
        if item[11]==1 and i[0]==11:
             z[11]=i[1]
             i[1]+=1
        if item[12]==1 and i[0]==12:
             z[12]=i[1]
             i[1]+=1
        if item[13]==1 and i[0]==13:
             z[13]=i[1]
             i[1]+=1
        if item[14]==1 and i[0]==14:
             z[14]=i[1]
             i[1]+=1
        if item[15]==1 and i[0]==15:
             z[15]=i[1]
             i[1]+=1
        if item[16]==1 and i[0]==16:
             z[16]=i[1]
             i[1]+=1
        if item[17]==1 and i[0]==17:
             z[17]=i[1]
             i[1]+=1
        if item[18]==1 and i[0]==18:
             z[18]=i[1]
             i[1]+=1
        if item[19]==1 and i[0]==19:
             z[19]=i[1]
             i[1]+=1
        if item[20]==1 and i[0]==20:
             z[20]=i[1]
             i[1]+=1
        if item[21]==1 and i[0]==21:
             z[21]=i[1]
             i[1]+=1
        if item[22]==1 and i[0]==22:
             z[22]=i[1]
             i[1]+=1
        if item[23]==1 and i[0]==23:
             z[23]=i[1]
             i[1]+=1
        if item[24]==1 and i[0]==24:
             z[24]=i[1]
             i[1]+=1
        if item[25]==1 and i[0]==25:
             z[25]=i[1]
             i[1]+=1
    #手持ちのアイテムあるパターン↑
    #手持ちのアイテムないパターン↓
        if item[1]==0:
             z[1]=10000
        if item[2]==0:
             z[2]=10000
        if item[3]==0:
             z[3]=10000
        if item[4]==0:
             z[4]=10000
        if item[5]==0:
             z[5]=10000
        if item[6]==0:
             z[6]=10000
        if item[7]==0:
             z[7]=10000
        if item[8]==0:
             z[8]=10000
        if item[9]==0:
             z[9]=10000
        if item[10]==0:
             z[10]=10000
        if item[11]==0:
             z[11]=10000
        if item[12]==0:
             z[12]=10000
        if item[13]==0:
             z[13]=10000
        if item[14]==0:
             z[14]=10000
        if item[15]==0:
             z[15]=10000
        if item[16]==0:
             z[16]=10000
        if item[17]==0:
             z[17]=10000
        if item[18]==0:
             z[18]=10000
        if item[19]==0:
             z[19]=10000
        if item[20]==0:
             z[20]=10000
        if item[21]==0:
             z[21]=10000
        if item[22]==0:
             z[22]=10000
        if item[23]==0:
             z[23]=10000
        if item[24]==0:
             z[24]=10000
        if item[25]==0:
             z[25]=10000
    #手持ちのアイテムないパターン↑
    #手持ちのアイテム表示する処理↓
        screen.draw.text("・どこかの部屋のカギ",(0,z[1]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("このカギがあれば今まで入れなかった部屋にはいれるかも？",(0,z[1]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・どこかの通路のカギ",(0,z[2]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("このカギがあれば、また新しいところに行けそうだ",(0,z[2]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・館内のマップ",(0,z[3]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("このマップがあればAキーで現在地を確認できそうだ",(0,z[3]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・メモ帳",(0,z[4]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("パソコンのパスワードの6～8文字はSOUだ、と書いてある",(0,z[4]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・デザイン科のカギ",(0,z[5]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("このカギで1Fのデザイン科のa号室とb号室に入れそうだ",(0,z[5]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・黄色い絵の具",(0,z[6]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("黄色い絵の具、かなり古びている",(0,z[6]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・青い絵の具",(0,z[7]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("青い絵の具、かなり古びている",(0,z[7]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・赤い絵の具",(0,z[8]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("赤い絵の具、かなり古びている",(0,z[8]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・長い棒",(0,z[9]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("棚の上など、高いところの物をとれそうだ、",(0,z[9]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・懐中電灯",(0,z[10]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("棚の下など、暗いところにあるアイテムを拾えそうだ",(0,z[10]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・被覆室のカギ",(0,z[11]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("このカギで被覆科の部屋に入れそうだ",(0,z[11]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・曲がった棒",(0,z[12]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("曲がっている割にかなり頑丈だ",(0,z[12]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・ゴミ箱",(0,z[13]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("少し頑丈な作りだ",(0,z[13]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・バケツ",(0,z[14]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("これで何かをすくえるかも？",(0,z[14]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・ロープ",(0,z[15]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("長い何かに巻き付けて使えそうだ",(0,z[15]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・ロープ付きバケツ",(0,z[16]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("遠くにある物をすくえるかも",(0,z[16]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・ビジネス科のカギ",(0,z[17]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("４Fビジネス科の教室に入れそうだ",(0,z[17]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・紫のカギ",(0,z[18]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("なんだろう、変なカギだ",(0,z[18]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・ハンマー",(0,z[19]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("これを使って壁をたたくと何かあるかも",(0,z[19]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・霊よけのお守り",(0,z[20]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("音葉が幸運を願って美香に渡したお守り",(0,z[20]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・三つ目のお守り",(0,z[21]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("あと二つつ",(0,z[21]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・四つ目のお守り",(0,z[22]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("あと一つ",(0,z[22]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        screen.draw.text("・五つ目のお守り",(0,z[23]*66),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=36)
        screen.draw.text("出口に出れる",(0,z[23]*66+40),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=23)
        if data[2]>10:#←どこで拾ったものなのかを見るボタン
            hirou[1].center=(550,z[1]*66+20)
            hirou[2].center=(550,z[2]*66+20)
            hirou[3].center=(550,z[3]*66+20)
            hirou[4].center=(550,z[4]*66+20)
            hirou[5].center=(550,z[5]*66+20)
            hirou[6].center=(550,z[6]*66+20)
            hirou[7].center=(550,z[7]*66+20)
            hirou[8].center=(550,z[8]*66+20)
            hirou[9].center=(550,z[9]*66+20)
            hirou[10].center=(550,z[10]*66+20)
            hirou[11].center=(550,z[11]*66+20)
            hirou[12].center=(550,z[12]*66+20)
            hirou[13].center=(550,z[13]*66+20)
            hirou[14].center=(550,z[14]*66+20)
            hirou[15].center=(550,z[15]*66+20)
            hirou[16].center=(550,z[16]*66+20)
            hirou[17].center=(550,z[17]*66+20)
            hirou[18].center=(550,z[18]*66+20)
            hirou[19].center=(550,z[19]*66+20)
            hirou[20].center=(550,z[20]*66+20)
            hirou[1].draw()
            hirou[2].draw()
            hirou[3].draw()
            hirou[4].draw()
            hirou[5].draw()
            hirou[6].draw()
            hirou[7].draw()
            hirou[8].draw()
            hirou[9].draw()
            hirou[10].draw()
            hirou[11].draw()
            hirou[12].draw()
            hirou[13].draw()
            hirou[14].draw()
            hirou[15].draw()
            hirou[16].draw()
            hirou[17].draw()
            hirou[18].draw()
            hirou[19].draw()
            hirou[20].draw()
        if  on[4]==3 and on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc))and data[2]>23:#アイテム合成の時qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
            if data[2]<27:
                gousei[4].center=(550,z[13]*66+20)
                gousei[4].draw()
                gousei[3].center=(550,z[12]*66+20)
                gousei[3].draw()
            if data[2]>=27:
                gousei[4].center=(550,z[15]*66+20)
                gousei[4].draw()
                gousei[3].center=(550,z[14]*66+20)
                gousei[3].draw()
            gousei[2].center=(550,z[11]*66+20)
            gousei[2].draw()
            gousei[1].center=(550,z[3]*66+20)
            gousei[1].draw()
            gousei[0].center=(550,z[2]*66+20)
            gousei[0].draw()
            dekinai1.y=1000
            dekinai2.y=1000
            if z[1]!=10000:
                dekinai1.center=(550,z[1]*66+20)
            if z[4]!=10000:
                if z[1]==10000:
                    dekinai1.center=(550,z[4]*66+20)
                if z[1]!=10000:
                    dekinai2.center=(550,z[4]*66+20)
            if z[5]!=10000:
                if z[1]==10000 and z[4]==10000:
                    dekinai1.center=(550,z[5]*66+20)
                if z[1]!=10000 or z[4]!=10000:
                    dekinai2.center=(550,z[5]*66+20)
            if z[6]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000:
                    dekinai1.center=(550,z[6]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000:
                    dekinai2.center=(550,z[6]*66+20)
            if z[7]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000:
                    dekinai1.center=(550,z[7]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000:
                    dekinai2.center=(550,z[7]*66+20)
            if z[8]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000:
                    dekinai1.center=(550,z[8]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000:
                    dekinai2.center=(550,z[8]*66+20)
            if z[9]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000:
                    dekinai1.center=(550,z[9]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000:
                    dekinai2.center=(550,z[9]*66+20)
            if z[10]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000:
                    dekinai1.center=(550,z[10]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000:
                    dekinai2.center=(550,z[10]*66+20)
            if z[16]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000:
                    dekinai1.center=(550,z[16]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000:
                    dekinai2.center=(550,z[16]*66+20)
            if z[17]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000:
                    dekinai1.center=(550,z[17]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000:
                    dekinai2.center=(550,z[17]*66+20)
            if z[18]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000 and z[17]==10000:
                    dekinai1.center=(550,z[18]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000 or z[17]!=10000:
                    dekinai2.center=(550,z[18]*66+20)
            if z[19]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000 and z[17]==10000 and z[18]==10000:
                    dekinai1.center=(550,z[19]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000 or z[17]!=10000 or z[18]!=10000:
                    dekinai2.center=(550,z[19]*66+20)
            if z[20]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000 and z[17]==10000 and z[18]==10000 and z[19]==10000:
                    dekinai1.center=(550,z[20]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000 or z[17]!=10000 or z[18]!=10000 or z[19]!=10000:
                    dekinai2.center=(550,z[20]*66+20)
            if z[21]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000 and z[17]==10000 and z[18]==10000 and z[19]==10000 and z[20]==10000:
                    dekinai1.center=(550,z[21]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000 or z[17]!=10000 or z[18]!=10000 or z[19]!=10000 or z[20]!=10000:
                    dekinai2.center=(550,z[21]*66+20)
            if z[22]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000 and z[17]==10000 and z[18]==10000 and z[19]==10000 and z[20]==10000 and z[21]==10000:
                    dekinai1.center=(550,z[22]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000 or z[17]!=10000 or z[18]!=10000 or z[19]!=10000 or z[20]!=10000 or z[21]!=10000:
                    dekinai2.center=(550,z[22]*66+20)
            if z[23]!=10000:
                if z[1]==10000 and z[4]==10000 and z[5]==10000 and z[6]==10000 and z[7]==10000 and z[8]==10000 and z[9]==10000 and z[10]==10000 and z[16]==10000 and z[17]==10000 and z[18]==10000 and z[19]==10000 and z[20]==10000 and z[21]==10000 and z[22]==10000:
                    dekinai1.center=(550,z[23]*66+20)
                if z[1]!=10000 or z[4]!=10000 or z[5]!=10000 or z[6]!=10000 or z[7]!=10000 or z[8]!=10000 or z[9]!=10000 or z[10]!=10000 or z[16]!=10000 or z[17]!=10000 or z[18]!=10000 or z[19]!=10000 or z[20]!=10000 or z[21]!=10000  or z[22]!=10000:
                    dekinai2.center=(550,z[23]*66+20)
            dekinai1.draw()
            dekinai2.draw()
            if z[12]!=10000 and z[13]!=10000:#なんのアイテム持ってるか判断する
                if z[12]==0:#
                    if gousei[8]==1:
                        ka[8]=1
                if z[12]==1:#
                    if gousei[9]==1:
                        ka[8]=1
                if z[12]==2:#
                    if gousei[10]==1:
                        ka[8]=1
                if z[12]==3:#
                    if gousei[11]==1:
                        ka[8]=1
                if z[12]==4:#
                    if gousei[12]==1:
                        ka[8]=1
                if z[13]==0:
                    if gousei[8]==1:
                        ka[8]=1
                if z[13]==1:
                    if gousei[9]==1:
                        ka[9]=1
                if z[13]==2:
                    if gousei[10]==1:
                        ka[9]=1
                if z[13]==3:
                    if gousei[11]==1:
                        ka[9]=1
                if z[13]==4:
                    if gousei[12]==1:
                        ka[9]=1
            if z[14]!=10000 and z[15]!=10000:#なんのアイテム持ってるか判断する
                if z[14]==0:#
                    if gousei[8]==1:
                        ka[8]=1
                if z[14]==1:#
                    if gousei[9]==1:
                        ka[8]=1
                if z[14]==2:#
                    if gousei[10]==1:
                        ka[8]=1
                if z[14]==3:#
                    if gousei[11]==1:
                        ka[8]=1
                if z[14]==4:#
                    if gousei[12]==1:
                        ka[8]=1
                if z[15]==0:
                    if gousei[8]==1:
                        ka[8]=1
                if z[15]==1:
                    if gousei[9]==1:
                        ka[9]=1
                if z[15]==2:
                    if gousei[10]==1:
                        ka[9]=1
                if z[15]==3:
                    if gousei[11]==1:
                        ka[9]=1
                if z[15]==4:
                    if gousei[12]==1:
                        ka[9]=1
            if ka[7]==1:
                gousei[5].draw()
            if ka[7]==2:
                gousei[5].draw()
                gousei[6].draw()
                gousei[7].draw()#合成ボタン
            if ka[7]==3 and i[4]>1:
                    screen.draw.text("合成できません",(228,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
    #手持ちのアイテム表示する処理↑            
        if i[0]==25:
          i[0]=0
          i[1]=0
    if on[1]==2 or on[0]==2:#セーブ欄・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
         q.draw()
         if on[0]!=2 and i[4]==30:
             u[0]=1
             screen.draw.text("aで戻る",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
             screen.draw.text("    　 (マウスでsavedataをクリックすれば↑\n   　 　　　　そのsavedataにセーブすることができます)",(0,425),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=26)
         if on[0]!=2 and i[4]!=30 and u[0]==1:
          if 2<i[7]<6:
             screen.draw.text("セーブ中です 80%-- -- -- --",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
          if 6<=i[7]<11:
             screen.draw.text("セーブ中です 60%-- -- --",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
          if 11<=i[7]<16:
             screen.draw.text("セーブ中です 40%-- --",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
          if 16<=i[7]<21:
             screen.draw.text("セーブ中です 20%--",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
          if 21<=i[7]<26:
             screen.draw.text("セーブ中です 0%",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
          if i[7]<=2:
             screen.draw.text("セーブ中です 100%-- -- -- -- -→完了！",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
         if i[5]<5:
             zz[i[5]]=i[5]
             i[5]+=1
             qq1.draw()
             qq2.draw()
             qq3.draw()
             qq4.draw()
             screen.draw.text("savedata1　記録なし",(0,zz[0]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
             screen.draw.text("savedata2　記録なし",(0,zz[1]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
             screen.draw.text("savedata3　記録なし",(0,zz[2]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
             screen.draw.text("savedata4　記録なし",(0,zz[3]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
         if i[5]==5:
             i[5]=0
    #セーブ・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
    if 0<i[7]<26:
        if i[8]==1:
            if on[1]==2 and on[0]!=2:#game中にセーブするとき
                 save1[i[7]]=data[i[7]]
                 if i[7]==2 and so[6]==0:
                     save1[i[7]]=data[i[7]]+1#セーブ
                 if i[7]==2 and so[6]==1:
                     save1[i[7]]=data[i[7]]#セーブ
                 save1[i[7]+10]=item[i[7]]#itemセーブ
                 save1[0]=data[0]#プレイ時間
                 save11[1]=data[10]
                 stop1[i[7]-1]=items[i[7]-1]
                 #save1[18]=data[10]#階
                 with open("save1.txt","w") as file:#ファイルsave
                      for wwww in save1:
                         file.write(str(wwww)+"\n")
                 with open("save11.txt","w") as file:
                      for wwww in save11:
                         file.write(str(wwww)+"\n")
                 with open("stop1.txt","w") as file:#ファイルsave
                      for wwww in stop1:
                         file.write(str(wwww)+"\n")
               
            if on[0]==2:
                 items[i[7]-1]=int(stop1[i[7]-1])
                 item[i[7]]=int(save1[i[7]+10])#itemセーブデータ起動
        if i[8]==2:
            if on[1]==2 and on[0]!=2:#game中にセーブするとき
                 save2[i[7]]=data[i[7]]#セーブ
                 if i[7]==2 and so[6]==0:
                     save2[i[7]]=data[i[7]]+1#セーブ
                 if i[7]==2 and so[6]==1:
                     save2[i[7]]=data[i[7]]#セーブ
                 save2[i[7]+10]=item[i[7]]#itemセーブ
                 save2[0]=data[0]#プレイ時間
                 save22[1]=data[10]
                 stop2[i[7]]=items[i[7]-1]
                 with open("save2.txt","w") as file:#ファイルsave
                      for wwww in save2:
                         file.write(str(wwww)+"\n")
                 with open("save22.txt","w") as file:
                      for wwww in save22:
                         file.write(str(wwww)+"\n")
                 with open("stop2.txt","w") as file:#ファイルsave
                      for wwww in stop2:
                         file.write(str(wwww)+"\n")
               
            if on[0]==2:
                 items[i[7]-1]=int(stop2[i[7]-1])
                 item[i[7]]=int(save2[i[7]+10])#itemセーブデータ起動
        if i[8]==3:
            if on[1]==2 and on[0]!=2:#game中にセーブするとき
                 save3[i[7]]=data[i[7]]#セーブ
                 if i[7]==2 and so[6]==0:
                     save3[i[7]]=data[i[7]]+1#セーブ
                 if i[7]==2 and so[6]==1:
                     save3[i[7]]=data[i[7]]#セーブ
                 save3[i[7]+10]=item[i[7]]#itemセーブ
                 save3[0]=data[0]#プレイ時間
                 save33[1]=data[10]
                 stop3[i[7]]=items[i[7]-1]
                 with open("save3.txt","w") as file:#ファイルsave
                      for wwww in save3:
                         file.write(str(wwww)+"\n")
                 with open("save33.txt","w") as file:
                      for wwww in save33:
                         file.write(str(wwww)+"\n")
                 with open("stop3.txt","w") as file:#ファイルsave
                      for wwww in stop3:
                         file.write(str(wwww)+"\n")
            if on[0]==2:
                 items[i[7]-1]=int(stop3[i[7]-1])
                 item[i[7]]=int(save3[i[7]+10])#itemセーブデータ起動
        if i[8]==4:
            if on[1]==2 and on[0]!=2:#game中にセーブするとき
                 save4[i[7]]=data[i[7]]#セーブ
                 if i[7]==2 and so[6]==0:
                     save4[i[7]]=data[i[7]]+1#セーブ
                 if i[7]==2 and so[6]==1:
                     save4[i[7]]=data[i[7]]#セーブ
                 save4[i[7]+10]=item[i[7]]#itemセーブ
                 save4[0]=data[0]#プレイ時間
                 save44[1]=data[10]
                 stop4[i[7]]=items[i[7]-1]
                 with open("save4.txt","w") as file:#ファイルsave
                      for wwww in save4:
                         file.write(str(wwww)+"\n")
                 with open("save44.txt","w") as file:
                      for wwww in save44:
                         file.write(str(wwww)+"\n")
                 with open("stop4.txt","w") as file:#ファイルsave
                      for wwww in stop4:
                         file.write(str(wwww)+"\n")
            if on[0]==2:
                 items[i[7]-1]=int(stop4[i[7]-1])
                 item[i[7]]=int(save4[i[7]+10])#itemセーブデータ起動
        i[7]-=1
    if i[7]==0:#セーブ後元に戻す
         if on[0]!=2:
              with open("item.txt","w") as file:
               for wwww in gyara:
                    file.write(str(wwww)+"\n")
              with open("time.txt","w") as file:#１行書き込み
                    file.write(str(iii[2]))
              with open("kyara.txt","w") as file:
                    file.write(str(kgyara[6]))
              with open("game.txt","w") as file:
                    file.write(str(sgyara[6]))
              with open("story.txt","w") as file:#１行書き込み
                    file.write(str(siinn2[0]))
         i[7]=26
         i[8]=0
         if on[0]==2:#ゲーム開始
            on[0]=0
   #セーブデータ表示・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・                 
    if save1[i[6]]!=str(0):
         i[9]=1
    if save2[i[6]]!=str(0):
         i[10]=1
    if save3[i[6]]!=str(0):
         i[11]=1
    if save4[i[6]]!=str(0):
         i[12]=1
    if i[6]>=10:
         i[6]=0
    i[6]+=1
    if on[1]==2 or on[0]==2 :
        if i[9]==1:
            screen.draw.text("savedata  =========　➡　記録あり",(0,zz[0]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
            screen.draw.text("ゲームのプレイ時間:"+str(save1[0])+"分",(0,zz[0]*100+35),fontname='a.ttc',owidth=1.5,gcolor="WHITE",color="LIGHT BLUE",fontsize=20)
            savek[0].topleft=(288,zz[0]*100+25)
            savek[0].draw()
        if i[10]==1:
            screen.draw.text("savedata  =========　➡　記録あり",(0,zz[1]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
            screen.draw.text("ゲームのプレイ時間:"+str(save2[0])+"分",(0,zz[1]*100+35),fontname='a.ttc',owidth=1.5,gcolor="WHITE",color="LIGHT BLUE",fontsize=20)
            savek[1].topleft=(288,zz[1]*100+25)
            savek[1].draw()
        if i[11]==1:
            screen.draw.text("savedata  =========　➡　記録あり",(0,zz[2]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
            screen.draw.text("ゲームのプレイ時間:"+str(save3[0])+"分",(0,zz[2]*100+35),fontname='a.ttc',owidth=1.5,gcolor="WHITE",color="LIGHT BLUE",fontsize=20)
            savek[2].topleft=(288,zz[2]*100+25)
            savek[2].draw()
        if i[12]==1:
            screen.draw.text("savedata  =========　➡　記録あり",(0,zz[3]*100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=30)
            screen.draw.text("ゲームのプレイ時間:"+str(save4[0])+"分",(0,zz[3]*100+35),fontname='a.ttc',owidth=1.5,gcolor="WHITE",color="LIGHT BLUE",fontsize=20)
            savek[3].topleft=(288,zz[3]*100+25)
            savek[3].draw()
    if 1<on[0]<5:#ホーム画面の戻るボタン・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        modoru.draw()
    if on[0]==2:#セーブデーター開く
            modoru.topleft=(500,395)
            screen.draw.text("savedataをマウスでクリックすれば↑",(5,420),fontname='a.ttc',color="WHITE",owidth=1.5,gcolor="LIGHT BLUE",fontsize=29)
            screen.draw.text(" そのセーブした所から始められます",(0,450),fontname='a.ttc',owidth=1.5,color="WHITE",gcolor="LIGHT BLUE",fontsize=29)
    if on[5]>=0:#敵が出てきた
        tekilist[5].draw()
    if on[1]==3:#テキスト・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        data[1]=ii[4]#テキスト表示中にセーブするので(動くのはプレイヤーかマップか)
        data[3]=on[2]#テキスト表示中にセーブするので、map
        data[10]=on[4]#テキスト表示中にセーブするので、map
        if on[0]==0:
            data[4]=music[0]#テキスト表示中にセーブするので、BGM
        data[5]=m1.x#mapのx
        data[6]=m1.y#mapのy
        data[7]=c.x#プレイヤーのx
        data[8]=c.y#プレイヤーのy
        data[0]=ii[31]#セーブした時のゲームのプレイ時間
        if ii[14]==2:
            q.draw()
            if data[2]==0 and ii[3]>2:
                tai[0].draw()
                sikai.draw()
        if ii[14]==1:
            if ii[23]==-37:
                kotarou[7].draw()
            if ii[23]==-36:
                kotarou[6].draw()
            if ii[23]==-35:
                kotarou[5].draw()
            if ii[23]==-34:
                kotarou[4].draw()
            if ii[23]==-33:
                kotarou[3].draw()
            if ii[23]==-32:
                kotarou[2].draw()
            if ii[23]==-31:
                kotarou[1].draw()
            if ii[23]==-30:
                kotarou[0].draw()
                
            if ii[23]==100:
                ninngenn[0].draw()
            if ii[23]==101:
                ninngenn[1].draw()
            if ii[23]==102:
                ninngenn[2].draw()
            if ii[23]==103:
                ninngenn[3].draw()
            if ii[23]==104:
                ninngenn[4].draw()
            if ii[23]==105:
                ninngenn[5].draw()
            if ii[23]==106:
                ninngenn[6].draw()
            if ii[23]==107:
                ninngenn[7].draw()
                
            if ii[23]==-17:
                sakuma2[5].draw()
            if ii[23]==-16:
                sakuma2[4].draw()
            if ii[23]==-15:
                sakuma2[3].draw()
            if ii[23]==-14:
                sakuma2[2].draw()
            if ii[23]==-13:
                sakuma2[1].draw()
            if ii[23]==-12:
                sakuma2[0].draw()
            if ii[23]==-11:
                sakuma[0].draw()
            if ii[23]==-10:
                sakuma[1].draw()
            if ii[23]==-9:
                sakuma[2].draw()
            if ii[23]==-8:
                sakuma[3].draw()
            if ii[23]==-7:
                sakuma[4].draw()
            if ii[23]==-6:
                 sakuma[5].draw()
            if ii[23]==-5:
                sakuma[6].draw()
            if ii[23]==-4:
                sakuma[7].draw()
            if ii[23]==-3:
                sakuma[8].draw()
            if ii[23]==-2:#ii[23]の数値で、表情の割り振り
                nae.draw()
            if ii[23]==-1:#ii[23]の数値で、表情の割り振り
                zetu.draw()
            if ii[23]==0:#ii[23]の数値で、表情の割り振り
                wara.draw()
            if ii[23]==1:#ii[23]の数値で、表情の割り振り
                g1.draw()#ノーマル顔
            if ii[23]==2:
                am3.draw()#口開けてなくて汗かいて困ってる
            if ii[23]==3:
                am4.draw()#口開けて困ってる
            if ii[23]==4:
                am2.draw()#口も明けず汗もかかず普通に困ってる
            if ii[23]==5:
                am5.draw()#めっちゃ焦ってる、目の瞳孔小さくなるぐらい
            if ii[23]==6:#普通
                hito[2].draw()
            if ii[23]==7:
                hito[0].draw()
            if ii[23]==8:
                hito[1].draw()
            if ii[23]==9:
                hito[3].draw()
            if ii[23]==10:#普通
                hito[4].draw()
            if ii[23]==11:#しゃべる
                hito[5].draw()
            if ii[23]==12:#しゃべる2
                hito[6].draw()
            if ii[23]==13:#じー#普通
                hito[7].draw()
            if ii[23]==14:#下見てる
                hito[8].draw()
            if ii[23]==15:#ふつう
                hito[9].draw()
            if ii[23]==16:#しゃべる2
                hito[10].draw()
            if ii[23]==17:#へこんでしゃべる
                hito[11].draw()
        if ii[14]==3:#背景
                pc.draw()
        nn.draw()
        if ii[14]==1:
            if 100<=ii[23]<=107:
                screen.draw.text("[17歳少年T]",(530,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="YELLOW",fontsize=30)


            if -29>ii[23]>-38:
                screen.draw.text("[小太郎]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
            if (5<ii[23]<10 or -2>ii[23]>-12) and data[2]!=12:
                    if on[2]==2:
                        k1.k.y=1000
                    screen.draw.text("[音葉]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
            if -12>ii[23]>-18 or ii[23]==9 and data[2]==12:
                screen.draw.text("[音葉]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
            if -3<ii[23]<6:
                    k1.k.y=300
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
            if 9<ii[23]<14:
                    screen.draw.text("[奈々子]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
            if 13<ii[23]<18:
                    screen.draw.text("[海斗]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
        i[4]=40#テキスト読んでいる間にアイテム欄など開けないように
        if ii[2]!=3:#ii[3]に入った数の回数、セリフを流してくれる
            screen.draw.text("SPACEキー➡文章スキップ",(100,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
        if ii[2]==3:
            screen.draw.text("Dキー➡次の文へ",(100,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
        if ii[9]==1 and ii[3]==1:
            screen.draw.text("itemをgetします、セーブしますか？",(327,0),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=22)#アイテムは最終段落中に増やすようにする
            screen.draw.text("はい→Q　いいえ→D　をクリック",(325,30),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=24)
            #if ii[3]==段落数 and 障害物.colliderect(c):※アイテムが手に入る場合はテキスト内でゲットさせる#シーンのテキストの時はシーン番号をかいておく
            #ii[15]=1ストーリー進めるii[15]=2ストーリー進めると同時にテキスト表示後自動でロック画面表示
        if ka[12]==0:
            if data[2]==-100:
                ii[15]=1
                ii[14]=1
                ii[23]=101
                if ii[3]==4:
                    screen.draw.text("│やーこんにちは!!このゲームをプレイする君に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ゲームの遊び方を説明する！17歳少年Tだよ!自│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│己紹介は以上だ！早速Dキーを押してくれ！!!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    
                    screen.draw.text("│OK！！君いいね！何かセリフや文章が流れたら│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│Dをすんだよ!笑笑。みんなわかったかなぁ～～│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│～！？それじゃあ、早速操作説明しよう！・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                   
                    screen.draw.text("│今、画面に、ちっちぇー(小さい)キャラクター│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│がこの部屋にいるんだけど!!www笑wげへへ!!そ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れが君が操作するキャラクターだよ!!アハハ!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                   
                    screen.draw.text("│そんじゃあ！じゃあまずは手始めとして、矢印│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│キーの「↑↓→←」を押して移動してみよう！│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│全てを試してみてくれ！とっても簡単だよ ^v^│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==-99:
                ii[15]=1
                ii[14]=1
                if ii[3]==6:
                    ii[23]=100
                    screen.draw.text("│素晴らしい！それじゃあ、wwwwwwww。えーと,,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あ！,,,,これで君もゲームプレイにいっぽ進ん│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だ！あははははwwwwwwwwwwwwwwwwwwwwwwwwwwww│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│ちなみにマジでどうでもいい話なんだけど！俺│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が目をモザイクしてるのは個人情報を漏らさな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いようにするためさ！！これが理由だよ！！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│でもそんなこと言ったら!なんで,テメー,,自分│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の顔写真をゲーム制作で使ってんだよってツッ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│コミでもきそうだな。ガハハハハハww,,,,,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=107
                    music[0]=13
                    screen.draw.text("│まあ、そんなふざけたことは置いとこう!!説明│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に戻るが、ゲーム中はマップを移動したりする│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│！！！その時は扉や通路を通ることになる！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│なので移動する際は扉や次の部屋につながる通│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│路にぶつかるだけでオーケーだぞ!!それ以外は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何もしなくていい!試しにぶつかってみよっか!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│このマップの右にある黒い細長いブロック(扉)│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にぶつかればOKだ,あのブロックは,このゲーム│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│内での扉だ！扉だと理解したらさっそく迎え！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==-98:
                ii[15]=1
                ii[14]=1
                if ii[3]==21:
                    ii[23]=103
                    screen.draw.text("│Hey！そう！その通りよくできた！！感動だ!笑│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│笑(嘘),実際はマップ移動するからな!今はチュ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ートリアルだから移動しないだけだからな!!!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[23]=102
                    screen.draw.text("│あと既に気づいた人もいるかもしれないが、基│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│本このゲームでは、画面の端のほうに何を押せ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ば何ができるかの説明が表示されるんだ！・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[23]=104
                    screen.draw.text("│だから、君たちはそれに従ってゲームをプレイ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│すれば大丈夫だ!!だからゲーム中に「何すれば│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いいかわからん!」ってなったら画面端を見ろ!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[23]=103
                    screen.draw.text("│何を押せば何ができるかの説明が書いてあるは│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ずだ!!基本それに従えばいい!!後は今操作した│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みたいに矢印キーでマップを探索すれば完璧!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=106
                    screen.draw.text("例➡目標[マップを探索してみよう]",(320,40),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
                    screen.draw.text("│その探索するときに1つ注意!実は今もそうなん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だが、ゲーム中は画面右上に緑の文字で目標と│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いうのが表示されたりするんだ。・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=104
                    screen.draw.text("例➡目標[マップを探索してみよう]",(320,40),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
                    screen.draw.text("│必ずこの目標に従ってゲームプレイをするよう│",(0,350),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│にするんだ!!じゃねーと先進むことできないか│",(0,390),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│らな!ストーリー進まんからな！充分注意しろ!│",(0,430),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                if ii[3]==15:
                    ii[23]=102
                    screen.draw.text("│それでは、次はセーブについて説明しよう、こ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のゲームではセーブできるタイミングが20回あ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│る。セーブポイントが20箇所ともいえるだろう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=107
                    screen.draw.text("│ストーリーが進めば自動的にセーブポイントが│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│来るからその時はちゃんとセーブすることを強│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くお勧めするぞ。・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[23]=106
                    screen.draw.text("itemをgetします、セーブしますか？",(327,0),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=22)#アイテムは最終段落中に増やすようにする
                    screen.draw.text("はい→Q　いいえ→D　をクリック",(325,30),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=24)
                    screen.draw.text("│ちなみに、セーブポイントが来たときは!!画面│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│右上に今写ってるみたいな感じで黄色い文字が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│表示される!。とりあえず今はDを押してくれ!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=105
                    screen.draw.text("│実際は,qキーを押すとセーブ画面に移動するぞ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│!!ゲーム内で今みたいな黄色い文字が表示され│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たら,qを押してセーブするようにすること・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=102
                    screen.draw.text("│まあ、20カ所あるとは言ったが、厳密に言えば│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な、このゲームでは新しいアイテムをゲットす│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るごとにセーブが可能なんだ、・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[23]=100
                    screen.draw.text("│ただ、ゲーム内でゲットするアイテムが20個だ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│からセーブポイントが20箇所あるって説明して│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いる感じだ。まあこれは気にしなくていい話だ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=102
                    screen.draw.text("│あと、セーブしたら、ホーム画面に戻った時に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│続きから始めるってボタンを押して、、続きか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らゲームを始めることができるよ、・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=107
                    screen.draw.text("│ストーリーが進めば自動的にセーブポイントが│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│来るからその時はちゃんとセーブすることを強│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くお勧めするぞ！・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("│また,ゲーム内ではsキーを押すことでアイテム│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│欄が開ける!画面端にもsキーでアイテム欄を開│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くって操作説明があるから参考にするといい！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=103
                    screen.draw.text("│あと、このゲームではeキーを押すことで,ヒン│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│トが見れる!!スムーズにゲームを進行させたい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("              スムーズにゲームを進行させたい│",(0,390),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│人はマジでこのヒントを大いに活用してくれ!!│",(0,430),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│とにかくヒントに関してはゲームでつまずくこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とがあったら、すぐ活用することをお勧めする│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│！ゲーム内には謎解きとかも入ってるからね!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=102
                    screen.draw.text("│ちなみに、ゲームストーリーが進むとギャラリ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ーの中身が変わるよ!!ホーム画面のギャラリー│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ボタンを押せば見れるから良かったら見てくれ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│!!それでは最後に,Dキーについて少し説明しよ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│う。このゲームでは、タンスや机などマップ内│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にあるさまざまな所をDで調べることができる!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=105
                    screen.draw.text("│ただ、ここで注意なんだが、調べる際は必ず足│",(0,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│を止めた状態にするよう心がけてくれ！実はこ│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│のゲームは,歩きながら調べることができない!│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                if ii[3]==1:
                    ii[23]=104
                    screen.draw.text("│ためしに今左側にあるPCを調べてみてくれ！た│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だ足を止めて！画面端にキーの説明が表示され│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│だ",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たタイミングで調べるようにしろ!絶対だぞ！?│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            if data[2]==-97:
                ii[15]=1
                ii[14]=1
                if ii[3]==8:
                    ii[23]=106
                    screen.draw.text("│おっけーだ！ちなみに今画面の向こうの君は文│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│章をDで読んでくれていると思うが,スペースキ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ーでスキップが可能だ（今は押さないように）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=104
                    screen.draw.text("│文章が全部表示される前にスペースキーを押せ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ば文章をスキップできる、ただ今はスキップす│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ると,この後の説明がきけなくなるからするな!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=105
                    screen.draw.text("│ではこのスキップするにあたり一つ注意がある│",(0,350),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│文章をスキップしてしまうと、セーブポイント│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│を逃す可能性がある、!!!!!!!!!!!!!!!!!!!!!!│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│※だからセーブしたい場合は、セーブポイント│",(0,350),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│(右上に黄色い文字が出る文章付近)でスキップ│",(0,390),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│しないように十分気をつけるようにしてくれ！│",(0,430),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                if ii[3]==4:
                    ii[23]=107
                    screen.draw.text("│説明はこんな感じだ、とりあえず後はゲームを│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│実際にやってみることだな、!!!!!!!!!!!!!!!!│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│このチュートリアルを終わりたい時は,Wキーを│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│押してスタート画面に戻ってくれ・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=104
                    screen.draw.text("│その時本当に終了しますか?!みたいな,,余計な│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│問いかけが上に表示されるとは思うが、今はチ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ュートリアルだから無視してくれ!ガン無視だ!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=103
                    screen.draw.text("│実際にゲームプレイ中も,Wキーで同じ感じに終│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│了できるぞ！！それじゃチュートリアルは以上│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だゲーム楽しんでくれ！あばよ！～wwwwww^ｖ^│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if 44<=data[2]<=54:
                ii[15]=1
                ii[9]=0
            if data[2]==44:
                if ii[3]==4:
                    ii[14]=1
                    ii[23]=3
                    screen.draw.text("│え！ここ何！壁の色が全て一色淡、灰色になっ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てる・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=6
                    screen.draw.text("│どうやら出口が作られると同時に新しくできた│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│通路みたいよ、じゃあ今から私が言う通りに動│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いて！！まずはこの通路をまっすぐに進んで！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=-5
                    screen.draw.text("│茶色いブロックが次の部屋につながる扉だわ、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そこにむかえばOKよ・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=4
                    screen.draw.text("│あ、はい！わかりました！・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==46:
                if ii[3]==1:
                    ii[23]=6
                    screen.draw.text("│よし！じゃあこの部屋も同じく、まっすぐ通路│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を進んで扉を目指して！・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==48:
                if ii[3]==1:
                    ii[23]=6
                    screen.draw.text("│この部屋は、まずは上に向かって走って、その│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あと壁にいくつか扉があると思うんだけど・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│右から2番目の扉に入って!・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==50:
                if ii[3]==1:
                    ii[23]=6
                    screen.draw.text("│ここの部屋にもいくつかドアがあるわ・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この部屋の一番右上にあるドアを目指して走っ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==52:
                if ii[3]==1:
                    ii[23]=6
                    screen.draw.text("│よし！この部屋には部屋の一番右下の所に扉が│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あるからそこに向かって走って！・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==54:
                if ii[3]==1:
                    ii[23]=6
                    screen.draw.text("│よし！後はこの通路を右に向かって走るだけだ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わ！！！頑張って！！！！！・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==2 and so[2]==1:#←シーンのセリフかon[3]←そのシーン中のどのセリフかso[2]
                ii[14]=2
                if ii[3]==8:
                    screen.draw.text("│思うようにならなかった時は苦しんだり、反対│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に思うようになった時は嬉しくなったり・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・このように人々には感情、心がある・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("│ただ、思うようにいかない事による心の苦しみ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が、果てしなく大きい場合は死を望んでしまう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│人もいる、自ら命を捨てたいと・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    screen.draw.text("│そのような、死に対する抵抗感が薄くなった人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│間を、屋敷に連れ込んで攫うお化けがいる。,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そのお化けは霊鬼と呼ばれるお化けだ・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│しかし、死を望んだとは言え、望んだ人すべて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が攫われるわけではない。その中でも、村の人│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│々からみて、存在価値の薄れた人を攫うんだ。│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│攫っても村の人々に何の悪影響も出ない・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そんな、不必要と言えてしまうような人間を,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│存在価値が薄れた人間を,,可哀想な人間を,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    if ii[2]<=3 and ii[1]>10:
                        tai[4].draw()
                    if ii[2]<=2 or ii[2]==3 and ii[1]<11:
                        tai[3].draw()
                    if ii[2]<=1:
                        tai[2].draw()
                    if ii[2]<=0:
                        tai[1].draw()
                    if ii[2]>0:
                        sikai.draw()
                    if ii[2]>1:
                        sikai.draw()
                if ii[3]==2:
                    screen.draw.text("[？？]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│ん～なんだろうこの変な感じ・・・・頭が痛い│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ってなんで、体にたくさん歩いた疲労があるよ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うな、ん？私そんな長距離歩いてないよね,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("[？？]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│あれ！・・・・・寝てたのかな？意識が遠のい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ていたような・・って・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・え？・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==2 and so[2]==7:#←シーンのセリフかon[3]←そのシーン中のどのセリフかso[2]
                ii[14]=1#←キャラクター表示
                if ii[3]==4:
                    music[0]=2
                    if kgyara[6]==0:#キャラクターギャラリー
                        kgyara[6]=1
                    ii[23]=5#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│ここはどこなの・・？・・そもそも私はなんで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こんなところにいるの？・・・何があったのか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わからない、・・・・・・・頭が整理できない│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=3#←表情設定
                    screen.draw.text("│確か、私は買い物に行って外に出て、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・ん～～思い出せない、、わからないことが│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│多すぎる・・・、あの後何があったんだっけ？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=2#←表情設定
                    screen.draw.text("│・・なんだか暗くて怖いな・・・・見たところ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│周りに人もいないし・・・・、心細い・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どうしよう、とりあえず出口とかないかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("│※矢印キーでプレイヤーを操作「←↑↓→」　│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│　Sキーでアイテム欄を開く「S」　　　　  　│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│　Dキーでマップ内の物を調べる「D」　　　　│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if  on[2]==-2 and kabe4.colliderect(cc)and on[4]==2:#体育館倉庫マップの壁４にぶつかってた時(時計を見るシーン)
                ii[15]=1#ストーリー進めるストッパー（data[2]の数値のストッパー）これをつけると、読み終わったらdata[2]に＋１される
                if ii[3]==3:
                    ii[14]=0
                    screen.draw.text("│とても古い時計だ、カチカチ音を立てながら、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│短針が回ってる、見た目からして長年使われて│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いるようだ・・・時計の針は22時を示している│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[14]=1#←キャラクター表示
                    ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│え！今こんな時間帯なの、どうしよう・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│お父さんとお母さん、心配してるかな・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・早く帰りたい・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[14]=1#←キャラクター表示
                    ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│あ、・・そうだ、電話とかないかな・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│電話を使えば助けを呼べるかも・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どこかにないかな・・・・・探してみよう・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if  on[3]==3 and so[2]==1:#体育館、電話見つけるシーン
                ii[15]=1
                if ii[3]==3:
                    ii[14]=1#←キャラクター表示
                    ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│あった、電話、早速使えるか試してみようかな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・ん～～～・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=4#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│反応しない・・古すぎるのかな？もう壊れちゃ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ってるのかな・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│全然動かない・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if  on[3]==3 and so[2]==5:#体育館、電話見つけるシーン
                ii[14]=1
                if ii[3]==4:
                    ii[23]=5#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│今何か大きな音が・・・！・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・だ、誰かいるの？・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│・・・・・・・・・・・もうここ怖いよ・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・早く帰りたい・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=2#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│あいにく、携帯電話も今は持っていないし・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんで、持ってこなかったんだろ・・・でも、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ここにいても、変わらないし・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│怖いけど、探索しなきゃ・・・・、そういえば│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何か外に出るのに役立ちそうな道具とかないか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な・・いいアイテムがないか探してみようかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if  on[2]==0 and kabe7.colliderect(cc) and data[2]<10:#体育館で鍵ゲット
                if ii[3]==1:
                    item[1]=1#鍵ゲット
                    gyara[1]=item[1]
                    ii[15]=1
                    ii[14]=1#←キャラクター表示
                    ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│こんなところに、何かのカギがある、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんだろう、多分どこかの部屋のカギかな・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とりあえず手にもっておこうかな・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if  on[2]==-1 and kabe5.colliderect(cc) and on[4]==2:
                if ii[3]==5:
                    ii[14]=1#←キャラクター表示
                    ii[23]=1
                    screen.draw.text("│青色の本が置いてある、この色、綺麗だな、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でもずいぶん、薄い本みたい・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│中に何が書いてあるんだろう、読んでみよう、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[14]=0
                    screen.draw.text("│5月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│今日、突然彼女が家を飛び出した、なぜ飛び出│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│したのかはわからない、でも早く見つけなきゃ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│6月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あれから一か月、警察も私も、ずっと彼女を探│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しているのに見つからない・・そろそろ疲れた│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│7月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きずいたら一人で泣いていた、今思えば私は、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│彼女に何もしてやれてなかった、情けなかった│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│8月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私は、初めて彼女にプレゼントを作った、もし│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いま天国にいるなら、喜んでくれてるかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if so[2]==3 and on[3]==4:#体躯倉庫でロック解除、
                if ii[3]==1:
                    ii[14]=1
                    ii[23]=3
                    screen.draw.text("│あれ！壁に書かれている五つの漢字の表記がい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きなり[隠れろ]っていう表記に変わった！？？│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どういうこと！？・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if so[2]==5 and on[3]==4:#体躯倉庫でロック解除、
                if ii[3]==2:
                    ii[14]=0
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[14]=1
                    ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│怖い、絶対おかしい、何かが私に近付いてきて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│る気がする、明らかに変な音がする、やだ・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│早くどこかに隠れなきゃ危ないかも、・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if  on[2]==-2 and kabe5.colliderect(cc) and data[2]==4:#体育館のロッカーに隠れる
                if ii[3]==8:
                    so[5]=1
                    ii[15]=1
                    time[1]=-1
                    item[2]=1#鍵2つ目
                    gyara[2]=item[2]
                    ii[14]=1
                    ii[23]=2#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│こんなところに私が入れそうなロッカーがある│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・ちょっと壊れかけだけど、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│見た感じ・・隠れることはできるかも・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│ほかに隠れれそうないい場所もなさそうだし、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ひとまずこの中に隠れようかな・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[14]=2
                    screen.draw.text("│（なんで私はこんな目にあっているんだろう、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私は何か悪いことしたのかな・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    music[0]=0
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│おさまったかな・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│迫ってくる音が聴こえなくなった・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そろそろ、出てみようかな・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・何もなければいいけど・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[14]=1
                    ii[23]=4#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│・・・・・・・見た感じもう大丈夫そう・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そういえば、ロッカーの中に何か入っていた気│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│がする・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    music[0]=2
                    ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                    screen.draw.text("│これは、なんだろう、カギ？・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│またどこかのカギなのかな？・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│使えるかもしれないから、拾っておこうかな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if so[2]==2 and on[3]==5:
                if ii[3]==2:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│あれ？・・・そういえば、今通った扉って、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│さっきまでなかった気がする。この部屋は初め│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てくるところだ・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│さっき手に入れたカギを使ったらこの扉開いた│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けど、なんでさっきまで見えなかったんだろ。│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私の見間違いだったのかな・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if so[2]==4 and on[3]==5:
                ii[14]=2
                music[0]=5
                if ii[3]==8:
                    screen.draw.text("│ある日一人ぼっちの少女がいました、少女には│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│友達がいませんでした・・・・ただ一人教室の│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│端っこの席で読書をするのが彼女の習慣でした│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("│彼女は友達を欲しがっていました・・しかし、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│不器用な彼女には周りの子たちと上手くなじむ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ことができませんでした・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    screen.draw.text("│彼女はクラスメイトの子たちと仲良くなろうと│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いろんな子にたびたび話しかけたりしました、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しかし思うように会話が弾むことはありません│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│そんな中、一緒に関わろうとと声をかけてくる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│彼女に、周りの子たちは不満を抱くようになり│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│次第に、その気持ちは悪化していきました、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│最終的に彼女は、周りから仲間外れにされたり│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│時には、ひどくいじめられ、悪口を言われる、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そんな羽目になってしまいます・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│次第に、彼女は心に傷を追うようになり、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│友達を作ろうと、話しかけるのをやめるように│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なりました・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│「傷つくぐらいなら、私は一人でいいや」、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そう考えるようになり、それ以降毎日、彼女は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│友達のいない学校生活を送るようになりました│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そういえば、私って嫌われているんだった・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            #if so[2]==4 and on[3]==5:
            if on[3]==14 and so[2]==4:
                ii[14]=2
                music[0]=5
                if ii[3]==27:
                    screen.draw.text("│そんな彼女に転機が訪れました・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・ある日、彼女のクラスで│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│席替えをする事になりました・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    screen.draw.text("│そこで彼女はとある男の子の隣の席になります│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・彼はとても気の利いた│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│優れた子でした・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    screen.draw.text("│「おはよう、少し気になったことがあるんだけ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ど、天野さんはお友達と話したり、周りにいる│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│クラスメイトと遊んだりしないの？・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    screen.draw.text("│特に彼女に悪い印象を持つこともなく・・彼は│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│仲のいいお友達とお話しするかのように話かけ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てくれました、彼女は彼にこう返しました・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    screen.draw.text("│「え？・・あ。いや・・その周りのみんなと、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│遊んだりして、仲良くなりたいなとは、思うの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でも私人づきあいがかなり苦手で・・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    screen.draw.text("│「その、なんかね、気づかないうちに悪気はな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いのに、いつの間にか相手を傷つけちゃったり│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│相手に嫌われるような事したりしちゃうの、」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    screen.draw.text("│「なんか、どうしても上手くなじめなくて、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんか、それで結局上手くかかわれないから、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│それが怖くて、、だから私は一人でいるの、」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    screen.draw.text("│自信のないその返答に対して、彼は悩むような│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しぐさを見せました、・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そして少年は、また彼女に問いかけました・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「でも・・1人でいて寂しくないの？,・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    screen.draw.text("│しばらく二人は会話を続けます・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│少女は、少年にこう返しました・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    screen.draw.text("│「まー・・寂しいけど、また嫌われたり傷つく│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ようなことはしたくないから、、私は、一人で│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いたいかな、もう友達つくる勇気もないし、」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    screen.draw.text("│「小学一年生の頃から、なかなかいい友達が作│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れなくてね・・・・やっぱ自分にとっては、、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│誰とも話さない事がもう1番いいのかなって,」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    screen.draw.text("│ーー少年ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「差し支えなければなんだけど、僕と友達にな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らない？・・・・・・・・・・・・・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「・・・え・・私が？・・いや、、嬉しいけど│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│悪いよ・・私は別に一人でも大丈夫だし・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「後、読書しか趣味がないから、みんなみたい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にゲームや、アニメのお話も知らないし・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「五十嵐君が思うような友達には・・・多分な│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れないと思う無意識に傷つけちゃうかも・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    screen.draw.text("│ーー少年ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「それでもいいよ！天野さんが仲良くなろうと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│頑張ってるのが分かれば僕は全然いいよ！、」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「え、・・・確かに仲良くなろうと頑張ってる│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けど・・・・・・・・・・・でも・・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    screen.draw.text("│ーー少年ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「実は少し気になってたんだ、みんなが笑って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るときも天野は笑顔を見せないなって・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    screen.draw.text("│ーー少年ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「僕もそんなに面白い人じゃないけど、よかっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たら気軽に友達として関わってもいいかな？」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「・・・・ほんとに・・いいの？・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│別に、変に気遣わなくていいんだよ・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    screen.draw.text("│ーー少年ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「気遣ってなんかいないよ！・・・・何かあっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たら、全然声かけていいからね！よろしく！」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「あ・・・うん・・えーっと五十嵐君よろしく│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・なんか、、えっと・・ありがと・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│ーー少年ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「お礼なんかいらないよww僕が仲良くなりたか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│っただけだから！、これからよろしくね！！」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│ーー少女ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「（・・・久しぶりにいいことがあったな・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・少しだけ元気が出た・・・・・・・・）」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│彼の行動は、まるで彼女の悩みを知っているか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のようなものだった、この瞬間、彼女の顔に、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│普段は見せない笑みが浮かんだ・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│彼の対応は、彼女がしてほしいと思う対応に、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│強く一致した・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そんな転機が訪れたのだった・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==1 and kabe5.colliderect(cc) and on[4]==2:
                 ii[14]=1
                 ii[23]=4
                 ii[15]=2
                 if ii[3]==3:
                    screen.draw.text("│館内マップだ、現在地とマップを見た感じ・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほんとに大きな建物みたい・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・私は今２階にいるんだ・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==2:
                    screen.draw.text("│・・・・・・・あれ？・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんか違和感がある・・・出口はどこなの？？│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・、見た感じどこもにない・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    screen.draw.text("│いや・・・そんなはずない・・・・じゃあ私、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どうやってここに来たの？ってことになるし、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もっとちゃんと見てみよう・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==6 and so[2]==2:
                 ii[14]=1
                 ii[23]=4
                 if ii[3]==1:
                    screen.draw.text("│この壁なんだろう、ちょっと気になるというか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ドアみたいな模様があるというか・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==6 and so[2]==4:
                 ii[14]=1
                 ii[23]=4
                 ii[15]=1
                 if ii[3]==2:
                    screen.draw.text("│・・・・！！！！！・・・・・・ドア？・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・よく見たら、ドアノブみたいな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何かがくっついてある・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    screen.draw.text("│でも開かないみたい,,とりあえず何かドアを開│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けれる手掛かりになりそうなものはないかな？│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もっと部屋の隅々までちゃんと調べてみよう,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==2 and kabe7.colliderect(cc):
                 ii[14]=1
                 ii[23]=4
                 ii[15]=1
                 item[3]=1#鍵2つ目
                 music[0]=5
                 gyara[3]=item[3]
                 if kgyara[6]==1:#キャラクターギャラリー
                        kgyara[6]=2
                 if siinn2[0]<=3:#ゲームストーリーギャラリー
                    siinn2[0]=4
                 k1.draw()
                 if ii[3]==22:
                    so[5]=1
                    ii[14]=0
                    screen.draw.text("[？？？]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・すごいね、この屋敷に来た人の中では、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│すごい珍しいね・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==21:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│・・・・（ん・・・今人の声が聞こえたような│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・でも周りにだれもいないし、、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│気のせいかな）・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==20:
                    ii[14]=1
                    ii[23]=5
                    screen.draw.text("│・・・・！！！！！壁から人が！！・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==19:
                    ii[23]=6
                    screen.draw.text("│ごめんね、急に驚かせちゃって・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│安心して、私はあなたを襲ったりなんかしない│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から・・後壁から出てきたわけじゃないよｗｗ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==18:
                    ii[23]=3
                    screen.draw.text("│え・・あの、・・・・え？・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・どういうこと？・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│怖い・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==17:
                    ii[23]=7
                    screen.draw.text("│・・・・・まあまあ・・・・・一回落ち着いて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、・・・でも知らない場所に迷い込んでこんな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│不思議な現象を見たらびっくりだよね・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==16:
                    ii[23]=2
                    screen.draw.text("│・・・誰なんですか？・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私は襲われるんですか？・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==15:
                    ii[23]=8
                    screen.draw.text("│だから私はあなたの味方だからｗｗｗ・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私の名前は音葉、この屋敷をうろついてるの、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│急に質問なんだけど調子はどう？大丈夫そ？,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==14:
                    ii[23]=3
                    screen.draw.text("│調子はどう？って・・・・・・・・それよりも│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│早く家に帰りたいです、私をここに連れてこさ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│せたのはあなたなんですか？・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==13:
                    ii[23]=6
                    screen.draw.text("│私じゃないよ、むしろあなたが自分からこの屋│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│敷に来たって感じかな・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│(この子に現実を押し付けるのは可哀想かな、)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==12:
                    ii[23]=2
                    screen.draw.text("│どういうこと？・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私この建物知らないよ・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ただ気づいたらここにいて・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==11:
                    ii[23]=6
                    screen.draw.text("│ここはそういう場所なの、ちょっと変わってる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│よね、まあ、ほんとに不思議な建物よ、でもこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の建物からからでれる場合もなくはないのよ,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==10:
                    ii[23]=3
                    screen.draw.text("│？？・・お願いします教えてください・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きっと家族も、家族も心配してるので・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==9:
                    ii[23]=9
                    screen.draw.text("│心配・・か、フーンまあ手助けはするよ、ただ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│その前にあなたに考えてほしいことがあるの、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あなたは今までたくさん苦しんできたと思う？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==8:
                    ii[23]=9
                    screen.draw.text("│・・・・ここの屋敷に来てしまう人の特徴に当│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てはまっているかを知りたくてね、・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==7:
                    ii[23]=2
                    screen.draw.text("│私は・・・苦しい記憶がたくさんありますね、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・でもなんでそんなことを聞くんですか？│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==6:
                    ii[23]=6
                    screen.draw.text("│ううん、なんでもないわ、そういえば今あなた│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│がそれぞれのパネルを正しい数字にそろえた事│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でさっきまで開かなかった扉が開いたみたいよ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==5:
                    ii[23]=6
                    screen.draw.text("│あと、あなたに気をつけてほしいことが一つ、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│霊鬼というお化けに遭遇したら、すぐに逃げて│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│そのお化けはあなたの命を狙ってるから、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                 if ii[3]==4:
                    ii[23]=1
                    screen.draw.text("│・・・・ん？？？・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・（霊鬼って何？命を狙ってるって│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いったいどういうこと？・・・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==3:
                    ii[23]=6
                    screen.draw.text("│とりあえず開いた扉の先を探索してみるといい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わ、その時現在地がわかるようにこの屋敷の館│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│内マップを渡すわね、では行ってらっしゃい、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==2:
                    ii[23]=3
                    screen.draw.text("│あ！・・・・・・・行ってしまった・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あれ？・・今の人がくれたんだ,館内マップだ,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いつの間に手に？とりあえず従うしかないかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("│Aキーを押すことで,自分が今どこにいるのかの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│現在地を確認できるようになりました・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│今いる部屋の位置を図で教えてくれます・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==1 and  kabe6.colliderect(cc) and on[4]==2:
                 if ii[3]==7:
                    ii[14]=1
                    ii[23]=4
                    screen.draw.text("│そういえばさっきは見てなかったけど、壁に何│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│か文が書かれてある,なんだろう？5人の会話と│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│その発言がそれぞれ記されてるみたいだ・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==6:
                    screen.draw.text("│あれ？でも,注意書きで[この中の5人のうちの2│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│人の発言は,まるっきり嘘の発言]と書いてある│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│誰がとまでは記してない,1人づつ読んでみよう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==5:
                    ii[14]=0
                    screen.draw.text("│Aさん「右にあるパソコンのミニゲームは,壁に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あるボタンを全て押さないとクリアできない、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そして白は9,だわ。これが正解!...........」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==4:
                    screen.draw.text("│Bさん「ミニゲームをクリアしたら白い文字で,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│[ゲームクリア！]と表示されてる！実際にプレ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│イしてみることだな,緑は8青は6だ赤は4だよ」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==3:
                    screen.draw.text("│Cさん「ミニゲームをクリアしたら,黒い文字で│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│[ゲームクリア！]と表示される緑は3白は6で赤│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は5だよ！！絶対これが正解..断言します!!!」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==2:
                    screen.draw.text("│Dさん「ミニゲーム内の牢屋の廊下には,壁にボ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│タンが設置されていない,黄色は5だよ、パネル│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の数字をそろえたら、黒い床を調べなさい!!」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    screen.draw.text("│Eさん「このミニゲームでは,牢屋の廊下の壁に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ボタンが設置されてある,黄色は2青は1だ,数字│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│をそろえたら開かなかった扉を調べなさい!!」│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 #if on[2]==8 and on[4]==2 and  kabe6.colliderect(cc):
            if on[2]==5 and kabe7.colliderect(cc) and so[2]==1 and  on[4]==2:
                 ii[14]=1
                 if ii[3]==1:
                    basyo[0]=1
                    ii[23]=4
                    screen.draw.text("│なんだろう、こんなところに何か書いてある、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「霊鬼は苦手なのは直線移動、ただ霊鬼が得意│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│とするのは斜め移動、十分気を付けるように」│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            if on[2]==7 and kabe5.colliderect(cc) and so[2]==1 and  on[4]==2:
                 ii[14]=1
                 if ii[3]==1:
                    basyo[1]=1
                    ii[23]=4
                    screen.draw.text("│なんだろう、こんなところに何か書いてある、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「霊鬼をまく方法は、マップをまたぐこと、ま│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│た、マップをまたぐほど霊鬼に遭遇しやすい」│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            if on[2]==-6 and kabe4.colliderect(cc) and so[2]==1 and  on[4]==2:
                 ii[14]=1
                 if ii[3]==1:
                    basyo[2]=1
                    ii[23]=4
                    screen.draw.text("│なんだろう、こんなところに何か書いてある、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│「霊鬼は壁をすり抜けて、あなたを追いかけて│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│る、捕まれば死んでしまう・・・・・・・・」│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            if on[3]==7 and so[2]==2:
                 ii[14]=1
                 ii[23]=4
                 ii[15]=1
                 if ii[3]==2:
                    screen.draw.text("│どうやら霊鬼？っていう何かに気をつけたほう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│がいいような記述が壁にいくつか書いてある、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんでこんなのが書いてあるんだろう・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    screen.draw.text("│ここには誰もいないし・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・気を付ける必要性もないと思うけど、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もしかしてまだ遭遇していないだけなのかな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==7 and so[2]==4:
                 ii[14]=1
                 if siinn2[0]<=4:#ゲームストーリーギャラリー
                    siinn2[0]=5
                 if ii[3]==2:
                    ii[23]=5
                    screen.draw.text("│・・・・！！！！！・・・・・・なに？・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・どこから出てきたの？！！！！│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    ii[23]=3
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│と、とりあえず早く逃げなきゃ！！！・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==8 and  kabe5.colliderect(cc) and on[4]==2 and data[2]==10:
                 ii[15]=1
                 item[4]=1
                 gyara[4]=item[4]
                 if ii[3]==14:
                    ii[23]=2
                    ii[14]=1
                    so[5]=1
                    screen.draw.text("│なんだろう、ここに一札だけ本が置いてある、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│本の表紙には霊鬼って書いてある、さっき壁に│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│も書いてあったな、読んでみようかな・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==13:
                    reiki[1].draw()
                    if ii[2]<3:
                        screen.draw.text("SPACEキー➡文章スキップ",(0,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
                 if ii[3]==12:
                    ii[23]=3
                    screen.draw.text("│確かに、一人暮らししたら、お化けに襲われち│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ゃうらしいから、絶対したくない！って周りの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│子は言ってたな、私はよくわからなかったけど│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==11:
                    ii[23]=4
                    screen.draw.text("│でも、思い返せば、そのお化けってもしかして│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│霊鬼のことだったりするのかな？おそらくこの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│本に書いてある内容は私が住んでいる村で・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==10:
                    ii[23]=4
                    screen.draw.text("│私自信、あまり心配されてなかったからそんな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│忠告は誰からも言われたことなかったけど、恐│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らくこの本に書いてある内容はこの村のことだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==9:
                    ii[23]=2
                    screen.draw.text("│でも霊鬼の屋敷ってなんだろう？もしかして今│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私がいる建物って霊鬼の屋敷だったりするのか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な？さっきも霊鬼って単語が壁に書かれてたし│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==8:
                    screen.draw.text("│ただ、私一人暮らししてないから、この本を読│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│む限り、霊鬼に襲われる事は無いはずなのに、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何なんだろう・・・何かの悪い夢だと信じたい│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==7:
                    screen.draw.text("│でもあの怪物を見た限りは急いでここから出な│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くちゃ,今からどうすればいいのかなぁ,でも普│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│通に考えたら建物の出口って1階にあるよね,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==6:
                    screen.draw.text("│もうおびえてなんかいられないし,,,1階を探索│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│してみようかな、でもどんどん荷物も増えてき│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たから、必要なさそうなものは戻そうかな、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==5:
                    ii[14]=0
                    screen.draw.text("│ーーーこの先のゲームについて補足説明ーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│天野美香は(現在操作しているキャラクター)は│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│アイテムを5つまでしか持つことができません,│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                 if ii[3]==4:
                    screen.draw.text("また,ITEMが置いてあった場所には,緑の矢印の表示がされるように\nなります！この表示も,ITEMを拾う際や戻す際に参考にしましょう!",(0,150),fontname='a.ttc',owidth=3,color="LIGHT GREEN",fontsize=23)
                    screen.draw.text("[新しく追加されたITEM欄の機能について補足説明↓]",(6,20),fontname='a.ttc',owidth=5,color="BLUE",gcolor="WHITE",fontsize=28)
                    screen.draw.text("　 [↓アイテムを元の場所に戻す際の補足説明↓]",(6,110),fontname='a.ttc',owidth=5,color="GREEN",gcolor="WHITE",fontsize=28)
                    screen.draw.text("SキーでITEM欄を開いた時に,手持ちにあるアイテムが元々どこにあ\nったのかが、見れるようになりました,戻す際は参考にしましょう!",(0,60),fontname='a.ttc',owidth=3,color="LIGHT BLUE",fontsize=23)
                    screen.draw.text("│手持ちのアイテムをゲットしたところを再度調│",(0,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│べると、もともとそこにあったアイテムを元の│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│位置に戻せます（※一部戻せないものもある）│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                 if ii[3]==3:
                    screen.draw.text("また,ITEMが置いてあった場所には,緑の矢印の表示がされるように\nなります！この表示も,ITEMを拾う際や戻す際に参考にしましょう!",(0,150),fontname='a.ttc',owidth=3,color="LIGHT GREEN",fontsize=23)
                    screen.draw.text("[新しく追加されたITEM欄の機能について補足説明↓]",(6,20),fontname='a.ttc',owidth=5,color="BLUE",gcolor="WHITE",fontsize=28)
                    screen.draw.text("　 [↓アイテムを元の場所に戻す際の補足説明↓]",(6,110),fontname='a.ttc',owidth=5,color="GREEN",gcolor="WHITE",fontsize=28)
                    screen.draw.text("SキーでITEM欄を開いた時に,手持ちにあるアイテムが元々どこにあ\nったのかが、見れるようになりました,戻す際は参考にしましょう!",(0,60),fontname='a.ttc',owidth=3,color="LIGHT BLUE",fontsize=23)
                    screen.draw.text("│また、元の場所に戻したアイテムを再び取るこ│",(0,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│とも可能です。アイテムが5つの状態だと,新し│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│いアイテムをゲットすることができません、、│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                 if ii[3]==2:
                    screen.draw.text("また,ITEMが置いてあった場所には,緑の矢印の表示がされるように\nなります！この表示も,ITEMを拾う際や戻す際に参考にしましょう!",(0,150),fontname='a.ttc',owidth=3,color="LIGHT GREEN",fontsize=23)
                    screen.draw.text("[新しく追加されたITEM欄の機能について補足説明↓]",(6,20),fontname='a.ttc',owidth=5,color="BLUE",gcolor="WHITE",fontsize=28)
                    screen.draw.text("　 [↓アイテムを元の場所に戻す際の補足説明↓]",(6,110),fontname='a.ttc',owidth=5,color="GREEN",gcolor="WHITE",fontsize=28)
                    screen.draw.text("SキーでITEM欄を開いた時に,手持ちにあるアイテムが元々どこにあ\nったのかが、見れるようになりました,戻す際は参考にしましょう!",(0,60),fontname='a.ttc',owidth=3,color="LIGHT BLUE",fontsize=23)
                    screen.draw.text("注意※一度ゲットしたアイテムを再度ゲット場合は",(0,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("セーブできません!!セーブできるのは、初めてその",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("アイテムをゲットした時のみになるので注意!!!!!!",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("注意※",(0,350),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                 if ii[3]==1:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│あれ、よく見たら本の間に何かが挟まってるこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れは何かのメモかな？・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-5 and on[4]==2 and kabe4.colliderect(cc) and on[3]!=9:
                if ii[3]==1 and ka[11]==0:
                    kagi[1].draw()
                    kagi[2].draw()
                    kagi[3].draw()
                    screen.draw.text("│ホンがいくつかおいてある・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1 and ka[10]==1:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1 and ka[10]==2:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│服飾デザイン科の部屋のカギをゲットした・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1 and ka[10]==3:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│デザイン科の部屋のカギを・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            #if  (on[2]==-6 and on[4]==2 and kabe5.colliderect(cc))or (on[2]==-5 and on[4]==3 and kabe4.colliderect(cc)):
                    #ii[3]==1
                   # screen.draw.text("│黒板だ、何か書いてある、なんだろう・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    #screen.draw.text("│アルファベットが並んでる・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                   # screen.draw.text("│でも四角になってるところもある・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==11 and so[2]==2:
                 ii[14]=1
                 if ii[3]==3:
                    ii[23]=2
                    screen.draw.text("│どうやらここが出口のようには思えるけど・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんでだろう、外に出ることができない・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・でもここが出口に見えるんだけど│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==2:
                    ii[23]=2
                    screen.draw.text("│ただ、出口の扉があかないなら、しょうがない│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│カギを探したりするしかないか・・でも建物の│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│中からなら普通外に出れる気もするんだけどな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("[？？？]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│あら・・・こんにちは、お嬢さん・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・もしかしてこのお屋敷で迷ってしまった│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│感じかしら？・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==11 and so[2]==4:
                if ii[3]==1:
                    ii[14]=1
                    ii[23]=3
                    screen.draw.text("│だれ!・・・・・・・・・どこからか声が!!,,,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│（もしかしてまた壁の中からいきなり誰かが出│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てきたりして）・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==11 and so[2]==7:
                ii[15]=1
                item[5]=1
                gyara[5]=item[5]
                music[0]=5
                if kgyara[6]==2:#キャラクターギャラリー
                    kgyara[6]=3
                if siinn2[0]<=5:#ゲームストーリーギャラリー
                    siinn2[0]=6
                if ii[3]==28:
                    ii[14]=1
                    ii[23]=2
                    so[5]=1
                    screen.draw.text("│また、壁の中から人が出てきた、この屋敷の人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│はなんで壁をすり抜けることができるの？・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この現象を見るたびにびっくりする・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==27:
                    ii[23]=10
                    screen.draw.text("│あら、・・また・・・ってことは、多分その感│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│じだと、もうこの屋敷ですでに誰かに話しかけ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│られたかんじかしら・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    ii[23]=2
                    screen.draw.text("│え？・・・・あ・・まあ・・はい、そうです、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│その人も急に壁から出てきて私に話しかけてき│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て・・(この人も悪い人ではなさそう・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    ii[23]=3
                    screen.draw.text("│あの、それより気になるのですが、なんで壁を│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│すり抜けることができるんですか？、・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・私にはそんなことできないのですが│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    ii[23]=10
                    screen.draw.text("│あら、まだ何も知らないらしいわね、何も知ら│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないみたいだから少し教えてあげようかしら、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・でも聞き流してもらっても構わないわ、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    ii[23]=11
                    screen.draw.text("│実は、私はもう他界してしまってるの、そして│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│今の私は幽霊の状態になっているのよ、あなた│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にさっき話しかけてきた子もおそらく同じよ、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    ii[23]=12
                    screen.draw.text("│でも普通、幽霊は人間の目では見ることができ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないのよ、、でもこの屋敷では、それが可能な│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│状態になっているものすごく特殊な屋敷なの、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    ii[23]=12
                    screen.draw.text("│でもこの屋敷に出てくる幽霊の大半は霊鬼とい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うお化けに攫われて命を落としてしまった人達│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、もちろん私もそのうちの一人よ・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[23]=11
                    screen.draw.text("│まあそんな感じに、一歩現実離れした、幽霊の│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│さまよう屋敷に、あなたは今いるって状態なの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    screen.draw.text("│本題に戻るけど、壁をすり抜けれるわけは、す│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でに幽霊になってしまったことで、物理的な概│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│念がなくなったからなの、、、、、、、、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    screen.draw.text("│厳密にいえば壁を狙ってすり抜けているわけじ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ゃなくて壁にそもそもぶつかることができない│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みたいな感じかな・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=10
                    screen.draw.text("│私なりに説明したけどどうかな？わかったかな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│？・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│(変な人に思われたかも・・・・・・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=3
                    screen.draw.text("│すみません、私コミュニケーションが元々苦手│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でちょっと話についていけないませんが、とに│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かく生きている状態ではないって感じですか？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[23]=12
                    screen.draw.text("│まあそんな感じね、、ごめんね、わかりにくく│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て・・・・でもあなたみたいなまだ小さい子が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こんなところに来るのはほんとに珍しいのよ、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=11
                    screen.draw.text("│普通は年寄りとか、独身の人がよくここに来る│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のに,(まぁ私も生きて、ここをさまよって行っ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た時は似たようなことを幽霊にいわれたけど）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[23]=1
                    screen.draw.text("│ん？・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=11
                    screen.draw.text("│まぁそれはそうとしてあなたに一つ質問したい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のだけれど、あなたはこの屋敷に訪れる前、誰│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かに大切にされていたとは思う？・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=3
                    screen.draw.text("│え、あー大切にされていた、、か、、、そこま│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│で大切にされていた記憶は無いのですが、あ、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でも1人だけ仲の良い男の子が最近できて,,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    screen.draw.text("│その子はたくさん気遣ってくれました、その時│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は大切にされたかもなと感じましたね・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まあ、別に大したことではないと思いますが、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=13
                    screen.draw.text("│そう・・・・なるほどね、・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・,(この│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│子はまだ見捨てられてない可能性があるわね),│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=1
                    screen.draw.text("│ん？どういうことですか？・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=11
                    screen.draw.text("│まだ断言することはできないけど、、あなたは│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まだ助かるかも、話を聞く感じきっとあなたな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らここから出られると思うわ・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=3
                    screen.draw.text("│ほ、ほんとですか！どうすればいいですか？！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=12
                    screen.draw.text("│いや、あなたなら出口を見つけることができる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│んじゃないかと思っただけよ、あくまで出口と│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かの場所を知ってるわけじゃないから・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=11
                    screen.draw.text("│でも、あなたには無事にここから脱出してもら│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いたいわ、とりあえず頑張ってね！応援してる│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わ・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=3
                    screen.draw.text("│あ！いってしまった、もう少しいろいろ質問し│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たかった、・・そういえばあの人名前名乗って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なかった,,,,何て名前の人だったんだろう？..│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=1
                    screen.draw.text("│ん？あれ？よく見たら床に何か落ちてる・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もしかして、これが出口のカギ？・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・いやでもカギ穴の形が全然違う・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=1
                    screen.draw.text("│ん？カギに何か書いてある・・・これは・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│1Fデザイン科って書いてある・・1Fのどこかの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│部屋のカギみたいだ、少し探してみようかな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-6 and on[4]==1 and data[2]==12 or on[2]==8 and on[4]==2 and not kabe5.colliderect(cc)and data[2]==12:
                ii[15]=1
                ii[14]=1
                kotarou1.draw()
                otohac.draw()
                if kgyara[6]==3:#キャラクターギャラリー
                        kgyara[6]=4
                if siinn2[0]<=6:#ゲームストーリーギャラリー
                    siinn2[0]=7
                if ii[3]<28:
                    music[0]=11
                if 29==ii[3]:
                    music[0]=0
                if ii[3]==1:
                    music[0]=0
                if ii[3]==33:
                    ii[23]=1
                    screen.draw.text("│なんだろう、机に金庫みたいなのがおいてある│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほかの机には何もないみたい・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほんとにここで絵をかいたりしてるのかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==32:
                    screen.draw.text("│でも金庫はロックがかかって開かない,,あれ？│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│机の下の床に何か書いてある、なんだろう、、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│[色を3つ見つければ金庫の暗証番号がわかる],│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==31:
                    ii[23]=4
                    screen.draw.text("│どういうこと？、インク？絵の具？・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とりあえず色を見つけたらこの金庫のロック解│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│除の番号がわかるってことかな？なにこれ？,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==30:
                    ii[23]=1
                    screen.draw.text("│あれ,さっき拾ったカギよく見たらデザイン科a│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│号室b号室のカギって書いてある,他にも入れる│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│部屋があるってことかな？少し行ってみよう,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==29:
                    ii[14]=2                                                                                                
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そのころ、別の場所では・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│対立が繰り広げられていた・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==28:  
                    on[2]=8
                    on[4]=2
                    ii[14]=1
                    hito[3].topleft=(500,40)
                    ii[23]=9
                    serihu[0]=1
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│(探索した跡がある・・・・見た感じ,あの子は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まだちゃんと生きてるみたい・・良かった,,,)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==27:
                    hito[3].topleft=(20,40)
                    on[2]=8
                    on[4]=2
                    ii[14]=0
                    screen.draw.text("[？？？]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│なあ、なんで、君はいつもそうやって誤魔化す│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│んだ、さっさと言ってしまえばいいのに、だか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ら君はまた苦しむんだよ・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    on[2]=8
                    on[4]=2
                    ii[23]=-14
                    screen.draw.text("│・・・・・・・・!!・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・(この声はおそらく・・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    on[2]=8
                    on[4]=2
                    ii[23]=-14
                    screen.draw.text("│なんのようなの？小太郎・・・・・・・・・ま│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た私を否定しにきたの？・・・・・・・いつも│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│邪魔ばっかしてきて、・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    on[2]=8
                    on[4]=2
                    ii[23]=-32
                    screen.draw.text("│邪魔とは,ひどいな～,僕はただこの屋敷に迷い│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│込んでしまった人たちに現状を教えているだけ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だよ。君の邪魔なんて何もしてない・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==23:
                    on[2]=8
                    on[4]=2
                    ii[23]=-13
                    screen.draw.text("│それが邪魔なのよ、毎回貴方が現実を押し付け│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るせいで、この屋敷に迷い込んでしまった人た│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ちが脱出を諦めてしまうじゃないの！・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    on[2]=8
                    on[4]=2
                    ii[23]=-15
                    screen.draw.text("│迷い込んでしまった人間に、わざわざ現実を押│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│し付ける必要なんてないでしょう。むしろ脱出│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│できるように協力してあげるべきじゃないの？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    on[2]=8
                    on[4]=2
                    ii[23]=-32
                    screen.draw.text("│まあ、そういう考え方も一理あるよ。ただね、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│結局出れないんだよ。出れる人なんてほとんど│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いないんだよ。、・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    on[2]=8
                    on[4]=2
                    ii[23]=-33
                    screen.draw.text("│逆に出れるって期待した挙句に後々現実を見て│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│絶望する方が僕は迷い込んでしまった人に申し│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│訳ないと思うけどな、君はそうは思わないの？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    on[2]=8
                    on[4]=2
                    ii[23]=-14
                    screen.draw.text("│・・・・・・・そうだけど、・・・最後まで希│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│望を捨てないで頑張ろうとは思わないの？可能│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│性はゼロでは無いのよ、少しはあるのよ？・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    on[2]=8
                    on[4]=2
                    ii[23]=-33
                    screen.draw.text("│少しはあるって言ったってそれがどれぐらいの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│確率なのかを知ったらみんな諦めるだろ・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==17:
                    on[2]=8
                    on[4]=2
                    ii[23]=-30
                    screen.draw.text("│だったら、最初から死を受け入れる体制を作っ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ておくように言っといたほうが僕はいいと思う│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けどな、・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    on[2]=8
                    on[4]=2
                    ii[23]=-32
                    screen.draw.text("│なんせ、ここに来た人はみんな死を望んでるん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だし。ある意味助けようとしないのもその人に│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とっていいんじゃないのか？・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    on[2]=8
                    on[4]=2
                    ii[23]=-16
                    screen.draw.text("│・・・うるさいわね・・・あなたに何を言われ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ようと私はあきらめないわ、・・だから、私は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あの子に現実をストレートに伝えたりはしない│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    on[2]=8
                    on[4]=2
                    ii[23]=-16
                    screen.draw.text("│むしろ最後まで言わないようにするわ！この屋│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│敷から出れるって希望的であってもらわないと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│脱出なんてできないもの・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==13:
                    on[2]=8
                    on[4]=2
                    ii[23]=-33
                    screen.draw.text("│君が言わないなら、今回も俺が直接伝えておこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うかな、ここに迷い込んできた人に本当の現実│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    on[2]=8
                    on[4]=2
                    ii[23]=-15
                    screen.draw.text("│！！！・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・なんで、あの子はこの屋敷に来た│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│人の中でも特に頑張ってるじゃない！！！！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    on[2]=8
                    on[4]=2
                    ii[23]=-15
                    screen.draw.text("│なんであの子まで陥れようとするの！さすがに│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│それはやめて！お願いだから、・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    on[2]=8
                    on[4]=2
                    ii[23]=-31
                    screen.draw.text("│ふーん、だったらお前の口からあの子に現実を│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│伝えろ、お前が伝えないなら、俺が伝えにいく│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│。,,すまんな、俺はお前の考えには乗れない！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==9:
                    on[2]=8
                    on[4]=2
                    ii[23]=-13
                    screen.draw.text("│だから、もうあなたは何もしなくていいのよ。│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ただ見てるだけでいいから、だから黙っていて│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・お願いだから・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    on[2]=8
                    on[4]=2
                    ii[23]=-33
                    screen.draw.text("│もういいよ。話聞いてなさそうだから、あの子│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にいまの置かれている現状を伝えに行くわ。じ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ゃあね・・・・・・・・・バイバイ・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    on[2]=8
                    on[4]=2
                    ii[23]=-12
                    screen.draw.text("│あ！ちょっと待って！、・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・勝手に話を先に進めないで！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    on[2]=8
                    on[4]=2
                    ii[23]=-31
                    screen.draw.text("│なんだよ,君は話さないんじゃなかったのかよ,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どうせ助けようとしたところで無駄なんだ、、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なら、ちゃんと事実は言うべきだ・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    on[2]=8
                    on[4]=2
                    ii[23]=-16
                    screen.draw.text("│わかったから、・・ちゃんと話すから、自分の│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│口から話すから、だから貴方はおとなしく、黙│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ってて・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==4:
                    on[2]=8
                    on[4]=2
                    ii[23]=-33
                    screen.draw.text("│ふーん、わかったよ、ちゃんと言えよ、見とく│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から、・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    on[2]=8
                    on[4]=2
                    ii[23]=-16
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[14]=2
                    on[2]=-6
                    on[4]=1
                    screen.draw.text("│(いつか必ず,この屋敷から救って見せるんだか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ら!・・・・・迷い込んでしまった人間を・・)│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    on[2]=-6
                    on[4]=1
                    ii[23]=1
                    serihu[0]=0
                    screen.draw.text("│ん？何かの気配が？,,気のせいか,,でも新しい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│部屋でもITEMをゲットできるようにしたいから│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いらないITEMを元に戻してから探索しに行こう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==14 and so[2]==2:
                ii[15]=1
                ii[14]=1
                if kgyara[6]==4:#キャラクターギャラリー
                    kgyara[6]=5
                if siinn2[0]<=8:#ゲームストーリーギャラリー
                    siinn2[0]=10
                if ii[3]<=33:
                    music[0]=5
                if ii[3]>33:
                    music[0]=4
                k3.draw()
                if ii[3]==42:
                    ii[23]=1
                    screen.draw.text("│金庫のロックが解除された、中に何か入ってる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・なんだろう、これは本かな？,,どうやら霊│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│鬼についての本みたい,,少し読んでみようかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==41:
                    reiki[2].draw()
                    if ii[2]<3:
                        screen.draw.text("SPACEキー➡文章スキップ",(0,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
                if ii[3]==40:
                    ii[23]=2
                    screen.draw.text("│霊鬼は人を襲うために、自分のいる屋敷まで人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を連れて来るみたい、あと連れて来られた人は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│来るまでの記憶がないみたい..多分私も同じだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==39:
                    ii[23]=2
                    screen.draw.text("│でもそしたらなんで日常生活の中で攫われる人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│をあまり見ないんだろう、しかも不思議となぜ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私だけがここに連れて来られてしまったの？,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==38:
                    ii[23]=2
                    screen.draw.text("│この文章を見た感じだと入り口は封鎖されてし│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まっている？それが本当ならもう出れない？、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でもそれを言ったら音葉さんの発言に矛盾が,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==37:
                    ii[23]=1
                    screen.draw.text("│ただ、出口は見つからなくても、霊鬼の内容の│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│本があったりするからこの調子で調べていけば│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いずれ私がここにいる理由もわかりそう・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==36:
                    ii[14]=0
                    screen.draw.text("[？？？]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│その本を、見つけたんだ、さすがだね・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│その調子で屋敷を探索してみるといいよ・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==35:
                    ii[14]=1
                    ii[23]=2
                    screen.draw.text("│またどこからか声が！・・・・でも声からして│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まだ話したことがない幽霊みたい、誰だろう、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│またどこかから出てくるのかな・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)            
                if ii[3]==34:
                    ii[23]=1
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│（また新しい幽霊が出てきたな・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・今度はどうやら男の人見たい）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==33:
                    ii[23]=15
                    screen.draw.text("│あれ、君おどろいたりしないの？・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・すごいね・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│普通だったらすごく驚きそうな気もするけど、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==32:
                    ii[23]=3
                    screen.draw.text("│いえ、、実はこの屋敷に来てから何回か幽霊と│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は話したので・・・今となってはもう慣れまし│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==31:
                    ii[23]=14
                    screen.draw.text("│ここにいるってことは、君はまだ霊鬼につかま│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ってないんだね!!、しかも屋敷のこんな細かい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│所まで探索してるなんて本当にたくましいよ..│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==30:
                    ii[23]=16
                    screen.draw.text("│申し遅れたね・・・僕の名前は海斗だ・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この屋敷をうろついている幽霊さ・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この屋敷の霊鬼にさらわれて他界した人なんだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==29:
                    ii[23]=17
                    screen.draw.text("│実は僕はこの屋敷に閉じ込められていた時に君│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みたいに勇気をもって屋敷を探索出来なかった│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│んだ、そのせいで僕はすぐに霊鬼に捕まった、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==28:
                    screen.draw.text("│でも,もしかしたら,僕の場合は出口が作られて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たのかもって,,この屋敷から出られる人間だっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たのかもって,,いまだにそれを後悔してるんだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==27:
                    ii[23]=4
                    screen.draw.text("│..ん？「僕の場合は出口が作られてたのかも」│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│っていうのは,,,,具体的にどういうことですか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│？・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    ii[23]=16
                    screen.draw.text("│実はね、この屋敷には出口が作られてないんだ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でも・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    ii[23]=5
                    screen.draw.text("│！！！出口が作られてない？！！え、つまり出│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│口がないってこと！！？ってことは私は出るこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とができないってこと？！！・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    ii[23]=3
                    screen.draw.text("│え、、それってほんとなんですか？・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│じゃあもう私はこの屋敷から出られないってこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│となんですか？・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    ii[23]=16
                    screen.draw.text("│いや,実は出口がないのは,君みたいな、霊鬼に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│閉じ込められた人間が外に出られないようにす│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るためなんだ、だけどそれには一部例外もある│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    ii[23]=3
                    screen.draw.text("│どういうこと？出口がないってことは、もうこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こで霊鬼にさらわれて死ぬのを待つ事しかでき│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないんじゃないの？・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    ii[23]=14
                    screen.draw.text("│実は霊鬼というお化けはある一定の基準を満た│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│してる人間だけを狙ってるんだ、満たしてる人│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│間だけを屋敷に閉じ込めて攫おうとしてるんだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[23]=16
                    screen.draw.text("│ただ時々その基準を満たしてない人間を霊鬼が│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│間違えて屋敷に閉じ込めてしまう時もあるんだ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、霊鬼が閉じ込めたくないと思う人間をね,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[23]=17
                    screen.draw.text("│実はそういう時だけ！基準を満たしてない人が│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│外へ脱出することができるように、屋敷のどこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かに出口が作られるようになっているんだ・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[23]=16
                    screen.draw.text("│つまり霊鬼の屋敷の特徴的な部分は、お化けと│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│人間が関われるという部分だけではないんだ、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・それ以外にも特徴的な部分はある│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=16
                    screen.draw.text("│間違えて霊鬼が基準を満たしてない人を中に閉│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│じ込めてしまった場合はその人が脱出できるよ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うに自動で出口ができるという特徴もあるんだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=2
                    screen.draw.text("│？？じゃあ、閉じ込められたとしても、その基│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│準を満たしてなかった場合は、その時だけは屋│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│敷から脱出することが可能って感じですか？..│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[23]=16
                    screen.draw.text("│そう、でも出口は屋敷のどこかにランダムで作│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│られるようになってるから、作られても探索す│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│る勇気がないと脱出できないって感じだ,,,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=16
                    screen.draw.text("│もちろんランダムな場所に出口が作られるから│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│変な話,1階に出口が作られるとも限らないんだ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│３階,4階に作られることも全然ある・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[23]=3
                    screen.draw.text("│少しややこしくなりそうですが、なんとなくわ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かりました、でも、基準？、基準って具体的に│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どういうのなんですか？・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=3
                    screen.draw.text("│その基準のラインに引っかかっていなければい│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いってことですよね？閉じ込められても霊鬼が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│求める人間の基準を私が満たしていなければ、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=16
                    screen.draw.text("│そう、基準を満たしていない状態だったら出口│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│があるってことだからね、基準のラインについ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ての説明は、、ん～なんていえばいいのかな..│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[23]=17
                    screen.draw.text("│上手く説明できるかわからないけど、見放され│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ている人間であるかそうじゃないかみたいな感│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│じかな？見放されてたら基準を満たしていて,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=2
                    screen.draw.text("│？？？・・・・・・？？？・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・？？？？？？？？？・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=17
                    screen.draw.text("│ごめん、僕の説明力じゃ少し難しいかもしれな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│い、ただ、とりあえずその基準を満たしている│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│か、いないかで変わってくるってことだよ、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=16
                    screen.draw.text("│でも、今君が見つけて読んだ本のように、霊鬼│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│についての内容が書かれている本はこの屋敷に│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほかにもいくつかあった気がするよ・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=16
                    screen.draw.text("│その本を読めばきちんと理解できるかもしれな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│い、よかったら出口以外にも、そういう本とか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を探してみることもオススメするよ・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=4
                    screen.draw.text("│いろいろ説明してくれてありがとうございます│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まだ私は自分がその基準を満たしていないかが│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わからないのでついでにその本も探してみます│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=16
                    screen.draw.text("│よしじゃあ引き続き頑張ってね・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・幸運を願ってるよ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=4
                    screen.draw.text("│どこかに消えていってた、、ただ、今の話で分│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かったのは、出口は屋敷のどこかにランダムで│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│作られるってことだ、(なんかややこしいな..)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=1
                    screen.draw.text("│話によれば、おかしな話だけど一階以外の階に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│出口が作られる可能性も全然あり得る・・・一│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│階以外の階も探してみるのも全然ありだ・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=1
                    screen.draw.text("│1階と2階はある程度探索したから,次は3階を探│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│索してみようかな、、この屋敷の事や、私がこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こにいる理由がもっとわかるかもしれない・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            #if on[3]==14 and so[2]==4:
            if on[3]==15 and so[2]==4:
                ii[14]=2
                music[0]=5
                if ii[3]==10:
                    screen.draw.text("│五十嵐君と友達になってから彼は私にとても優│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しくしてくれた,私が1人でいる時も優しく話し│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かけてくれて,,私をよく気遣ってくれた、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    screen.draw.text("│私がずっとついていけなかった勉強も、五十嵐│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│君は頑張って私に教えてくれた,,あらゆる気力│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を失ってしまった私を元気づけてくれた・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    screen.draw.text("│おかげで、私は、席替えして以来、学校に行く│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のが少し楽しかった、毎日の生活がガラッと変│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わった、本当に変わった・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("│ただ、つくづくとあの事件が起きなければよか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ったのになとおもっていた、でも五十嵐君はそ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│んな、落ち込んだ私の心にも寄り添ってくれた│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    screen.draw.text("│あれ以来私は、そんな彼の優しさに助けられて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いた、ただ私は、、彼に何もお返しする事がで│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きなかった、それが申し訳なかった・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│私が彼に、してほしい事がないか尋ねても、彼│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は私に何かをしてほしいというわけではなかっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│一緒に遊んだり、話し相手になってくれてるだ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けで、もう十分だから、お返ししようなんて考│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│えなくていいよ！・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│そんな感じに、いつも言葉を返してくれるのだ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・私はなんて、返事を返せばいいかわ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│からなかった・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│ただ一つだけわかるのは、本当に五十嵐君は優│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しいという事だった、どんな人に対しても優し│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│く接してくれるということだ・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│本当に彼の隣の席に座れてよかったなーと、私│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は思うようになった、精神的にも今の苦痛に対│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しても彼の隣になれたことがほんとによかった│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-2 and  (kabe5.colliderect(cc)or kabe4.colliderect(cc)or kabe6.colliderect(cc)) and on[4]==1 and data[2]==13:
                 ii[15]=1
                 item[6]=1
                 gyara[6]=item[6]
                 if ii[3]==2:
                    ii[14]=1
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│こんなところにポツンと何かが置いてある、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これは黄色い絵の具だ・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│一応まだ使えそうだ・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    ii[23]=1
                    screen.draw.text("│色をそろえるって、絵具をそろえるとか、そう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いうことだったりするのかな？・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まあこの調子でもう少し探索してみようかな。│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==0 and item[7]==0 and item[8]==0:#白
                 if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("│本に何か書いてある、私は白、絵の具持った状│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│態でこの部屋にきてごらん、・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きっと何かが変わるよ・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==1 and item[7]==0 and item[8]==0 and on[3]!=12:#黄色
                 ii[14]=0
                 if ii[3]==1:
                    if data[2]==14:
                        data[2]=15
                    screen.draw.text("│ーー黄色ーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│私は黄色、あなたに青の位置を教えてあげる。│",(0,390),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
                    screen.draw.text("│机の左から2上から2のテーブルのどこかにある│",(0,430),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==1 and item[7]==1 and item[8]==0:#緑
                 ii[14]=0
                 if ii[3]==1:
                    screen.draw.text("│ーー緑ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
                    screen.draw.text("│私は緑、パスワードの下12文字はOUGIZYUTUNSG│",(0,390),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
                    screen.draw.text("│それ箇所以外の情報は青が知っていたかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==0 and item[7]==1 and item[8]==0:#青
                 ii[14]=0
                 if ii[3]==4:
                    screen.draw.text("│ーー青ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│私は青,パスワードは前からNIIZASOUGそれ以外│",(0,390),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│は緑が知ってる.あと,あの教室に戻るといいよ│",(0,430),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                 if ii[3]==3:
                    screen.draw.text("│ーー青ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│あと、赤い絵の具があると,a号室にある金庫の│",(0,390),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│暗証番号を知ることができるようになるんだ！│",(0,430),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                 if ii[3]==2:
                    screen.draw.text("│ーー青ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│なぜなら赤たちが暗証番号を知っているからさ│",(0,390),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│、赤い絵の具を持って赤たちに聞くといいよ！│",(0,430),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                 if ii[3]==1:
                    screen.draw.text("│ーー青ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│ただ、特にオレンジに聞いておくことをオスス│",(0,390),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
                    screen.draw.text("│メするよ、あとの二色はあてにならないんだ。│",(0,430),fontname='a.ttc',owidth=0.3,color="BLUE",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==0 and item[7]==0 and item[8]==1:#赤
                 ii[14]=0
                 if ii[3]==1:
                    screen.draw.text("│ーー赤ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│確かあの教室、ダイヤル、があるのよ。33456.│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                    screen.draw.text("│・・だったかしら？・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==1 and item[7]==0 and item[8]==1:#オレンジ
                 ii[14]=0
                 if ii[3]==1:
                    screen.draw.text("│ーーオレンジーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="ORANGE",fontsize=30)
                    screen.draw.text("│私はオレンジ、赤は1を３と主張する。紫は6を│",(0,390),fontname='a.ttc',owidth=0.3,color="ORANGE",fontsize=30)
                    screen.draw.text("│2と主張する,どうやら二色ともまともじゃない│",(0,430),fontname='a.ttc',owidth=0.3,color="ORANGE",fontsize=30)
            if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and item[6]==0 and item[7]==1 and item[8]==1:#紫
                 ii[14]=0
                 if ii[3]==1:
                    screen.draw.text("│ーー紫ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="PURPLE",fontsize=30)
                    screen.draw.text("│確かあの教室、ダイヤル、があるんだけど、、│",(0,390),fontname='a.ttc',owidth=0.3,color="PURPLE",fontsize=30)
                    screen.draw.text("│11452だっけ？・・・・・・・・・・・・・・,│",(0,430),fontname='a.ttc',owidth=0.3,color="PURPLE",fontsize=30)
            if data[2]==16 and on[2]==0 and on[4]==1 and kabe3.colliderect(cc):
                 ii[15]=1
                 item[7]=1
                 gyara[7]=item[7]
                 if ii[3]==3:
                    ii[14]=1
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│こんなところに青い絵の具があった！・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ん？・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==2:
                    screen.draw.text("│・・青い絵の具があったところの床に何かが、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│書いてある、下から２左から５のテーブルをみ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てみるといいって書いてある、・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                 if ii[3]==1:
                    screen.draw.text("│青い絵の具で二つ絵の具をゲットしたけど、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほかにも絵具ってあったりするのかな、まあ、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とりあえずまたほかのテーブルも観察しよう。│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==12:#
                ii[15]=1
                k1.draw()
                if siinn2[0]<=7:#ゲームストーリーギャラリー
                    siinn2[0]=8
                if ii[3]<19:
                    music[0]=5
                if ii[3]==19:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│今読んだ本・・・・・どうやら・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│青い絵の具の場所を示してくれてるみたい・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│少し探してみようかな・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[14]=0
                    screen.draw.text("[音葉]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・どうやら・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│問題なく探索を進めることができているみたい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ね・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│（あれ、この声は確か・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・音葉さん？・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│また私に話しかけに来たのかな・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=-6
                    screen.draw.text("│こんにちは、どうやら見た感じ、屋敷の探索は│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│順調に進んでいるみたいね,,やっぱあなたが脱│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│出できるようにちゃんと協力してあげようかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[23]=0
                    screen.draw.text("│え・・・・本当ですか？・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│それはとても助かります・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=-10
                    screen.draw.text("│じつはね、私は、あなたみたいな人間が霊鬼に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│捕まって死ぬような様子を目の当たりにしたく│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないの、、すごく残酷で痛々しいから・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[23]=-9
                    screen.draw.text("│だからさっきは、あなたに地図だけを渡して霊│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│鬼が襲いに来る前にすぐ戻ろうと、あなたとの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│会話を少しおろそかにしてしまったわ・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=-9
                    screen.draw.text("│ごめんね、先走っちゃって・・でも、どうやら│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あなたは霊鬼に捕まらないように気を付けなが│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ら屋敷の探索を頑張っているみたいだから・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=9
                    screen.draw.text("│あなたには精一杯、手助けしてあげないといけ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないかもって思ったの、だってほんとに頑張っ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てるから..生きて帰ろうと必死に動いてるから│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[23]=9
                    screen.draw.text("│だから私も、あなたの出口探しに協力してあげ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ようと思ったの........だから私もあなたが出│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れそうな出口が屋敷にないか探してみるわ!,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=0
                    screen.draw.text("│あ、ありがとうございます、、でも、この屋敷│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│をすでにうろついてる幽霊なら、出口の場所と│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かすでに分かっていたりとかしないんですか？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=-6
                    screen.draw.text("│あ～実はね、それは・・なんていえばいいのか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わからないけど・・出口はね・・・屋敷のどこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かにできたりできなかったりするの・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=1
                    screen.draw.text("│ん？・・・・・・出口って、普通に建物を出入│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│りできる場所のことですよね・・できるできな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いっていうのはいったいどういうことですか？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=-11
                    screen.draw.text("│え～っと,(この子にあんなことを説明してしま│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うと屋敷から出ようとするのをあきらめかけて│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しまうかもしれないから,今は説明を避けよう)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=9
                    screen.draw.text("│ううん、なんでもない、今の発言は忘れて、と│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│りあえず探索しないことには何も進展しないか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らあなたはひたすら出口探しに取り組みなさい│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=8
                    screen.draw.text("│私も、いまからあなたが探索していないエリア│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を探索するように頑張るから・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そういえばあなたの名前をまだ聞いてなかった│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=0
                    screen.draw.text("│あ、そうでしたね、私は天野美香といいます、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・あなたは音葉さんであってますよね？、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=6
                    screen.draw.text("│そうよ、佐久間音葉って名前よ、じゃあこれか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らは美香って呼ばせてもらうわね・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・それじゃあ引き続き探索頑張ってね│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=0
                    screen.draw.text("│はい!頑張ります!協力してくれるみたいだ、心│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│強いかも,引き続き探索頑張らないと!えっと,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│青い絵の具を探そうとしてたんだ,,早速探そう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==13:#赤い絵の具見つけた
                ii[15]=1
                item[8]=1
                gyara[8]=item[8]
                if ii[3]==2:
                    ii[14]=1
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│あ！机の下にある金庫ロックが外れた！、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・中には・・・あ！・・赤い絵の具だ・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんでこんなの金庫にしまうんだろう・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│三つで全部かな,,青色の部屋で、赤い絵の具が│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あれば,a号室の金庫の暗証番号がわかるって書│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かれてたから番号がわかったら解除しに戻ろう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-5 and kabe5.colliderect(cc) and on[4]==3 and data[2]==20:
                ii[15]=1
                item[9]=1
                gyara[9]=item[9]
                if ii[3]==2:
                    ii[14]=1
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│でっかい鍋のようだ、中身は全部水のようだ、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│コンロがあるわけでもなくただ単に鍋が置いて│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ある、、ん？中に長い棒が入っている・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これがあれば、高いところにおいてある、アイ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ムをとることができそう、探してみようかな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==1 and kabe5.colliderect(cc) and on[4]==3 and data[2]==21:
                ii[15]=1
                item[10]=1
                gyara[10]=item[10]
                if ii[3]==2:
                    ii[14]=1
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│棚の上に何かある、先ほど見つけた棒を使うと│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│棚の上の物がとれそうだ、早速とってみよう、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│懐中電灯らしきものが取れた、・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│・・・・・・・・・・・・、これがあれば、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│暗いところにある物をとることができるかもし│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れない・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==7 and kabe5.colliderect(cc) and on[4]==3 and data[2]==22:
                ii[15]=1
                item[11]=1
                gyara[11]=item[11]
                if ii[3]==2:
                    ii[14]=1
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│棚の下が暗くなっている、懐中電灯で照らして│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みようかな、、、あれ、何か下に落ちている、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│拾ってみようかな、・・・被覆室のカギ？、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│・・・・どうやら被覆室のカギみたい3F部屋か│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な、でもこれでまた新しいところに行けそうだ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ちょっとそこに行ってみようかな・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==-6 and kabe5.colliderect(cc) and on[4]==3 and data[2]==24:
                ii[15]=1
                item[12]=1
                ii[14]=1
                ii[23]=1
                gyara[12]=item[12]
                if ii[3]==2:
                    so[5]=1
                    screen.draw.text("│こんなところに、曲がった棒がある、どうやら│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│形からして、元々何かの元手の部分だったので│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│はないかと思われる感じがする・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│この棒と合成できそうなアイテムがないか探し│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てみようかな・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if ((on[2]==8 and kabe5.colliderect(cc)or kabe6.colliderect(cc)and on[4]==3) or (on[4]==1 and on[2]==-2 and not (kabe5.colliderect(cc)or kabe6.colliderect(cc)or kabe4.colliderect(cc))))and data[2]==23:
                ii[15]=1
                ii[14]=1
                kotarou2.draw()
                otohac2.draw()
                if siinn2[0]<=10:#ゲームストーリーギャラリー
                    siinn2[0]=11
                if ii[3]<26:
                    music[0]=11
                if ii[3]<4 or ii[3]==26:
                     music[0]=0
                if ii[3]==27:
                    ii[23]=1
                    screen.draw.text("│作業台・・？・・・・どうやら作業ができそう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│机の上に、様々な道具が置いてある・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│少し調べてみようかな・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    ii[14]=2                                                                                                
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そのころ、別の場所では・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    serihu[0]=1
                    on[2]=-2
                    on[4]=1
                    ii[23]=-34
                    screen.draw.text("│何故黙ったんだ。ちゃんと言うようにと言った│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だろ、。・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-16
                    screen.draw.text("│言うわ、ちゃんという、ただまだタイミングを│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│見計らってるだけよ！・・いずれ真実を伝える│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から！・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-33
                    screen.draw.text("│次あの子と話したときに、お前が現実を言わな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かったら、次は俺が話に行くからな、・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-13
                    screen.draw.text("│・・なんであなたは、そうなのよ、この屋敷に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いる幽霊は、迷い込んできてしまった人にみん│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な希望的な言葉を与えるようにしてるのに・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-15
                    screen.draw.text("│何故貴方は、希望を持たせようとしないの？だ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ったらこの屋敷から出ていけばいいのに、人が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│死ぬのはあなただって見たくないでしょう！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==20:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-31
                    screen.draw.text("│そうだよ!!見たくはないよ、ただ死ぬ前の心構│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│えぐらいは持たせておきたいと思っているんだ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、だって俺がそれで死んだときに後悔したから│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-35
                    screen.draw.text("│俺はこの屋敷に迷い込んでしまったときに出れ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るかもって聞いてすごく安心したよ。、だけど│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、それは一瞬の出来事だった・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-35
                    screen.draw.text("│すぐに俺は霊鬼に捕まった,だけど,その時出れ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るって思っていたのに出れなかった期待外れの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│現実を見て俺は苦しかったんだ!!!!・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-36
                    screen.draw.text("│死ぬのが辛かったんじゃないんだ、死を望んで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た中でも、再び人生を頑張ろうとしたからこそ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、現実を見て辛かったんだ!!!!・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-36
                    screen.draw.text("│でも僕はその時思ったんだ、最初からこうなる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ってわかっていた方が、死ぬってわかっていた│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│方が苦しくなかったなって,,平和だったなって│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-31
                    screen.draw.text("│後から知るのはすごいショックなんだよ、苦し│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│い人生の中でも、希望を持って脱出を頑張った│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のに、結局これが現実だって知ってしまうのが│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==14:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-33
                    screen.draw.text("│だったら、最初から死を受け入れる体制を作っ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ておくように言っといたほうが僕はいいと思う│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けどな、・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-34
                    screen.draw.text("│でも、死を望んでいる人に対して、わざわざ生│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きて帰らせようと脱出を試みさせるって本当に│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│その人のためになってるのか？・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-32
                    screen.draw.text("│その人が死を望んでいるなら、それはもはや助│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けない方がその人のためになっているんじゃな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いのか？そのまま安静に死を迎えられる方が。│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-13
                    screen.draw.text("│・・・・・でも、死を望むのは、今が平和じゃ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないからだと思うわよ、・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│死にたい人の願いは死ぬことじゃないの!!・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==10:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-16
                    screen.draw.text("│苦しくて逃避したいから死にたいって思ってる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だけで、たとえそう思っていたとしても、環境│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が変われば死にたくないって思うはずだわ！,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-33
                    screen.draw.text("│まぁ、ただ俺ら幽霊は現実世界の人々に触れる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ことができない。触れることができないなら、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│戻ってもまた同じく苦しむだけだろ・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-17
                    screen.draw.text("│そうかもしれないけどこの屋敷に入ってきた人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に脱出時に勇気を与えたりする事はできるはず│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だわ,,生きて帰った際も頑張るように言えば,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-30
                    screen.draw.text("│まぁそう素直に従う人がいるのかね??まぁあの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│子ならあり得そうだけど、まぁその前に出口が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないと話にならないけどね。どうなるもんかね│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==6:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-31
                    screen.draw.text("│まぁ、とにかく次君がほぼ出れないってことを│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いわなかったら僕が言うからな、いいな？・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・わかったな？・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    on[2]=-2
                    on[4]=1
                    ii[23]=-17
                    screen.draw.text("│あなたにはほんとに呆れるわ、目の前の光を捨│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ててしまうのね・・しょうがないわね・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わかったわよ,,そこまで言うなら・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    serihu[0]=0
                    ii[14]=2
                    on[2]=8
                    on[4]=3                                                                                     
                    screen.draw.text("│(確かに小太郎の言うことは,一部正しいかもし│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れない,,,,だけど、賛成はできない・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・私には、願いがあるから,・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=4
                    serihu[0]=0
                    screen.draw.text("│ん・・なんだろうこの変な感じ、また何かの気│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│配が・・・・いったいどこから来るものなんだ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ろう・・・・・・ちょっと不気味だな・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=1
                    screen.draw.text("│でも調べてみた感じこの机でどうやら手持ちの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ITEM同士を合成して新しいアイテムが作れそう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│！何か合成できそうなITEMがないか探そうかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("│現在立っている、場所（作業台の目の前）で、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│Sキーを押してアイテム欄を開くと,手持ちの、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│アイテムを合成させることができます、、！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==27 and on[2]==-2 and on[4]==3 and kabe4.colliderect(cc):
                ii[15]=1
                item[15]=1
                gyara[15]=item[15]
                ii[14]=1
                if ii[3]==2:
                    ii[23]=1
                    so[5]=1
                    screen.draw.text("│こんなところに何かがある、、なんだろう、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│少し見てみようかな・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・これは、どうやらロープかな？、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│もしかしたら、何かに使えるかもしれない、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│拾っておこうかな・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==8:
                ii[15]=1
                ii[14]=1
                if data[2]<27:
                    item[14]=1
                    gyara[14]=item[14]
                if data[2]>27:
                    item[16]=1
                    gyara[16]=item[16]
                if ii[3]==1 and data[2]==26:
                    ii[23]=1
                    screen.draw.text("│曲がった棒と、ゴミ箱で、バケツが作れた！！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そういえばさっきプールに何か沈んでた物を、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これに何かつければとることができるかも、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1 and data[2]==28:
                    ii[23]=1
                    screen.draw.text("│ロープと、バケツを合成させて、ロープ付きバ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ケツを手に入れることができた・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これでプールの中のアイテムをすくえるかも、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==0 and kabe7.colliderect(cc)and on[4]==3 and data[2]==25:
                ii[15]=1
                item[13]=1
                ii[14]=1
                ii[23]=1
                gyara[13]=item[13]
                if ii[3]==3:
                    so[5]=1
                    screen.draw.text("│・・・・この部屋のプールに何か沈んでいる気│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│がする、、なんだろう、少し気になる、何かあ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るのかな？・・・あ・・ここに何かおいてある│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│なんだろう、、ゴミ箱が置いてある、でもよく│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│見たら何かが外れたような跡があるような気が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│する、気になるから拾ってみよう・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│おそらく、今ゲットしたアイテムを合成すれば│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何か作れそう、早速試しに行こうかな・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・もう一度被覆室に向かおう・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc))and on[4]==4 and data[2]==30:
                ii[15]=1
                ii[14]=1
                ii[23]=1
                if ii[3]==3:
                    screen.draw.text("│あれ、このパソコンだけ動かすことができそう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だ・・電源をつけてみようかな・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・早速ボタンを押してみよう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[14]=3
                    if ii[1]==0 and ii[2]==2:
                        so[0]=1
                    if so[0]==2 and ii[1]>3:
                        so[0]=0
                    screen.draw.text("│あ、画面がついた、・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・なんだろう？パスワードの入力が必要み│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たい、、・・・・これじゃあ動かせないな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│ん？・・・でもなんだろう、何かが動いたよう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な、、、ん？電源をつけたからかな、今部屋の│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│別のパソコンから音がなった気がする・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==8 and kabe7.colliderect(cc)and on[4]==4 and data[2]==31:
                ii[15]=1
                ii[14]=1
                if siinn2[0]<=13:#ゲームストーリーギャラリー
                    siinn2[0]=14
                if ii[3]==1:
                    ii[23]=1
                    screen.draw.text("│あれ、どうやらこのパソコンが動いたみたい、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・あ、どうやらミニゲームができるそうだ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・Dキーでプレイできそう・,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==18 and so[2]==2:
                ii[14]=1
                ii[23]=2
                if ii[3]==1:
                    screen.draw.text("│扉が開いた！、、どうやら、扉の先へ行けるみ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たい、・・・・いったい何があるんだろう・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│先に進もう・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==18 and so[2]==4:
                ii[14]=1
                ii[23]=2
                if ii[3]==3:
                    screen.draw.text("│なんだろうこの扉、不気味な色をしてる、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あれ、？地図を見る限り、この先に部屋はない│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│はず、なんでこんなところにドアがあるんだろ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│・・・・館内マップが作られた後にできた部屋│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だったりするのかな・・・・もう一度地現在地│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を確認してみたけど、この先に部屋はない、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│あれ、右に何か本が置いてある、この扉のそば│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│においてあるならこの扉の先の部屋について、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何か書かれていたりするのかな、読んでみよう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==41 and kabe9.colliderect(cc):
                ii[15]=1
                ii[14]=1
                if ii[3]==5:
                    ii[23]=2
                    screen.draw.text("│ずいぶん古びた本のようにみえるから最近書か│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れたわけではないのかな,,・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│さっそく読んでみよう・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    reiki[4].draw()
                    if ii[2]<3:
                        screen.draw.text("SPACEキー➡文章スキップ",(0,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
                if ii[3]==3:
                    ii[23]=-2
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=2
                    screen.draw.text("│思い出したくないものを思い出してしまったか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もしれない・・・・・・・・いや、・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│考えないようにしよ・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この扉の先に行こう・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[2]==8 and kabe7.colliderect(cc)and on[4]==4 and data[2]==35:
                ii[15]=1
                ii[14]=1
                item[18]=1
                gyara[18]=item[18]
                if ii[3]==3:
                    so[5]=1
                    ii[23]=4
                    screen.draw.text("│特にカギのようなものはなさそうだけど、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あ、、パソコンが載っている机の引き出しの中│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に何かが入っている、、とってみようかな、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=1
                    screen.draw.text("│なんだろう紫色のカギみたい、・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・でもいったいどこで使える鍵なんだろう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│でも、鍵の形からどこかの部屋の鍵のように見│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│える、タンスやロッカーのカギではなさそう、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│このカギも持っておこうかな・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==15 and so[2]==2:
                ii[15]=1
                ii[14]=1
                k1.draw()
                if siinn2[0]<=14:#ゲームストーリーギャラリー
                    siinn2[0]=15
                if ii[3]<47:
                    music[0]=5
                if ii[3]==48:
                    ii[23]=1
                    screen.draw.text("│ミニゲームをクリアした画面に12文字目～19文│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│字目はBIZINESUっと出てきた、でもこんな感じ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のパスワード情報って別の場所でも見た気が,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==47:
                    screen.draw.text("│ここに表示されたパスワードの情報も使って、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あのパソコンのパスワードを入力したら、動い│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たりするのかな・・・・試してみよっかな、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==46:
                    ii[14]=0
                    screen.draw.text("[音葉]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│美香、・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・出口らしきものは見つかったかな？│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==45:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│（あ、この声は,,音葉さんだ・・・・何かあっ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たのかな）音葉さん、出口見つかりましたか？│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==44:
                    ii[23]=9
                    screen.draw.text("│あ、いや、まだ見つかってないの、、ただもう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│少しだけ頑張って探そうと思ってて・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==43:
                    ii[23]=1
                    screen.draw.text("│（そうだ出口に出られる人の基準とかを聞いて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みたら答えてくれたりするかな？少し質問して│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みようかな）・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==42:
                    ii[23]=4
                    screen.draw.text("│あの、音葉さん、さっき別の幽霊から、聞いた│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│話や、ここの屋敷についていくつか質問したい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のですが・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==41:
                    ii[23]=4
                    screen.draw.text("│この屋敷に閉じ込められる場合は、霊鬼に体を│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│乗っ取られて、ここまで連れてこられた時って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│本に記してあったのですがそれは本当ですか？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==40:
                    ii[23]=-11
                    screen.draw.text("│・・・・・・・・そうよ・・本当よ、この屋敷│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は幽霊と人間が共存できる唯一の場所、だから│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│霊鬼は人を襲えるこの屋敷まで人を移動させる│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==39:
                    ii[23]=-9
                    screen.draw.text("│人と幽霊が共存できる場に人間がいないと、霊│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│鬼はその人間を襲うことができないから・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==38:
                    ii[23]=4
                    screen.draw.text("│そこで少し質問したいのですが、霊鬼はある一│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│定の基準を満たしている人だけをこの屋敷に閉│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│じ込めて襲おうとしているんですか？・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==37:
                    ii[23]=-10
                    screen.draw.text("│そうよ、基準を満たしている人だけを狙ってこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の屋敷に閉じ込めようとしてるわ・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==36:
                    ii[23]=-6
                    screen.draw.text("│そこまでわかっているなら私も少しこの屋敷に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ついて説明してあげようかしら,,この屋敷につ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いて知ろうと頑張っているみたいだし,,,,,,,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==35:
                    ii[23]=0
                    screen.draw.text("│ほんとですか！・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==34:
                    ii[23]=-9
                    screen.draw.text("│ただ、聞いても、決して心を折ったりしないよ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うに覚悟して聞いて・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│(この子ならおそらく、知っても頑張れそう,,)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==33:
                    ii[23]=2
                    screen.draw.text("│え？・・・・・・・あ・・・・・はい・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│（いったいどんなことを話すんだろう・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・心を折らないようにって・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==32:
                    ii[23]=-10
                    screen.draw.text("│実はね、この屋敷には出口はないの、出口がな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いのは霊鬼が人間を捕まえたときに外に出れな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いようにするため,,この事は知ってるかしら？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==31:
                    ii[23]=1
                    screen.draw.text("│はい、さっき別の幽霊にその内容については、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│教えてもらったので・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==30:
                    ii[23]=7
                    screen.draw.text("│,,、そして、さっき美香も言ってくれたように│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│霊鬼はある基準を満たしている人だけをこの屋│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│敷に閉じ込めようとしている状態・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==29:
                    ii[23]=4
                    screen.draw.text("│でも、閉じ込めらたとしても、霊鬼がその基準│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を満たしてない人を間違えて連れてくることも│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あるから、その場合は外に出れるんですよね？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==28:
                    ii[23]=-6
                    screen.draw.text("│そうよ・・・・・・・・でも・・美香は、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どのぐらいの頻度で、霊鬼が間違えるか知って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│る？ここに、基準を満たさない人が来る頻度を│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==27:
                    ii[23]=1
                    screen.draw.text("│・・・・・・・・・・いえ・・・・・そこまで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は、知らないです・・・・でも時々っていうな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ら結構頻繁にあるんじゃないんですか？・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    ii[23]=-9
                    screen.draw.text("│いや・・その逆よ、間違えることなんてめった│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にないの、数字で表すと0.1%ほど,1000回に1回│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の頻度だわ・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    ii[23]=-1
                    screen.draw.text("│・・・・・え・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・それって、もう脱出できないの同然み│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たいな感じゃないですか・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    ii[23]=7
                    screen.draw.text("│私は、あなたに、美香に初めて会った時からこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れを知ってたわ、、私は今まで何人もの人がこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の屋敷で襲われるのを見てきた・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    ii[23]=-11
                    screen.draw.text("│私は、何度もその人たちの脱出を試みたの,,で│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│も誰一人として脱出させることはできなかった│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だから私は今回も無理だと最初から思っていた│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    ii[23]=-11
                    screen.draw.text("│助けようとして死んでしまう、そして、さっき│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まで話していた人が死ぬ・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・こんな悲惨な現状を何度も見てきた・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    ii[23]=-10
                    screen.draw.text("│だから私は、どうせ上手くいかないならもう人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を助けようとするのはやめて、この屋敷から離│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れていってしまってもいいかなって・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[23]=9
                    screen.draw.text("│だけどね、私は、この屋敷を離れたくはなかっ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たのよ、この屋敷で霊鬼に攫われて命を落とし│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た時から、、こう思うようになったから・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[23]=-6
                    screen.draw.text("│こんな悲惨な死を村の人々に味わってほしくな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いと、だから、一人でもいいからここに閉じ込│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│められてしまった人を救ってやりたいと・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[23]=-9
                    screen.draw.text("│私は幽霊になったときにそう思うようになった│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の、だから、ずっと誰かを助けたくてこの屋敷│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│をうろついてたの・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=-9
                    screen.draw.text("│・・・・・そこにあなたが訪れたのよ、美香、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・私は、あなたの様子を、この屋敷に来た時│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から見てた・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=-10
                    screen.draw.text("│でもね、あまりにも救うことができないから私│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は手助けしようとするのにも少し抵抗感を持っ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てしまったの、だから最初は声をかけなかった│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[23]=-10
                    screen.draw.text("│だけどね、あなたの脱出しようとする姿勢、怖│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│がらずに前に進む姿を見てこの子は助けたいと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│思うようになったの、それで美香に声をかけた│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=-9
                    screen.draw.text("│だから、私は、あなたに希望的であってほしか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ったからこのことを黙ってたの、ごめんね・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[23]=-2
                    screen.draw.text("│そ・・・・・・・・・そんな・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=7
                    screen.draw.text("│でも、まだあきらめないで、美香！、実をいう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とあなたは、今まで私が助けようとしてきた人│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の中で一番助かる見込みが今のところあるの！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=-1
                    screen.draw.text("│・・・そ・・・・・そうなんですか？・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でも,,,4階以外の階を全て探して・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│も出口はなかったのに・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[23]=-11
                    screen.draw.text("│確かに二人で屋敷中を探しても、いまだに出口│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が見つからないとなると、それは霊鬼が狙って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いる人間の基準を満たしてしまってる気もする│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=-6
                    screen.draw.text("│だけど、まだあなたがちゃんと基準を満たして│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いるかが、わからない以上、そう決めつけるこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とはできない,だからまだ可能性はあるわ!！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=2
                    screen.draw.text("│まあ、確かにそうですね、まだ自分自身で基準│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を満たしているかいないかがわかったわけでは│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないので・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=-4
                    screen.draw.text("│私は、あなたを全力で応援してるわよ、私もど│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こかに、出口がないかを粘り強く探すわ！！！│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だから美香も頑張って！！！・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=-2
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=3
                    screen.draw.text("│そうですね！少し衝撃的でしたが、私も頑張り│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ます！・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・音葉さんありがとうございます、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    sakuma[7].draw()
                    nn.draw()
                    screen.draw.text("│よし、じゃあ引き続き頑張ってね！！！！！！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=2
                    screen.draw.text("│あ、、、衝撃的過ぎて、基準がどういうものな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のか質問し忘れてしまった・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=2
                    screen.draw.text("│でも、音葉さんは、私が今まで見てきた人の中│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│で一番助かる見込みがあるって言ってくれた、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そうだ,,心を折らないようにって言われたんだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=2
                    screen.draw.text("│よし！0.1%なんて気にしないようにしよう！！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│希望を持って頑張ろう！！・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30) 
            if on[3]==16:
                ii[15]=1
                ii[14]=1
                if ii[3]==6:
                    ii[23]=1
                    screen.draw.text("│あ、パソコンがついた、何かのテキストが開き│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│っぱなしになっている、なんだろう、テキスト│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│には文章が書かれてる、読んでみようかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    reiki[3].draw()
                    if ii[2]<3:
                        screen.draw.text("SPACEキー➡文章スキップ",(0,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
                if ii[3]==4:
                    ii[23]=4
                    screen.draw.text("│霊気の屋敷で出口を見つけるためにはただ歩く│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だけじゃ難しいって書いてある・・・この文章│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は霊鬼の本に書かれている文章みたい・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=4
                    screen.draw.text("│ちゃんと探索しないと見つからないならまだ見│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│つかってないだけの可能性も高い、まだ希望は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ある,,ん？文章の一番下に何かのメモがある？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=1
                    screen.draw.text("│「ミニゲームができるパソコンのそばにカギが│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ある」って書いてある？,,ん？さっきのパソコ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ンのこと?え,,カギみたいな物ってあったっけ?│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│さっきそんなの見てないから、ない気もするけ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ど。ちゃんと調べてみたらあったりするのかな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│?,,一応もう一回調べてみようかな?・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==19 and so[2]==2:
                ii[14]=1
                kotarou4.draw()
                if siinn2[0]<=18:#ゲームストーリーギャラリー
                    siinn2[0]=19
                if ii[3]<=28:
                    music[0]=11
                if ii[3]==35:
                    ii[23]=2
                    screen.draw.text("│・・・・探索するのがつらくなってきた・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│さっきの本を読んでから、何か少しでもきっか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けがあれば嫌な記憶を思い出してしまいそう,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==34:
                    ii[23]=2
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│今目の前にまた別の霊鬼の本が置いてあるけど│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│正直読みたくない、真実を知りたくない・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==33:
                    ii[23]=2
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いや、ダメだ・・・・・・ここまで来たんだ、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│読むのを怠ってはいけない、ちゃんと読もう,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==32:
                    reiki[5].draw()
                    if ii[2]<3:
                        screen.draw.text("SPACEキー➡文章スキップ",(0,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
                if ii[3]==31:
                    ii[23]=4
                    ii[23]=-2
                    screen.draw.text("│・・・・不必要とされていて、・・・死を望ん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でいる存在・・・か・・・・ああ、確かに私も│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そうかもしれない・・・もうだめかもしれない│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==30:
                    ii[23]=2
                    screen.draw.text("│でも、・・・・ここで沈んでしまったら、今ま│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│で探索してきた努力が水の泡になる・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ダメだ、、引き続き、辛くても頑張らないと、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==29:
                    ii[14]=0
                    screen.draw.text("[小太郎]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│もうあきらめておいたほうがいいぞ、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あまり脱出しようとは考えないほうがいい・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==28:
                    ii[14]=1
                    ii[23]=2
                    screen.draw.text("│・・・・・・・・・・・・・・・・、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あなたは・・・・・・・・誰ですか？・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私はここから出ることはできないんですか？,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==27:
                    ii[23]=-30
                    screen.draw.text("│だいぶ苦しんでるみたいだね,,,,,,俺は小太郎│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│,どうやら君は,その霊鬼が捕まえようとする人│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│間の基準が書かれた本を今よんだみたいだね、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    ii[23]=-30
                    screen.draw.text("│今の本に書かれていた内容は、まぎれもない事│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│実だ、君は読んでみてどうだったかい？基準を│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│満たしていたかい？・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    ii[23]=-2
                    screen.draw.text("│・・　お　　そ　ら く はい,,私満たしてます│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・でも、ほかの幽霊さんは、私はきっと脱出│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│できるって言ってましたし・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    ii[23]=2
                    screen.draw.text("│まだあきらめません！ちゃんと外に出たいです│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から、帰りたいですから・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    ii[23]=-33
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どうして外に出たい、帰りたいって思うんだ??│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    ii[23]=2
                    screen.draw.text("│え？・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・どうしてって│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・この屋敷に閉じ込められちゃったから・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    ii[23]=-30
                    screen.draw.text("│君、ここに来る前、苦しくなかったのか？・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ここに来る人はみんな死を望んでいるんだよ、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│みんな生きてるのがつらくなった人たちだから│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[23]=-33
                    screen.draw.text("│考えてみろ、君は、生きて帰らないほうが幸せ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんじゃないのか？、だって、どうせ戻ったと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ころで、またつらい人生を歩むだけになるんだ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[23]=-2
                    screen.draw.text("│,,はい,,,,確かにそうですね,,,,言われてみれ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ば、私は元に戻ってもきっと苦しむだけです,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・きっと苦しい中生活をするだけです・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[23]=-2
                    screen.draw.text("│(この人と話してたら,なんかだんだん思い出し│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てしまった、嫌な記憶を全て思い出してしまっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│た,、私・・の両親そういえばもういないんだ)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    screen.draw.text("│(携帯・・,そんなのない・・全部あの家ととも│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に全て燃やされてしまったから・・想いでも全│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│部、前住んでいた家と共に全て燃やされた,,,)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    screen.draw.text("│(そして消防車が来てから両親の死が発覚して,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あ～やだやだ思い出したくない!!でもなぜこの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│屋敷ではそれを忘れることができてたんだろ?)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    screen.draw.text("│(忘れようと,頭の中に浮かび上がらないように│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│していたのは以前もそうだ、ただ今回はいろい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ろ現実離れなことがおきたから,,,,,,,,,,,,,)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    screen.draw.text("│(・・・その驚きが大きすぎたから,脱出するの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に必死だったから・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・,おそらく忘れることができたんだ)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    screen.draw.text("│(両親がなくなって数か月,私は感情の停止した│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ような心を、死んだような心を抱えて生活する│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ようになり,友達を作ろうとする気力を失った)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    screen.draw.text("│(誰かと仲良くなりたいという欲望を失った,,,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そして私はいじめられた、私が空気を読めない│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から,,,私がなじめないから、・・・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    screen.draw.text("│(新しいところで生活するようになってからも,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│不器用な私は、ずっと怒られっぱなしだった、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│自己管理も,,,とても苦手だった・・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    screen.draw.text("│(せっかく住まわせてもらっているのに、私は,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・あまりの容量の悪さにあきれられていた│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・),│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    screen.draw.text("│(そういえば育てるだけでも大変だから正直,,,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│出てってほしいとか言ってたっけな・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほんとに情けないな,・・・・・・・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    screen.draw.text("│(学校ではいじめられて,容量の悪さと不器用す│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ぎる面から新しい家に帰ってきたら何度も怒ら│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れて・・,時々両親の死を思い出してしまって)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("│(,,,最悪だ・・・・苦しさのあまりに、反省し│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て自分を改善するゆとりもない,,あまりの行動│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│力のなさに,,,自分が嫌いになった・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    screen.draw.text("│(私を心配してくれる人なんてもういなかった,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から,私は死を望んでしまった,誰からも必要と│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│されてないから,・・・・・・・・・・・・・)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    screen.draw.text("│(そうだよね,こんなに情けない子なんだもん、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そうなって当たり前よね,,今本を読んでみた限│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│り私は基準も満たしてしまってるようだし,,,)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    screen.draw.text("│そうですね、よくよく考えたら脱出する必要な│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│んてないかもしれませんね・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│戻っても苦しむだけ、いらないと思われるだけ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    screen.draw.text("│そんな私みたいな人間が生きて帰ったところで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・私にも、、周りの人にとっても、いいこと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は何もないですね、・・邪魔になるだけです,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=-32
                    screen.draw.text("│やはり君にも辛い記憶はあったんだね、・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・もう大丈夫だよ、もうすぐで君も楽になる│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から、屋敷でおとなしくしてれば迎えが来るさ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[14]=0
                    screen.draw.text("│天野美香は・・ひどく落ち込んだ・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==19 and so[2]==4:
                item[1]=0
                item[2]=0
                item[4]=0
                item[5]=0
                item[6]=0
                item[7]=0
                item[8]=0
                item[9]=0
                item[10]=0
                item[11]=0
                item[12]=0
                item[13]=0
                item[14]=0
                item[15]=0
                item[16]=0
                item[17]=0
                item[18]=0
                item[20]=0
                item[21]=0
                item[22]=0
                item[23]=0
                k1.draw()
                nn.draw()
                music[0]=11
                kotarou5.draw()
                if ii[3]<=5:
                    music[0]=0
                if ii[3]==8:
                    ii[14]=0
                    screen.draw.text("[音葉]",(0,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│起きて！起きて！美香！・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・ダメ！そんな人の話なんて聞いちゃダメ！│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│・・・・・（この声は音葉さん？、なんでそん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なに必死なんだろう、また私を元気づけに来て│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くれたのかな・・・・・・・・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[14]=1
                    ii[23]=-35
                    screen.draw.text("│やめとけ音葉、そんな愚かなことをするな、出│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│口がない以上何やったって無駄なんだ、こうや│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ってこいつの心構えを変えるしかないんだ・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=-4
                    screen.draw.text("│愚かなんてよくも言ったわね！愚かなんかじゃ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないわ！美香！起きて！あったわ！出口があっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たわよ！だから起きて！あきらめないで・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[14]=1
                    ii[23]=-37
                    screen.draw.text("│なにを言っているんだ？何かの勘違いだろ??さ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│っき、こいつは基準を満たしてるって言ったん│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だ・・・満たしてたら出口があるわけない！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[14]=0
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│（え・・・・うそでしょ・・・・なんで・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私は基準も満たしてたし、もう見放され切って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・あ・・そんなことないかもしれない）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│（そうだ、一人だけ私にさりげなく寄り添って│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くれた子がいた。孤独だった、私に、話しかけ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てくれた子が、・・・・・・・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│（間違いない、あの子だ、、泣いていた私に話│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しかけてくれた子が、ひとりだけいた・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│唯一私を心配してくれた子が・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==19 and so[2]==6:
                ii[15]=1
                item[19]=1
                gyara[19]=item[19]
                k1.draw()
                nn.draw()
                music[0]=12
                kotarou6.draw()
                if ii[3]<10:
                    music[0]=0
                if ii[3]<8:
                    music[0]=2
                if ii[3]==23:
                    ii[14]=0
                    so[5]=1
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│（五十嵐君・・・・きっと出口が作られている│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│って事はあの子が私を必要としてくれたんだ,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なんで忘れてたんだろう・・あの子のこと,,）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│（でも、出口があるなんて本当なのかな・・い│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│や！・・疑っちゃだめだ！どっちにしろ、信じ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て頑張んなきゃ！ここまで来たんだから！！）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    screen.draw.text("[美香]",(600,295),fontname='a.ttc',owidth=3,color="WHITE",gcolor="GRAY",fontsize=30)
                    screen.draw.text("│（そうだ、音葉さんもついてる！！私を応援し│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てくれる存在がいる！そうだ、今は一人じゃな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いんだ！生きてこの屋敷から出ないと！！！）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[14]=1
                    ii[23]=0
                    screen.draw.text("│ありがとうございます音葉さん、私すごく落ち│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│込んでましたけど、また頑張れそうです・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[14]=1
                    ii[23]=-37
                    screen.draw.text("│なに！さっきまであんなに落ち込んでたのに、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│急にどうしたんだ？、基準を満たしてる場合は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│確実に出口はないんだぞ！！わかってるのか？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[14]=1
                    ii[23]=0
                    screen.draw.text("│いや、違うんです、私が忘れてたんです、必要│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│としてくれてた人を、今思い返せばいたんです│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│！私を必要としてくれる人が！・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=-3
                    screen.draw.text("│良かったちゃんと目を覚ましてくれて！ひどく│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うなされてたみたいだから・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[14]=1
                    ii[23]=-33
                    screen.draw.text("│本当に、出口を見つけたんだな？俺にはにわか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に信じがたいが,,音葉？それはまぎれもない事│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│実ってことでいいんだな？・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[14]=1
                    ii[23]=6
                    screen.draw.text("│ええ！断言できるわ私がちゃんとこの目で見た│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もの！！・・・・・・・・・・・・だからあな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たはこの子にもう手は出さないでちょうだい！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[14]=1
                    ii[23]=-34
                    screen.draw.text("│（・・奈々子が言っていたのは本当だったのか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もしれない・・それを踏まえて考えれば出口が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あってもおかしな話ではないか・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[14]=1
                    ii[23]=-32
                    screen.draw.text("│そうかい、まあ確かにそうだな・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・君の粘り強さには感心だよ、数値だけ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に囚われないその粘り強さには、さすがだね、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[14]=1
                    ii[23]=-32
                    screen.draw.text("│なら,俺はそいつにもう手出しはしない,それが│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│本当なら、ここからは君たちの自由にすればい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│い、俺はここを去るよ、後は二人で頑張れ・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│あれ,,小太郎さんどこかに行っちゃいましたよ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[14]=1
                    ii[23]=-4
                    screen.draw.text("│いいの！もうあんな奴のことは気にしないで！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│碌な奴じゃないから！美香！頑張って出口に行│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きましょ！・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=0
                    screen.draw.text("│え！？、あ！、は、はい！でも一体どこに出口│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│があるんですか？・・・・私は見つけることが│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│できなかったのですが・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=6
                    screen.draw.text("│私に任せて！まさか、こんなひねくれた場所に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あるとは思わなかったわ、どうりで見つからな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いわけ・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=8
                    screen.draw.text("│いったんあなたが使わないと思われるアイテム│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は全部私がもらってしまうわ、荷物は少ないほ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│うがいい・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=9
                    screen.draw.text("│その代わりこのアイテムを手に取って・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・、これであなたが今いるこの通路のひび│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│割れていそうな壁をたたいて！！・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=1
                    screen.draw.text("│これはハンマー？ですか、え、・・たたくって│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ことは壁を壊すってことですか？・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=8
                    screen.draw.text("│そう、私は壁をすり抜けれるからわかったんだ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│けど,見たところ,この壁の向こう側に通路があ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│って、その先に出口がある状態になってるわ！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=0
                    screen.draw.text("│え！そうなんですか、そんな変な場所に出口が│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あるんですかんですか！・・・それはどうりで│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│探しても見つからないわけですね・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=-5
                    screen.draw.text("│もうすぐ霊鬼が来るかもしれないから、急いで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│試してみて!!!!・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=0
                    screen.draw.text("│あ！はい、音葉さんありがとうございます！！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│早速試してみます！・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==20 and so[2]==2:
                item[19]=1
                gyara[19]=item[19]
                k1.draw()
                nn.draw()
                item[19]=0
                if ii[3]==1:
                    ii[14]=1
                    ii[23]=1
                    screen.draw.text("│この壁、、少しひびが入っている・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│(もしかして強くたたけば壊れたりするかな,,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もらったハンマーを使って試してみよう、、）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==20 and so[2]==4:
                k1.draw()
                nn.draw()
                music[0]=12
                if ii[3]==21:
                    ii[14]=1
                    ii[23]=1
                    music[0]=0
                    screen.draw.text("│あ！壁が割れた、・・・でもほんとにこの先に│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│道なんて,,あるのかな,,ない気もするんだけど│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│,,ん?壁の向こうから何かの音が,・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[14]=1
                    ii[23]=0
                    screen.draw.text("│!!鳥の声？奥から涼しい風が!!,,,,これ,,,,,,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│嘘じゃない!!本当だ!!音葉さんの話は本当だ!!│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これは外の音!この感じは外につながっている!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[14]=1
                    ii[23]=-3
                    screen.draw.text("│やったわね！美香！これで脱出できるわね！！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│（そっか、これで脱出してしまえば、もうこの│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│子とはおわかれなんだ・・・・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[14]=1
                    ii[23]=0
                    screen.draw.text("│ほんとに？！ほんとに生きて帰ることができる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│んですか？・・かなり諦めかけていましたから│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│信じられなくて・・まるで夢みたいですよ・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=-7
                    screen.draw.text("│そうよ！ほんとに帰れるわ！・・・あとはこの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│先の通路をどう進んでいけば出口にたどり着く│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かを私が頑張って説明して案内するわ！・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=9
                    screen.draw.text("│あと,,その前に美香についでにこれも渡そうと│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│思う・・・・・霊よけのお守り,,とはいっても│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私が作った、ただのお守りなんだけどね・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[23]=1
                    screen.draw.text("│あ、おまもり、、・・・ありがとうございます│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・いいんですかもらっちゃって・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│手作りのお守り・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=9
                    screen.draw.text("│全然いいわよ！大事にしてくれると嬉しいわ!!│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あと,,これであなたが、この屋敷を脱出したら│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│もう私はあなたとお別れ・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[14]=1
                    ii[23]=4
                    screen.draw.text("│え。。あ。。そっか、そうですよね、音葉さん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は幽霊ですから、この屋敷の外に出てしまうと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、もう関わることができませんもんね・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=-3
                    ii[23]=4
                    screen.draw.text("│なんといえばいいか、ここまで助けてもらった│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のに、会えなくなっちゃうなんてなんか私寂し│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いです・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=1
                    ii[23]=6
                    screen.draw.text("│ｗｗ、そんなこと言わないで美香、もしあなた│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が無事に脱出したら、私は空からあなたのこと│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を見守ってるわ・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[23]=6
                    screen.draw.text("│あなたには私の姿は見えないけど、私はあなた│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を応援するつもりよ、だって初めてこの屋敷で│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私が救うことができた人になるんだから！！,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=-6
                    screen.draw.text("│あなたは、ある意味私の願いを叶えてくれた人│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│にもなるんだから！,,でもこの屋敷に来たって│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│事はあなたも辛い出来事を味わってきたと思う│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=4
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・そうですね・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=-6
                    screen.draw.text("│でもたとえ脱出した後似たような目にあっても│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あきらめないで,,人生を投げやったりしないで│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│..私はあなたが幸せになる姿を見守ってたい..│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=-10
                    screen.draw.text("│だからもしも自ら命を経とうと考えるようなこ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とがこの先あれば、そのお守りでも何でもいい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│から私のことを思い出してほしい・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    ii[23]=-11
                    screen.draw.text("│・・・私はあなたが幸せになれることを願って│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るって・・・あなたがそのようなことで死んで│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しまったら,,それは音葉の心の傷になるって,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=9
                    screen.draw.text("│だから約束して、生きてここを脱出したら、無│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│理にとは言わないけど..あなたのできる範囲で│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いい,幸せになってほしい!私は応援するから!!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=0
                    screen.draw.text("│..音葉さん..本当にありがとうございます,,わ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│かりました!確かにつらいことは多いけど,私は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│自分のためにも音葉さんのためにも頑張ります│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=0
                    screen.draw.text("│絶対に幸せになれるように頑張って見せます!!│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│あ、あと、お守り大切にしますね！・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=6
                    screen.draw.text("│よし!!これで私があなたに言い残すことはない│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│わ！あとは早く・・・この通路の先に行って急│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いでこの屋敷を脱出しましょう！・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==20 and so[2]==6:
                ii[15]=1
                item[20]=1
                gyara[20]=item[20]
                k1.draw()
                nn.draw()
                music[0]=7
                if ii[3]==3:
                        ii[23]=5
                        so[5]=1
                        screen.draw.text("│わああ！霊鬼だ!!急いで逃げなきゃ！！・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                        ii[23]=8
                        screen.draw.text("│今持ってるハンマーは捨ててお守りはポケット│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│にでも入れときなさい!,,よし！美香!私が案内│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│するからそれに従って逃げて！・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                        ii[23]=3
                        screen.draw.text("│は・・・・・・はい！！！・・わかりました！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if data[2]==8 and on[2]==1 and on[4]==2 and kabe7.colliderect(cc):
                if sgyara[6]<=1:
                    sgyara[6]=1
                if siinn2[0]<=2:#ゲームストーリーギャラリー
                    siinn2[0]=3
                if ii[3]==2:
                        ii[14]=1
                        ii[23]=1
                        screen.draw.text("│あれ、、、さっきよく見てなかったけど、この│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│パソコンでどうやらどうやら宝探しのミニゲー│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                        screen.draw.text("│ムができるみたい,,ちょっと遊んでみようかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[1]=0
                    ii[2]=0
                    ii[3]=0
                    i[4]=0
                    ii[9]=0
                    on[1]=0
                    ii[24]=0
                    ka[11]=0
                    ka[10]=0
                    on[1]=14
                    game.i=0
                    game.h=[Actor('a3(1)',center=(350,150)),Actor('a33(1)',center=(350,150)),Actor('a3(1)',center=(350,150)),Actor('a333(1)',center=(350,150))]
                    game.r=[Actor('a4(1)',center=(350,150)),Actor('a44(1)',center=(350,150)),Actor('a4(1)',center=(350,150)),Actor('a444(1)',center=(350,150))]
                    game.a5=Actor('a5(1)',center=(350,150))
                    game.heya=[Actor('heya1',topleft=(0,-150)),Actor('heya2',topleft=(320,-150)),Actor('heya3',topright=(380,-150))
                               ,Actor('heya4',topleft=(320,-150)),Actor('heya5',topright=(380,-150)),Actor('heya6',topleft=(320,-150))]
                    game.doa=[Actor('kabe2'),Actor('kabe2'),0]#いき０戻り１アドレス2
                    game.w=0
                    game.ww=0
                    game.time=[1,104,300]
                    game.takara=["ない","ない","ない","ない",4]
                    game.back=[Actor('game',topleft=(0,-150)),Actor('sikai',center=(450,365-100))]
                    game.reba=[Actor('botann'),Actor('botann'),0,0,0,0,Actor('takara')]
            if data[2]==29 and ((on[2]==0 and on[4]==3 and kabe3.colliderect(cc)) or (on[2]==-2 and on[4]==2 and not kabe4.colliderect(cc) and not kabe6.colliderect(cc) and not kabe5.colliderect(cc))):
                ii[15]=1
                item[17]=1
                gyara[17]=item[17]
                ii[14]=1
                ii[23]=1
                kotarou8.draw()
                kaitonanako.draw()
                if siinn2[0]<=11:#ゲームストーリーギャラリー
                    siinn2[0]=12
                if ii[3]==35:
                    so[5]=1
                    ii[23]=1
                    screen.draw.text("│この位置からロープ付きバケツを使ってプール│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の中にあるアイテムをすくえるかもしれない!!│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ちょっと試してみよう・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==34:
                    ii[14]=2
                    on[2]=-2
                    on[4]=2
                    serihu[0]=1
                    music[0]=0
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そのころ別の場所では・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==33:
                    ii[23]=14
                    music[0]=5
                    screen.draw.text("│奈々子、それは本当なのか？今回迷い込んだ子│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は屋敷の外に出れる可能性が高いっていうのは│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│？・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==32:
                    ii[23]=10
                    screen.draw.text("│ええ・・・まだ確実と言えるわけじゃないけど│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、おそらくあの子は脱出できるような気がする│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==31:
                    ii[23]=11
                    screen.draw.text("│霊鬼が攫うのは、周囲の人から見て存在価値が│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なくなった人,,なおかつ自らの死を望んでいる│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│人間、この条件に当てはまっている人を攫う、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==30:
                    ii[23]=11
                    screen.draw.text("│だから、今回もその条件に当てはまっているか│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│、確かめようと一つ質問してみたのよ！そした│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│らね、気遣ってくれるお友達がいたらしいのよ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==29:
                    ii[23]=11
                    screen.draw.text("│今まで、友達がいた人ならまだしも、優しさを│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│向けてくれる友達を持つような人は,過去1人も│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この屋敷で見たことがないわ・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==28:
                    ii[23]=10
                    screen.draw.text("│それがもし本当なら、この時点で一人でも必要│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│としている人がいる限り、すでに、不必要とさ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│れているって言う基準からは逸脱してるわ、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==27:
                    ii[23]=12
                    screen.draw.text("│そもそも、霊鬼と言うものは、村の人口が減る│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のを恐れている。だから、自分が人を、攫って│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いるのもバレないように気をつけてる・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==26:
                    ii[23]=12
                    screen.draw.text("│自身の人攫いによる現象を多くの人が見た場合│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│それを恐れて村の人が減るきっかけを産む可能│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│性があるもの,,この村に住むのは危ないってね│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==25:
                    ii[23]=12
                    screen.draw.text("│霊鬼が攫うことができる人間は、その村に住ん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でいる人だけだから・・・・・・村から人がい│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│なくなってしまえば・・人攫いができなくなる│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==24:
                    ii[23]=12
                    screen.draw.text("│だからそのきっかけを作らないように霊鬼は誰│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│からも必要とされていない。かわいそうな人間│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│だけをあえて攫うようにしてるのよ・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==23:
                    ii[23]=11
                    screen.draw.text("│でも、そういう霊鬼の特長に鑑みたら、あの子│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│は基準を満たしてない。だから私はかなり可能│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│性を感じるのよ！！脱出の可能性をね・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    ii[23]=15
                    screen.draw.text("│なるほど、確かに僕も思ったんだ、あの子は屋│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│敷の隅々まで驚くほど探索できている。僕も希│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│望が見えたよ。脱出できるんじゃないかって！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:
                    ii[23]=10
                    screen.draw.text("│あの子のこの先の様子が楽しみだわ、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・上手くいってくれると嬉しいわ！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    ii[23]=-30
                    music[0]=11
                    screen.draw.text("│何を話してるんだ、君たち・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│何か発見でもあったのか？・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    ii[23]=17
                    screen.draw.text("│いや、特に大したことじゃないよ、あ、、でも│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│小太郎、申し訳ないんだが、今回の子にはどう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│か諦めさせる言葉を伝えないでもらえるかな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    ii[23]=-31
                    screen.draw.text("│何かと思えばまたその話か、無理だね、だって│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│僕は海斗、奈々子、お前らのせいで、ショック│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を受けたんだ。期待外れの大きさでね・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    ii[23]=13
                    screen.draw.text("│悪かったわよ、でも遠い昔の話でしょう、貴方│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│が生きていた時、私たちが貴方の脱出を試みた│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│事をまだ恨んでるの？・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==16:
                    ii[23]=-33
                    screen.draw.text("│まぁ、もう恨みと言えるような恨みは消えたさ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│さすがにもう時がたったからな・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    ii[23]=-30
                    screen.draw.text("│ただあまりにもたくさんの人が結局出れないの│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│を幽霊になってからみるようになって、君たち│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│の行動に疑問をもつようになったんだよ・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    ii[23]=-30
                    screen.draw.text("│これって本当に迷い込んでしまった人たちの為│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│になっているのかなって？・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    ii[23]=-30
                    screen.draw.text("│もう死ぬって分かり切ってるような人にそんな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こと言うのはどうなのか？って二人ともそうは│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│思わないのかい？・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    ii[23]=14
                    screen.draw.text("│まぁ、確かにその考えには賛成だよ,ただ,まだ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│救える見込みがあるのに、救わないのもどうな│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のか？って思うんだ・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    ii[23]=11
                    screen.draw.text("│ただ、今回のあの子は違うわよ、あの子は探索│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│する能力もあるし、仲の良い知り合いもいる。│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│脱出できる可能性が高いのよ。・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==10:
                    ii[23]=-31
                    screen.draw.text("│そうなのか？まぁ俺は、そんなの知らんがな、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│それぐらいで考えを曲げたりはしないよ、もう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│自分の考えがまとまったんだ・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    ii[23]=17
                    screen.draw.text("│やっぱ君はそうだよね、俺たちが何か言ったと│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ころで何も変わらないよな、・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    ii[23]=-30
                    screen.draw.text("│とにかく俺は今までどうり行動させてもらうよ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│,じゃあな,,(海斗はまだしも奈々子が反応する│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│のは珍しい、本当なのか？,,,なわけないよな)│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    ii[23]=12
                    screen.draw.text("│あの子は決意が固まりすぎたのか・・・・人の│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│考えを素直に取り入れてくれないのよね・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・最初は、ああじゃなかったのに・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==6:
                    ii[23]=16
                    screen.draw.text("│そうだね・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    serihu[0]=0
                    on[2]=0
                    on[4]=3
                    ii[23]=0
                    music[0]=0
                    screen.draw.text("│・・・・・・あ！、上手くいったかも,,アイテ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ムをバケツですくうことができた・・このアイ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│テムは何だろう？、どうやら何かのカギみたい│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    ii[23]=1
                    screen.draw.text("│あ！カギに4F総合ビジネス科って書いてある、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私がまだ行ってない4Fの部屋のカギだ・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│こんなところにあるのも不思議だな・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    ii[23]=4
                    screen.draw.text("│3階にも特に予想道理出口みたいなものはない,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でも次で最後の階だ・・・4Fで見つからなかっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たらもうあきらめるしかないのかな・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    ii[23]=2
                    screen.draw.text("│いや！あきらめようとしちゃだめだ、まだ、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│屋敷内を全て探索するまではわからない、、、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│考えても仕方がない,最上階の4Fを探索しよう!│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    item[16]=0
                    ii[23]=1
                    screen.draw.text("│とりたいアイテムはもう取れたから、ロープ付│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│きバケツはもう持たなくてもいいかな、、、、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ここら辺においておこ・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==17 and so[2]==2:
                if ii[3]==1:
                    ii[14]=1
                    ii[23]=4
                    screen.draw.text("│新しいマップだ、紫のカギを使っていけるよう│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│になった場所、この先を探索すれば、おそらく│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│この建物は大体全部探索したことになる、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==17 and so[2]==8:
                if siinn2[0]<=15:#ゲームストーリーギャラリー
                    siinn2[0]=16
                ii[14]=1
                ii[23]=5
                if ii[3]==2:
                    screen.draw.text("│あれ！！どうして今通ったドアが開かない！！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・さっきまでは通れたのに、紫のカギだっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てあるのに、・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    screen.draw.text("│さっきロックがかかった音もしたし,,もしかし│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│てここに閉じ込められちゃったのかな・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これじゃ,,さっきいた場所に戻れない・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==17 and so[2]==10:
                ii[15]=1
                ii[14]=1
                kotarou3.draw()
                otohac3.draw()
                if siinn2[0]<=16:#ゲームストーリーギャラリー
                    siinn2[0]=17
                if ii[3]==22 or ii[3]==1:
                    music[0]=0
                if 22>ii[3]>1:
                    music[0]=11
                if ii[3]==23:
                    ii[23]=2
                    screen.draw.text("│もう私はこの先に進むしかなさそうだな、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│生きて帰れることを願うしかない、、・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│先に進もう、、きっともうすぐ何かがわかる、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==22:
                    ii[14]=2
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そのころ・・別の場所では・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==21:  
                    on[2]=8
                    on[4]=3
                    ii[23]=-16
                    serihu[0]=1
                    screen.draw.text("│言ったわよ、でも言ったせいで、あの子が脱出│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しようとする意欲を失っちゃったかもしれない│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│じゃない！！・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==20:
                    on[2]=8
                    on[4]=3
                    ii[23]=-33
                    screen.draw.text("│まぁそうだな、お前なりにはがんばったなぁ、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ただ言い方が気に食わなかったな～なんで、希│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│望的な言葉を付け足して言うんだ・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==19:
                    on[2]=8
                    on[4]=3
                    ii[23]=-13
                    screen.draw.text("│別にいいでしょ、言ったんだから、とりあえず│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│これであなたはもうあの子に手を出そうとはし│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ないで・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==18:
                    on[2]=8
                    on[4]=3
                    ii[23]=-33
                    screen.draw.text("│すまないな,あの子に俺も伝えに行くよ,お前の│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│伝え方は目的に適してない,,あれではまだ生き│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て帰ろうとしてしまって死ぬ覚悟を持ててない│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==17:
                    on[2]=8
                    on[4]=3
                    ii[23]=-15
                    screen.draw.text("│え！,,なんで！どうして！約束したじゃない！│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私が事実を言えば、あなたは伝えに行かないっ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│て！！・・話が違うわ！・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==16:
                    on[2]=8
                    on[4]=3
                    ii[23]=-30
                    screen.draw.text("│いや,確かに約束をしたかもな,でも言い方が気│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│に食わなかったから、俺も行く、しかもお前が│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│伝えたら俺は伝えに行かないとは言ってない,,│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==15:
                    on[2]=8
                    on[4]=3
                    ii[23]=-33
                    screen.draw.text("│お前が伝えに行かないなら、、俺が伝えに行く│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│と言っただけだ、・・・約束といえるような約│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│束はしていないだろ,,君が勘違いしただけでさ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==14:
                    on[2]=8
                    on[4]=3
                    ii[23]=-16
                    screen.draw.text("│そんなの、都合がよすぎる,,あまりにもわがま│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│まじゃない!!、ひどいわ・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==13:
                    on[2]=8
                    on[4]=3
                    ii[23]=-34
                    screen.draw.text("│まぁでも、君もあの子もだいぶ屋敷の中を探索│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│し尽くしたから、ほんとに出口があるならそろ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│そろ見つかるんじゃないか？・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==12:
                    on[2]=8
                    on[4]=3
                    ii[23]=-33
                    screen.draw.text("│でもこんなに探索しても出口が見つからないな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ら、もうないって言い切って伝えてもいいかも│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│しれないな,,出口はない!諦めろ!っ的な感じに│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==11:
                    on[2]=8
                    on[4]=3
                    ii[23]=-32
                    screen.draw.text("│なるべく重い現実を押し付けてたほうが、どん│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│な悲劇が来ようと、受け止めやすくなるだろう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│し,,そう考えればこう伝えるのも悪くないな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==10:
                    on[2]=8
                    on[4]=3
                    ii[23]=-17
                    screen.draw.text("│やめて！そんなこと言わないで！・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・せめて出口はないって言いきったようなこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│とは伝えないで！・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==9:
                    on[2]=8
                    on[4]=3
                    ii[23]=-17
                    screen.draw.text("│まだ全箇所探索しきったわけじゃないんだから│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│！まだわからないんだから！・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・勝手にあやふやなことを伝えないで！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==8:
                    on[2]=8
                    on[4]=3
                    ii[23]=-31
                    screen.draw.text("│ちっ!!お前もしつこいな・・・まあ確かに、な│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│いって言いきるのは、少し嘘になるから、別の│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│言い方を探してあの子に伝えるか・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==7:
                    on[2]=8
                    on[4]=3
                    ii[23]=-32
                    screen.draw.text("│・・・まあ俺は正直絶対無理だと思うがな、も│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│う君も諦めたらどうだ、人助けなんて,,人を救│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│えない人助けなんてやっててつまらないだろｗ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==6:
                    on[2]=8
                    on[4]=3
                    ii[23]=-17
                    screen.draw.text("│あんた、よくもそんな皮肉なことを堂々と言え│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│るわね、でも私は心を曲げないから、少なから│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ず、絶対あるって信じて最後まで探すわ！！！│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==5:
                    on[2]=8
                    on[4]=3
                    ii[23]=-32
                    screen.draw.text("│・・・そうかいｗｗｗｗじゃあ今も俺と話して│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│る暇があるなら、さっさと出口探しでもしたら│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│どうだ？意味がない出口探しをｗｗｗ・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==4:
                    on[2]=8
                    on[4]=3
                    ii[23]=-16
                    screen.draw.text("│もういい！何が何でも見つけてみせるわ！,,,,│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たとえそれが不況に陥ってしまったとしても,,│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│絶対見つけ出すつもりで探す！！！！・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==3:
                    on[2]=8
                    on[4]=3
                    ii[23]=-33
                    screen.draw.text("│まぁもうないと思うけどな、せいぜい頑張って│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│くれ・・さて・・・・じゃあ俺はあの子のとこ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ろに向かうか、邪魔者も消えたし・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)                                                                                                                
                if ii[3]==2:
                    ii[14]=2
                    on[2]=4
                    on[4]=4                                                                                     
                    screen.draw.text("│(お願い！お願いだから生きてて美香！,・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│私はあなたを見捨てたりはしないから,,お願い│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・希望を捨てないで・・・・・・・・・),│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    serihu[0]=0
                    ii[23]=2                                                                                    
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)


            if data[2]==38 and on[2]==1 and on[4]==4 and kabe5.colliderect(cc):
                ii[15]=1
                ii[14]=1
                ii[23]=1
                if siinn2[0]<=17:#ゲームストーリーギャラリー
                    siinn2[0]=18
                if ii[3]==1:
                    screen.draw.text("│あれ、こんなところにパソコンがある、どうや│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ら壁除けのアクションゲームができるみたい、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│Dキーで遊べそうだ!・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==21 and so[2]==11:
                ii[14]=1
                ii[23]=1
                music[0]=9
                if ii[3]==2:
                    screen.draw.text("│あれ？ここは・・・・外？・・・私外に出られ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│たの？・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=0
                    screen.draw.text("│やった！脱出できた！！！・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ほんとにできてしまった・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==21 and so[2]==13:
                ii[14]=1
                ii[23]=1
                music[0]=9
                if ii[3]==3:
                    ii[23]=0
                    screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│音葉さん今頃喜んでるかな・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・どんな気持ちなんだろう・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==2:
                    screen.draw.text("│・・・・・・・多分きっと喜んでくれてるはず│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│でも、この後も、この先もちゃんと期待に応え│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│ていけるように頑張って生きていかなきゃ・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                if ii[3]==1:
                    ii[23]=0
                    screen.draw.text("│ちゃんと辛くても頑張らないとね・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・まだまだ私の人生は始まったばかり│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                    screen.draw.text("│・・・・・・・・・・帰ろう・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if on[3]==10:
                if items[0]==1:
                    ii[9]=0
                ii[14]=0
                so[5]=1
                so[6]=1#セーブストッパー（データーずらしてセーブするため）
                if ii[2]<3:
                 screen.draw.text("=======================\n➡今はスキップできません",(90,0),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
                screen.draw.text("│戻したアイテムを再び手に入れた・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
        if ii[3]==1 and ii[12]==6:
                ka[12]=1
                ii[14]=0
                so[5]=1
                if ii[2]<3:
                 screen.draw.text("=======================\n➡今はスキップできません",(100,0),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                screen.draw.text("│拾おうとしたがアイテムがいっぱいで持つこと│",(0,390),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
                screen.draw.text("│ができないのでそのアイテムを元に戻した・・│",(0,430),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
        if on[3]==9:
                ii[14]=0
                so[5]=1
                if ii[2]<3:
                 screen.draw.text("=======================\n➡今はスキップできません",(100,0),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
                screen.draw.text("│アイテムをもとの位置に戻した・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=30)
        if so[5]==1 and ii[3]!=1:
            if ii[2]<3:
                 screen.draw.text("=======================\n➡今はスキップできません",(100,0),fontname='a.ttc',owidth=0.3,color="RED",fontsize=20)
            screen.draw.text("セーブポイントがこの段落で出てきますスキ\nップするとセーブできないので要注意!!!!!!\n※次の文章からスキップが可能になります!!",(340,0),fontname='a.ttc',owidth=0.3,gcolor="PINK",color="WHITE",fontsize=17)
            if data[2]>11 and not data[2]==29 and not on[3]==20 and not on[3]==19:
                screen.draw.text("\n\n                          \n(現時点でITEMを5個持っている場合はセーブ\nできませんその場合はITEMを減らした状態で\nまたここのアイテムを取りにくるとその時に\nセーブができます!!）",(340,0),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=17)
        if ii[0]<3:#3はテキスト表示の速さii[1]はx座標ii[2]はｙ座標
            ii[0]+=1
            if ii[0]==3:
                ii[24]=1
                ii[0]=0
                ii[1]+=1
                if ii[1]==21:
                    ii[1]=0
                    ii[2]+=1
        if ii[2]>=3:
            ii[2]=3
        n1.y=ii[2]*40+490
        n.x=ii[1]*30+670
        n.y=ii[2]*40+450
        n1.draw()
        n.draw()
        if i[13]==0 and ii[2]<3:
            #if ii[14]!=1:
                #sounds.ec.play()
            #if ii[14]==1:
            sounds.ga.play()
            i[13]=4#何秒間ならないようにするか        
    if on[1]==4 and i[4]<=10 or on[3]!=0 and on[1]==4 and ii[5]!=0:#上移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        ii[3]=0#ロック画面にならないように
        if ii[4]==1:
               c.y-=3
        if ii[4]==0:
            m1.y+=3
    if on[1]==5 and i[4]<=10 or on[3]!=0 and on[1]==5 and ii[5]!=0:#下移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        ii[3]=0#ロック画面にならないように
        if ii[4]==1:
               c.y+=3
        if ii[4]==0:
            m1.y-=3
    if on[1]==6 and i[4]<=10 or on[3]!=0 and on[1]==6 and ii[5]!=0:#左移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        ii[3]=0#ロック画面にならないように
        if ii[4]==1:
               c.x-=3
        if ii[4]==0:
            m1.x+=3
    if on[1]==7 and i[4]<=10 or on[3]!=0 and on[1]==7 and ii[5]!=0:#右移動・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        ii[3]=0#ロック画面にならないように
        if ii[4]==1:
               c.x+=3
        if ii[4]==0:
            m1.x-=3       
#ストーリーシーン
    if on[3]==2:#一番最初のストーリーシーン
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=8#←そのテキストの段落数
                on[1]=3#←３テキスト表示
            if so[2]==2:#シーン２段落
                music[0]=0
                on[1]=7#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=10#何秒間歩かせるか
            if so[2]==3:#シーン3段落
                on[1]=0#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=60*1#何秒間歩かせるか
            if so[2]==4:#シーン4段落
                on[1]=6#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=10#何秒間歩かせるか
            if so[2]==5:#シーン5段落
                on[1]=0#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=60*1#何秒間歩かせるか
            if so[2]==6:#シーン6段落
                on[1]=5#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=10#何秒間歩かせるか
            if so[2]==7:#シーン7段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=4#←そのテキストの段落数
                    on[1]=3
                on[1]=3#←３テキスト表示
            if so[2]==8:#シーン8段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==1:#シーンを流すときはso[2]==1とon[3]==nを書く(nは流すシーンの種類)
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=5#←シーンでキャラクター動かす
                ii[5]=60*1#何秒間歩かせるか
            if so[2]==2:#シーン２段落
                on[1]=4#←３テキスト表示（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=60*1#何秒間歩かせるか
            if so[2]==3:#段落
                on[1]=0#←３テキスト表示（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=60*1#何秒間歩かせるか
            if so[2]==4:#段落
                ii[5]=60*1#何秒間歩かせるか
                on[1]=7#←３テキスト表示（キャラクター　４上　５下　６左　７右 0止まる）
            if so[2]==5:
                on[1]=3#←３テキスト表示（キャラクター　４上　５下　６左　７右 0止まる）
            if so[2]==6:
                ii[5]=60*1#何秒間歩かせるか
                on[1]=7#←３テキスト表示（キャラクター　４上　５下　６左　７右 0止まる）
            if so[2]==7:
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==8:
                on[1]=8#反応
                ii[6]=2#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==9:
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==10:
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==3:
          if ii[5]==0:
            if so[2]==1:#シーン1段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=3#←そのテキストの段落数
            if so[2]==2:#シーン2段落
                so[0]=3
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==3:#シーン3段落
                on[1]=6#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=10#何秒間歩かせるか
            if so[2]==4:#シーン4段落
                on[1]=7#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=10#何秒間歩かせるか
            if so[2]==5:#シーン5段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=4#←そのテキストの段落数
                    on[1]=3
            if so[2]==6:
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==4:#体育館倉庫、金庫のロック解除
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==3:#シーン3段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==4:#シーン4段落
                on[1]=5#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=10#何秒間歩かせるか
                music[0]=3
            if so[2]==5:#シーン5段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==6:#シーン6段落
                time[1]=45
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==5:#食道前廊下へ
        if ii[5]==0:
            data[2]=6
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==4:#シーン4段落                
                 if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=8#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン4段落                
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==6:#ドアが見えた
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=2#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==4:#シーン4段落                
                 if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン4段落                
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==7:#霊鬼が来た
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
                on[5]=0
                teki[0]=0
                tekilist[0].midtop=(680,40)
            if so[2]==4:#シーン4段落                
                 if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン4段落                
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==8:#アイテム合成
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
                item[12]=0
                item[13]=0
                if data[2]>27:
                    item[14]=0
                    item[15]=0
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落                
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==9:#
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
                   
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    so[2]=1#←シーン終わるとき
                    on[3]=0#←シーン終わるとき

    if on[3]==10:#
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
                    
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    so[2]=1#←シーン終わるとき
                    on[3]=0#←シーン終わるとき

    if on[3]==11:#昇降口
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=3#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==4:#シーン4段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン5段落
                on[1]=4#反応
                ii[5]=80#どのくらい反応させるか
            if so[2]==6:#シーン6段落                
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=180#どのくらい反応させるか
            if so[2]==7:#シーン6段落                
               if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=28#←そのテキストの段落数
                    on[1]=3
            if so[2]==8:#シーン7段落                
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==12:#
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=19#←そのテキストの段落数
                    on[1]=3
            if so[2]==2:#シーン２段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき

    if on[3]==13:#体育館倉庫、金庫のロック解除
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==3:#シーン3段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==4:#シーン4段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==14:#、金庫のロック解除
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=42#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==4:#シーン3段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=27#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン5段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==15:#ミニゲームクリア（総合ビジネス科）
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=48#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==4:#シーン4段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=10#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#
                 so[2]=1#←シーン終わるとき
                 on[3]=0#←シーン終わるとき
    if on[3]==16:#ミニゲームクリア（総合ビジネス科）
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=6#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==17:#紫のカギ
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=4#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=70#何秒間歩かせるか
            if so[2]==4:#シーン4段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
                so[0]=3
            if so[2]==5:#シーン5段落
                on[1]=5#
                ii[5]=70#どのくらい反応させるか
            if so[2]==6:#
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=60#どのくらい反応させるか
                so[0]=6
            if so[2]==7:#
                on[1]=0#
                ii[5]=60#どのくらい反応させるか
                so[0]=6
            if so[2]==8:#
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=2#←そのテキストの段落数
                    on[1]=3
            if so[2]==9:#
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==10:#
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=23#←そのテキストの段落数
                    on[1]=3
            if so[2]==11:#
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==18:#最後のロック解除
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=3#反応の種類
                ii[5]=90#どのくらい反応させるか
                data[2]=41
                ii[3]=0
                i[4]=30
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=4#←（キャラクター　４上　５下　６左　７右 0止まる）
                ii[5]=180#何秒間歩かせるか
            if so[2]==4:#シーン4段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=3#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン3段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==19:#最後の部屋
        if ii[5]==0:
            if so[2]==1:#シーン1段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==2:#シーン２段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=35#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#シーン3段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==4:#シーン4段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=8#←そのテキストの段落数
                    on[1]=3
            if so[2]==5:#シーン段落
                on[1]=8#反応
                ii[6]=1#反応の種類
                ii[5]=90#どのくらい反応させるか
            if so[2]==6:#シーン段落
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=23#←そのテキストの段落数
                    on[1]=3
            if so[2]==7:#シーン段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==20:#最後の部屋２
        if ii[5]==0:
            if so[2]==1:#ハンマーで割れそうだな
                on[1]=8
                ii[6]=3
                ii[5]=90
            if so[2]==2:#ハンマーで割れそう
                if ii[3]==0:#テキスト表示させるときはこれつける
                    ii[3]=1#←そのテキストの段落数
                    on[1]=3
            if so[2]==3:#割った
                so[0]=3
                on[1]=8
                ii[6]=1
                ii[5]=90
            if so[2]==4:#別れの会話と応援の会話
                if ii[3]==0:
                    ii[3]=21
                    on[1]=3
            if so[2]==5:#霊鬼出現
                ii[23]=5
                on[1]=8
                ii[6]=1
                ii[5]=90
            if so[2]==6:#逃げ始める
                if ii[3]==0:
                    ii[3]=3
                    on[1]=3
            if so[2]==7:#シーン段落
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき
    if on[3]==21:#最後
        if ii[5]==0:
            if so[2]==1:
                on[1]=0
                ii[5]=300
            if so[2]==2:
                on[1]=8
                ii[6]=1
                ii[5]=90
            if so[2]==3:
                on[1]=8
                ii[6]=2
                ii[5]=90
            if so[2]==4:
                on[1]=8
                ii[6]=3
                ii[5]=90
            if so[2]==5:
                on[1]=6
                ii[5]=60
            if so[2]==6:
                on[1]=0
                ii[5]=60
            if so[2]==7:
                on[1]=7
                ii[5]=120
            if so[2]==8:
                on[1]=0
                ii[5]=60
            if so[2]==9:
                on[1]=6
                ii[5]=60
            if so[2]==10:
                on[1]=0
                ii[5]=60
            if so[2]==11:
                if ii[3]==0:
                    ii[3]=2
                    on[1]=3
            if so[2]==12:
                on[1]=8
                ii[6]=1
                ii[5]=90
                ending[0].topleft=(0,500)
            if so[2]==13:
                if ii[3]==0:
                    ii[3]=3
                    on[1]=3
            if so[2]==14:
                on[1]=5
                ii[5]=1000
            if so[2]==15:
                on[1]=11
                so[2]=1#←シーン終わるとき
                on[3]=0#←シーン終わるとき       
    if ii[5]!=0:
        ii[5]-=1
        i[4]=0#←歩いているときはほかのプログラム止めるため
        if so[2]==6 and on[3]==11:
             k2.draw()
        if ii[5]==1:
            so[2]+=1
            ii[6]=0
        if (so[2]==5 and on[3]==19)or ((so[2]==3 or so[2]==5)and on[3]==20):
            k1.draw()
        if on[3]==21 and so[2]==14:
            if ending[0].y<-280:
                screen.clear()
            ending[0].draw()
            if ending[0].y>-680 and ii[5]<900:
                ending[0].y-=3
        
    if on[1]==8:#シーン内の反応
        #反応表示プログラム
        if  ii[6]==1:#沈黙
            maaku1.bottomright=c.topleft
            maaku1.draw()
            if ii[5]<70:
                maaku1n1.bottomright=c.topleft
                maaku1n1.draw()
            if ii[5]<50:
                maaku1n2.bottomright=c.topleft
                maaku1n2.draw()
            if ii[5]<30:
                maaku1n3.bottomright=c.topleft
                maaku1n3.draw()
        if  ii[6]==2:#？
            maaku2.bottomright=c.topleft
            maaku2.draw()
        if  ii[6]==3:#!
            maaku3.bottomright=c.topleft
            maaku3.draw()
        #反応表示プログラム   
#ストーリーシーン    
    cc.midbottom=c.midbottom
            #on[1]=3←セリフ出す#ii[3]＝n←セリフ出すときｎ段落出す#on[3]=ｎ←ｎ番目のストーリーシーン流す
    #if kabe1.colliderect(tekilist[1]):#0ンター1左2右3上4下
            #teki[1]=1
            #tekilist[0].x+=3
    #if kabe1.colliderect(tekilist[2]):#0ンター1左2右3上4下
            #teki[2]=1
            #tekilist[0].x-=4
    #if kabe1.colliderect(tekilist[4]):#0ンター1左2右3上4下
            #teki[4]=1
            #tekilist[0].y-=4
   # if kabe1.colliderect(tekilist[3]):#0ンター1左2右3上4下
            #teki[3]=1
            #tekilist[0].y+=4
        
    if on[2]!=ii[28] or on[4]!=iii[0]:
        ii[29]+=1
        ii[28]=on[2]
        tekilist[0].y=10000
        teki[0]+=1
        teki[5]=0
        if on[4]!=iii[0]:
            ka[14]=1
            iii[0]=on[4]
        if on[5]>=0:#追われてる最中にマップが変わったら
            i[4]=-30
            if on[2]==1:
                i[4]=-45
            teki[3]=c.x
            teki[4]=c.y
            if teki[0]>5:
                ii[27]=random.randrange(2)
                if ii[27]==1:
                    teki[0]=0
                    on[5]=-1
                    music[0]=0
        if teki[0]>16 and not on[5]>=0:
                ii[27]=random.randrange(5)
                if (ii[27]==0 or teki[0]==25) and lim[3]==0 and serihu[0]==0:#limでお化け出ないようにするストッパー
                    on[5]=0
                    teki[0]=0
                    teki[5]=45
                    if c.x<=350:
                        tekilist[0].x=700#敵の出現位置
                        if ii[4]==0:
                            tekilist[0].x+=300#敵の出現位置
                    if c.x>350:
                        tekilist[0].x=0#敵の出現位置
                        if ii[4]==0:
                            tekilist[0].x-=300#敵の出現位置
                    if c.y<=240:
                        tekilist[0].y=480#敵の出現位置
                        if ii[4]==0:
                            tekilist[0].y+=300#敵の出現位置
                    if c.y>240:
                        tekilist[0].y=0#敵の出現位置
                        if ii[4]==0:
                            tekilist[0].y-=300#敵の出現位置
    if teki[5]==40 and on[5]>=0:
            if on[1]==4:#上に向かってたら
                tekilist[0].center=c.center
                tekilist[0].y+=300#すこし下に出現させる
            if on[1]==5:#下に向かってたら
                tekilist[0].center=c.center
                tekilist[0].y-=300#すこし上に出現させる
            if on[1]==6:#左に向かってたら
                tekilist[0].center=c.center
                tekilist[0].x+=300#すこし右に出現させる
                teki[3]=tekilist[0].x
                teki[4]=tekilist[0].y
            if on[1]==7:#右に向かってたら
                tekilist[0].center=c.center
                tekilist[0].x-=300#すこし左に出現させる
                teki[3]=tekilist[0].x
                teki[4]=tekilist[0].y
                if on[2]==6 and ka[14]==1:#階段の場合
                    tekilist[0].x+=150#すこし右に出現させる
                    ka[14]=0
            so[0]=8
    if on[2]==6 and -800<m1.x<-5  and on[5]>=0 and teki[5]==239:
            teki[1]=1
    if on[2]==6 and -800<m1.x<-5  and on[5]>=0 and teki[5]==300:
        if (teki[1]==3 and m1.x>teki[2]) or (teki[1]==2 and m1.x<teki[2]):
            if teki[4]<195:#ぶつかってないのにゲームオーバーになるのを防ぐため
                tekilist[0].x=teki[3]
                tekilist[0].y=teki[4]
            teki[1]=0
    if teki[1]==1:
        if teki[1]==1:
            if m1.x<-400:
                tekilist[0].y=350
                tekilist[0].x=800
                teki[1]=2
            if m1.x>-400:
                tekilist[0].y=350
                tekilist[0].x=-100
                teki[1]=3
            teki[2]=m1.x
    if teki[5]<350:
        teki[5]+=1
    if on[5]>=0:#0センター1左2右3上4下・・敵・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        tekilist[5].center=tekilist[0].center
        if on[0]>=1 or data[2]<=9:
            on[5]=-1
        if not (on[0]>=1 or data[2]<=9 or serihu[0]==1):
            music[0]=3
        if on[5]==0 and so[2]==1:
            if tekilist[0].x>c.x:
                tekilist[0].x-=3
                on[5]=5
            if tekilist[0].x<c.x:
                tekilist[0].x+=3
                on[5]=5
            if tekilist[0].y>c.y:
                tekilist[0].y-=3
                on[5]=5
            if tekilist[0].y<c.y:
                tekilist[0].y+=3
                on[5]=5
            if teki[5]<239 and on[2]==6:
                if tekilist[0].x>c.x:
                    tekilist[0].x+=3
                if tekilist[0].x<c.x:
                    tekilist[0].x-=3
                if tekilist[0].y>c.y:
                    tekilist[0].y+=3  
                if tekilist[0].y<c.y:
                    tekilist[0].y-=3
            if ii[4]==0  and so[1]!=1 and i[4]!=30:
                if on[1]==4:#逆も作る
                   tekilist[0].y+=3
                   if tekilist[0].y<c.y:#
                        tekilist[0].y+=6
                if on[1]==5:
                    tekilist[0].y-=3
                    if tekilist[0].y>c.y:#
                       tekilist[0].y-=6
                if on[1]==6:
                    tekilist[0].x+=3
                    if tekilist[0].x<c.x:#
                       tekilist[0].x+=6
                if on[1]==7:
                    tekilist[0].x-=3
                    if tekilist[0].x>c.x:#
                       tekilist[0].x-=6
        if on[5]!=0 and ii[25]<4 and on[2]==0:
            ii[25]+=1
        if on[5]!=0 and ii[25]<4 and on[2]!=0:
            ii[25]+=random.randrange(5)
            if on[2]==6:
                ii[25]+=1
        if on[5]!=0 and ii[25]>=4:
            on[5]=0
            ii[25]=0
        #if on[5]==1:#左移動
         #   tekilist[0].x-=3
          #  if tekilist[1].x<100:
           #     tekilist[0].x+=6
        #if on[5]==2:#右移動
         #   tekilist[0].x+=3
          #  if tekilist[2].x>600:
           #     tekilist[0].x-=6
        #if on[5]==3:#上移動
         #   tekilist[0].y-=3
          #  if tekilist[3].y<100:
           #     tekilist[0].y+=6
        #if on[5]==4 :#下移動
         #   tekilist[0].y+=3
          #  if tekilist[4].y>380:
           #     tekilist[0].y-=6

        #tekilist[4].midtop=tekilist[0].midbottom
        #tekilist[3].midbottom=tekilist[0].midtop
        #tekilist[1].midright=tekilist[0].midleft
        #tekilist[2].midleft=tekilist[0].midright
        #tekilist[0].draw()
        #tekilist[1].draw()
        #tekilist[2].draw()
        #tekilist[3].draw()
        #tekilist[4].draw()
                #teki[0]=random.randrange(4)+1#1～4の数字をランダムで出す
            #if teki[0]==1:#左に向かう
                #on[5]=1
                #if teki[1]==1:#左側がぶつかっていた時
                   # on[5]=0
           # if teki[0]==2:#右に向かう
                #on[5]=2
              #  if teki[2]==1:#右側がぶつかっていた時
           #         on[5]=0
           # if teki[0]==3:#上に向かう
           #     on[5]=3
          #      if teki[3]==1:#上側がぶつかっていた時
           #         on[5]=0
          #  if teki[0]==4:#下に向かう
          #      on[5]=4
           #     if teki[4]==1:#下側がぶつかっていた時
         #           on[5]=0
################################動く矢印
    if on[2]==6 and data[2]>10:
        move1.draw()
    if on[5]==-1:
        if data[2]>10 and on[2]==0 and on[4]==2:
            item1move.draw()
        if data[2]>10 and on[2]==-2 and on[4]==2:
            item2move.draw()
        if data[2]>10 and on[2]==8 and on[4]==2:
            item4move.draw()
        if data[2]>11 and on[2]==8 and on[4]==1:
            item5move.draw()
        if data[2]>13 and on[2]==-2 and on[4]==1:
            item6move.draw()
        if data[2]>16 and on[2]==0 and on[4]==1:
            item7move.draw()
        if data[2]>17 and on[2]==0 and on[4]==1:
            item8move.draw()
        if data[2]>20 and on[2]==-5 and on[4]==3:
            item9move.draw()
        if data[2]>21 and on[2]==1 and on[4]==3:
            item10move.draw()
        if data[2]>22 and on[2]==7 and on[4]==3:
            item11move.draw()
        if 27>data[2]>24 and on[2]==-6 and on[4]==3:
            item12move.draw()
        if 27>data[2]>25 and on[2]==0 and on[4]==3:
            item13move.draw()
        if 28==data[2] and on[2]==-2 and on[4]==3:
            item15move.draw()
        if 35<data[2] and on[2]==8 and on[4]==4:
            item18move.draw()
################################動く矢印
    if i[4]==30 and (on[1]==0 or 3<on[1]<8) and on[5]==-1:#←移動していない最中押しボタンの説明画面に表示
        #kabann.draw()
        if item[3]==1 and not 44<=data[2]<=54 and not data[2]==4:
            screen.draw.text("Aキーで現在地を見る",(80,0),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="PINK",fontsize=22)
        if  on[4]==3 and on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc))and data[2]>=24:
            screen.draw.text("Sキーでアイテムを合成する",(0,140),fontname='a.ttc',owidth=0.3,gcolor="BLUE",color="PINK",fontsize=22)
        if not 44<=data[2]<=54 and not data[2]==4:
            screen.draw.text("┌─┐\n│Ｅ│\n│を│\n│押│\n│し│\n│て│\n│ヒ│\n│ン│\n│ト│\n│表│\n│示│\n└─┘",(647,30),fontname='a.ttc',owidth=1.3,gcolor="PINK",color="RED",fontsize=19)
            screen.draw.text(" Dキーで確かめる Sキーでアイテム欄開く Ｗキーでゲームを中断",(0,460),fontname='a.ttc',owidth=0.3,gcolor="WHITE",color="LIGHT BLUE",fontsize=23)
        if ii[3]!=0 and (on[1]==0 or 3<on[1]<8) and on[5]==-1:
            tennmetu.draw()
        screen.draw.text(str(on[4])+"階",(0,0),fontname='a.ttc',owidth=0.3,color="LIGHT BLUE",gcolor="WHITE",fontsize=30)
        if data[2]==-99:
            screen.draw.text("目標[矢印キーで歩いてみよう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==-98:
            screen.draw.text("目標[マップ右にある扉にぶつかろう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==-97:
            screen.draw.text("目標[マップ左にあるPCを調べよう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==-96:
            screen.draw.text("目標[Wでゲームを終了しよう！！]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)   
        if -1<data[2]<1 or 2<data[2]<4 or 4<data[2]<7 or data[2]==8:
            screen.draw.text("目標[マップを探索してみよう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 9<=data[2]<11:
            screen.draw.text("目標[2Fを探索してみよう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==1:
            screen.draw.text("目標[電話を探してみよう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 11==data[2]:
            screen.draw.text("目標[1Fを探索してみよう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 12==data[2]:
            screen.draw.text("目標[a号室を探索してみよう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 12<data[2]<16:
            screen.draw.text("目標[メモ帳とどこかの部屋のカギをもとの位置\nに戻した状態でデザイン科b号室を探索しよう!!]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=18)
        if data[2]==16:
            screen.draw.text("目標[メモ帳とどこかの部屋のカギをもとの位置\nに戻した状態にして、1Fで青い絵の具を探そう!!]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=18)
        if data[2]==17:
            screen.draw.text("目標[メモ帳とどこかの部屋のカギをもとの位置\nに戻した状態で、他の机の下も調べてみよう!!!!]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=18)
        if data[2]==19:
            screen.draw.text("目標[a号室の金庫の,暗証番号を\n     調べてロックを解除しよう\n",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==2:
            screen.draw.text("目標[アイテムを探そう]",(325,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==4:
            screen.draw.text("目標[ロッカーに隠れよう]",(325,0),fontname='a.ttc',owidth=0.3,color="RED",fontsize=22)
        if data[2]==7:
            screen.draw.text("目標[館内マップの？の所に行こう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==20:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップの２つの\n ITEMだけを持った状態で3Fを探索してみよう！]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=18)
        if data[2]==21:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップ,長い棒,の3つの\nITEMだけをもって3Fで高い所にあるITEMを探そう!!!!!!]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=16)
        if data[2]==22:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップ,懐中電灯,の3つ\nのITEMだけをもって3Fで暗い所にあるITEMを探そう!!!!]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=16)
        if data[2]==23:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップ,被覆室のカギの\n３つのITEMだけをもって3F被覆室のを探索してみよう！]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=16)
        if data[2]==24:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップ,被覆室のカギの\n３つのITEMだけをもって合成できそうなITEMを探そう！]",(290,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=16)
        if data[2]==25:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップ,被覆室のカ\nギ,曲がった棒の4つのITEMだけを持ち,合成可能な\n2つ目のITEMを探そう！！！！]",(288,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=17)
        if data[2]==26:
            screen.draw.text("目標[どこかの通路のカギ,館内のマップ,被覆室のカ\nギ,曲がった棒,ゴミ箱の5つのITEMを持った状態で\nITEMを合成しに行こう！！！！]",(288,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=17)
        if 27<=data[2]<=28:
            screen.draw.text("目標[バケツと何かITEMを合成しよう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==29:
            screen.draw.text("目標[プールに沈んだITEMを取ろう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==30:
            screen.draw.text("目標[4Fを探索してみよう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 33>=data[2]>=31:
            screen.draw.text("目標[ほかのパソコンを調べてみよう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==34:
            screen.draw.text("目標[パスワードを入力してみよう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==35:
            screen.draw.text("目標[さっきのpcを確かめよう]",(310,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if data[2]==36:
            screen.draw.text("目標[紫の鍵を使い新しいMAPに行こう]",(300,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 40>data[2]>=38:
            screen.draw.text("目標[新しいMAPを探索しよう]",(300,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 41==data[2]:
            screen.draw.text("目標[扉のそばにある本を読んでみよう]",(300,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 42==data[2]:
            screen.draw.text("目標[扉の先へ向かおう]",(300,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 43==data[2]:
            screen.draw.text("目標[ひび割れた壁をたたこう]",(300,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
        if 44<=data[2]:
            screen.draw.text("目標[脱出しよう]",(300,0),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=22)
    if ((music[0]==3 and data[2]==4)or (music[0]==7 and(45==data[2] or 47==data[2] or 49==data[2] or 51==data[2] or 53==data[2] or 55==data[2]))) and(on[1]==0 or 3<on[1]<8) and on[1]!=3:#タイムリミット表示
        if time[0]<30:
            if data[2]<40:
                screen.draw.text("急げ..残り"+str(time[1])+"秒",(0,40),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
            if data[2]>40:
                screen.draw.text("霊鬼が来るまで残り"+str(time[1])+"秒",(0,40),fontname='a.ttc',owidth=0.3,color="RED",fontsize=30)
    if time[1]!=-1 and data[2]>40:
        if  data[2]==45 or data[2]==47:
            lim[1]=c.x+time[1]*70
            lim[2]=c.y
        if data[2]==49:
            lim[2]=c.y+time[1]*70
            lim[1]=c.x
        if  data[2]==51 or data[2]==53 or data[2]==55:
            lim[1]=c.x+time[1]*70*-1
            lim[2]=c.y
        lim[0].x=lim[1]
        lim[0].y=lim[2]
        if data[2]==44 or data[2]==46 or data[2]==48 or data[2]==50 or data[2]==52 or data[2]==54:
            lim[0].y=1000
        lim[0].draw()
    if on[1]==9:#←暗号ロック見ているとき
        if (on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc)))or on[2]==0 and (on[4]==1 or on[4]==4):#パスワード解除するところだったら
            on[1]=13#パスワード画面へ
        ii[3]=0
        if on[2]==2:
            if kabe5.colliderect(cc):
                R.draw()
                R1.draw()
                R5.x=9999
                if i[4]!=30 and (ii[16]==0 or ii[16]==116):#ボタン押されていた時
                    R5.topleft=(ii[16],70)
                R5.draw()
                screen.draw.text("["+str(ii[17]),(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[18]),(116,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("赤　黄",(0,200),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=64)
                screen.draw.text("aで戻る　 (↑マウスを動かしてパネルをクリック)",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if kabe6.colliderect(cc):
                R2.draw()
                R3.draw()
                R5.x=9999
                if i[4]!=30 and (ii[16]==232 or ii[16]==348):#ボタン押されていた時
                    R5.topleft=(ii[16],70)
                R5.draw()
                screen.draw.text("["+str(ii[19]),(232,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[20]),(348,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("　　　　青　緑",(0,200),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=64)
                screen.draw.text("aで戻る　 (↑マウスを動かしてパネルをクリック)",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if kabe7.colliderect(cc):
                R4.draw()
                R5.x=9999
                if i[4]!=30 and ii[16]==464:#ボタン押されていた時
                    R5.topleft=(ii[16],70)
                R5.draw()
                screen.draw.text("["+str(ii[21]),(464,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("　　　　　　　　白",(0,200),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=64)
                screen.draw.text("aで戻る　 (↑マウスを動かしてパネルをクリック)",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if on[2]==1:
             A2F.draw()
        if i[4]==30:
                screen.draw.text("aで戻る",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if i[4]==30 and (on[2]==-1 or on[2]==-6):
                screen.draw.text("aで戻る　 (↑マウスを動かしてパネルをクリック)",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if on[2]==-1:
            if kabe6.colliderect(cc):#←どこのロック画面出すか指定
                R.draw()
                R1.draw()
                R2.draw()
                R3.draw()
                R4.draw()
                R5.x=9999
                if i[4]!=30:#ボタン押されていた時
                    R5.topleft=(ii[16],70)
                R5.draw()
                screen.draw.text("["+str(ii[17]),(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[18]),(116,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[19]),(232,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[20]),(348,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[21]),(464,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("私　彼　家　月　日",(0,200),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=64)
        if on[2]==-6:
            if kabe5.colliderect(cc):#←どこのロック画面出すか指定
                R.draw()
                R1.draw()
                R2.draw()
                R3.draw()
                R4.draw()
                R5.x=9999
                if i[4]!=30:#ボタン押されていた時
                    R5.topleft=(ii[16],70)
                R5.draw()
                screen.draw.text("["+str(ii[17]),(0,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[18]),(116,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[19]),(232,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[20]),(348,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
                screen.draw.text("["+str(ii[21]),(464,90),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=70)
    if on[1]==10:#GAME OVERとリセット
            if time[1]==0:#GAMEOVER
                time[2]-=1
                over.draw()
                music[0]=0
            if time[1]==-1:#リセット
                time[2]+=1
                if time[2]%10<2:
                    roudo[0].draw()
                if 2<=time[2]%10<5:
                    roudo[1].draw()
                if 5<=time[2]%10<8:
                    roudo[2].draw()
                if 8<=time[2]%10<=9:
                    roudo[3].draw()
                screen.draw.text("残り\nあと"+str((time[2]-240)*-2)+"%",(0,130),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=50)
                music[0]=0
            if   (time[2]-240)*-2<10:
                 screen.draw.text("---------→OK!",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<20:
                 screen.draw.text("---------",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<30:
                 screen.draw.text("--------",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<40:
                 screen.draw.text("-------",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<50:
                 screen.draw.text("------",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<60:
                 screen.draw.text("-----",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<70:
                 screen.draw.text("----",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<80:
                 screen.draw.text("---",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<90:
                 screen.draw.text("--",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if   (time[2]-240)*-2<100:
                 c1.draw()
                 c1.topleft=(135,424)
                 screen.draw.text("-",(170,430),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=60)
            if time[2]==240:#1秒待ってスタート画面に戻る（リセット）
                on[1]=0
                on[2]=0
                on[3]=0
                data[2]=0
                on[0]=1
                c1.topleft=(350,300)
                c.topleft=(350,300)#プレイヤーの初期位置
                ii[17]=0#暗号リセット
                ii[18]=0#暗号リセット
                ii[19]=0#暗号リセット
                ii[20]=0#暗号リセット
                ii[21]=0#暗号リセット
                basyo[0]=0
                basyo[1]=0
                basyo[2]=0
                ii[3]=0
                time[2]=180
            if time[2]==0:#3秒GAMEOVER表示
                time[2]=180#3秒GAMEOVER表示できるように戻す
                on[1]=0
                on[2]=0
                on[3]=0
                data[2]=0
                on[0]=1
                c.topleft=(350,300)#プレイヤーの初期位置
            if i[0]<21:#アイテムリセット
                if item[i[0]]!=0:
                    item[i[0]]=0  
                i[0]+=1
    if on[1]==13:#パスワード
        if on[4]==4 and on[2]==8:
            pc.draw()
        if on[4]==1:
            pasu[0].draw()
        if on[4]==4 and on[2]==0:
            pasu[1].draw()
        pc1.draw()
        pc2.draw()

        if i[4]<20 and ka[6]==1:
            if keyboard.a:
                    listkey[0].draw()
            if keyboard.b:
                    listkey[1].draw()
            if keyboard.c:
                    listkey[2].draw()
            if keyboard.d:
                    listkey[3].draw()
            if keyboard.e:
                    listkey[4].draw()
            if keyboard.f:
                    listkey[5].draw()
            if keyboard.g:
                    listkey[6].draw()
            if keyboard.h:
                    listkey[7].draw()
            if keyboard.i:
                    listkey[8].draw()
            if keyboard.j:
                    listkey[9].draw()
            if keyboard.k:
                    listkey[10].draw()
            if keyboard.l:
                    listkey[11].draw()
            if keyboard.m:
                    listkey[12].draw()
            if keyboard.n:
                    listkey[13].draw()
            if keyboard.o:
                    listkey[14].draw()
            if keyboard.p:
                    listkey[15].draw()
            if keyboard.q:
                    listkey[16].draw()
            if keyboard.r:
                    listkey[17].draw()
            if keyboard.s:
                    listkey[18].draw()
            if keyboard.t:
                    listkey[19].draw()
            if keyboard.u:
                    listkey[20].draw()
            if keyboard.v:
                    listkey[21].draw()
            if keyboard.w:
                    listkey[22].draw()
            if keyboard.x:
                    listkey[23].draw()
            if keyboard.y:
                    listkey[24].draw()
            if keyboard.z:
                    listkey[25].draw()
        if i[4]==1:
            so[0]=1
            ka[4]+=1
            if ka[4]==22:
                 ka[5]=ka[2]
        if i[4]==30:
            ka[6]=1
            screen.draw.text(" ↓キーボードをクリックしてパスワードの入力↓\n",(0,18),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            screen.draw.text(" ➡　　　　　➡\n\n↑マウスでボタンをクリックして、戻る、パスワード書き直し",(0,400),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=25)
            if  ka[4]<=22:
                if keyboard.a and i[4]==30:
                        ka[2]+="A"
                        i[4]=0
                if keyboard.b and i[4]==30:
                        ka[2]+="B"
                        i[4]=0
                if keyboard.c and i[4]==30:
                        ka[2]+="C"
                        i[4]=0
                if keyboard.d and i[4]==30:
                        ka[2]+="D"
                        i[4]=0
                if keyboard.e and i[4]==30:
                        ka[2]+="E"
                        i[4]=0
                if keyboard.f and i[4]==30:
                        ka[2]+="F"
                        i[4]=0
                if keyboard.g and i[4]==30:
                        ka[2]+="G"
                        i[4]=0
                if keyboard.h and i[4]==30:
                        ka[2]+="H"
                        i[4]=0
                if keyboard.i and i[4]==30:
                        ka[2]+="I"
                        i[4]=0
                if keyboard.j and i[4]==30:
                        ka[2]+="J"
                        i[4]=0
                if keyboard.k and i[4]==30:
                        ka[2]+="K"
                        i[4]=0
                if keyboard.l and i[4]==30:
                        ka[2]+="L"
                        i[4]=0
                if keyboard.m and i[4]==30:
                        ka[2]+="M"
                        i[4]=0
                if keyboard.n and i[4]==30:
                        ka[2]+="N"
                        i[4]=0
                if keyboard.o and i[4]==30:
                        ka[2]+="O"
                        i[4]=0
                if keyboard.p and i[4]==30:
                        ka[2]+="P"
                        i[4]=0
                if keyboard.q and i[4]==30:
                        ka[2]+="Q"
                        i[4]=0
                if keyboard.r and i[4]==30:
                        ka[2]+="R"
                        i[4]=0
                if keyboard.s and i[4]==30:
                        ka[2]+="S"
                        i[4]=0
                if keyboard.t and i[4]==30:
                        ka[2]+="T"
                        i[4]=0
                if keyboard.u and i[4]==30:
                        ka[2]+="U"
                        i[4]=0
                if keyboard.v and i[4]==30:
                        ka[2]+="V"
                        i[4]=0
                if keyboard.w and i[4]==30:
                        ka[2]+="W"
                        i[4]=0
                if keyboard.x and i[4]==30:
                        ka[2]+="X"
                        i[4]=0
                if keyboard.y and i[4]==30:
                        ka[2]+="Y"
                        i[4]=0
                if keyboard.z and i[4]==30:
                        ka[2]+="Z"
                        i[4]=0
        if ka[4]>22:
            ka[2]=ka[5]
            ka[4]=22
        screen.draw.text(ka[2],(150,250),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=35)
    if on[3]==21 and so[2]==1 and ii[5]!=0:
        owari.y=ii[5]*1+335
        owari.draw()
    if on[3]==20 and 6>=so[2]>=5 and not (5<ii[23]<10 or -2>ii[23]>-12)and on[1]!=2:
        lim[0].topleft=(50,150)
        lim[0].draw()
    if on[1]==14:
        game.draw()
        music[0]=7
    if on[1]==15:
        game2.draw()
        music[0]=7
    if on[1]==16:
        game3.draw()
        music[0]=7
    if keyboard.d and(on[1]==0 or 3<on[1]<8) and i[4]==30 and ii[3]==0 and so[3]==0:
        screen.draw.text(" Ｄを押してもそばに\n 確かめれる物がない",(c.x-91,c.y),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=17)
    if on[1]==17:
        screen.draw.text("[ゲームストーリーを進めるためのヒント↓]",(50,50),fontname='a.ttc',owidth=5,color="ORANGE",fontsize=30)
        screen.draw.text("Eで戻る",(0,450),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if data[2]==0:
            screen.draw.text("どこかに今の時間帯がわかる物は\nないだろうか？わかりそうな物の\n目の前にいる状態で、キーボード\nのDキーを押してみるといい,しか\nし,,歩きながら調べることはでき\nないのでしっかり止まるように！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==1:
            screen.draw.text("電話を探してみよう、時計がある\n部屋に来るまでに歩いた所をよく\n調べてみるといい、おそらく電話\nらしきものがあるだろう、見つけ\nたら,近くで再びDキーを押してみ\nよう、ストーリーが進行する！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==2:
            screen.draw.text("時計のあった部屋から、電話のあ\nった場所に来るまでの歩いた所に\nアイテムがある、時計があった部\n屋の入り口にとても近い場所だ、\n",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==3:
            screen.draw.text("私、彼、家、月、日の５つの漢字\n日記内にも同じような漢字がある\nそれぞれの個数を当てはめてみる\nといい、正解すると自動でストー\nリーが進み、新しいイベントが起\nこる,,青い本も呼んでみるといい",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==4:
            screen.draw.text("時計のあった部屋に、ロッカーが\nある、、そこに向かって,,,Dキー\nでロッカーらしきものを調べよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==5:
            screen.draw.text("電話の近くを探索してみるといい",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==6:
            screen.draw.text("壁に貼ってある、物を調べてみよ\n",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==7:
            screen.draw.text("黄色いじゅうたんがある部屋の壁\n付近を歩いてみよう！！イベント\nが発生するだろう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==8:
            screen.draw.text("館内マップが貼ってあった部屋に\nあるパソコンと、その部屋の壁に\n書かれている,5人の会話を参考に\nして、その右隣の部屋の壁にある\nパネルの数字をそろえるといい！\nちなみに黄色の所の数字は５！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==9:
            screen.draw.text("新しいマップの部屋や通路で文が\n書かれてる壁を3つ見つけて,,,そ\nれぞれＤキーで調べて読んでみよ\nう!3か所調べ終わると,,またイベ\nントが発生するだろう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==10:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("2Fで地図の以下の場所に本がない\nかを探してみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==11:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==12:
            hinnto[6].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==13:
            hinnto[3].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、デザイン\n科のカギ、以外のアイテムはもと\nの場所に戻した状態にしよう！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==14:
            hinnto[4].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、その時は黄色い絵の具を\n持った状態にしよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==15:
            screen.draw.text("表示できるヒントはありません,,\n",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==16:
            hinnto[0].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、左から２番目上から２番\n目の位置の机を調べてみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==17:
            hinnto[4].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、その時は、何の絵の具を\n持っているのかで、その部屋にあ\nる本の内容が変わる、持つ絵の具\nの種類や個数を変えて見てみよう\n!!そして右から2番目下から2番目\nの机にある金庫のロックを解こう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==19:
            hinnto[4].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("1Fで地図の以下の場所を探索して\nみよう、その時は、赤い絵の具を\n持った状態で探索してみよう、、\nまた、赤い絵の具と、赤色以外の\n絵具も持った状態で部屋の探索を\nしてみよう！！,a号室にあった金\n庫のロックを解く為の情報がある",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==20:
            hinnto[5].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップの二つのア\nイテムだけ持った状態にしよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==21:
            hinnto[1].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、長い棒の\n三つのアイテムだけを所持して探\n索するようにしよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==22:
            hinnto[7].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、懐中電灯\nの三つのアイテムだけを所持して\n探索するようにしよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==23:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、被覆室の\nカギの三つのアイテムだけを所持\nして探索するようにしよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==24:
            hinnto[6].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、被覆室の\nカギの三つのアイテムだけを所持\nして探索するようにしよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==25:
            hinnto[0].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、被覆室の\nカギ、曲がった棒の四つのアイテ\nムだけを所持して探索しよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==26:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、被覆室の\nカギ、曲がった棒、ゴミ箱を手に\n持った状態にしておこう！！！！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==27:
            hinnto[3].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、被覆室の\nカギ、バケツ以外のアイテムはも\nは持たない状態にしよう！！！！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==28:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時は、どこかの通路\nのカギ、館内のマップ、被覆室の\nカギ、バケツ、ロープを手に持っ\nた状態にしておこう！！！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==29:
            hinnto[0].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("3Fで地図の以下の場所を探索して\nみよう、その時、プールサイドの\n白い部分を調べてみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==30:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("4Fで地図の以下の場所を探索して\nみよう、その時、どこかの通路の\nカギ、館内のマップ、ビジネス科\nのカギ以外のアイテムは、もとの\n位置に戻しておくのが望ましい！！",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==31:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("4Fで地図の以下の場所を探索して\nみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==32:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("4Fで地図の以下の場所を探索して\nみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==34:
            screen.draw.text("2Fで見つけた、メモ帳の内容や、\n4階の様々な部屋の床や,壁などに\n書かれた、数字や文字を参考にし\nてパスワードを解くといい",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==35:
            hinnto[8].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("4Fで地図の以下の場所を探索して\nみよう,,その際新しくアイテムを\n手にもてるようにしておくといいい",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if data[2]==36:
            screen.draw.text("4Fにある紫の扉に、、、ミニゲー\nムができるパソコンの近くにあっ\nたカギを持った状態でぶつかって\nみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if 39>=data[2]>=38:
            hinnto[0].draw()
            screen.draw.text(" ↑(青色になっているところ)↑",(172,450),fontname='a.ttc',owidth=3,gcolor="BLUE",color="WHITE",fontsize=23)
            screen.draw.text("今いる4階のマップにある,壁除け\nのミニゲームをプレイし、新しい\nマップの部屋の床や壁に書かれて\nいる数字や文字を参考にして,4Fの\n以下の場所にあろロックのかかった\n扉を開けてみよう",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
        if 40<=data[2] or data[2]<0:
            screen.draw.text("表示できるヒントはありません,,\n",(172,100),fontname='a.ttc',owidth=2,color="WHITE",fontsize=23)
    #if so[4]==1:
    if v[0]<300 and data[2]>=56:#ラストシーンの一瞬暗黙になるところ
        screen.clear()
        if v[0]>150:
            music[0]=0

    if on[3]==19 and  (so[2]==3 or so[2]==5):
            kotarou7.draw()
    if serihu[1]==0 and keyboard.a and on[0]==6  and  sgyara[6]==0:
        serihu[2]=0
        serihu[3]=1
    if serihu[1]==0 and keyboard.s and on[0]==6  and  sgyara[6]<2:
        serihu[2]=0
        serihu[3]=1
    if serihu[1]==0 and keyboard.d and on[0]==6  and  sgyara[6]<3:
        serihu[2]=0
        serihu[3]=1
    if serihu[2]!=50 and serihu[3]==1:
        screen.draw.text("このゲームはまだプレイできません！",(172,450),fontname='a.ttc',owidth=2,gcolor="RED",color="ORANGE",fontsize=23)
    if so[4]==1 and (on[1]==0 or 3<on[1]<8):
        screen.draw.text(" Ｄを押して拾ったアイテム\n   を元の位置に戻す",(c.x-91,c.y+30),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=17)
        so[4]=0
    if so[4]==2 and (on[1]==0 or 3<on[1]<8):
        screen.draw.text(" Ｄを押して戻したアイテム\n   再びゲットする!!",(c.x-91,c.y+30),fontname='a.ttc',owidth=0.3,color="GREEN",fontsize=17)
        so[4]=0
def update():
    #セーブストッパー２↓
    if item[1]==1 and (on[1]==0 or 3<on[1]<8):
        items[1]=1
    if item[2]==1 and (on[1]==0 or 3<on[1]<8):
        items[2]=1
    if item[3]==1 and (on[1]==0 or 3<on[1]<8):
        items[3]=1
    if item[4]==1 and (on[1]==0 or 3<on[1]<8):
        items[4]=1
    if item[5]==1 and (on[1]==0 or 3<on[1]<8):
        items[5]=1
    if item[6]==1 and (on[1]==0 or 3<on[1]<8):
        items[6]=1
    if item[7]==1 and (on[1]==0 or 3<on[1]<8):
        items[7]=1
    if item[8]==1 and (on[1]==0 or 3<on[1]<8):
        items[8]=1
    if item[9]==1 and (on[1]==0 or 3<on[1]<8):
        items[9]=1
    if item[10]==1 and (on[1]==0 or 3<on[1]<8):
        items[10]=1
    if item[11]==1 and (on[1]==0 or 3<on[1]<8):
        items[11]=1
    if item[12]==1 and (on[1]==0 or 3<on[1]<8):
        items[12]=1
    if item[13]==1 and (on[1]==0 or 3<on[1]<8):
        items[13]=1
    if item[14]==1 and (on[1]==0 or 3<on[1]<8):
        items[14]=1
    if item[15]==1 and (on[1]==0 or 3<on[1]<8):
        items[15]=1
    if item[16]==1 and (on[1]==0 or 3<on[1]<8):
        items[16]=1
    if item[17]==1 and (on[1]==0 or 3<on[1]<8):
        items[17]=1
    if item[18]==1 and (on[1]==0 or 3<on[1]<8):
        items[18]=1
    if item[19]==1 and (on[1]==0 or 3<on[1]<8):
        items[19]=1
    if on[1]==15:
        game2.update()
    if on[1]==16:
        game3.update()
################################動く矢印
    if on[2]==6 and data[2]>10:
        move1.update()
    if data[2]>10 and on[2]==0 and on[4]==2:
        item1move.update()
    if data[2]>10 and on[2]==-2 and on[4]==2:
        item2move.update()
    if data[2]>10 and on[2]==8 and on[4]==2:
        item4move.update()
    if data[2]>11 and on[2]==8 and on[4]==1:
        item5move.update()
    if data[2]>13 and on[2]==-2 and on[4]==1:
        item6move.update()
    if data[2]>16 and on[2]==0 and on[4]==1:
        item7move.update()
    if data[2]>17 and on[2]==0 and on[4]==1:
        item8move.update()
    if data[2]>20 and on[2]==-5 and on[4]==3:
        item9move.update()
    if data[2]>21 and on[2]==1 and on[4]==3:
        item10move.update()
    if data[2]>22 and on[2]==7 and on[4]==3:
        item11move.update()
    if 27>data[2]>24 and on[2]==-6 and on[4]==3:
        item12move.update()
    if 27>data[2]>25 and on[2]==0 and on[4]==3:
        item13move.update()
    if 28==data[2] and on[2]==-2 and on[4]==3:
        item15move.update()
    if 35<data[2] and on[2]==8 and on[4]==4:
        item18move.update()
################################動く矢印
        
    #マップ内の物check・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・

    #if on[1]!=3 and i[4]==30:#and ii[3]==段落数 and 障害物.colliderect(c):
     #   ii[3]=2
    if  on[2]==-2 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==0:#体育館倉庫マップの壁４にぶつかってた時
        ii[3]=3
    if  on[2]==0 and kabe3.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==1:#体育館　電話
        on[3]=3#←ストーリーのシーン流すとき
    if  on[2]==0 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==2:#体育館　鍵
        ii[3]=1
    if  on[2]==0 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]>10 and item[1]==1 and on[4]==2 and on[5]==-1:#体育館　鍵を戻す
        so[4]=1
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8):#アイテム
            on[3]=9#アイテム戻すとき
            item[1]=0
    if  on[2]==0 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]>10 and item[1]!=1 and on[4]==2 and on[5]==-1:#体育館　鍵をとる
        so[4]=2
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10#アイテム再びとるとき
            if items[1]==0:#セーブストッパー２
                items[0]=0
            if items[1]==1:
                items[0]=1
            item[1]=1
    if  on[2]==-1 and  kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==3:
        ii[3]=5
    if  on[2]==-1 and kabe6.colliderect(cc) and on[1]!=9 and i[4]==30 and data[2]==3:#体育館　
        ii[3]=-1#←ロック画面出させるとき
    if  on[2]==-2 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==4:#体育館　ロッカー
        ii[3]=8
    if  on[2]==-2 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]>10 and item[2]==1 and on[4]==2 and on[5]==-1:#体育館　ロッカーあいてむを戻す
        so[4]=1
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9#アイテム戻すとき
            item[2]=0
            ka[10]=1
    if  on[2]==-2 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]>10 and item[2]!=1 and on[4]==2 and on[5]==-1:#体育館　ロッカーあいてむとる
        so[4]=2
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10#アイテム再びとるとき
            if items[2]==0:#セーブストッパー２
                items[0]=0
            if items[2]==1:
                items[0]=1
            item[2]=1
    if  on[2]==0 and kabe6.colliderect(cc) and data[2]==5 and on[4]==2:#体育館から食道前廊下
        on[3]=5#←ストーリーのシーン流すとき
        ii[3]=0
        if siinn2[0]<=1:
             siinn2[0]=2
    if  on[2]==1 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and 6<=data[2] and on[4]==2:
        if data[2]==6:
            ii[3]=3
        if 6<data[2]:
            ii[3]=-1
    if  on[2]==3 and 7==data[2] and  kabe5.colliderect(cc):
        on[3]=6#←ストーリーのシーン流すとき
    if  on[2]==2 and (kabe5.colliderect(cc)or kabe6.colliderect(cc)or kabe7.colliderect(cc)) and on[1]!=9 and i[4]==30 and data[2]==8:#実習棟廊下
        ii[3]=-1
    if  on[2]==1 and kabe6.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==8:#嘘つきの会話
        ii[3]=7
    if  on[2]==1 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==8:#嘘つきのミニゲーム
        ii[3]=2
    if data[2]==9:#3箇所押したらいい
        if  on[2]==5 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30:
            ii[3]=1
        if  on[2]==-6 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30:
            ii[3]=1
        if  on[2]==7 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and on[4]!=3:
            ii[3]=1
        if basyo[0]==1 and basyo[1]==1 and basyo[2]==1 and on[1]!=3:#3箇所押したらいい
            on[3]=7#←ストーリーのシーン流すとき
    if data[2]==10 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==2 and on[2]==8:#図書室
        ii[3]=14
    if data[2]>10 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==2 and item[4]==1 and on[2]==8 and on[5]==-1:#図書室
        so[4]=1
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9#アイテム戻すとき
            item[4]=0
    if data[2]>10 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==2 and item[4]!=1 and on[2]==8 and on[5]==-1:#図書室
        so[4]=2
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[4]==0:#セーブストッパー２
                items[0]=0
            if items[4]==1:
                items[0]=1
            item[4]=1
    if data[2]==11 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==1 and item[5]!=1 and on[2]==8:#昇降口
        on[3]=11
    if data[2]>11 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==1 and item[5]!=1 and on[2]==8 and on[5]==-1:#昇降口
        so[4]=2
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[5]==0:#セーブストッパー２
                items[0]=0
            if items[5]==1:
                items[0]=1
            item[5]=1
    if data[2]>11 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==1 and item[5]==1 and on[2]==8 and on[5]==-1:#昇降口
        so[4]=1
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[5]=0
    if data[2]==12 and kabe5.colliderect(cc)and on[1]!=3 and i[4]==30 and on[4]==1 and on[2]==-6:#デザイン
        ii[3]=33
    if data[2]==13 and (kabe5.colliderect(cc)or kabe4.colliderect(cc)or kabe6.colliderect(cc))and on[1]!=3 and i[4]==30 and on[4]==1 and on[2]==-2 and item[6]==0:#黄色い絵の具
        ii[3]=2
    if data[2]>13 and (kabe5.colliderect(cc)or kabe4.colliderect(cc)or kabe6.colliderect(cc))and on[1]!=3 and i[4]==30 and on[4]==1 and on[2]==-2 and item[6]==1 and on[5]==-1:#黄色い絵の具もどす
        so[4]=1
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[6]=0
    if data[2]>13 and (kabe5.colliderect(cc)or kabe4.colliderect(cc)or kabe6.colliderect(cc))and on[1]!=3 and i[4]==30 and on[4]==1 and on[2]==-2 and item[6]==0 and on[5]==-1:#黄色い絵の具toru
        so[4]=2
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[6]==0:#セーブストッパー２
                items[0]=0
            if items[6]==1:
                items[0]=1
            item[6]=1
    if data[2]==15 and on[1]!=3:#青い絵の具探し始める
        on[3]=12
    if data[2]==16 and kabe3.colliderect(cc)and on[1]!=3 and on[4]==1 and on[2]==0:#青い絵の具
        ii[3]=3
    if data[2]>16 and kabe3.colliderect(cc)and on[1]!=3 and on[4]==1 and on[2]==0 and item[7]==1 and i[4]==30 and on[5]==-1:#青い絵の具
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[7]=0
    if data[2]>16 and kabe3.colliderect(cc)and on[1]!=3 and on[4]==1 and on[2]==-0 and item[7]!=1 and i[4]==30 and on[5]==-1:#青い絵の具
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[7]==0:#セーブストッパー２
                items[0]=0
            if items[7]==1:
                items[0]=1
            item[7]=1
    if data[2]==17 and kabe7.colliderect(cc)and on[1]!=3 and on[4]==1 and on[2]==0 and so[3]==0:#赤い絵の具
        ii[3]=-1
    if on[2]==-1 and  kabe5.colliderect(cc) and on[4]==1 and on[1]!=3:#
        ii[3]=1
        if item[6]==0 and item[7]==1 and item[8]==0:
             ii[3]=4
    if data[2]>17 and kabe7.colliderect(cc)and on[1]!=3 and on[4]==1 and on[2]==0 and item[8]==1 and i[4]==30 and on[5]==-1:#赤い絵の具
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[8]=0
    if data[2]>17 and kabe7.colliderect(cc)and on[1]!=3 and on[4]==1 and on[2]==0 and item[8]!=1 and i[4]==30 and on[5]==-1:#赤い絵の具
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[8]==0:#セーブストッパー２
                items[0]=0
            if items[8]==1:
                items[0]=1
            item[8]=1
    if  on[2]==-6 and kabe5.colliderect(cc) and on[1]!=9 and i[4]==30 and data[2]==19:#デザイン科　
        ii[3]=-1#←ロック画面出させるとき
    if  on[2]==-5 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==20 and on[4]==3:#長い棒　
        ii[3]=2
    if data[2]>20 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==-5 and item[9]==1 and i[4]==30 and on[5]==-1:#長い棒
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[9]=0
    if data[2]>20 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==-5 and item[9]!=1 and i[4]==30 and on[5]==-1:#長い棒
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[9]==0:#セーブストッパー２
                items[0]=0
            if items[9]==1:
                items[0]=1
            item[9]=1
    if  on[2]==1 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==21 and on[4]==3:#懐中電灯
        ii[3]=2
    if data[2]>21 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==1 and item[10]==1 and i[4]==30 and on[5]==-1:#懐中電灯
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[10]=0
    if data[2]>21 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==1 and item[10]!=1 and i[4]==30 and on[5]==-1:#懐中電灯
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[10]==0:#セーブストッパー２
                items[0]=0
            if items[10]==1:
                items[0]=1
            item[10]=1
    if  on[2]==7 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==22 and on[4]==3:#被覆室のカギ
        ii[3]=2
    if data[2]>22 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==7 and item[11]==1 and i[4]==30 and on[5]==-1:#被覆室のカギ
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[11]=0
    if data[2]>22 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==7 and item[11]!=1 and i[4]==30 and on[5]==-1:#被覆室のカギ
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[11]==0:#セーブストッパー２
                items[0]=0
            if items[11]==1:
                items[0]=1
            item[11]=1
    if  on[2]==8 and (kabe5.colliderect(cc) or kabe6.colliderect(cc)) and on[1]!=3 and i[4]==30 and data[2]==23 and on[4]==3:#合成できることを知る
        ii[3]=27
    if  on[2]==-6 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==24 and on[4]==3:#曲がった棒
        ii[3]=2
    if 27>data[2]>24 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==-6 and item[12]==1 and i[4]==30 and on[5]==-1:#曲がった棒
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[12]=0
    if 27>data[2]>24 and kabe5.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==-6 and item[12]!=1 and i[4]==30 and on[5]==-1:#曲がった棒
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[12]==0:#セーブストッパー２
                items[0]=0
            if items[12]==1:
                items[0]=1
            item[12]=1
    if  on[2]==0 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==25 and on[4]==3:#ゴミ箱
        ii[3]=3
    if 27>data[2]>25 and kabe7.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==0 and item[13]==1 and i[4]==30 and on[5]==-1:#ゴミ箱
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[13]=0
    if 27>data[2]>25 and kabe7.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==0 and item[13]!=1 and i[4]==30 and on[5]==-1:#ゴミ箱
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[13]==0:#セーブストッパー２
                items[0]=0
            if items[13]==1:
                items[0]=1
            item[13]=1
    if  on[2]==-2 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==27 and on[4]==3:#縄
        ii[3]=2
    if 28==data[2] and kabe4.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==-2 and item[15]==1 and i[4]==30 and on[5]==-1:#縄
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[15]=0
    if 28==data[2] and kabe4.colliderect(cc)and on[1]!=3 and on[4]==3 and on[2]==-2 and item[15]!=1 and i[4]==30 and on[5]==-1:#縄
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=10
            if items[15]==0:#セーブストッパー２
                items[0]=0
            if items[15]==1:
                items[0]=1
            item[15]=1
    if  on[2]==0 and kabe3.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==29 and on[4]==3:#総合ビジネス科のカギ
        ii[3]=35
    if  on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc)) and on[1]!=3 and i[4]==30 and data[2]==30 and on[4]==4:#総合ビジネスパスワード発見
        ii[3]=3
    if  on[2]==8 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==31 and on[4]==4:#総合ビジネスGAME
        ii[3]=1       
    if  on[2]==8 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and 34>=data[2]>=32 and on[4]==4  and on[1]!=14 and (on[1]==0 or 3<on[1]<8) and keyboard.d:#総合ビジネスGAME
            on[1]=15
            if sgyara[6]<=2:
                sgyara[6]=2
            if not game2.sukoa >= 50:
                game2.sukoa = 0 #左上に表示されるスコアの値の変数
                game2.damtime= 0#ダメージ受けている間か、間じゃないか確認するやつ
                game2.dd = []#敵がランダムに出てくれるようにここから敵画像ここから引っ張って来る
                game2.gg = []#玉出すための入れ物
                game2.g=0 #g=60で割って1秒間に１回球が出てくれるようにしてくれる
                game2.kenn = Actor('無題617_20230824200038',topleft=(0,0))#kenn=プレイヤー
                game2.daiya2 = Actor('無題617_20230824200119',topleft=(0,0))#kenn=プレイヤー
                game2.dame = 6#←HP変数をdameにしHPを１０に
                game2.q=0
                game2.hai = Actor('botann.png',topleft=(1000,-500))#背景
                game2.a=0#ダメージで揺れる
                game2.b=0#ダメージで揺れるときの動き
                game2.c=1#スピード上げるための変数
                game2.d=1#
                game2.t=60#　T÷60の秒数ごとに敵が出現
                game2.mini=Actor('minigame2',topleft=(0,-150))
    if  on[2]==8 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==33 and on[4]==4 and (on[1]==0 or 3<on[1]<8):#総合ビジネスGAME
            on[3]=15
    if  on[2]==8 and kabe7.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]==35 and on[4]==4 and (on[1]==0 or 3<on[1]<8):#総合ビジネスGAME
            ii[3]=3
    if 35<data[2] and kabe7.colliderect(cc)and on[1]!=3 and on[4]==4 and on[2]==8 and item[18]==1 and i[4]==30 and on[5]==-1:#紫のカギ
         so[4]=1
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8) :#アイテム
            on[3]=9
            item[18]=0
    if 35<data[2] and kabe7.colliderect(cc)and on[1]!=3 and on[4]==4 and on[2]==8 and item[18]!=1 and i[4]==30 and on[5]==-1:#紫のカギ
         so[4]=2
         if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8):#アイテム
            on[3]=10
            if items[18]==0:#セーブストッパー２
                items[0]=0
            if items[18]==1:
                items[0]=1
            item[18]=1
    if  on[2]==4 and on[1]!=3 and so[3]==0 and data[2]==36 and on[4]==4 and (on[1]==0 or 3<on[1]<8):#紫のカギで新マップ
            on[5]=-1
            music[0]=0
            on[3]=17
            data[2]+=1
    if  on[2]==1 and on[1]!=3 and data[2]==38 and on[4]==4 and (on[1]==0 or 3<on[1]<8)and kabe5.colliderect(cc):#紫のカギで新マップ
        ii[3]=1
    if  on[2]==1 and on[1]!=3 and data[2]==39 and on[4]==4 and (on[1]==0 or 3<on[1]<8)and kabe5.colliderect(cc) and i[4]==30 and keyboard.d:#紫のカギで新マップ
         game3.c = Actor('a5(1).png',center=(350,170))#kenn=プレイヤー
         game3.map = Actor('minigame3.png',topleft=(0,-200))#kenn=プレイヤー
         game3.m = Actor('minigame2',topleft=(0,-150))#kenn=プレイヤー
         game3.i=[0,0]
         if sgyara[6]<=3:
            sgyara[6]=3
         on[1]=16
    #if  on[2]==-6 and on[4]==2 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]>10:#物理室
        #ii[3]=1
    #if  on[2]==-5 and on[4]==3 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30 and data[2]>10:#科学室
        #ii[3]=1
    #if  on[2]==-5 and on[4]==2 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30 and item[4]!=1 and item[5]!=1 and item[6]!=1 and data[2]>10:#職委員室
        #ii[3]=1
    #if  on[2]==-5 and on[4]==2 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30 and (item[4]==1 or item[5]==1 or item[6]==1) and data[2]>10:#職委員室アイテム戻す
        #if keyboard.d:#アイテム戻すとき
            #on[3]=9#アイテム戻すとき
            #item[4]=0
            #item[5]=0
           # item[6]=0
    if  on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc)) and on[1]!=3 and i[4]==30 and data[2]>=31 and on[4]==4:
        ii[3]=-1
    if ka[8]==1 and ka[9]==1 and ka[7]==3 and on[1]==1:#アイテム合成出来たら
                    on[3]=8
    if  on[2]==0 and kabe3.colliderect(cc) and on[1]!=3 and i[4]==30 and 40>data[2]>=38 and on[4]==4:
        ii[3]=-1
    if  on[2]==0 and kabe9.colliderect(cc) and on[1]!=3 and i[4]==30 and 41==data[2] and on[4]==4:#地図にない
        ii[3]=5
    if  on[2]==999 and kabe4.colliderect(cc) and on[1]!=3 and i[4]==30 and 42==data[2] and on[4]==4:#地図にない
        on[3]=19
    if  on[2]==999 and kabe5.colliderect(cc) and on[1]!=3 and i[4]==30 and 43==data[2] and on[4]==4:#地図にない#脱出イベント
        if keyboard.d and on[3]==0 and (on[1]==0 or 3<on[1]<8):
            on[3]=20
#暗号ロック・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
    if ii[17]==3 and ii[18]==4 and ii[19]==1 and ii[20]==5 and ii[21]==5 and i[4]==30 and data[2]<4:#暗号がそろったとき（青い本の奴）
        data[2]=4
        on[1]=0
        on[3]=4#ストーリーシーン
        ii[3]=0#←暗号解除した際はこれつける
    if ii[17]==4 and ii[18]==5 and ii[19]==6 and ii[20]==8 and ii[21]==9 and i[4]==30 and data[2]==8:
        ii[3]=22
    if data[2]==17 and kabe7.colliderect(cc)and so[3]==0 and on[4]==1 and on[2]==0 and ka[2]=="NIIZASOUGOUGIZYUTUNSG" and i[4]==30:#赤い絵の具SADHBVPLMOPISHGBWSAQW"
        on[3]=13
        ii[3]=0
        data[2]+=1
        ka[2]=""
        ka[4]=0#パスワードリセット
    if ii[17]==1 and ii[18]==1 and ii[19]==4 and ii[20]==5 and ii[21]==6 and i[4]==30 and data[2]==19:#暗号がそろったときデザイン
        on[1]=0
        on[3]=14#ストーリーシーン
        ii[3]=0#←暗号解除した際はこれつける
    if data[2]==34 and (kabe5.colliderect(cc)or kabe6.colliderect(cc)) and so[3]==0 and on[4]==4 and on[2]==8 and ka[2]=="NIIZASOUGOUBIZINESUKA" and i[4]==30:#赤い絵の具SADHBVPLMOPISHGBWSAQW"
        on[3]=16
        ii[3]=0
        ka[2]=""
        ka[4]=0#パスワードリセット
    if 40>data[2]>=38 and kabe3.colliderect(cc) and on[4]==4 and on[2]==0 and ka[2]=="MINIGAMEKURIAKABEYOKE" and i[4]==30:#MINIGAMEKABEYOKEKURIA
        on[3]=18
        data[2]=40
        ka[2]=""
        ka[4]=0#パスワードリセット
    #マップ内の物check・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
    if on[1]!=10 and on[5]==-1 and not 44<=data[2]<=54:
        if keyboard.s and on[1]==18 and i[4]==30:
            on[1]=1
            i[4]=0
            so[0]=1
            iii[3]=0
        if keyboard.e and (on[1]==0 or 3<on[1]<8) and i[4]==30 and not data[2]==4:#ヒント
            on[1]=17
            i[4]=0	                          
            so[0]=1
        if keyboard.e and on[1]==17 and i[4]==30:#ヒント
            on[1]=0
            i[4]=0	                          
            so[0]=1
        if keyboard.a and (on[1]==0 or 3<on[1]<8) and i[4]==30 and item[3]==1 and not data[2]==4:#on[0]でボタンの種類┤
            on[1]=12	                            #	                │      
            i[4]=0	                            # ─────────┘
            so[0]=5
        if keyboard.a and on[1]==12 and i[4]==30:#on[0]でボタンの種類┤
            on[1]=0	                            #	                │      
            i[4]=0	                            # ─────────┘
            so[0]=5
        if keyboard.w and (on[1]==0 or 3<on[1]<8) and i[4]==30 and not data[2]==4:#on[0]でボタンの種類┤
            on[1]=11	                            #	                │      
            i[4]=0	                            # ─────────┘
            so[0]=2
        if keyboard.w and on[1]==11 and i[4]==30 and on[2]!=500:#on[0]でボタンの種類┤
            on[1]=0	                            #	                │      
            i[4]=0	                            # ─────────┘
            so[0]=2
        if keyboard.s and (on[1]==0 or 3<on[1]<8) and i[4]==30 and not data[2]==4:#on[0]でボタンの種類┐
            on[1]=1	                            #                   │
            i[4]=0	                            #                   │
            so[0]=5	                            #                   │←#item欄ボタン(S)
        if keyboard.s and on[1]==1 and i[4]==30:#on[0]でボタンの種類┤
            on[1]=0	                            #	                │      
            i[4]=0	                            # ─────────┘
            so[0]=5
            gousei[8]=0
            gousei[9]=0
            gousei[10]=0
            gousei[11]=0
            gousei[12]=0
            i[4]=0
            ka[7]=0
        if keyboard.q and on[1]==3 and ii[9]==1 and ii[2]==3 and ii[3]==1:
            on[1]=2	                            #                   │
            i[4]=0	                            #                   │←#save欄ボタン(A)&Q
        if keyboard.a and i[4]==30 and (on[1]==2 and ii[9]==1 or on[1]==9):
            ii[9]=0	                            #on[0]でボタンの種類│
            on[1]=0	                            #	                │      
            i[4]=0	                            #                   │
            ii[1]=0                             #                   │
            ii[2]=0                             #                   │
            ii[3]=0                             # ─────────┘
            ii[24]=0
            u[0]=0
            if ii[15]>=1:#ストーリーを進める
                data[2]+=1#ストーリーを1進める
                if ii[15]==2:#ロック画面を読み終わりと同時に表示
                    on[1]=9
                ii[15]=0
            if on[3]!=0:#流しているテキストがシーンの奴だった時
                    so[2]+=1
    if keyboard.d and (on[1]==0 or 3<on[1]<8) and i[4]==30 and ii[3]!=0 and not data[2]==15:#───┐
        on[1]=3                                          #      │
        if ii[3]<0:#←もし表示するのが暗号ロック画面の時は　　　│
            on[1]=9	                    #                   │
            ii[3]=0
        i[4]=0	                            #                   │←#checkボタン（D）
        #ii[9]=0#セーブバグ削除　※アイテムは一番最後の段落でゲットさせるように
    if (keyboard.d or (ka[10]!=0 and ka[11]==0)) and on[1]==3 and i[4]==40 and ii[2]==3:
        ii[1]=0	                            #ii[2]↑読み終わるまで	                 
        ii[2]=0                             # ─────────┘
        ii[3]-=1#段落一つ減らす
        ii[0]=0
        ka[11]=1
        so[5]=0#文章スキップストッパー
        so[6]=0#アイテムを再び手に入れる場面でのセーブストッパー
        if  ii[3]==0  and ii[12]>5 and ka[12]==0:#アイテムがいっぱい
                ii[3]+=1
        if ii[3]==0 and (ii[12]<=5 or ka[12]==1 and ii[12]>5):#段落が最終段落だった時
            i[4]=0
            on[1]=0
            ii[9]=0
            ii[24]=0
            ka[11]=0
            ka[10]=0
            if  ii[12]>5:#アイテムがいっぱい
                ii[12]=5
                ka[12]=0
                if on[2]==0 and on[4]==2 and kabe7.colliderect(cc):#どの場面でどのアイテム取れなくするか
                    item[1]=0
                if on[2]==-1 and on[4]==2:#どの場面でどのアイテム取れなくするか
                    item[2]=0
                if on[2]==8 and on[4]==2 and kabe5.colliderect(cc):#どの場面でどのアイテム取れなくするか
                    item[4]=0
                if on[2]==8 and on[4]==1 and kabe5.colliderect(cc):#どの場面でどのアイテム取れなくするか
                    item[5]=0
                if on[2]==-2 and on[4]==1 and (kabe5.colliderect(cc)or kabe4.colliderect(cc)or kabe6.colliderect(cc)):
                    item[6]=0
                if on[2]==0 and on[4]==1 and kabe3.colliderect(cc):
                    item[7]=0
                if on[2]==0 and on[4]==1 and kabe7.colliderect(cc):
                    item[8]=0
                if on[2]==-5 and on[4]==3 and kabe5.colliderect(cc):
                    item[9]=0
                if on[2]==1 and on[4]==3 and kabe5.colliderect(cc):
                    item[10]=0
                if on[2]==7 and on[4]==3 and kabe5.colliderect(cc):
                    item[11]=0
                if on[2]==-6 and on[4]==3 and kabe5.colliderect(cc):
                    item[12]=0
                if on[2]==0 and on[4]==3 and kabe7.colliderect(cc):
                    item[13]=0
                if on[2]==-2 and on[4]==3 and kabe4.colliderect(cc):
                    item[15]=0
                if on[2]==8 and on[4]==4 and kabe7.colliderect(cc):
                    item[18]=0
            if ii[15]>=1:#ストーリーを進める
                data[2]+=1#ストーリーを1進める
                if ii[15]==2:#ロック画面を読み終わりと同時に表示
                    on[1]=9
                ii[15]=0
            if on[3]!=0:#流しているテキストがシーンの奴だった時
                so[2]+=1
    if keyboard.space and on[1]==3 and i[4]==40 and ii[2]!=3 and so[5]==0:#会話スキップ
        ii[1]=0
        ii[2]=0
        ii[3]=0
        i[4]=0
        ii[9]=0
        on[1]=0
        ii[24]=0
        ka[11]=0
        ka[10]=0
        if serihu[0]==1:
            serihu[0]=0
            if on[2]==8 and on[4]==2:
                on[2]=-6
                on[4]=1
            if on[2]==-2 and on[4]==1:
                on[2]=8
                on[4]=3
            if on[2]==8 and on[4]==3:
                on[2]=4
                on[4]=4
            if on[2]==-2 and on[4]==2:
                on[2]=0
                on[4]=3
        if  ii[12]>5:#アイテムがいっぱい
                ii[12]=5
                ka[12]=0
                if on[2]==0 and on[4]==2 and kabe7.colliderect(cc):#どの場面でどのアイテム取れなくするか
                    item[1]=0
                if on[2]==-1 and on[4]==2:#どの場面でどのアイテム取れなくするか
                    item[2]=0
                if on[2]==8 and on[4]==2 and kabe5.colliderect(cc):#どの場面でどのアイテム取れなくするか
                    item[4]=0
                if on[2]==8 and on[4]==1 and kabe5.colliderect(cc):#どの場面でどのアイテム取れなくするか
                    item[5]=0
                if on[2]==-2 and on[4]==1 and (kabe5.colliderect(cc)or kabe4.colliderect(cc)or kabe6.colliderect(cc)):
                    item[6]=0
                if on[2]==0 and on[4]==1 and kabe3.colliderect(cc):
                    item[7]=0
                if on[2]==0 and on[4]==1 and kabe7.colliderect(cc):
                    item[8]=0
                if on[2]==-5 and on[4]==3 and kabe5.colliderect(cc):
                    item[9]=0
                if on[2]==1 and on[4]==3 and kabe5.colliderect(cc):
                    item[10]=0
                if on[2]==7 and on[4]==3 and kabe5.colliderect(cc):
                    item[11]=0
                if on[2]==-6 and on[4]==3 and kabe5.colliderect(cc):
                    item[12]=0
                if on[2]==0 and on[4]==3 and kabe7.colliderect(cc):
                    item[13]=0
                if on[2]==-2 and on[4]==3 and kabe4.colliderect(cc):
                    item[15]=0
                if on[2]==8 and on[4]==4 and kabe7.colliderect(cc):
                    item[18]=0
        if ii[15]>=1:#ストーリーを進める
                data[2]+=1#ストーリーを1進める
                if ii[15]==2:#ロック画面を読み終わりと同時に表示
                    on[1]=9
                ii[15]=0
        if on[3]!=0:#流しているテキストがシーンの奴だった時
                so[2]+=1
        if music[0]==3 and on[2]==-2 and data[2]<8:
            music[0]=2
    if on[1]!=10 and on[1]!=1 and on[1]!=11 and on[1]!=2 and on[1]!=9 and on[1]!=12 and on[1]!=13 and on[1]!=14 and on[1]!=15 and on[1]!=16 and on[1]!=17 and on[1]!=18 and on[1]!=19:
        if keyboard.up and i[4]>10 and on[1]!=3 and on[2]!=999:  #on[0]でボタンの種類　#上移動ボタン  on[1]!=9で暗号ロック中じゃないとき#999で２Dスクロールの時は上移動できない
            on[1]=4
            i[4]=0
        if keyboard.down and i[4]>10 and on[1]!=3 and on[2]!=999:#on[0]でボタンの種類　#下移動ボタン
            on[1]=5
            i[4]=0
        if keyboard.left and i[4]>10 and on[1]!=3:#on[0]でボタンの種類　#左移動ボタン
            on[1]=6
            i[4]=0
        if keyboard.right and i[4]>10 and on[1]!=3:#on[0]でボタンの種類 #右移動ボタン
            on[1]=7
            i[4]=0 
    #if keyboard.w and on[1]!=3:#on[0]でボタンの種類 シーン
     #   on[3]=1#何のシーンか

    if serihu[1]==0 and keyboard.a and on[0]==6 and serihu[2]==50 and  sgyara[6]>=1:
                    on[0]=0
                    serihu[1]=1
                    ii[1]=0
                    ii[2]=0
                    ii[3]=0
                    i[4]=0
                    ii[9]=0
                    on[1]=0
                    ii[24]=0
                    ka[11]=0
                    ka[10]=0
                    on[1]=14
                    game.i=0
                    game.h=[Actor('a3(1)',center=(350,150)),Actor('a33(1)',center=(350,150)),Actor('a3(1)',center=(350,150)),Actor('a333(1)',center=(350,150))]
                    game.r=[Actor('a4(1)',center=(350,150)),Actor('a44(1)',center=(350,150)),Actor('a4(1)',center=(350,150)),Actor('a444(1)',center=(350,150))]
                    game.a5=Actor('a5(1)',center=(350,150))
                    game.heya=[Actor('heya1',topleft=(0,-150)),Actor('heya2',topleft=(320,-150)),Actor('heya3',topright=(380,-150))
                               ,Actor('heya4',topleft=(320,-150)),Actor('heya5',topright=(380,-150)),Actor('heya6',topleft=(320,-150))]
                    game.doa=[Actor('kabe2'),Actor('kabe2'),0]#いき０戻り１アドレス2
                    game.w=0
                    game.ww=0
                    game.time=[1,104,300]
                    game.takara=["ない","ない","ない","ない",4]
                    game.back=[Actor('game',topleft=(0,-150)),Actor('sikai',center=(450,365-100))]
                    game.reba=[Actor('botann'),Actor('botann'),0,0,0,0,Actor('takara')]
    if serihu[2]<50 and on[0]>0:
        serihu[2]+=1
        if serihu[2]==50:
            serihu[3]=0
    if serihu[1]==0 and keyboard.s and on[0]==6 and  sgyara[6]>=2:
                on[0]=0
                on[1]=15
                serihu[1]=1
                game2.sukoa = 0 #左上に表示されるスコアの値の変数
                game2.damtime= 0#ダメージ受けている間か、間じゃないか確認するやつ
                game2.dd = []#敵がランダムに出てくれるようにここから敵画像ここから引っ張って来る
                game2.gg = []#玉出すための入れ物
                game2.g=0 #g=60で割って1秒間に１回球が出てくれるようにしてくれる
                game2.kenn = Actor('無題617_20230824200038',topleft=(0,0))#kenn=プレイヤー
                game2.daiya2 = Actor('無題617_20230824200119',topleft=(0,0))#kenn=プレイヤー
                game2.dame = 6#←HP変数をdameにしHPを１０に
                game2.q=0
                game2.hai = Actor('botann.png',topleft=(1000,-500))#背景
                game2.a=0#ダメージで揺れる
                game2.b=0#ダメージで揺れるときの動き
                game2.c=1#スピード上げるための変数
                game2.d=1#
                game2.t=60#　T÷60の秒数ごとに敵が出現
                game2.mini=Actor('minigame2',topleft=(0,-150))
    if serihu[1]==0 and keyboard.d and on[0]==6  and  sgyara[6]>=3:
         game3.c = Actor('a5(1).png',center=(350,170))#kenn=プレイヤー
         game3.map = Actor('minigame3.png',topleft=(0,-200))#kenn=プレイヤー
         game3.m = Actor('minigame2',topleft=(0,-150))#kenn=プレイヤー
         game3.i=[0,0]
         on[0]=0
         serihu[1]=1
         on[1]=16

        
#効果音↓
    if so[0]!=0:
        if so[0]==1:
            sounds.koukaonn1.play()
        if so[0]==2:
            sounds.koukaonn7.play()
        if so[0]==3:
            sounds.bikkuri.play()
        if so[0]==4:
            sounds.ga.play()
        if so[0]==5:
            sounds.temoti.play()
        if so[0]==6:
            sounds.koukaonn4.play()
        if so[0]==7:
            sounds.over.play()
        if so[0]==8:
            sounds.koukaonn7.play()
            sounds.bikkuri.play()
        so[0]=0
#効果音↑
     
#BGM・・・・・・・・・・・・・・・・・・・・
    if music[0]!=0:#BGM流しているとき#起動させるときは、種類[0]指定する
        if music[2]==0:
            if music[0]==1:#[0]でBGMの種類[1]で流す秒数[2]ストッパー
                winsound.PlaySound('home.wav',winsound.SND_ASYNC)
                music[1]=45+(60*70)#70秒間再生
            if music[0]==2:
                music[1]=45+(60*70)#70秒間再生
                winsound.PlaySound('map1.wav',winsound.SND_ASYNC)
            if music[0]==3:
                winsound.PlaySound('owareru.wav',winsound.SND_ASYNC)
                music[1]=70+(60*17)#17秒間再生
            if music[0]==4:
                winsound.PlaySound('bgm2.wav',winsound.SND_ASYNC)
                music[1]=70+(60*70)#秒間再生
            if music[0]==5:
                winsound.PlaySound('bgm1.wav',winsound.SND_ASYNC)
                music[1]=70+(60*70)#秒間再生
            if music[0]==6:
                winsound.PlaySound('bgm3.wav',winsound.SND_ASYNC)
                music[1]=70+(60*70)#秒間再生
            if music[0]==7:
                winsound.PlaySound('bgm4.wav',winsound.SND_ASYNC)
                music[1]=70+(60*104)#秒間再生
            if music[0]==8:
                winsound.PlaySound('bgm6.wav',winsound.SND_ASYNC)
                music[1]=70+(60*70)#秒間再生
            if music[0]==9:
                winsound.PlaySound('bgm5.wav',winsound.SND_ASYNC)
                music[1]=70+(60*70)#秒間再生
            if music[0]==10:
                winsound.PlaySound('bgm7.wav',winsound.SND_ASYNC)
                music[1]=70+(60*79)#秒間再生
            if music[0]==11:
                winsound.PlaySound('bgm8.wav',winsound.SND_ASYNC)
                music[1]=70+(60*89)#秒間再生
            if music[0]==12:
                winsound.PlaySound('bgm9.wav',winsound.SND_ASYNC)
                music[1]=70+(60*71)#秒間再生
            if music[0]==13:
                winsound.PlaySound('bgm10.wav',winsound.SND_ASYNC)
                music[1]=70+(60*53)#秒間再生
            music[2]=1
        if music[1]==1:#ストッパー解除
            music[2]=0
        if music[1]>0:#カウント
            music[1]-=1
    if music[0]!=music[3]:#もし途中でBGMが変わったら
        music[3]=music[0]#BGM更新
        music[1]=0#カウントリセット
        music[2]=0#ストッパーリセット
        winsound.PlaySound('S.wav',winsound.SND_ASYNC)
    game.update()
    if ka[7]==3:
                gousei[8]=0
                gousei[9]=0
                gousei[10]=0
                gousei[11]=0
                gousei[12]=0
                ka[8]=0
                ka[9]=0
                if i[4]==30:
                    ka[7]=0
def on_mouse_move(pos):
    osita.topleft=(1000,1000)
    if on[0]==1 and tuduki.collidepoint(pos):#続きから始める
        osita.topleft=tuduki.topleft
    if on[0]==1 and setumei.collidepoint(pos):#操作説明表示
        osita.topleft=setumei.topleft
    if on[0]==1 and gyarari.collidepoint(pos):#操作説明表示
        osita.topleft=gyarari.topleft
    if on[0]==1 and start.collidepoint(pos):#操作説明表示
        osita.topleft=start.topleft
def on_mouse_down(pos):
#  keys.
#def on_key_down(key,mod,unicode)
 #   str+=unicode
    #どこにセーブするか・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
    if on[1]==2 or on[0]==2:#セーブ
        if qq1.collidepoint(pos) and ((on[0]==0 and i[4]==30)or on[0]==2):
            if on[1]==2:#ゲーム中にセーブするときは
                 i[7]=25
                 i[8]=1
                 i[4]=0
            if on[0]==2 and int(save1[2])>=1:
                  ii[4]=int(save1[1])#動くのは　map or キャラクター
                  on[2]=int(save1[3])#マップの種類
                  data[2]=int(save1[2])#進み具合
                  music[0]=int(save1[4])#BGM
                  m1.x=float(save1[5])#mapのx
                  m1.y=float(save1[6])#mapのy
                  c.x=float(save1[7])#プレイヤーのx
                  c.y=float(save1[8])#プレイヤーのy
                  ii[31]=int(save1[0])#プレイ時間
                  on[4]=int(save11[1])
                  i[7]=25
                  i[8]=1
#i[13]=5#何秒間ならないようにするか←多分このコメントいらない？
        if qq2.collidepoint(pos) and ((on[0]==0 and i[4]==30)or on[0]==2):
            if on[1]==2:#ゲーム中にセーブするときは
                 i[7]=25
                 i[8]=2
                 i[4]=0
            if on[0]==2 and int(save2[2])>=1:
                  ii[4]=int(save2[1])#動くのは　map or キャラクター
                  on[2]=int(save2[3])#マップの種類
                  data[2]=int(save2[2])#進み具合
                  music[0]=int(save2[4])#BGM
                  m1.x=float(save2[5])#mapのx
                  m1.y=float(save2[6])#mapのy
                  c.x=float(save2[7])#プレイヤーのx
                  c.y=float(save2[8])#プレイヤーのy
                  ii[31]=int(save2[0])#プレイ時間
                  on[4]=int(save22[1])
                  i[7]=25
                  i[8]=2
        if qq3.collidepoint(pos) and ((on[0]==0 and i[4]==30)or on[0]==2):
            if on[1]==2:#ゲーム中にセーブするときは
                 i[7]=25
                 i[8]=3
                 i[4]=0
            if on[0]==2 and int(save3[2])>=1:
                  ii[4]=int(save3[1])#動くのは　map or キャラクター
                  on[2]=int(save3[3])#マップの種類
                  data[2]=int(save3[2])#進み具合
                  music[0]=int(save3[4])#BGM
                  m1.x=float(save3[5])#mapのx
                  m1.y=float(save3[6])#mapのy
                  c.x=float(save3[7])#プレイヤーのx
                  c.y=float(save3[8])#プレイヤーのy
                  ii[31]=int(save3[0])#プレイ時間
                  on[4]=int(save33[1])
                  i[7]=25
                  i[8]=3
        if qq4.collidepoint(pos) and ((on[0]==0 and i[4]==30)or on[0]==2):
            if on[1]==2:#ゲーム中にセーブするときは
                 i[7]=25
                 i[8]=4
                 i[4]=0
            if on[0]==2 and int(save4[2])>=1:
                  ii[4]=int(save4[1])#動くのは　map or キャラクター
                  on[2]=int(save4[3])#マップの種類
                  data[2]=int(save4[2])#進み具合
                  music[0]=int(save4[4])#BGM
                  m1.x=float(save4[5])#mapのx
                  m1.y=float(save4[6])#mapのy
                  c.x=float(save4[7])#プレイヤーのx
                  c.y=float(save4[8])#プレイヤーのy
                  ii[31]=int(save4[0])#プレイ時間
                  on[4]=int(save44[1])
                  i[7]=25
                  i[8]=4
        so[0]=1
    if on[1]==9:#ロック・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        if on[2]==-1 or on[2]==2 or on[2]==-6:
            if R.collidepoint(pos)and i[4]==30:
                ii[16]=0
                i[4]=0
                ii[17]+=1
                so[0]=4
                if on[2]==2 and not kabe5.colliderect(cc):#違うパネルの時は
                    ii[17]-=1
                    so[0]=0
                if ii[17]==10:
                    ii[17]=0
            if R1.collidepoint(pos)and i[4]==30:
                ii[16]=116
                i[4]=0
                ii[18]+=1
                so[0]=4
                if on[2]==2 and not kabe5.colliderect(cc):#違うパネルの時は
                    ii[18]-=1
                    so[0]=0
                if ii[18]==10:
                    ii[18]=0
            if R2.collidepoint(pos)and i[4]==30:
                ii[16]=232
                i[4]=0
                ii[19]+=1
                so[0]=4
                if on[2]==2 and not kabe6.colliderect(cc):#違うパネルの時は
                    ii[19]-=1
                    so[0]=0
                if ii[19]==10:
                    ii[19]=0
            if R3.collidepoint(pos)and i[4]==30:
                ii[16]=348
                i[4]=0
                ii[20]+=1
                so[0]=4
                if on[2]==2 and not kabe6.colliderect(cc):#違うパネルの時は
                    ii[20]-=1
                    so[0]=0
                if ii[20]==10:
                    ii[20]=0
            if R4.collidepoint(pos)and i[4]==30:
                ii[16]=464
                i[4]=0
                ii[21]+=1
                so[0]=4
                if on[2]==2 and not kabe7.colliderect(cc):#違うパネルの時は
                    ii[21]-=1
                    so[0]=0
                if ii[21]==10:
                    ii[21]=0
    if on[1]==1 and data[2]>10 and not(on[4]==3 and on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc))and data[2]>=24):
        if i[4]==30 and(hirou[1].collidepoint(pos)or hirou[2].collidepoint(pos)or hirou[3].collidepoint(pos)or hirou[4].collidepoint(pos)or hirou[5].collidepoint(pos)or hirou[6].collidepoint(pos)or hirou[7].collidepoint(pos)or hirou[8].collidepoint(pos)or hirou[9].collidepoint(pos)or hirou[10].collidepoint(pos)or hirou[11].collidepoint(pos)or hirou[12].collidepoint(pos)or hirou[13].collidepoint(pos)or hirou[14].collidepoint(pos)or hirou[15].collidepoint(pos)or hirou[16].collidepoint(pos)or hirou[17].collidepoint(pos)or hirou[18].collidepoint(pos)or hirou[19].collidepoint(pos)or hirou[20].collidepoint(pos)):
            on[1]=18
            i[4]=0
            so[0]=1
            if hirou[1].collidepoint(pos):
                iii[3]=1
            if hirou[2].collidepoint(pos):
                iii[3]=2
            if hirou[3].collidepoint(pos):
                iii[3]=3
            if hirou[4].collidepoint(pos):
                iii[3]=4
            if hirou[5].collidepoint(pos):
                iii[3]=5
            if hirou[6].collidepoint(pos):
                iii[3]=6
            if hirou[7].collidepoint(pos):
                iii[3]=7
            if hirou[8].collidepoint(pos):
                iii[3]=8
            if hirou[9].collidepoint(pos):
                iii[3]=9
            if hirou[10].collidepoint(pos):
                iii[3]=10
            if hirou[11].collidepoint(pos):
                iii[3]=11
            if hirou[12].collidepoint(pos):
                iii[3]=12
            if hirou[13].collidepoint(pos):
                iii[3]=13
            if hirou[14].collidepoint(pos):
                iii[3]=14
            if hirou[15].collidepoint(pos):
                iii[3]=15
            if hirou[16].collidepoint(pos):
                iii[3]=16
            if hirou[17].collidepoint(pos):
                iii[3]=17
            if hirou[18].collidepoint(pos):
                iii[3]=18
            if hirou[19].collidepoint(pos):
                iii[3]=19
            if hirou[20].collidepoint(pos):
                iii[3]=20
    if on[1]==1 and on[4]==3 and on[2]==8 and (kabe5.colliderect(cc)or kabe6.colliderect(cc)):#アイテム欄・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        if  ka[7]<2:
            if gousei[0].collidepoint(pos)and i[4]==30 and gousei[8]!=1:
                gousei[8]=1
                so[0]=6
                i[4]=0
                if ka[7]==0:
                    gousei[5].center=(550,z[2]*66+20)
                if ka[7]==1:
                    gousei[6].center=(550,z[2]*66+20)
                ka[7]+=1
            if gousei[1].collidepoint(pos)and i[4]==30 and gousei[9]!=1:
                 gousei[9]=1
                 so[0]=6
                 i[4]=0
                 if ka[7]==0:
                    gousei[5].center=(550,z[3]*66+20)
                 if ka[7]==1:
                    gousei[6].center=(550,z[3]*66+20)
                 ka[7]+=1
            if gousei[2].collidepoint(pos)and i[4]==30 and gousei[10]!=1:
                 gousei[10]=1
                 so[0]=6
                 i[4]=0
                 if ka[7]==0:
                    gousei[5].center=(550,z[11]*66+20)
                 if ka[7]==1:
                    gousei[6].center=(550,z[11]*66+20)
                 ka[7]+=1
            if gousei[3].collidepoint(pos)and i[4]==30 and gousei[11]!=1:
                 gousei[11]=1
                 so[0]=6
                 i[4]=0
                 if ka[7]==0:
                     if item[12]==1:
                        gousei[5].center=(550,z[12]*66+20)
                     if item[14]==1:
                        gousei[5].center=(550,z[14]*66+20)
                 if ka[7]==1:
                     if item[12]==1:
                        gousei[6].center=(550,z[12]*66+20)
                     if item[14]==1:
                        gousei[6].center=(550,z[14]*66+20)
                 ka[7]+=1
            if gousei[4].collidepoint(pos)and i[4]==30 and gousei[12]!=1:
                 gousei[12]=1
                 so[0]=6
                 i[4]=0
                 if ka[7]==0:
                     if item[13]==1:
                        gousei[5].center=(550,z[13]*66+20)
                     if item[15]==1:
                        gousei[5].center=(550,z[15]*66+20)
                 if ka[7]==1:
                     if item[13]==1:
                        gousei[6].center=(550,z[13]*66+20)
                     if item[15]==1:
                        gousei[6].center=(550,z[15]*66+20)
                 ka[7]+=1
        if gousei[7].collidepoint(pos)and i[4]==30 and ka[7]==2:
                ka[7]=3
                so[0]=6
                i[4]=0
    if on[1]==3 and on[4]==2 and on[2]==-5:
        if kagi[1].collidepoint(pos) and ka[10]==0:
            ka[10]=1
            ii[3]+=1
            so[0]=1
        if  kagi[2].collidepoint(pos) and ka[10]==0:
            ii[3]+=1
            ka[10]=2
            so[0]=1
        if  kagi[3].collidepoint(pos) and ka[10]==0:
            ii[3]+=1
            ka[10]=3
            so[0]=1
    if on[1]==13:#パスワード・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        if pc1.collidepoint(pos):
            on[1]=0
            i[4]=0
            so[0]=1
            ka[6]=0
            ka[2]=""
            ka[4]=0#パスワードリセット
        if pc2.collidepoint(pos):
            ka[2]=""
            i[4]=0
            so[0]=1
            ka[4]=0#パスワードリセット
#ホーム画面ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    if on[0]==1 and start.collidepoint(pos):#game開始するときは以下の9個を指定すればいい
        so[0]=6#押したときの効果音
        on[0]=0#←スタート画面モード（on[0]>0）の状態を解除
        on[3]=2#←ストーリーのシーン流すとき
        music[0]=5#再生BGMの種類
        data[2]=0#進み具合指定
        m1.topleft=(0,0)#プレイヤーの初期位置
        on[2]=0#マップの種類
        ii[4]=0#プレイヤー動かす状態（1）かマップ動かす状態（0）か？
        on[4]=2
        if siinn2[0]==0:
             siinn2[0]=1
        item[1]=0
        item[2]=0
        item[3]=0
        item[4]=0
        item[5]=0
        item[6]=0
        item[7]=0
        item[8]=0
        item[9]=0
        item[10]=0
        item[11]=0
        item[12]=0
        item[13]=0
        item[14]=0
        item[15]=0
        item[16]=0
        item[17]=0
        item[18]=0
        item[19]=0
        item[20]=0
        item[21]=0
        item[22]=0
        item[23]=0
        items[1]=0#
        items[2]=0
        items[3]=0
        items[4]=0
        items[5]=0
        items[6]=0
        items[7]=0
        items[8]=0
        items[9]=0
        items[10]=0
        items[11]=0
        items[12]=0
        items[13]=0
        items[14]=0
        items[15]=0
        items[16]=0
        items[17]=0
        items[18]=0
        items[19]=0
        items[20]=0
        items[21]=0
        items[22]=0
        items[23]=0
    if on[0]==3 and tyuuto[0].collidepoint(pos):#チュートリアル
        so[0]=6#押したときの効果音
        on[0]=0#←スタート画面モード（on[0]>0）の状態を解除
        music[0]=2#再生BGMの種類
        iii[4]=0
        iii[5]=0
        iii[6]=0
        iii[7]=0
        data[2]=-100#進み具合指定
        ii[4]=1#プレイヤー動かす状態（1）かマップ動かす状態（0）か？
        item[1]=0
        item[2]=0
        item[3]=0
        item[4]=0
        item[5]=0
        item[6]=0
        item[7]=0
        item[8]=0
        item[9]=0
        item[10]=0
        item[11]=0
        item[12]=0
        item[13]=0
        item[14]=0
        item[15]=0
        item[16]=0
        item[17]=0
        item[18]=0
        item[19]=0
        item[20]=0
        item[21]=0
        item[22]=0
        item[23]=0
    if on[0]==1 and tuduki.collidepoint(pos):#続きから始める
        on[0]=2#セーブデータ表示
        so[0]=6
    if on[0]==1 and reset[0].collidepoint(pos):#
         on[0]=8
         so[0]=6
    if on[0]==8 and reset[1].collidepoint(pos):#
         sounds.koukaonn1.play()
         i[9]=0
         i[10]=0
         i[11]=0
         i[12]=0
         for ttt in range(36):
              save1[ttt]=str(savee[ttt])
         for ttt in range(1):
              save11[ttt]=str(saveee[ttt])
         for ttt in range(36):
              save2[ttt]=str(savee[ttt])
         for ttt in range(1):
              save22[ttt]=str(saveee[ttt])
         for ttt in range(36):
              save3[ttt]=str(savee[ttt])
         for ttt in range(1):
              save33[ttt]=str(saveee[ttt])
         for ttt in range(36):
              save4[ttt]=str(savee[ttt])
         for ttt in range(1):
              save44[ttt]=str(saveee[ttt])
         with open("item.txt","w") as file:
          for wwww in gyaraa:
               file.write(str(wwww)+"\n")
         with open("time.txt","w") as file:#１行書き込み
               file.write(str(gyaraa[0]))
         with open("kyara.txt","w") as file:
               file.write(str(gyaraa[0]))
         with open("game.txt","w") as file:
               file.write(str(gyaraa[0]))
         with open("story.txt","w") as file:#１行書き込み
               file.write(str(gyaraa[0]))
         with open("save4.txt","w") as file:#ファイルsave
            for wwww in savee:
                    file.write(str(wwww)+"\n")
         with open("save44.txt","w") as file:
            for wwww in saveee:
                    file.write(str(wwww)+"\n")
         with open("save3.txt","w") as file:#ファイルsave
            for wwww in savee:
                    file.write(str(wwww)+"\n")
         with open("save33.txt","w") as file:
            for wwww in saveee:
                    file.write(str(wwww)+"\n")
         with open("save2.txt","w") as file:#ファイルsave
            for wwww in savee:
                    file.write(str(wwww)+"\n")
         with open("save22.txt","w") as file:
            for wwww in saveee:
                    file.write(str(wwww)+"\n")
         with open("save1.txt","w") as file:#ファイルsave
            for wwww in savee:
                    file.write(str(wwww)+"\n")
         with open("save11.txt","w") as file:
            for wwww in saveee:
                    file.write(str(wwww)+"\n")
         with open("stop1.txt","w") as file:
            for wwww in stoppppp:
                    file.write(str(wwww)+"\n")
         with open("stop2.txt","w") as file:
            for wwww in stoppppp:
                    file.write(str(wwww)+"\n")
         with open("stop3.txt","w") as file:
            for wwww in stoppppp:
                    file.write(str(wwww)+"\n")
         with open("stop4.txt","w") as file:
            for wwww in stoppppp:
                    file.write(str(wwww)+"\n")
         for ttt in range(25):
              gyara[ttt]=gyaraa[ttt]
         siinn2[0]=0
         kgyara[6]=0
         sgyara[6]=0
         iii[2]=0
    if on[0]==1 and setumei.collidepoint(pos):#操作説明表示
        on[0]=3#操作説明表示
        so[0]=6
    if on[0]==1 and gyarari.collidepoint(pos):#
        on[0]=4
        so[0]=6
        siinn[5]=0
        modoru.bottomright=(690,485)
    if on[0]==4  and kgyara[0].collidepoint(pos):#ギャラリーの中身
        on[0]=5
        so[0]=6
    if on[0]==4  and sgyara[0].collidepoint(pos):#ギャラリーの中身
        on[0]=6
        so[0]=6
    if on[0]==4  and siinn[0].collidepoint(pos)and siinn[5]==30:#ギャラリーの中身
        on[0]=7
        so[0]=6
        siinn[5]=0
    if on[0]==7 and siinn[3].collidepoint(pos)and siinn[5]==30 and siinn[2]!=1:#ギャラリーの中身
        siinn[2]-=1
        siinn[5]=0
        so[0]=6
    if on[0]==7 and siinn[4].collidepoint(pos)and siinn[5]==30 and siinn[2]!=10:#ギャラリーの中身
        siinn[2]+=1
        siinn[5]=0
        so[0]=6
    if (on[0]==5 or on[0]==6 or on[0]==7) and kgyara[7].collidepoint(pos) and siinn[2]==1:
        on[0]=4
        so[0]=6
    if (5>on[0]>1  and modoru.collidepoint(pos)) or (on[1]==11 and modoru.collidepoint(pos))or on[0]==8 and (reset[2].collidepoint(pos)or reset[1].collidepoint(pos)):#:#ホーム画面に戻る
        i[4]=0
        if on[1]!=11:
            on[0]=1
            so[0]=6
            music[0]=1
        if on[1]==11:
            i[0]=0
            on[1]=10
            so[0]=6
            
#def on_key_down(key):
pgzrun.go()
