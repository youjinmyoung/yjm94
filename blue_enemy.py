from pico2d import *
import random

class BlueEnemy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
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
    twist_image = None
    dead_image = None
    dead_sound = None
    LEFT_FLY, RIGHT_FLY = 0, 1

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.dead_frame = 0
        self.total_frames = 0.0
        self.dead_total_frames = 0.0
        self.dir = 1
        self.state = 0
        self.dead = False

        self.image = load_image('resource/enemy/blue_enemy.png')
        self.dead_image = load_image('resource/enemy/dead.png')
        if self.twist_image == None:
            self.twist_image = load_image('resource/enemy/blue_enemy_twist.png')
        if BlueEnemy.dead_sound == None:
            BlueEnemy.dead_sound = load_wav('wav_sounds/explosion.wav')
            BlueEnemy.dead_sound.set_volume(32)


    def update(self, frame_time):
        self.total_frames += BlueEnemy.FRAMES_PER_ACTION * BlueEnemy.ACTION_PER_TIME * frame_time
        self.dead_total_frames +=BlueEnemy.DEAD_FRAMES_PER_ACTION * BlueEnemy.DEAD_ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) %2
        self.dead_frame =int(self.dead_total_frames) % 4
        distance = self.RUN_SPEED_PPS * self.dir * frame_time
        self.y -= distance
        if self.y <= 345:
            self.RUN_SPEED_PPS = 0


    def die(self):
        self.dead = True
        self.dead_sound.play()
        pass
    def draw(self):
        if self.y >= 345:
            self.twist_image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        if self.dead == False and self.y <= 345:
            self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        elif self.dead == True:
            self.dead_image.clip_draw(self.dead_frame * 70, 0, 60, 80, self.x,self.y)
            if self.dead_frame == 3:
                self.dead_frame = -1
                self.dead = False
                self.x, self.y = -100, -100


    def get_bb(self):
        return self.x - 25, self.y - 15, self.x + 25, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
