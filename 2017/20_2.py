#!python3

'''Day 20, part 2.'''

from collections import defaultdict

from data_20 import particles


class Model(object):
    '''Model particle movement.'''

    def __init__(self, particles):
        self.particles = particles


    def run(self):
        '''Run the model.'''
        while True:
            print('particle count', len(self.particles))
            input()
            self.collisions()
            self.update()


    def update(self):
        '''Update time step.'''
        for particle in self.particles:
            particle.update()


    def collisions(self):
        '''Eliminate particles that collide.'''
        positions = defaultdict(list)
        for particle in self.particles:
            positions[particle.p].append(particle)
        new_particles = []
        for particles in positions.values():
            if len(particles) == 1:
                new_particles.extend(particles)
        self.particles = new_particles



if __name__ == '__main__':
    model = Model(particles)
    model.run()
