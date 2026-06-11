import pgzrun#普段
from pygame import mixer#普段
import RPG3
WIDTH =700
HEIGHT=490
q=Actor('q',topleft=(0,0))
g1=Actor('am1',topleft=(500,70))#キャラクター（主人公）
am2=Actor('am2',topleft=(500,70))#キャラクター（主人公）
am4=Actor('am4',topleft=(500,70))#キャラクター（主人公）
am5=Actor('am5',topleft=(500,70))#キャラクター（主人公）
am3=Actor('am3',topleft=(500,70))#キャラクター（主人公）
nn=Actor('nn',topleft=(0,330))
def draw():
        if RPG3.ii[14]==2:
            q.draw()
        if RPG3.ii[14]==1:
            if RPG3.ii[23]==1:#ii[23]の数値で、表情の割り振り
                g1.draw()#ノーマル顔
            if RPG3.ii[23]==2:
                am3.draw()#口開けてなくて汗かいて困ってる
            if RPG3.ii[23]==3:
                am4.draw()#口開けて困ってる
            if RPG3.ii[23]==4:
                am2.draw()#口も明けず汗もかかず普通に困ってる
            if ii[23]==5:
                am5.draw()#めっちゃ焦ってる、目の瞳孔小さくなるぐらい

        nn.draw()
        RPG3.i[4]=40#テキスト読んでいる間にアイテム欄など開けないように
        if RPG3.ii[2]!=3:#ii[3]に入った数の回数、セリフを流してくれる
            screen.draw.text("SPACEキー➡文章スキップ",(100,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
        if RPG3.ii[2]==3:
            screen.draw.text("Dキー➡次の文へ",(100,0),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=20)
        if RPG3.ii[9]==1 and RPG3.ii[3]==1:
            screen.draw.text("itemをgetします、セーブしますか？",(327,0),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=22)#アイテムは最終段落中に増やすようにする
            screen.draw.text("はい→Q　いいえ→D　をクリック",(325,30),fontname='a.ttc',owidth=0.3,color="YELLOW",fontsize=24)
        #if ii[3]==段落数 and 障害物.colliderect(c):※アイテムが手に入る場合はテキスト内でゲットさせる#シーンのテキストの時はシーン番号をかいておく        
        if RPG3.on[3]==2 and RPG3.so[2]==1:#←シーンのセリフかon[3]←そのシーン中のどのセリフかso[2]
            RPG3.ii[14]=2
            if RPG3.ii[3]==8:
                screen.draw.text("│ある日一人ぼっちの少女がいました、少女には│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│友達がいませんでした、、、、ただ一人教室の│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│端っこの席で読書をするのが彼女の習慣でした│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==7:
                screen.draw.text("│彼女は友達を欲しがっていました、、しかし、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│不器用な彼女には周りの子たちと上手くなじむ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│ことができませんでした、、、、、、、、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==6:
                screen.draw.text("│彼女はクラスメイトの子たちと仲良くなろうと│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│いろんな子にたびたび話しかけたりしました、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│しかし思うように会話が弾むことはありません│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==5:
                screen.draw.text("│そんな中、一緒にかかわろうと声をかけてくる│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│彼女に、周りの子たちは不満を抱くようになり│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│次第に、その気持ちは悪化していきました、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==4:
                screen.draw.text("│最終的に彼女は、周りから仲間外れにされたり│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│時には、ひどくいじめられ、悪口を言われる、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│そんな羽目になってしまいます、、、、、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==3:
                screen.draw.text("│次第に、彼女は心に傷を追うようになり、、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│友達を作ろうと、話しかけるのをやめるように│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│なりました、、、、、、、、、、、、、、、、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                screen.draw.text("│「傷つくぐらいなら、私は一人でいいや」、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│そう考えるようになり、それ以降毎日、彼女は│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│友達のいない学校生活を送るようになりました│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                ii[14]=0
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・は！・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・え？・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if RPG3.on[3]==2 and RPG3.so[2]==7:#←シーンのセリフかon[3]←そのシーン中のどのセリフかso[2]
            RPG3.ii[14]=1#←キャラクター表示
            if RPG3.ii[3]==4:
                RPG3.ii[23]=5#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│ここはどこなの・・？・・そもそも私はなんで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│こんなところにいるの？・・・何があったのか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│わからない、・・・・・・・頭が整理できない│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==3:
                RPG3.ii[23]=3#←表情設定
                screen.draw.text("│確か、私は買い物に行って外に出て、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・ん～～思い出せない、、わからないことが│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│多すぎる・・・、あの後何があったんだっけ？│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                RPG3.ii[23]=2#←表情設定
                screen.draw.text("│・・なんだか暗くて怖いな・・・・見たところ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│周りに人もいないし・・・・、心細い・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│どうしよう、とりあえず出口とかないかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                RPG3.ii[14]=0
                screen.draw.text("│※十字キーでプレイヤーを操作「←↑↓→」　│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│　Sキーでアイテム欄を開く「S」　　　　  　│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│　Dキーでマップ内の物を調べる「D」　　　　│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if  RPG3.on[2]==-2 and RPG3.kabe4.colliderect(RPG3.cc):#体育館倉庫マップの壁４にぶつかってた時(時計を見るシーン)
            RPG3.ii[15]=1#ストーリー進めるストッパー（data[2]の数値のストッパー）これをつけると、読み終わったらdata[2]に＋１される
            if RPG3.ii[3]==3:
                RPG3.ii[14]=0
                screen.draw.text("│とても古い時計だ、カチカチ音を立てながら、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│短針が回ってる、見た目からして長年使われて│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│いるようだ・・・時計の針は22時を示している│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                RPG3.ii[14]=1#←キャラクター表示
                RPG3.ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│え！今こんな時間帯なの、どうしよう・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│お父さんとお母さん、心配してるかな・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・早く帰りたい・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                RPG3.ii[14]=1#←キャラクター表示
                RPG3.ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│あ、・・そうだ、電話とかないかな・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│電話を使えば助けを呼べるかも・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│どこかにないかな・・・・・探してみよう・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if  RPG3.on[3]==3 and RPG3.so[2]==1:#体育館、電話見つけるシーン
            RPG3.ii[15]=1
            if RPG3.ii[3]==3:
                RPG3.ii[14]=1#←キャラクター表示
                RPG3.ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│あった、電話、早速使えるか試してみようかな│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・ん～～～・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                RPG3.ii[23]=4#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│反応しない・・古すぎるのかな？もう壊れちゃ│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│ってるのかな・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│全然動かない・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if  RPG3.on[3]==3 and RPG3.so[2]==5:#体育館、電話見つけるシーン
            if RPG3.ii[3]==4:
                RPG3.ii[23]=5#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│今何か大きな音が・・・！・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・だ、誰かいるの？・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==3:
                RPG3.ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│・・・・・・・・・・・もうここ怖いよ・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・早く帰りたい・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                RPG3.ii[23]=2#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│あいにく、携帯電話も今は持っていないし・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│なんで、持ってこなかったんだろ・・・でも、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│ここにいても、変わらないし・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                RPG3.ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│怖いけど、探索しなきゃ・・・・、そういえば│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│何か外に出るのに役立ちそうな道具とかないか│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│な・・いいアイテムがないか探してみようかな│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if  RPG3.on[2]==0 and RPG3.kabe7.colliderect(RPG3.cc):#体育館で鍵ゲット
            if RPG3.ii[3]==1:
                RPG3.item[1]=1#鍵ゲット
                RPG3.ii[15]=1
                RPG3.ii[14]=1#←キャラクター表示
                RPG3.ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│こんなところに、何かのカギがある、・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│なんだろう、多分どこかの部屋のカギかな・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│とりあえず手にもっておこうかな・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if  RPG3.on[2]==-1 and RPG3.kabe5.colliderect(RPG3.cc):
            if RPG3.ii[3]==5:
                RPG3.ii[14]=1#←キャラクター表示
                screen.draw.text("│青色の本が置いてある、この色、綺麗だな、、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│でもずいぶん、薄い本みたい・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│中に何が書いてあるんだろう、読んでみよう、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==4:
                RPG3.ii[14]=0
                screen.draw.text("│5月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│今日、突然彼女が家を飛び出した、なぜ飛び出│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│したのかはわからない、でも早く見つけなきゃ│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==3:
                screen.draw.text("│6月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│あれから一か月、警察も私も、ずっと彼女を探│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│しているのに見つからない・・そろそろ疲れた│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                screen.draw.text("│7月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│きずいたら一人で泣いていた、今思えば私は、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│彼女に何もしてやれてなかった、情けなかった│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                screen.draw.text("│8月1日ーーーーーーーーーーーーーーーーーー│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│私は、初めて彼女にプレゼントを作った、もし│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│いま天国にいるなら、喜んでくれてるかな・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if RPG3.so[2]==3 and RPG3.on[3]==4:#体躯倉庫でロック解除、
            if RPG3.ii[3]==1:
                RPG3.ii[14]=1
                screen.draw.text("│ロックが外れた、なんだろう、箱の中に何か書│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│かれているみたい、なんて書いてあるんだろう│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│[隠れろ]って書いてある、どうゆう意味だろう│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if RPG3.so[2]==5 and RPG3.on[3]==4:#体躯倉庫でロック解除、
            if RPG3.ii[3]==2:
                RPG3.ii[14]=0
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                RPG3.ii[14]=1
                RPG3.ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│怖い、絶対おかしい、何かが私に近付いてきて│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│る気がする、明らかに変な音がする、やだ・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│早くどこかに隠れなきゃ危ないかも、・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if  RPG3.on[2]==-2 and RPG3.kabe5.colliderect(RPG3.cc) and RPG3.data[2]==4:#体育館のロッカーに隠れる
            if RPG3.ii[3]==8:
                RPG3.ii[15]=1
                RPG3.item[2]=1#鍵2つ目
                RPG3.ii[14]=1
                RPG3.ii[23]=2#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│こんなところに私が入れそうなロッカーがある│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・ちょっと壊れかけだけど、│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│見た感じ・・隠れることはできるかも・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==7:
                RPG3.ii[23]=3#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│ほかに隠れれそうないい場所もなさそうだし、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│ひとまずこの中に隠れようかな・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==6:
                RPG3.ii[14]=2
                screen.draw.text("│（なんで私はこんな目にあっているんだろう・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│私は何か悪いことしたのかな・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・）│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==5:
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==4:
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・おさまったかな・・・・・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│迫ってくる音が聴こえなくなった・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==3:
                screen.draw.text("│・・・・・・・・・・・・・・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│そろそろ、出てみようかな・・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・・・・・・何もなければいいけど・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==2:
                RPG3.ii[14]=1
                RPG3.ii[23]=4#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│・・・・・・・見た感じもう大丈夫そう・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│そういえば、ロッカーの中に何か入っていた気│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│がする・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                RPG3.ii[23]=1#←表情設定 1 ノーマル　2 汗かいて困ってる 3口開けて汗かいて困ってる 4困ってる　5 無茶苦茶ビビってる
                screen.draw.text("│これは、なんだろう、カギ？・・・・・・・・│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│またどこかのカギなのかな？・・・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│使えるかもしれないから、拾っておこうかな、│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if RPG3.so[2]==2 and RPG3.on[3]==5 and RPG3.kabe6.colliderect(RPG3.cc):#体躯倉庫でロック解除、
            if RPG3.ii[3]==2:
                RPG3.ii[15]=1
                RPG3.ii[14]=1
                screen.draw.text("│あれ？・・・さっきまでここに扉あったっけ、│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│私が気が付かなかっただけかな？・・・・・・│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│・・・・不思議というか、なんというか・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
            if RPG3.ii[3]==1:
                screen.draw.text("│・・・・あ！・・・・さっき手に入れたカギで│",(0,350),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│このドア開けられそうだ、開けて先に進んでみ│",(0,390),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
                screen.draw.text("│よう・・・・・・・・・・・・・・・・・・・│",(0,430),fontname='a.ttc',owidth=0.3,color="WHITE",fontsize=30)
        if RPG3.ii[0]<3:#3はテキスト表示の速さii[1]はx座標ii[2]はｙ座標
            RPG3.ii[0]+=1
            if RPG3.ii[0]==3:
                RPG3.ii[0]=0
                RPG3.ii[1]+=1
                if RPG3.ii[1]==21:
                    RPG3.ii[1]=0
                    RPG3.ii[2]+=1
        if RPG3.ii[2]>=3:
            RPG3.ii[2]=3
        RPG3.n1.y=RPG3.ii[2]*40+490
        RPG3.n.x=RPG3.ii[1]*30+670
        RPG3.n.y=RPG3.ii[2]*40+450
        RPG3.n1.draw()
        RPG3.n.draw()
        if RPG3.i[13]==0 and RPG3.ii[2]<3:
            mixer.init()
            mixer.music.load("da.wav")##8888888888888888888888888
            mixer.music.play(1)
            RPG3.i[13]=4#何秒間ならないようにするか
pgzrun.go()


    

