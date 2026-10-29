"""Reading time estimator tool.
 
Estimates how long a paragraph takes to read silently, using a fixed
words-per-minute (WPM) assumption.
"""
 
AUTHOR = "Connor Bishop"
APP_NAME = "Reading Time Estimator"
 
# Assumption: average adult silent reading speed for general prose is
# roughly 200-250 WPM. We use 200 WPM as a conservative, easy-to-explain value.
WORDS_PER_MINUTE = 200
 
 
def count_words(text):
    """Count whitespace-separated words in text."""
    return len(text.split())
 
 
def estimate_reading_time(text, wpm=WORDS_PER_MINUTE):
    """Return (word_count, total_seconds) for the given text."""
    words = count_words(text)
    seconds = round(words / wpm * 60)
    return words, seconds
 
 
def format_duration(seconds):
    """Turn a number of seconds into a friendly string."""
    if seconds < 60:
        return f"{seconds} second{'s' if seconds != 1 else ''}"
    minutes, rem = divmod(seconds, 60)
    label = f"{minutes} minute{'s' if minutes != 1 else ''}"
    if rem:
        label += f" {rem} second{'s' if rem != 1 else ''}"
    return label
 
 
def run():
    print(f"{APP_NAME}")
    print(f"Assumes {WORDS_PER_MINUTE} words per minute.")
    text = input("Paste a paragraph: ")
 
    if not text.strip():
        print("No text entered. Please paste at least one word.")
        return
 
    words, seconds = estimate_reading_time(text)
    print(f"Word count: {words}")
    print(f"Estimated reading time: {format_duration(seconds)}")
    print(f"Explanation: {words} words / {WORDS_PER_MINUTE} WPM "
          f"= {words / WORDS_PER_MINUTE:.2f} minutes.")