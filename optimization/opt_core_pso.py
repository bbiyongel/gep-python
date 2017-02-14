import time
from pyswarm import pso
from optimization.objfunc import calculate_fitness


def func(x):
    fn = calculate_fitness(x, 2)
    return fn[0]


lb = [-10, -10, -10]
ub = [10, 10, 10]

start_time = time.time()
xopt, fopt = pso(func, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={},
    swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=50000, minstep=1e-8,
    minfunc=1e-8, debug=False)
elapsed_time = time.time() - start_time

print('Elapsed time: {}\nBest swarm: {}\nBest fitness: {}'.format(elapsed_time, xopt, fopt))