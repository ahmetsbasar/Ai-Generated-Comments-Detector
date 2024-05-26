import random

# Define sets of phrases
beginnings = [
    "Exploring new horizons,",
    "Let's examine a different perspective:",
    "Have you ever contemplated",
    "It's intriguing to investigate",
    "One aspect that warrants attention is",
    "I'm fascinated by the idea of",
    "Unpacking the intricacies of",
    "Considering an alternative viewpoint,",
    "This raises questions regarding",
    "A unique take on",
    "Reflecting on current circumstances,",
    "Contemplating the significance of",
    "Reassessing common assumptions about",
    "Here's a novel angle:",
    "Diving deeper into",
    "Viewing things from a fresh viewpoint,",
    "Here's something to mull over:",
    "Envisioning the potential of",
    "Scrutinizing the dynamics between",
    "Exploring the connections within",
    "Dissecting the complexities of",
    "Investigating the interplay between",
    "Delving into the nuances of",
    "Reflecting on the implications of",
    "Considering alternate perspectives on",
    "Reflecting on recent events,",
    "Pondering the complexities of,",
    "Contemplating the future of,",
    "Investigating the origins of,",
    "Unveiling the mysteries behind,",
    "Examining the implications of,",
    "Probing deeper into,",
    "Uncovering hidden truths about,",
    "Speculating about the possibilities of,",
    "Questioning the assumptions surrounding,",
    "Challenging the status quo with regards to,",
    "Evaluating the impact of,",
    "Analyzing the trends in,",
    "Considering alternative perspectives on,",
    "Exploring the intersection between,"
]

middles = [
    " opens up unexplored territories.",
    " presents intriguing insights.",
    " ignites stimulating discussions.",
    " sheds light on pivotal issues.",
    " challenges conventional wisdom.",
    " offers a fresh outlook.",
    " questions established norms.",
    " encourages further investigation.",
    " prompts introspection and reflection.",
    " stimulates intellectual curiosity.",
    " fosters a deeper understanding.",
    " sparks curiosity and exploration.",
    " encourages a reevaluation of beliefs.",
    " offers a different viewpoint.",
    " invites us to question assumptions.",
    " broadens our understanding.",
    " promotes critical thinking.",
    " prompts reflection and contemplation.",
    " encourages exploration and inquiry.",
    " fosters creativity and innovation.",
    " encourages consideration of diverse viewpoints.",
    " promotes empathy and understanding.",
    " invites introspection and self-reflection.",
    " encourages critical analysis and discourse.",
    " inspires meaningful conversations and exchange.",
    " offers a fresh perspective on the topic.",
    " invites deeper reflection and introspection.",
    " sparks curiosity and intellectual inquiry.",
    " delves into the nuances of the subject matter.",
    " encourages critical thinking and analysis.",
    " presents novel insights into the discussion.",
    " fosters a deeper understanding of the issue.",
    " ignites meaningful conversations and debates.",
    " stimulates curiosity and exploration.",
    " prompts further investigation and study.",
    " provides valuable context and background information.",
    " sheds light on lesser-known aspects of the topic.",
    " offers a compelling narrative about the subject.",
    " encourages a reevaluation of existing beliefs and opinions.",
    " inspires new perspectives and viewpoints."
]

endings = [
    " What are your thoughts on this?",
    " Let's continue this dialogue!",
    " I'm eager to hear your perspective.",
    " Let's keep the conversation going!",
    " How does this resonate with your experiences?",
    " Share your insights with us!",
    " Let's explore this further together.",
    " What's your take on this matter?",
    " I value your thoughts and opinions.",
    " Let's continue this discussion.",
    " Your input adds depth to the conversation.",
    " How do you interpret this?",
    " Let's delve deeper into this topic.",
    " I'm curious about your perspective.",
    " Let's consider this from different angles.",
    " How does this fit into your worldview?",
    " Your perspective enriches the discussion.",
    " Let's ponder this further.",
    " Your insights are valuable.",
    " Let's explore this together.",
    " What implications do you see in this?",
    " I look forward to your reflections.",
    " Let's contemplate this together.",
    " What conclusions can we draw from this?",
    " I'm eager to hear your thoughts on this.",
    " How do you interpret these findings?",
    " Share your thoughts and reflections on this matter.",
    " Let's engage in a constructive dialogue about this topic.",
    " I'm curious to hear your perspective on this issue.",
    " What implications do you see in this analysis?",
    " Join the conversation and share your insights with us.",
    " Your input adds depth and richness to the discussion.",
    " Let's explore this further together. What are your ideas?",
    " How does this resonate with your own experiences?",
    " Your perspective enriches our understanding of the topic.",
    " I look forward to hearing your unique viewpoint on this.",
    " What are the potential ramifications of these findings?",
    " Let's delve deeper into this subject. What are your thoughts?",
    " Your contributions are valuable in shaping our understanding.",
    " Let's continue to explore this topic from different angles."
]

# Function to generate a single comment
def generate_comment():
    beginning = random.choice(beginnings)
    middle = random.choice(middles)
    ending = random.choice(endings)
    return beginning + middle + ending

# Function to generate a specified number of unique comments
def generate_comments(num_comments):
    comments = set()
    while len(comments) < num_comments:
        comments.add(generate_comment())
        if len(comments) % 1000 == 0:
            print(f"Generated {len(comments)} comments so far...")
    return list(comments)

# Generate 50,000 unique comments
num_comments = 50000
comments = generate_comments(num_comments)

# Save to a file
with open("generated_comments_random50K.csv", "w") as f:
    # Write the header
    f.write("Comment\n")
    
    # Write each comment in the "Comment" column
    for comment in comments:
        f.write(f'"{comment}"\n')

print(f"Generated {num_comments} unique comments and saved to 'generated_comments_random50K.csv'.")
