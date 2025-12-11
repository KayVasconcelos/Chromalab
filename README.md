# 🎨 Chromalab - Análise de Colorimetria com IA

Aplicação web para análise de colorimetria pessoal usando câmera em tempo real e IA Google Gemini.

## 🌟 Funcionalidades

- 📹 **Câmera em Tempo Real**: Visualize seu rosto com paletas de cores em overlay
- 🎨 **4 Paletas Sazonais**: Primavera, Verão, Outono e Inverno
- 📸 **Captura de Fotos**: Tire fotos para análise personalizada
- 🤖 **Análise com IA**: Google Gemini analisa subtom, profundidade e recomenda cores
- 🎭 **Modo Demonstração**: Teste a app sem usar quota da API
- 💾 **Histórico**: Salve suas análises

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.11+ (3.13 suportado)
- Câmera web
- Conexão com internet
- Navegador moderno (Chrome, Firefox, Safari, Edge)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/KayVasconcelos/Chromalab.git
cd Chromalab
```

2. **Crie um ambiente virtual**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# ou
source .venv/bin/activate  # macOS/Linux
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure a chave API Gemini**
   - Vá para: https://ai.google.dev/aistudio
   - Clique em "Create API Key"
   - Abra `.streamlit/secrets.toml` e adicione:
   ```toml
   GEMINI_API_KEY = "sua-chave-aqui"
   ```

5. **Execute a aplicação**
```bash
streamlit run app.py
```

A app abrirá em: `http://localhost:8502`

## 📁 Estrutura do Projeto

```
Chromalab/
├── app.py                           # Aplicação principal
├── check_models.py                  # Script para verificar modelos disponíveis
├── requirements.txt                 # Dependências Python
├── README.md                        # Este arquivo
├── GEMINI_SETUP.md                 # Guia de configuração Gemini
├── .gitignore                       # Arquivos a ignorar no Git
├── .streamlit/
│   ├── secrets.toml                 # 🔐 Chave API (não commitar)
│   └── config.toml                  # Configurações Streamlit
├── Semana 1/
│   └── Semana1.md                   # Documentação semana 1
└── Main.html                        # Versão A-Frame anterior (deprecated)
```

## 🎯 Como Usar

1. **Posicionar o Rosto**: Use a câmera para se posicionar bem iluminado
2. **Escolher Paleta**: Selecione uma paleta no painel lateral
3. **Capturar Foto**: Clique no botão "📸 Capturar Foto"
4. **Analisar**:
   - **Modo Demo**: Ative o checkbox para ver análise exemplo
   - **Modo Real**: Use sua chave Gemini para análise personalizada
5. **Ver Resultados**: Analise as recomendações de cores

## ⚙️ Configuração

### Variáveis de Ambiente
O arquivo `.streamlit/secrets.toml` armazena:
```toml
GEMINI_API_KEY = "sua-chave-api"
```

⚠️ **Segurança**: Este arquivo está no `.gitignore` e nunca deve ser commitado.

### Limites da API Gemini

| Plano | Requisições/min | Tokens/dia |
|-------|-----------------|-----------|
| Free Tier | 15 | 1 milhão |
| Paid Tier | 600+ | 50+ milhões |

Upgrade: https://ai.google.dev/billing/overview

## 🛠️ Desenvolvimento

### Dependências Principais
- **streamlit**: Framework web
- **streamlit-webrtc**: Captura de câmera
- **opencv-python-headless**: Processamento de imagens
- **google-generativeai**: API Gemini
- **pillow**: Manipulação de imagens
- **numpy**: Processamento de arrays

### Adicionar Novas Dependências
```bash
pip install novo-pacote
pip freeze > requirements.txt
```

### Estrutura do Código
- `VideoProcessor`: Classe que processa frames da câmera em tempo real
- `PALETAS_COLORIMETRIA`: Dicionário com paletas sazonais
- Lógica de captura e análise Gemini na seção "Análise Personalizada com IA"

## 🐛 Troubleshooting

### Câmera não funciona
- Verifique permissões no seu SO
- Teste a câmera em outro app
- Recarregue a página (F5)

### Erro "API Key not valid"
- Verifique se a chave está em `.streamlit/secrets.toml`
- Reinicie o Streamlit (Ctrl+C e `streamlit run app.py`)
- Confirme que a chave é válida em: https://ai.google.dev/aistudio

### Quota excedida
- Free Tier reseta a cada 24h
- Faça upgrade para usar mais: https://ai.google.dev/billing/overview
- Use "🎭 Modo Demo" para testar sem gastar quota

### App não carrega
- Verifique Python 3.11+: `python --version`
- Reinstale dependências: `pip install -r requirements.txt --force-reinstall`
- Limpe cache Streamlit: `streamlit cache clear`

## 📚 Documentação Adicional

- [Guia Gemini API](GEMINI_SETUP.md)
- [Documentação Streamlit](https://docs.streamlit.io)
- [Google Generative AI](https://ai.google.dev/docs)

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Kayla de Brito**
- GitHub: [@KayVasconcelos](https://github.com/KayVasconcelos)
- Projeto: [Chromalab](https://github.com/KayVasconcelos/Chromalab)

## ⭐ Créditos

- [Streamlit](https://streamlit.io) - Framework web
- [Google Generative AI](https://ai.google.dev) - API Gemini
- [OpenCV](https://opencv.org) - Processamento de imagens

---

**Última atualização**: Dezembro 2025

Se encontrar problemas, abra uma [Issue](https://github.com/KayVasconcelos/Chromalab/issues)! 🚀