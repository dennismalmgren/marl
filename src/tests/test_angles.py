import numpy as np
import scipy as scp
from numpy.linalg import norm

#############################################
# Add the one-folder-up-path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
#############################################

from envs.blocking_env import BlockingEnv

def test_create_environment():
    x = 5
    assert x == 5, 'test failed'

# 

# env_info = {
#     'agent_count_red': 4,
#     'agent_count_blue': 4
# }


# env = BlockingEnv(env_info)

