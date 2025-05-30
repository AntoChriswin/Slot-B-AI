import math

# Sample dataset: [Outlook, Temperature, Humidity, Wind], Label: PlayTennis
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# Calculate entropy
def entropy(data):
    label_count = {}
    for row in data:
        label = row[-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1

    ent = 0
    for label in label_count:
        p = label_count[label] / len(data)
        ent -= p * math.log2(p)
    return ent

# Information Gain
def info_gain(data, index):
    total_entropy = entropy(data)
    values = set([row[index] for row in data])
    subset_entropy = 0
    for value in values:
        subset = [row for row in data if row[index] == value]
        subset_entropy += (len(subset) / len(data)) * entropy(subset)
    return total_entropy - subset_entropy

# Find best feature to split
def best_feature(data, features):
    gains = [info_gain(data, i) for i in range(len(features))]
    return gains.index(max(gains))

# Build decision tree
def build_tree(data, features):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]  # Pure leaf
    if len(features) == 0:
        return max(set(labels), key=labels.count)  # Majority voting

    best = best_feature(data, features)
    best_feat = features[best]
    tree = {best_feat: {}}

    values = set([row[best] for row in data])
    for value in values:
        subset = [row[:best] + row[best+1:] for row in data if row[best] == value]
        sub_features = features[:best] + features[best+1:]
        subtree = build_tree(subset, sub_features)
        tree[best_feat][value] = subtree

    return tree

# Print tree recursively
def print_tree(tree, indent=""):
    if isinstance(tree, dict):
        for key, branches in tree.items():
            for value, subtree in branches.items():
                print(f"{indent}{key} = {value}:")
                print_tree(subtree, indent + "  ")
    else:
        print(indent + "→ " + tree)

# Build and display tree
decision_tree = build_tree(dataset, features)
print("Decision Tree:")
print_tree(decision_tree)
