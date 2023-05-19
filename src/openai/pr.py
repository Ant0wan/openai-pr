def generate_pull_request_description(stdin):
    """
    Generate a pull request description based on the provided input.

    Args:
     stdin (str): The input string for generating the pull request description.

    Returns:
     str: The generated pull request description.
    """
    data = INTRO_WRAP + stdin + INTRO_FMT + FORMAT
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model=MODEL,
        prompt=data,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    return response.choices[0].text


