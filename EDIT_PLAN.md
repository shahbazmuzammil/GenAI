# Edit Plan: Fix NLTK sentence tokenization LookupError

## Information Gathered
- `NLP/NLPwithNLTKTokenization.ipynb` contains:
  - `from nltk.tokenize import sent_tokenize`
  - `sent_tokenize(corpus)`
  - No code to ensure required NLTK resources (Punkt) exist locally.
- Running NLTK in the current environment shows missing NLTK data resources (e.g., Punkt and `wordnet`).
- Therefore, `sent_tokenize` can fail with `LookupError` due to unavailable NLTK corpora.

## Plan
### File: `NLP/NLPwithNLTKTokenization.ipynb`
1. Wrap the call to `sent_tokenize(corpus)` in a `try/except LookupError`.
2. In the `except`, use a lightweight regex-based sentence splitter:
   - Split on punctuation like `. ! ?` followed by whitespace.
   - Trim results and drop empty strings.
3. Keep outputs consistent (return list of sentences).

### (Optional) File: `NLP/TextPreproccessingStemmingfeatNLTK.ipynb`
- If the notebook uses `WordNetLemmatizer`, add a guard so it doesn’t crash when `wordnet` is missing.

## Dependent Files to be edited
- `NLP/NLPwithNLTKTokenization.ipynb`
- Possibly `NLP/TextPreproccessingStemmingfeatNLTK.ipynb` (only if WordNet lemmatizer is executed unguarded)

## Followup steps
- Re-run the tokenizer cell(s) in `NLPwithNLTKTokenization.ipynb`.
- Verify that it prints sentence list without throwing `LookupError`.

- <ask_followup_question>
  Please confirm you want me to update `NLP/NLPwithNLTKTokenization.ipynb` to add a fallback sentence splitter when NLTK Punkt data is missing.
  (I can also optionally add WordNet guards, but I’ll do that only if you approve.)
  </ask_followup_question>

