import requests
from bs4 import BeautifulSoup


class crawlers:
    def onoffmix_crawler(genre):
        """
         0 : 개발 공모전
         1 : 해커톤
         2 : 디자인
         3 : IoT
         4 : 게임제작
        """
        genre_dict = {
            0: ['개발'],
            1: ['톤'],
            2: ['디자인'],
            3: ['IoT'],
            4: ['게임'],
        }

        # 공백 퍼센트 인코딩 : %08
        header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
        			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        			"Accept":"text/html,application/xhtml+xml,application/xml;\
        			q=0.9,imgwebp,*/*;q=0.8"}
        # 가짜 헤더 ( 크롤링 차단 우회용 )


        # ===============파라미터 생성 ======
        research_params = '&research='
        for i in genre_dict[genre]:
            research_params += i
        # ===================================
        # ===================메인 화면 설정==========
        url = "https://www.onoffmix.com/event/main/?c=092" + research_params

        print(url)
        source = requests.get(url, headers = header).text
        soup = BeautifulSoup(source, "html.parser")
        page_moves = soup.select("a.page_move")
        # ================================

        # =====페이지 갯수 크롤링 ========
        page_num = 0
        for page_move in page_moves:
            page_move = int(page_move.text)
            if page_move> page_num:
                page_num = page_move
        # ==============================

        print("페이지 갯수 : " + str(page_num))

        comp_list = []
        for i in range(1 ,(page_num+1)):

            # ====================== 페이지 모두 조회 ===============
            url = url + '&page=' + str(i)

            source = requests.get(url, headers = header).text
            soup = BeautifulSoup(source, "html.parser")
            page_moves = soup.select("a.page_move")
            # ======================================================

            titles = soup.select("h5.title.ellipsis")

            for key in titles:
                comp_list.append(key.text.strip())

        comp_list = list(set(comp_list)) # 중복 제거

        for i in comp_list:
            print("대회 : " + str(i))
        return comp_list
