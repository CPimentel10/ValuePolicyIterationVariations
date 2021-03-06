from mdp_matrix import GridWorld
from value_iteration_matrix import ValueIteration, GaussSeidelValueIteration, JacobiValueIteration, PrioritizedSweepingValueIteration, GaussSeidelJacobiValueIteration
import matplotlib.pyplot as plt
import numpy as np

test_rewards = [[i, j, -1] for i in range(5) for j in range(5)]
test_rewards[2] = [0, 2, 1]
test_rewards[23] = [4,3,1]
# test_rewards = [[0, 3, 5],
#                 [0, 1, 10]]

gw = GridWorld(5, test_rewards)

vl = ValueIteration(gw)

# x = np.arange(2225)

optimal_policy, optimal_value, _  = vl.run()
optimal_policy, v, vs = vl.run(optimal_value=optimal_value, theta=0.01)
# import pdb; pdb.set_trace()
plt.plot(vs)

# import pdb; pdb.set_trace()

vl = GaussSeidelValueIteration(gw)

optimal_policy, v, vsgs = vl.run(optimal_value=optimal_value, theta=0.01)
plt.plot(vsgs)
# import pdb; pdb.set_trace()

vl = JacobiValueIteration(gw)
optimal_policy, v, vsj = vl.run(optimal_value=optimal_value, theta=0.01)
plt.plot(vsj)

vl = GaussSeidelJacobiValueIteration(gw)
optimal_policy, v, vsj = vl.run(optimal_value=optimal_value, theta=0.01)
plt.plot(vsj)

vl = PrioritizedSweepingValueIteration(gw)
optimal_policy, v, vsps = vl.run(optimal_value=optimal_value)
plt.plot(vsps)

# import pdb; pdb.set_trace()

plt.legend(['VI', 'GS', 'J', 'GSJ', 'PSVI'], loc='upper right')

plt.show()
