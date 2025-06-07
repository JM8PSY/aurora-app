const express = require('express');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
const PORT = 3000;
const API_BASE = process.env.API_BASE || 'http://localhost:8000';

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.use(express.static('public'));

app.get('/', async (req, res) => {
  try {
    const response = await fetch(`${API_BASE}/api/k-index`);
    const kIndex = await response.json();
    res.render('index', { kIndex });
  } catch (err) {
    console.error(err);
    res.render('index', { kIndex: null });
  }
});

app.listen(PORT, () => {
  console.log(`Express frontend running at http://localhost:${PORT}`);
});
