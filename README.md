<br />
<p align="center">
  <a href="">
    <img src=".logo.png" alt="Logo" width="90" height="90">
  </a>

  <h1 align="center">OpenAI PR</h1>

  <p align="center"><i>This GitHub Action generates a pull request description using OpenAI's GPT-3 API.</i>
  </p>
</p>

---

## Inputs

#### `api_key` (required)

Your OpenAI API key. You can get one from the [OpenAI website](https://beta.openai.com/signup/).


## Outputs

#### `text`

The generated pull request description.


## Example Usage

```yaml
name: OpenAI PR Description Generator

on:
  pull_request:
    types:
      - opened
      - synchronize

permissions:
  pull-requests: write
  contents: read

jobs:
  pull-request:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: Ant0wan/openai-pr@0.0.11
        with:
          api-key: ${{ secrets.OPENAI_API_KEY }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## How It Works

This action runs as a composite action with three steps:
1. **Install Python**: Installs Python version 3.10.
2. **Install Dependencies**: Installs the required dependencies listed in `requirements.txt`.
3. **Generate Description**: Runs `git show | python main.py` to generate the pull request description using OpenAI's GPT-3 API.


## License

This action is released under the [MIT License](https://chat.openai.com/LICENSE).

