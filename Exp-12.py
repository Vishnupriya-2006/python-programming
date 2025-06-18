def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve Tower of Hanoi problem recursively.

    Parameters:
    n (int): Number of disks
    source (str): The starting rod
    target (str): The destination rod
    auxiliary (str): The auxiliary rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, target, source)


# Example usage:
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')
