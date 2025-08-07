// servidor.js
import express from 'express';
import cors from 'cors';

const app = express();
app.use(cors());
app.use(express.json());

app.post('/pergunta', async (req, res) => {
    const { pergunta } = req.body;

    if (!pergunta) {
        return res.json({ erro: "Pergunta não recebida" });
    }

    try {
        const resposta = await fetch('http://127.0.0.1:5000/responder', {
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
