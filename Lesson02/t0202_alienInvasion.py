#
# 게임 클래스 생성, 빈 파이게임 창을 만든다.
#
import sys
import pygame

class AlienInvasion:
    """게임 전체의 자원과 동작을 관리하는 클래스"""

    def __init__(self):
        """게임을 초기화하고 게임 자원을 생성"""
        pygame.init() # 파이게임이 정상적으로 동작하기 위해 필요한 세팅을 초기화

        self.screen = pygame.display.set_mode((1200,800)) # (1200,800)은 창의 크기
        pygame.display.set_caption("Alien Invasion")
        #2단계에서 추가
        self.bg_color = (230, 230, 230)
        #여기까지

    def run_game(self):
        """게임의 메인 루프 시작"""
        while True:
            # 키보드와 마우스 이벤트를 주시
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #2단계에서 추가
            # 루프의 반복마다 화면을 다시 그림
            self.screen.fill(self.bg_color)
            #여기까지

            # 가장 최근에 그려진 화면을 표시
            pygame.display.flip()

if __name__ == '__main__':
    # 게임 인스턴스를 만들고 게임을 실행
    ai = AlienInvasion()
    ai.run_game()



