const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const DB_FILE = path.join(__dirname, 'db.json');

app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// Asegurar que exista la "base de datos"
if (!fs.existsSync(DB_FILE)) {
    fs.writeFileSync(DB_FILE, JSON.stringify([]));
}

// Endpoint para que los estudiantes guarden sus respuestas
app.post('/api/submit', (req, res) => {
    const data = req.body;
    
    // Leer respuestas actuales
    const currentData = JSON.parse(fs.readFileSync(DB_FILE, 'utf-8'));
    
    // Añadir timestamp
    data.timestamp = new Date().toISOString();
    
    // Guardar
    currentData.push(data);
    fs.writeFileSync(DB_FILE, JSON.stringify(currentData, null, 2));
    
    res.json({ success: true, message: 'Respuestas guardadas correctamente.' });
});

// Endpoint privado para la Profesora (Admin)
app.get('/api/responses', (req, res) => {
    const pwd = req.query.pwd;
    
    // Una contraseña sencilla para que ella acceda
    if (pwd !== 'superprofe') {
        return res.status(401).json({ error: 'Contraseña incorrecta' });
    }
    
    const currentData = JSON.parse(fs.readFileSync(DB_FILE, 'utf-8'));
    res.json(currentData);
});

// Rutas amigables
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'class-prep-workplace.html'));
});

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin.html'));
});

app.listen(PORT, () => {
    console.log(`\n==============================================`);
    console.log(`🚀 SERVIDOR LISTO!`);
    console.log(`==============================================`);
    console.log(`VISTA ESTUDIANTES: http://localhost:${PORT}/`);
    console.log(`VISTA PROFESORA:   http://localhost:${PORT}/admin`);
    console.log(`==============================================\n`);
});
