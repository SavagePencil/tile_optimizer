from bitarray import bitarray
from datetime import datetime

sprite_width = 8
sprite_height = 8

image = [
        [0,0,0,0,0,0,0,1],
        [0,0,0,1,1,1,0,0],
        [0,0,0,1,1,1,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]

# sveryx cross:
#image = [
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,1,1,    1,1,1,0,0,0,0,0,    0,0,0,0,0,0,0,0], 

#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,1,1,1,    1,1,1,1,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,1,1,1,    1,1,1,1,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,1,1,1,    1,1,1,1,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,1,1,1,    1,1,1,1,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,1,1,1,    1,1,1,1,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,1,    1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,    1,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,1,    1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,    1,0,0,0,0,0,0,0], 

#        [0,0,0,0,0,0,0,1,    1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,    1,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,1,    1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,    1,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,1,1,1,1,    1,1,1,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,1,1,1,1,    1,1,1,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,1,1,1,1,    1,1,1,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,1,1,1,1,    1,1,1,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,1,1,1,1,    1,1,1,0,0,0,0,0,    0,0,0,0,0,0,0,0], 

#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,1,1,1,    1,1,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0], 
#        [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0] 
#        ]

image_width = len(image[0])
image_height = len(image)

colors_to_ignore = {0}

class DumbTimer:
    def __init__(self, name):
        self.name = name
        self.__startTime = None
        self.__endTime = None

    def begin(self):
        self.__startTime = datetime.now()

    def end(self):
        self.__endTime = datetime.now()
        if self.__startTime is None:
            raise RuntimeError("Forgot to call begin() before end()!")
    
    def is_valid(self):
        if self.__startTime is None or self.__endTime is None:
            return False
        return True

    def elapsed(self):
        return self.__endTime - self.__startTime


# Returns True if the sprite_1 and sprite_2 overlap.
# sprite_1 and sprite_2 are represented as tuples referencing their upperleft X/Y positions
def sprites_overlap(sprite_1, sprite_2):
        dx = abs(sprite_1[0] - sprite_2[0])
        if (dx < sprite_width):
            dy = abs(sprite_1[1] - sprite_2[1])
            if (dy < sprite_height):
                return True

        return False

# Holds a definition for an in-progress solution path.  It maintains:
# * which nodes are in the current sequence
# * which targets are covered
# * which adjacencies are allowed
class SolutionChain:
    # When creating from scratch
    def __init__(self, num_nodes: int, num_targets: int):
        # Current path has no nodes to begin with.
        self.__path = bitarray(num_nodes)
        self.__path.setall(False)

        # Currently adjacent to everyone.
        self.__adjacencies = bitarray(num_nodes)
        self.__adjacencies.setall(True)

        # Currently covers nothing.
        self.__coverage = bitarray(num_targets)
        self.__coverage.setall(False)
    
    # TODO:  No multiple constructors???
    # When copying from an existing chain.
    def copy_from_existing(self, existing_chain):
        self.__path = bitarray(existing_chain.__path)
        self.__adjacencies = bitarray(existing_chain.__adjacencies)
        self.__coverage = bitarray(existing_chain.__coverage)

    # Tells us if the given node will work with the current chain (i.e., has adjacency).
    def can_add_to_path(self, node_index):
        # Does this node conflict with one of our adjacencies?
        return self.__adjacencies[node_index]

    # Adds the given node to the current chain.
    def add_to_path(self, node_index, adjacencies_for_node, coverage_for_node):
        if (False == self.can_add_to_path(node_index)):
            raise RuntimeError("Attempted to add node to a chain that couldn't accept it!")
        else:
            self.__path[node_index] = True

            # Adjacencies are reduced based on the new node.
            self.__and(self.__adjacencies, adjacencies_for_node)

            # Coverage is increased based on the new node.
            self.__or(self.__coverage, coverage_for_node)
    
    # Tells us if this chain provides coverage for the given target
    def has_coverage(self, target_index):
        return self.__coverage[target_index]

    # Does this chain cover all targets?
    def has_full_coverage(self):
        return self.__coverage.all()

    # Return a list of nodes that make up the current chain
    def get_path(self):
        path = []
        for node_idx in range(self.__path.length()):
            if (True == self.__path[node_idx]):
                path.append(node_idx)

        return path

    # Returns the length of the path.
    def get_path_len(self):
        return self.__path.count()

    # Returns the index of the first uncovered target.  Will return -1 if all are covered.
    # e.g., "1110111" will return 3.  "1111" will return -1.
    def get_lowest_uncovered_index(self):
        for idx in range(self.__coverage.length()):
            if (self.__coverage[idx] == False):
                return idx
        return -1

    # Probably a better way to do these
    def __or(self, bitarray_to_modify, const_bitarray):
        if (bitarray_to_modify.length() == const_bitarray.length()):
            for idx in range(bitarray_to_modify.length()):
                if const_bitarray[idx] == True:
                    bitarray_to_modify[idx] = True
        else:
            raise RuntimeError("Bitarray sizes must be the same for bitwise ops!")

    def __and(self, bitarray_to_modify, const_bitarray):
        if (bitarray_to_modify.length() == const_bitarray.length()):
            for idx in range(bitarray_to_modify.length()):
                if const_bitarray[idx] == False:
                    bitarray_to_modify[idx] = False
        else:
            raise RuntimeError("Bitarray sizes must be the same for bitwise ops!")

class SearchResults:
    def __init__(self):
        self.__solutions = []
        self.search_attempts = 0

    def get_solutions(self):
        return self.__solutions

    def add_solution(self, solution):
        self.__solutions.append(solution)


def search(chain, search_results, target_to_node_coverage, adjacencies, node_to_target_coverage):
    # If current chain satisfies all targets, add it as a solution and we're done.
    if chain.has_full_coverage():
        search_results.add_solution(chain)
        return
    else:
        # Find the next target we need coverage for.
        next_target_idx = chain.get_lowest_uncovered_index()

        # Which nodes provide cover for this target?
        potential_nodes = target_to_node_coverage[next_target_idx]

        for potential_node_idx in potential_nodes:
            search_results.search_attempts = search_results.search_attempts + 1

            # Will this node get along with our current chain?
            if chain.can_add_to_path(potential_node_idx):
                # What is this new node adjacent to?
                potential_node_adjacencies = adjacencies[potential_node_idx]
                potential_node_coverage = node_to_target_coverage[potential_node_idx]

                # Create a *new* chain that incorporates this potential path.
                # TODO:  Figure out multiple constructors.
                new_chain = SolutionChain(1,1)
                new_chain.copy_from_existing(chain)
                new_chain.add_to_path(potential_node_idx, potential_node_adjacencies, potential_node_coverage)

                # Recursively call it.
                search(new_chain, search_results, target_to_node_coverage, adjacencies, node_to_target_coverage)

timer_total = DumbTimer("Total")
timer_pixel_identification = DumbTimer("Identify Pixels")
timer_sprite_identification = DumbTimer("Identify Sprites")
timer_sprite_adjacency = DumbTimer("Determine Sprite Adjacency")
timer_find_solutions = DumbTimer("Find Solutions Total")
timer_solution_sort = DumbTimer("Sort Solutions")
timer_solutions_print = DumbTimer("Print Solutions")

timers = [
    timer_total,
    timer_pixel_identification,
    timer_sprite_identification,
    timer_sprite_adjacency,
    timer_find_solutions,
    timer_solution_sort,
    timer_solutions_print
    ]

timer_total.begin()

timer_pixel_identification.begin()

# Name each of the pixels in a way that they are ordered left-to-right, top-to-bottom.
# We'll use an index as the name, and offer a way to look them up by (x,y) position.
pixels = []
pixels_pos_to_index_dict = {}

for y in range(image_height):
    for x in range(image_width):
        pixel = image[y][x]
        if (pixel not in colors_to_ignore):
            tuple = (x,y)
            idx = len(pixels)
            pixels.append(tuple)
            pixels_pos_to_index_dict[tuple] = idx

# For each pixel, record which sprites cover it.  This will be empty initially.
pixel_sprite_coverage = []
for pixel_idx in range(len(pixels)):
    pixel_sprite_coverage.append(set())

timer_pixel_identification.end()

timer_sprite_identification.begin()

# Create all sprites
sprites = []

# Record which pixels a given sprite covers.
sprite_pixel_coverage = []

for spr_y in range(-sprite_height + 1, image_height):
    for spr_x in range(-sprite_width + 1, image_width):

        sprite = (spr_x, spr_y)
        sprite_idx = len(sprites)

        # Track which pixels this sprite covers.
        coverage = bitarray(len(pixels))
        coverage.setall(False)

        is_valid_sprite = False

        # If there are *any* pixels in this sprite, we'll consider it valid.
        for y in range(spr_y, spr_y + sprite_height):
            for x in range(spr_x, spr_x + sprite_width):

                pixel_pos = (x,y)
                if pixel_pos in pixels_pos_to_index_dict:
                    # Remember this as a valid sprite
                    is_valid_sprite = True

                    # Add this sprite to the list of "here's which sprites are associated with this pixel."
                    pixel_idx = pixels_pos_to_index_dict[pixel_pos]
                    pixel_sprite_coverage[pixel_idx].add(sprite_idx)

                    # This sprite covers this pixel.
                    coverage[pixel_idx] = True            

        # Were we valid?
        if is_valid_sprite == True:
            sprites.append(sprite)
            sprite_pixel_coverage.append(coverage)

timer_sprite_identification.end()

timer_sprite_adjacency.begin()

# Adjacency of sprites
sprite_adjacencies = []

# This is SUPER inefficient!
for sprite_idx, sprite in enumerate(sprites):
    adjacency = bitarray(len(sprites))

    for test_idx, test_sprite in enumerate(sprites):
        if (sprites_overlap(sprite, test_sprite)):
            adjacency[test_idx] = False
        else:
            adjacency[test_idx] = True

    sprite_adjacencies.append(adjacency)

timer_sprite_adjacency.end()

timer_find_solutions.begin()

# Track all solutions found.
search_results = SearchResults()

# Navigate the graph, finding all combinations of sprites that cover all of our pixels.
initial_chain = SolutionChain(len(sprites), len(pixels))

search(initial_chain, search_results, pixel_sprite_coverage, sprite_adjacencies, sprite_pixel_coverage)

timer_find_solutions.end()

print("Found " + str(len(search_results.get_solutions())) + " after " + str(search_results.search_attempts) + " attempts.")

timer_solution_sort.begin()

# Sort the solutions by length of path.
sorted_solutions = sorted(search_results.get_solutions(), key=SolutionChain.get_path_len)

timer_solution_sort.end()

timer_solutions_print.begin()

# Now let's print solutions.
cutoff = 50
for solution_idx, solution in enumerate(sorted_solutions):
    if (cutoff != None):
        if (solution_idx > cutoff):
            break;

    path = solution.get_path()

    output_str = "Solution " + str(solution_idx) + " (Length: " + str(len(path)) + "): "

    for path_idx in range(len(path)):
        if (path_idx != 0):
            output_str = output_str + " -> "

        sprite_idx = path[path_idx]
        sprite_tuple = sprites[sprite_idx]

        output_str = output_str + "(" + str(sprite_tuple[0]) + ", " + str(sprite_tuple[1]) + ")"
    
    print(output_str)

timer_solutions_print.end()

timer_total.end()

for timer in timers:
    outputStr = "Timer '" + timer.name + "':  "
    if timer.is_valid:
        outputStr = outputStr + str(timer.elapsed())
    else:
        outputStr = outputStr + "<NOT VALID>"

    print(outputStr)