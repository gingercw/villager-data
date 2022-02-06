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
        species.add(line.strip().split("|")[1])
    villagers.close()
    return species
print(all_species("villagers.csv"))


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
        if line.strip().split("|")[1] == search_string:
            villagers.append(line.strip().split("|")[0])
        elif search_string == "All":
            villagers.append(line.strip().split("|")[0])

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

        if "Fitness" in line:
            fitness.append(line.strip().split("|")[0])
        elif "Nature" in line:
            nature.append(line.strip().split("|")[0])
        elif "Education" in line:
            education.append(line.strip().split("|")[0])
        elif "Music" in line:
            music.append(line.strip().split("|")[0])
        elif "Fashion" in line:
            fashion.append(line.strip().split("|")[0])
        elif "Play" in line:
            play.append(line.strip().split("|")[0])
    
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
        all_data.append(tuple(line.strip().split("|")))

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
        if villager_name in line:
            return line.strip().split("|")[4]

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

    villagers_data = open(filename)
    same_personality = {}

    for line in villagers_data:
        if villager_name in line:    
            villager_personality = line.strip().split("|")[2]
            print(villager_personality)
    
        # if villager_personality in line:
        #     same_personality.add(line.strip().split("|")[0])
        #     print(line.strip().split("|")[0])


    villagers_data.close()
    return same_personality

print(find_likeminded_villagers("villagers.csv", "Olivia"))
