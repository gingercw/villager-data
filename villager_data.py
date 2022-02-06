"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()
    villagers = open(filename)

    for line in villagers:
        villager_data = line.strip().split("|")
        species.add(villager_data[1])
    villagers.close()
    return species





def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    villagers_data = open(filename)

    for line in villagers_data:
        villager_data = line.strip().split("|")
        name, species = villager_data[0:2]
        if species == search_string:
            villagers.append(name)
        elif search_string == "All":
            villagers.append(name)

    villagers_data.close()

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    villagers_data = open(filename)

    for line in villagers_data:
        villager_data = line.strip().split("|")
        name = villager_data[0]
        hobby = villager_data[3]
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)
    
    villagers_by_hobby = [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]

    villagers_data.close()

    return villagers_by_hobby


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    villagers_data = open(filename)

    for line in villagers_data:
        villager_data = line.strip().split("|")
        all_data.append(tuple(villager_data))

    villagers_data.close()

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """


    villagers_data = open(filename)

    for line in villagers_data:
        villager_data = line.strip().split("|")
        name = villager_data[0]
        motto = villager_data[4]

        if villager_name == name:
            return motto

    villagers_data.close()

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
