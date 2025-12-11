# 🔧 Configuração da API Google Gemini

## ✅ O que foi feito

A aplicação **Chromalab** foi atualizada com suporte completo para análise de colorimetria usando a IA Google Gemini. Agora você pode:

1. **📸 Capturar fotos** do seu rosto com a câmera em tempo real
2. **🤖 Analisar com Gemini** para receber feedback personalizado sobre sua análise de cores
3. **💾 Salvar análises** no histórico da sessão

## 🔑 Como obter a API Key do Gemini

### Passo 1: Acessar Google AI Studio
- Acesse: **https://ai.google.dev/**
- Clique em **"Get API Key"** ou **"Get started"**
- Faça login com sua conta Google (criar uma se necessário)

### Passo 2: Criar uma nova chave
- No painel do Google AI Studio, clique em **"Create API Key"**
- Selecione o projeto padrão (ou crie um novo)
- Copie a chave gerada (ex: `AIzaSy...`)

### Passo 3: Adicionar a chave ao projeto
- Abra o arquivo: `.streamlit/secrets.toml`
- Substitua `"sua-chave-api-aqui"` pela sua chave real:

```toml
GEMINI_API_KEY = "AIzaSy... (sua chave aqui)"
```

- **Salve o arquivo**
- **Reinicie a aplicação Streamlit** (Ctrl+C e execute novamente)

## 📋 Arquivo de configuração

O arquivo `.streamlit/secrets.toml` já foi criado no projeto com a seguinte estrutura:

```toml
GEMINI_API_KEY = "sua-chave-api-aqui"
```

## 🚀 Usando a análise de colorimetria

### Interface da Aplicação

1. **Câmera de Análise**: Veja seu rosto com a paleta de cores em tempo real
2. **Botão 📸 Capturar Foto**: Tira uma foto do frame atual da câmera
3. **Botão 🤖 Analisar com Gemini**: Envia a foto para análise (após capturada)
4. **Resultado**: Recebe análise detalhada incluindo:
   - Subtom da pele (quente, frio, neutro)
   - Profundidade da pele (claro, médio, profundo)
   - Contraste natural
   - Estação colorimétrica ideal (Primavera, Verão, Outono, Inverno)
   - Cores que realçam sua beleza
   - Cores a evitar
   - Recomendações práticas

## 📱 Compatibilidade

- ✅ Windows, macOS, Linux
- ✅ Navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ Requer câmera web ou dispositivo com câmera
- ✅ Conexão com internet (para Gemini API)

## ⚠️ Notas Importantes

1. **Segurança da chave**: A `GEMINI_API_KEY` no arquivo `secrets.toml` é privada e não deve ser compartilhada
2. **Limite de requisições**: Google oferece limite gratuito na API Generative AI
3. **Privacidade**: As fotos são enviadas para o servidor do Google Gemini durante a análise
4. **Uso local**: A aplicação roda localmente em seu computador (http://localhost:8502)

## 🛠️ Troubleshooting

### Erro: "Chave GEMINI_API_KEY não configurada em secrets.toml"
- Verifique se o arquivo `.streamlit/secrets.toml` existe
- Verifique se a chave foi inserida corretamente
- Reinicie a aplicação

### Erro: "Invalid API Key"
- A chave pode ter expirado
- Verifique se está correta no Google AI Studio
- Gere uma nova chave se necessário

### Câmera não funciona
- Verifique permissões de câmera no seu sistema
- Teste se a câmera funciona em outro aplicativo
- Recarregue a página do Streamlit

## 📚 Mais informações

- Documentação oficial: https://ai.google.dev/docs
- Modelos disponíveis: https://ai.google.dev/models
- Limites gratuitos: https://ai.google.dev/pricing

---

**Pronto!** Sua aplicação Chromalab está configurada e pronta para análise de colorimetria com IA! 🎨
