#!python3

'''
Typical step:
    
    Step C must be finished before step A can begin.
'''

from collections import defaultdict
import re

INPUT = '7.txt'

TEST_INPUT = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''


pattern = re.compile("Step (\w) must be finished before step (\w) can begin.")

OFFSET = 60
WORKERS = 5

class Worker(object):
    '''
    State:
        0: waiting
        1: working
        2: done
    '''
    
    def __init__(self):
        self.reset()
    
    def start(self, step):
#        print('starting work for step', step)
        self.state = 1
        self.time = 0
        self.total_time = ord(step) - 64 + OFFSET
        self.step = step
        
    def tick(self):
        if self.state != 1: return
        self.time += 1
        if self.time >= self.total_time:
            self.state = 2
            
    def is_waiting(self):
        return self.state == 0
        
    def is_working(self):
        return self.state == 1
        
    def is_done(self):
        return self.state == 2
        
    def reset(self):
        self.state = 0
        self.time = 0
        self.total_time = 0
        self.step = '.'
        
    def __repr__(self):
        return f'({self.step}, {self.time}/{self.total_time}, {self.state})'


def get_instructions():
    instructions = []
    with open(INPUT, 'r') as f:
        for line in f:
            instructions.append(line.strip('\n'))
    return instructions
    
    
def parse_instruction(instruction):
    match = pattern.fullmatch(instruction)
    if not match:
        raise ValueError("Invalid instruction")
    return match.groups()
    
    
def get_steps(instructions):
    steps = set()
    for (x, y) in instructions:
        steps.add(x)
        steps.add(y)
    return steps
    
    
def make_dependencies(instructions):
    result = defaultdict(list)
    for from_step, to_step in instructions:
        result[to_step].append(from_step)
    return result
    
    
def make_next_steps(instructions):
    result = defaultdict(list)
    for from_step, to_step in instructions:
        result[from_step].append(to_step)
    return result
    
    
def get_first_steps(steps, dependencies):
    dependency_keys = set(dependencies.keys())
    first_steps = steps - dependency_keys
    return first_steps
    
    
def get_last_step(steps, next_steps):
    next_step_keys = set(next_steps.keys())
    last_step_set = steps - next_step_keys
    if len(last_step_set) != 1:
        raise ValueError("No uinque last step")
    return last_step_set.pop()
    
    
def depth_search(steps, dependencies, next_steps):
    def get_next_step():
        for step in sorted(candidate_steps):
            step_dependencies = dependencies[step]
            if not step_dependencies:
                return step
            if set(step_dependencies) <= done_steps:
                return step
        raise ValueError("No next step")
            
    candidate_steps = get_first_steps(steps, dependencies)
    done_steps = set()
    path = []
    while candidate_steps:
        next_step = get_next_step()
        candidate_steps.remove(next_step)
        candidate_steps.update(next_steps[next_step])
        done_steps.add(next_step)
        path.append(next_step)
    return ''.join(path)
    
    
def depth_search_workers(steps, dependencies, next_steps, worker_count):
    def get_next_steps():
        next_steps = []
        for step in candidate_steps:
            step_dependencies = dependencies[step]
            if not step_dependencies:
                next_steps.append(step)
            elif set(step_dependencies) <= done_steps:
                next_steps.append(step)
        return next_steps
        
    def working(workers):
        return any(w.is_working() for w in workers)
    
    workers = [Worker() for _ in range(worker_count)]
    candidate_steps = get_first_steps(steps, dependencies)
    done_steps = set()
    path = []
    total_time = 0
    while candidate_steps or working(workers):
        
        for worker in workers: worker.tick()
        
        new_path_steps = []
        for worker in workers:
            if worker.is_done():
                step = worker.step
                new_path_steps.append(step)
                candidate_steps.update(next_steps[step])
                done_steps.add(step)
                worker.reset()
                
#        print('next steps', get_next_steps(), 'candidate steps', candidate_steps)
        waiting_workers = [worker for worker in workers if worker.is_waiting()]
#        print(candidate_steps, get_next_steps())
        for worker, step in zip(waiting_workers, get_next_steps()):
            if worker.is_waiting():
                candidate_steps.remove(step)
                worker.start(step)
        
        path.extend(new_path_steps)
                
        print(total_time, [w.step for w in workers], ''.join(path))
        total_time += 1
        
    return ''.join(path), total_time - 1


def part1(instructions):
    instructions = [parse_instruction(instruction) for instruction in instructions]
    steps = get_steps(instructions)
    dependencies = make_dependencies(instructions)
    next_steps = make_next_steps(instructions)
    first_steps = get_first_steps(steps, dependencies)
    path = depth_search(steps, dependencies, next_steps)
    print(path)
    
    
def part2(instructions):
    instructions = [parse_instruction(instruction) for instruction in instructions]
    steps = get_steps(instructions)
    dependencies = make_dependencies(instructions)
    next_steps = make_next_steps(instructions)
    path, total_time = depth_search_workers(steps, dependencies, next_steps, WORKERS)
    print(path, total_time)
    

def main():
    instructions = get_instructions()
    part1(instructions)
    
    
def main2():
    instructions = get_instructions()
    part2(instructions)
    
    
def test():
    instructions = TEST_INPUT.split('\n')
    part1(instructions)
    
    
def test2():
    instructions = TEST_INPUT.split('\n')
    part2(instructions)
    
    
if __name__ == '__main__':
#    main()
#    test()

    test2()
    main2()
