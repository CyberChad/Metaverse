from gym.envs.registration import register

register(
    id='customizd-env1-v0',
    entry_point='customized_env.envs:CustomizedEnv1',
)
register(
    id='customzied-env2-v0',
    entry_point='customized_env.envs:CustomizedEnv2',
)
