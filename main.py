import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace


if __name__ == '__main__':
    env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')
    env = JoypadSpace(env, SIMPLE_MOVEMENT)

    env.reset()
    done = False
    while not done:
        state, reward, done, info = env.step(env.action_space.sample())
        env.render()
    env.close()