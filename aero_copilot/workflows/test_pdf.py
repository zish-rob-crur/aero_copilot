import fitz

from aero_copilot.translation.translate import LLMTranslate

doc = fitz.open(
    "/Users/zhiwenwang/Downloads/Training language models to follow instructions with human feedback.pdf"
)

translator = LLMTranslate(
    provider="ollama",
    model="mistral:7b",
    # model="qwen:14b",
    # model="gemma:7b",
    prompt_name="translate_paper_v1",
)

for page in doc:
    text = page.get_text()
    
    translated_text = translator.translate(text)
    with open(f"translated_{page.number}.txt", "w") as f:
        f.write("Original text:\n" + text + "\n\nTranslated text:\n" + translated_text)
    break
