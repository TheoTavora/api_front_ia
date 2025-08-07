// servidor.js
import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';

// configurações de caminho
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

app.use(express.static(path.join(__dirname, 'public')));

app.post('/pergunta', async (req, res) => {
    const { pergunta } = req.body;

    if (!pergunta) {
        return res.json({ erro: "Pergunta não recebida" });
    }

    try {
        const resposta = await fetch('https://chatbotmovese-v1.onrender.com/responder', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pergunta })
        });

        const dados = await resposta.json();
        res.json(dados);
    } catch (err) {
        res.status(500).json({ erro: "Erro ao comunicar com o servidor Python", detalhe: err.message });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor Node rodando em http://localhost:${PORT}`);
});
