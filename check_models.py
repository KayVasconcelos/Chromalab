import google.generativeai as genai

# Ler chave do secrets.toml
import os
secrets_path = os.path.join(os.path.dirname(__file__), ".streamlit", "secrets.toml")

# Parser simples para secrets.toml
api_key = None
if os.path.exists(secrets_path):
    with open(secrets_path, "r") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY"):
                api_key = line.split("=")[1].strip().strip('"').strip("'")
                break

if api_key and api_key != "sua-chave-api-aqui":
    print(f"🔑 Usando chave: {api_key[:20]}...")
    genai.configure(api_key=api_key)
    
    print("\n📋 Modelos disponíveis:\n")
    try:
        models = genai.list_models()
        for model in models:
            print(f"  • {model.name}")
            if hasattr(model, 'supported_generation_methods'):
                print(f"    Métodos: {model.supported_generation_methods}")
    except Exception as e:
        print(f"❌ Erro ao listar modelos: {e}")
else:
    print("⚠️ Chave API não configurada ou inválida em .streamlit/secrets.toml")
    print("   Adicione sua chave real no arquivo!")
