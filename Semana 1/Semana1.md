# Projeto: Sistema Imersivo de Colorimetria por Filtro ao Vivo

## 1. Área e Tema do Projeto

**Área:** Estética, Tecnologia Interativa
**Tema:** Colorimetria de pele com filtro de realidade aumentada para análises e simulações de paletas em tempo real.

**Justificativa:**
Ferramentas tradicionais de colorimetria digital baseiam-se em envio de fotos ou imagens estáticas, o que gera erros por iluminação ou ângulo. Soluções mais modernas utilizam filtros em tempo real, que capturam a cor da pele diretamente pela câmera, aplicam paletas sobre o rosto e permitem testar combinações instantaneamente.
Este MVP visa proporcionar uma experiência imersiva e interativa, acessível via navegador.

## 2. Estado da Arte

### 2.1 Projetos analisados

* Filtros de redes sociais (Instagram, TikTok)
* Apps de AR Beauty (ex.: YouCam Real-Time)
* Ferramentas de análise de pele com AR básica

**Aspectos aproveitáveis:**

* Visualização em tempo real
* Mapeamento facial simples com bibliotecas prontas (ex.: MediaPipe, AR.js)
* Interatividade baseada em troca de paletas instantaneamente

### 2.2 Fragilidades e oportunidades

* Sistemas profissionais exigem hardware avançado
* Apps populares usam filtros estéticos, não educativos
* Poucas soluções mostram como a paleta afeta o contraste com a pele
* Há oportunidade de unir filtro ao vivo + educação sobre subtom

## 3. Ações e Verbos Envolvidos

**Verbros abstratos:**

* reconhecer
* analisar
* experimentar

**Ações práticas:**

* ativar câmera
* detectar rosto
* identificar subtom
* aplicar paleta
* alternar paletas em tempo real

**Verbros principais:**

* capturar
* analisar
* visualizar
* experimentar

## 4. Requisitos Funcionais e Não Funcionais (Versão AR – Filtro ao Vivo)

Todos os requisitos foram atualizados para o novo formato de experiência imersiva.

### 4.1 Requisitos Funcionais

## RF01 – Ativar Câmera e Captura em Tempo Real

| Campo              | Descrição                                                                    |
| ------------------ | ---------------------------------------------------------------------------- |
| Código             | RF01                                                                         |
| Título             | Ativação do modo câmera ao vivo                                              |
| Descrição          | Permitir que o usuário ative a câmera para iniciar o filtro de colorimetria. |
| Entradas           | Fluxo de vídeo da câmera.                                                    |
| Origem             | Dispositivo do usuário.                                                      |
| Lançamentos        | Vídeo ao vivo exibido na tela.                                               |
| Destino            | Interface do sistema.                                                        |
| Ação               | Solicitar permissão de acesso à câmera e iniciar captura contínua.           |
| Pré-condição       | Usuário deve conceder permissão de câmera.                                   |
| Pós-condição       | Câmera ativa e imagem exibida.                                               |
| Efeitos colaterais | Uso de bateria e processamento.                                              |

## RF02 – Detecção de Rosto em Tempo Real

| Campo              | Descrição                                                                        |
| ------------------ | -------------------------------------------------------------------------------- |
| Código             | RF02                                                                             |
| Título             | Reconhecimento facial para área de análise                                       |
| Descrição          | Detectar o rosto do usuário no vídeo ao vivo para aplicar o filtro corretamente. |
| Entradas           | Frames de vídeo.                                                                 |
| Origem             | Câmera.                                                                          |
| Lançamentos        | Coordenadas do rosto (regiões faciais).                                          |
| Destino            | Módulo de análise.                                                               |
| Ação               | Executar modelo de detecção facial (ex.: MediaPipe FaceMesh).                    |
| Pré-condição       | Câmera ativa.                                                                    |
| Pós-condição       | Região do rosto mapeada.                                                         |
| Efeitos colaterais | Pequena latência dependendo do dispositivo.                                      |

## RF03 – Análise de Subtom em Tempo Real

| Campo              | Descrição                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| Código             | RF03                                                                                                |
| Título             | Classificação rápida do subtom                                                                      |
| Descrição          | Identificar o subtom da pele analisando pixels do rosto durante o vídeo ao vivo.                    |
| Entradas           | Pixels capturados do rosto.                                                                         |
| Origem             | Frames do vídeo.                                                                                    |
| Lançamentos        | Subtom classificado: quente, frio, neutro.                                                          |
| Destino            | Interface e módulo de paletas.                                                                      |
| Ação               | Calcular valores médios de cor (RGB/HSV), aplicar regras simples e atualizar subtom constantemente. |
| Pré-condição       | Rosto detectado pelo RF02.                                                                          |
| Pós-condição       | Subtom atualizado periodicamente.                                                                   |
| Efeitos colaterais | Variações devido à iluminação ambiente.                                                             |

## RF04 – Aplicação de Paletas em Tempo Real no Filtro

| Campo              | Descrição                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Código             | RF04                                                                                                             |
| Título             | Aplicar paletas ao rosto ao vivo                                                                                 |
| Descrição          | Sobrepor no vídeo ao vivo uma paleta de cores harmonizada com o subtom identificado.                             |
| Entradas           | Paleta selecionada pelo usuário.                                                                                 |
| Origem             | Biblioteca interna de paletas.                                                                                   |
| Lançamentos        | Filtro com paleta ajustada aplicado no rosto.                                                                    |
| Destino            | Tela do usuário.                                                                                                 |
| Ação               | Aplicar máscara colorida suave sobre áreas de interesse (ex.: plano de fundo, contorno facial ou barra lateral). |
| Pré-condição       | Subtom identificado.                                                                                             |
| Pós-condição       | Filtro aplicado em tempo real.                                                                                   |
| Efeitos colaterais | Leve perda de FPS dependendo do hardware.                                                                        |

## RF05 – Troca Manual de Paletas em Tempo Real

| Campo              | Descrição                                                                          |
| ------------------ | ---------------------------------------------------------------------------------- |
| Código             | RF05                                                                               |
| Título             | Alternância de paletas durante o uso do filtro                                     |
| Descrição          | O usuário pode trocar entre diferentes paletas e ver o resultado instantaneamente. |
| Entradas           | Seleção da paleta.                                                                 |
| Origem             | Interação do usuário.                                                              |
| Lançamentos        | Atualização imediata do filtro.                                                    |
| Destino            | Vídeo ao vivo com nova paleta.                                                     |
| Ação               | Reprocessar o filtro usando a nova paleta escolhida.                               |
| Pré-condição       | RF01–RF04 funcionando.                                                             |
| Pós-condição       | Nova paleta refletida no filtro.                                                   |
| Efeitos colaterais | Nenhum.                                                                            |

## RF06 – Explicação Didática do Resultado

| Campo              | Descrição                                                                           |
| ------------------ | ----------------------------------------------------------------------------------- |
| Código             | RF06                                                                                |
| Título             | Explicação do subtom e das paletas                                                  |
| Descrição          | Exibir textos simples explicando o subtom e por que determinadas paletas funcionam. |
| Entradas           | Subtom detectado.                                                                   |
| Origem             | Base interna de textos.                                                             |
| Lançamentos        | Texto exibido em painel lateral.                                                    |
| Destino            | Interface do usuário.                                                               |
| Ação               | Carregar explicações pré-definidas por subtom.                                      |
| Pré-condição       | Subtom disponível.                                                                  |
| Pós-condição       | Usuário compreende o resultado.                                                     |
| Efeitos colaterais | Nenhum.                                                                             |

### 4.2 Requisitos Não Funcionais

## RNF01 – Usabilidade

Interface objetiva, com botões grandes e fluxo linear: ativar câmera, visualizar filtro, trocar paleta.

## RNF02 – Desempenho

A taxa mínima deve ser de 20 FPS para manter fluidez básica do filtro.

## RNF03 – Compatibilidade

Compatível com navegadores modernos que suportam WebRTC e WebGL.

## RNF04 – Segurança e Privacidade

Nenhum frame deve ser armazenado. Todo processamento ocorre localmente no dispositivo.

## RNF05 – Estabilidade

O sistema deve se recuperar automaticamente caso a câmera seja desligada ou bloqueada.

## 5. Funções e Tarefas do Projeto (Escopo Real para 4 Semanas)

O cronograma foi ajustado para incluir o filtro e análise em tempo real.

### 5.1 Cronograma de 4 Semanas (MVP com AR)

## Semana 1 – Pesquisa, Planejamento e Prototipação

* Estudo das técnicas de detecção facial simples (MediaPipe).
* Escolha da abordagem de AR (Webcam + Canvas).
* Definição das paletas para os três subtons.
* Criação dos textos explicativos.
* Desenho dos wireframes.

## Semana 2 – Implementação da Base do Filtro

* Ativação da câmera via WebRTC.
* Renderização do vídeo no canvas.
* Implementação da detecção facial.
* Criação das máscaras faciais simples.

## Semana 3 – Lógica de Análise e Aplicação de Paletas

* Implementação da leitura de pixels da área da pele.
* Classificação básica do subtom (regras simples).
* Aplicação da paleta escolhida ao filtro ao vivo.
* Função para alternar paletas manualmente.

## Semana 4 – Ajustes, Testes e Documentação Final

* Testes em diferentes iluminações.
* Ajustes de performance e fluidez.
* Correções de interface e mensagens.
* Revisão dos requisitos.
* Preparação da entrega final e apresentação.
