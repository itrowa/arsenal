/* 最简单的物联网服务端. */

var express = require('express');
var app = express();

var Database = require('./db');
var db = new Database();

app.get('/api', function(req, res) {
	res.send({led: false});
});


app.post('/api', function (req, res) {
	data.method = 'post';
	if (req.body.led === true) {
		data.led = true;
	}
	else if (req.body.led === false) {
		data.led = false;
	}
	res.send(data);
});

app.put('/api', function (req, res) {
	var data = {led: false};
	if (req.body.led === true) {
		data.led = true;
	}
	db.insert(data);
	res.send({db: "insert"});
});

app.delete('/api', function (req, res) {
	res.send({led: false})
})

app.listen(8080);