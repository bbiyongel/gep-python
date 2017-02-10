# -*- coding: utf-8 -*-

import time
import inspyred

from random import Random
from inspyred import ec
from inspyred.ec import terminators
from optimization.objfunc import calculate_fitness

MIN_ERROR = 9999999999999999999


def generate_design_variable(random, args):
    size = args.get('num_inputs', 1)
    return [(random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0))
            for i in range(size)]


def evaluate_optimization(candidates, args):
    global MIN_ERROR
    fitness = []
    for cs in candidates:
        fn = calculate_fitness(cs)
        fitness.append(fn[0])

        if MIN_ERROR > min(fitness):
            MIN_ERROR = min(fitness)
            for i in cs:
                print("var1 =", i[0], "|", "var2 = ", i[1], "|", "var3 = ", i[2])

            print("Fitness=", fn[0])
            print("RMSE=", fn[1])
            print("MAPE=", fn[2])
            print("U=", fn[3])
            print("------------------------------------------------")

    return fitness


def optimize_core():
    rand = Random()
    rand.seed(int(time.time()))
    es = ec.GA(rand)

    es.terminator = terminators.evaluation_termination
    es.observer = inspyred.ec.observers.stats_observer
    final_pop = es.evolve(generator=generate_design_variable,
                          evaluator=evaluate_optimization,
                          maximize=False,
                          bounder=inspyred.ec.Bounder([-10.0, -10.0, -10.0], [10.0, 10.0, 10.0]),
                          max_evaluations=30000,
                          num_inputs=1)

if __name__ == '__main__':
    optimize_core()