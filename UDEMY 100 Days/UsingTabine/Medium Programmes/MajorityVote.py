def majority_vote(votes):
    """
    Calculates the majority vote in a list of votes.

    Args:
        votes (list): The list of votes.

    Returns:
        object: The majority vote.
    """
    # Count the number of times each vote occurs
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    # Find the vote with the highest count
    max_count = 0
    majority_vote = None
    for vote, count in vote_counts.items():
        if count > max_count:
            max_count = count
            majority_vote = vote

    return majority_vote


# Test the function with some examples
votes = ["A", "A", "B", "B", "C", "C"]
print(majority_vote(votes))  # Output: "A"

votes = ["A", "B", "C", "B", "B", "B"]
print(majority_vote(votes))  # Output: "B"

votes = ["A", "A", "A", "B", "B", "B"]
print(majority_vote(votes))  # Output: "A"

votes = ["A", "A", "A", "A", "A", "B"]
print(majority_vote(votes))  # Output: "A"

votes = ["A", "C", "C", "D", "C", "C"]
print(majority_vote(votes))  # Output: "E"
