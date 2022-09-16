
text_flag = {1: False, 2: False, 3: True, 4: True, 5: True, 6: True}   # 자동으로 생성되는 텍스트는 그 스테이지가 끝나면 다시 못보도록 한다.

# 자동 생성 텍스트
texts = {0: [["흐음......",
              "이번달 남은 돈도 벌서 이만큼이네...",
              "(나는 자랑스러운 대한민국의 29세 군필 백수 김철수라고 한다.)",
              "(보다시피 매일매일 돈이 쪼달려서 사는 인생을 살고있다.)",
              "진짜 어떡하지??? 이대로 있다간 지금 살고있는 원룸의 월세도 못낼 거고..",
              "최악의 경우엔 쫓겨난다...!",
              "아르바이트는 어제 짤렸고... 돈을 어떻게 구해야 하지??",
              "이렇게 된 이상....어쩔 수 없다..!",
              "그만두겠다고 마음 먹었다만...일단 살아야 하지 않겠어?!",
              "도굴왕 김철수가 돌아올 시간이다!"]],

         1: [["한몫 단단히 챙기면 이 바닥을 뜰 거라고 자주 말했지만...",
              "정신을 차려보니 오늘도 유적을 찾아 어슬렁거리고 있네요.",
              "방향키로 움직일 수 있어요. 저기 열려있는 문까지 움직여 보세요."]],

         2: [["이런, 길이 없군요.",
              "하지만 걱정 마세요. 이런 유적들은 대개 어떠한 장치가 숨어있으니까요.",
              "주머니에 쓸만한 것이 있네요. Space 바를 눌러 돌을 던져 보세요.",
              "돌에 반응해서 마법진이 나타났네요!",
              "이제 문을 향해 나아갈 수 있어요."],

             ["저기 무언가 반짝거리는군요.",
              "돈이 좀 될 것 같지 않나요?",
              "가까이 가서 Tap 키를 꾸욱 눌러 주워보세요.",
              "가까이서 보니 더욱 반짝거리는 것 같아요.",
              "이제 문으로 가서 다른 곳도 찾아보도록 하죠."],

             ["무언가 신비로운 기운이 느껴져요. 저게 뭘까요?",
              "한번 가까이 가서 Tap 키를 꾸욱 눌러 주워볼까요?",
              "유물 조각이네요!",
              "스테이지에 흩어진 조각을 전부 모으면 유물을 얻을 수 있을 거에요.",
              "유물은 힘을 지닌 물건이에요.",
              "그 힘은 당신을 강하게 만들어 줄 수도 있고, 곤란하게 할 수도 있어요.",
              "다른 조각이 더 있을지도 모르니 문으로 가서 한번 찾아볼까요?"],

             ["이런 유적에는 저런 몬스터들도 많죠. 조심하세요.",
              "몬스터는 자신의 영역을 침범한 당신을 곱게 보고 있지만은 않을 테니까요.",
              "괜찮아요? 많이 놀랐죠? 이게 당신의 체력이에요.",
              "체력은 몬스터에게 공격을 받거나, 함정에 빠지거나, 길에서 떨어지면 수치가 줄어들어요.",
              "체력이 0이 되면...말하지 않아도 알겠죠?",
              "당신은 준비성이 철저한 도굴꾼이에요. 이럴 때를 대비해서 로프를 가져왔죠.",
              "체력이 모두 떨어지기 전에 R키를 눌러 로프를 사용해 긴급히 탈출해보세요.",
              "로프를 사용하면 더이상 피해는 없지만, 이 맵에서 얻은 것들은 어쩔 수 없이 놓고 가야해요.",
              "그래도 목숨이 먼저니까요. 로프는 개수 제한이 있으니 신중히 사용해야해요."],

             ["여기는 성소에요. 저 앞에서 특별한 운명들이 당신을 기다리는 것 같네요.",
              "한번 볼까요? WASD로 멀리 내다보세요.",
              "어떤 운명들이 기다리는지 궁금하네요. 한번 가볼까요?",
              "우리의 삶은 무수한 운명의 가능성으로 이루어져 있죠.",
              "당신은 이 중에 어떤 운명을 선택하실 건가요?",
              "빨강 : 유물을 획득한다.",
              "파랑 : 유물을 획득한다.",
              "초록 : 유물을 획득한다.",
              "아무런 대가도 치르지 않다니 운이 좋았네요!",
              "어떠한 운명은 대가를 치러야 하는 경우도 있고, 어떠한 운명은 불합리하기도 하죠.",
              "자, 저 문을 지나 앞으로는 어떤 운명이 당신을 기다리는지 맞이해 볼까요?"]]}

# 이벤트 텍스트(이벤트 트리거를 통해 생성되는 텍스트)
event_texts = {}