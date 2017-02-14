import time
from pyswarm import pso
from training import training, best_training
from prediction.prediction import prediction

############
EMBED = 2
###########

"""
http://pythonhosted.org/pyswarm/
"""


def func(x):
    return training(x, EMBED)


lb = [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100]
ub = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

start_time = time.time()

xopt, fopt = pso(func, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={}, swarmsize=100,
                 omega=0.5, phip=0.5, phig=0.5, maxiter=50000, minstep=1e-8, minfunc=1e-8, debug=False)

elapsed_time = time.time() - start_time

print('Elapsed time: {}\nBest swarm: {}\nBest fitness: {}'.format(elapsed_time, xopt, fopt))

# training & validation
best_training(xopt, EMBED)

# prediction
prediction(xopt, EMBED)