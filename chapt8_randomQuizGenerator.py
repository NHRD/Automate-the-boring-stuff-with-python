import random

capitals = {"北海道" : "札幌市","青森県" : "青森市","岩手県" : "盛岡市","宮城県" : "仙台市","秋田県" : "秋田市",
"山形県" : "山形市","福島県" : "福島市","茨城県" : "水戸市","栃木県" : "宇都宮市","群馬県" : "前橋市","埼玉県" : "さいたま市",
"千葉県" : "千葉市","東京都" : "特別行政区","神奈川県" : "横浜市","山梨県" : "甲府市","新潟県" : "新潟市","長野県" : "長野市",
"富山県" : "富山市","石川県" : "金沢市","福井県" : "福井市","愛知県" : "名古屋市","岐阜県" : "岐阜市","静岡県" : "静岡市",
"三重県" : "津市","大阪府" : "大阪市","京都府" : "京都市","兵庫県" : "神戸市","滋賀県" : "大津市","奈良県" : "奈良市",
"和歌山県" : "和歌山市","鳥取県" : "鳥取市","島根県" : "松江市","岡山県" : "岡山市","広島県" : "広島市","山口県" : "山口市",
"徳島県" : "徳島市","香川県" : "高松市","愛媛県" : "松山市","高知県" : "高知市","福岡県" : "福岡市","佐賀県" : "佐賀市",
"長崎県" : "長崎市","熊本県" : "熊本市","大分県" : "大分市","宮崎県" : "宮崎市","鹿児島県" : "鹿児島市","沖縄県" : "那覇市"}

for quiz_num in range(5):
    quiz_file = open(".\\The-first\\Automate the boring stuff with python\\test\\capitalsquiz{}.txt".format(quiz_num + 1), "w")
    answer_key_file = open(".\\The-first\\Automate the boring stuff with python\\test\\capitalsquiz_answers{}.txt".format(quiz_num + 1), "w")

    quiz_file.write("name:\n\ndate:\n\nsemester:\n\n")
    quiz_file.write((" " * 20) + "Quiz (No.{})".format(quiz_num + 1))
    quiz_file.write("\n\n")

    prefectures = list(capitals.keys())
    random.shuffle(prefectures)
    
    for questions_num in range(len(prefectures)):

        correct_answer = capitals[prefectures[questions_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write("{}. What is the name of {} capital?\n".format(questions_num + 1, prefectures[questions_num]))
        
        for i in range(4):
            quiz_file.write("{}. {}\n".format("ABCD"[i], answer_options[i]))

        quiz_file.write("\n")

        answer_key_file.write("{}. {}\n".format(questions_num + 1, "ABCD"[answer_options.index(correct_answer)]))

quiz_file.close()
answer_key_file.close()

