# -*- coding: utf-8 -*-
import time

from random import Random
import inspyred
from inspyred import ec
from inspyred.ec import terminators
from training import training, best_training
from prediction.prediction import prediction

EMBED = 2
BEST_FITNESS = 9999999999999999999
BEST_GENE = []


def generate_design_variable(random, args):
    size = args.get('num_inputs', 1)
    return [(random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
            for i in range(size)]


def evaluate_optimization(candidates, args):
    global BEST_FITNESS
    global BEST_GENE
    fitness = []

    for cs in candidates:
        fn = training(list(cs), EMBED)
        fitness.append(fn)

        if BEST_FITNESS > min(fitness):
            BEST_FITNESS = min(fitness)
            for i in cs:
                BEST_GENE = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]]

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
                          pop_size=100,
                          bounder=inspyred.ec.Bounder([-100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0],
                                                      [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]),
                          max_evaluations=10000,
                          num_elites=1,
                          num_inputs=1)


if __name__ == '__main__':

    start_time = time.time()
    optimize_core()
    elapsed_time = time.time() - start_time

    print('Elapsed time: {}\nBest gene: {}\nBest fitness: {}'.format(elapsed_time, BEST_GENE, BEST_FITNESS))

    # training & validation
    best_training(BEST_GENE, EMBED)

    # prediction
    prediction(BEST_GENE, EMBED)
