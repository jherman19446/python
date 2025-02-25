"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    else:
        print("Please choose ticket type 0 or 1")
 


def find_my_friend(queue, friend_name):
    return queue.index(friend_name)
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """


def add_me_with_my_friends(queue, index, person_name):
     queue.insert(index, person_name)
     return queue



def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """


def how_many_namefellows(queue, person_name):
    return queue.count(person_name)
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """




def remove_the_last_person(queue):
    return queue.pop(-1)

    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """




def sorted_names(queue):
    return sorted(queue)
    
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

