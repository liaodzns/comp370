1. What is the impact of including a stop word list? 
2. What differences do you observe with TF-IDF? 
3. Which method produces the best list?

1. What is the impact of including a stop word list? 
   Without stop words: Common words like "the", "a", "for", "to" dominate the naive frequency lists
   With stop words: More meaningful content words rise to the top
   - Example from anime.json (naive counting):
     - Without stops: includes "the"(56), "a"(33), "to"(32)
     - With stops: shows more relevant terms like "anime"(92), "discussion"(33), "episode"(32)

2. What differences do you observe with TF-IDF? 
   TF-IDF advantages:
     - Weights words based on their uniqueness across subreddits
     - Reduces the impact of commonly used words across all subreddits
     - Gives higher scores to subreddit-specific terminology
   - Example comparisons:
     - r/python: "python" has higher TF-IDF score (0.09154) showing it's distinctive
     - r/mechanicalkeyboards: "keyboard" and "keycaps" get higher relative importance
     - r/osugame: "fc" and "hddt" (game-specific terms) get emphasized

3. Which method produces the best list?
   The TF-IDF with stop words appears to produce the best results because:
   - Removes common English words that don't carry subject-specific meaning
   - Weights terms by their importance to specific subreddits
   - Produces more interpretable and distinctive word lists for each community
   - Example: r/machinelearning's top terms ("models", "training", "ml", "llm") clearly indicate the subject matter
