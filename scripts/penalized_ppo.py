from safe_rl import ppo_lagrangian, ppo
import gym
import highway_env


#ppo_lagrangian(env_fn = lambda : gym.make("merge-v0"),ac_kwargs = dict(hidden_sizes=(64,64)))
ppo_lagrangian(
    env_fn = lambda : gym.make("merge-v0"),
    ac_kwargs = dict(hidden_sizes=(64,64)),
    logger_kwargs = {"output_dir": "./fix_speed_01"},
    render=False,
    max_ep_len=70,
    epochs=150,
    steps_per_epoch=5000,
    penalty_iters=40,
    cost_lim=0.001,
    penalty_init=10,
    penalty_lr=0.05,
)
