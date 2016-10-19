// node.js 调用python文件
var exec = require('child_process').exec;
var arg1 = 'hello';
var arg2 = 'hh';

// 执行的文件默认是在同一个目录.
exec('python test.py' + ' ' + arg1 + ' ' + arg2 + ' ', function(error, stdout, stderr) {
	if(error) {
		console.log('ERROR EXEC PYTHON: ' + stderr);
	}
	console.log(stdout); // 回调函数用于捕获python返回的结果（捕获的是标准输出流）
})