const express = require('express');
const app = express();

app.listen(3000, '0.0.0.0', ()=>{
    console.log('Application listening at 0.0.0.0:3000');
})

app.get('/', (req, res)=>{
    res.send('Sample Applicaton: Hello World!');
})

const hobbies = [
    'Swimming', 'Diving', 'Jogging', 'Cooking', 'Singing'
];

app.get('/hobbies', (req, res)=>{
    res.send(hobbies);
})

app.get('/status', (req, res)=>{
    res.send('OK');
})

app.get('/colors', (req, res)=>{
    res.send(['red', 'green', 'blue']);
})