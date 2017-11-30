from pico2d import *
import random


class GreenEnemy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    DEAD_TIME_PER_ACTION = 1
    DEAD_ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    DEAD_FRAMES_PER_ACTION = 4

    image = None
    dead_image = None
    LEFT_FLY, RIGHT_FLY = 0, 1

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.dead_frame = 0
        self.total_frames = 0.0
        self.dead_total_frames = 0.0
        self.dir = 0
        self.state = 0
        self.dead = False

        self.image = load_image('resource/enemy/green_enemy.png')
        self.dead_image = load_image('resource/enemy/dead.png')


    def update(self, frame_time):
        self.total_frames += GreenEnemy.FRAMES_PER_ACTION * GreenEnemy.ACTION_PER_TIME * frame_time
        self.dead_total_frames += GreenEnemy.DEAD_FRAMES_PER_ACTION * GreenEnemy.DEAD_ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2
        self.dead_frame = int(self.dead_total_frames) % 4

    def die(self):
        self.dead = True

    def draw(self):
        if self.dead == False:
            self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        elif self.dead == True:
            self.dead_image.clip_draw(self.dead_frame * 70, 0, 60, 70, self.x,self.y)
            if self.dead_frame == 3:
                self.frame = -1
                self.dead = False
                self.x, self.y = -100, -100

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


