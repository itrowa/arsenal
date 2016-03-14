onload = function() {
    //////////////////////////////////////////
    // canvas object 的获取和画面的初始化
    //////////////////////////////////////////

    // get canvas object
    var c = document.getElementById('canvas');
    c.width = 300;
    c.height = 300;

    // get webgl context from canvas obj
    var gl = c.getContext("webgl") || c.getContext("experimental-wegbl") || c.getContext("webkit-3d") || c.getContext("moz-webgl")

    //////////////////////////////////////////
    // vertex shader & fragment shader相关
    //////////////////////////////////////////
    var v_shader = create_shader('vs');
    var f_shader = create_shader('fs');
    
    var prg = create_program(v_shader, f_shader);
    
    var attLocation = new Array(2);
    attLocation[0] = gl.getAttribLocation(prg, 'position');
    attLocation[1] = gl.getAttribLocation(prg, 'color');
    
    var attStride = new Array(2);
    attStride[0] = 3;
    attStride[1] = 4;

    //////////////////////////////////////////
    // 矩阵变换处理
    //////////////////////////////////////////

    // 生成一个MinMatrix对象
    var m = new matIV();

    var mMatrix = m.identity(m.create());   // 模型变换矩阵
    var vMatrix = m.identity(m.create());   // 视图变换矩阵
    var pMatrix = m.identity(m.create());   // 投影变换矩阵
    var tmpMatrix = m.identity(m.create());   // 临时用矩阵
    var mvpMatrix = m.identity(m.create()); // 最终的坐标变换矩阵

    // 计算视图变换坐标矩阵
    m.lookAt([0.0, 1.0, 3.0], [0, 0, 0], [0, 1, 0], vMatrix);
    // 计算投影坐标变换矩阵
    m.perspective(90, c.width / c.height, 0.1, 100, pMatrix);
    // 事先把p*v的结果放到临时矩阵中
    m.multiply(pMatrix, vMatrix, tmpMatrix);

    //////////////////////////////////////////
    // 模型数据
    //////////////////////////////////////////
    var position = [
         0.0, 1.0, 0.0,
         1.0, 0.0, 0.0,
        -1.0, 0.0, 0.0
    ];
    var color = [
        1.0, 0.0, 0.0, 1.0,
        0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 1.0, 1.0
    ];

    //////////////////////////////////////////
    // VBO相关
    //////////////////////////////////////////
    var pos_vbo = create_vbo(position);
    var col_vbo = create_vbo(color);
    set_attribute([pos_vbo, col_vbo], attLocation, attStride);   
    var uniLocation = gl.getUniformLocation(prg, 'mvpMatrix');


    // 主循环计数器
    var count = 0;

    // 主循环
    (function(){

        //////////////////////////////////////////
        // canvas对象的处理
        //////////////////////////////////////////
        gl.clearColor(0.0, 0.0, 0.0, 1.0);  
        gl.clearDepth(1.0);  
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);  

        count++;
        
        // 从计数器计算出当前的角度
        var rad = (count % 360) * Math.PI / 180;

        // model 1: 按照一个圆形轨道进行旋转
        var x = Math.cos(rad);
        var y = Math.sin(rad);
        m.identity(mMatrix);
        m.translate(mMatrix, [x, y + 1.0, 0,0], mMatrix);

        m.multiply(tmpMatrix, mMatrix, mvpMatrix);  
        gl.uniformMatrix4fv(uniLocation, false, mvpMatrix);  
        gl.drawArrays(gl.TRIANGLES, 0, 3);  

        // 模型2沿Y轴进行旋转  
        m.identity(mMatrix);  
        m.translate(mMatrix, [1.0, -1.0, 0.0], mMatrix);  
        m.rotate(mMatrix, rad, [0, 1, 0], mMatrix);  
          
        m.multiply(tmpMatrix, mMatrix, mvpMatrix);  
        gl.uniformMatrix4fv(uniLocation, false, mvpMatrix);  
        gl.drawArrays(gl.TRIANGLES, 0, 3);  

        // 模型3进行放大缩小  
        var s = Math.sin(rad) + 1.0;  
        m.identity(mMatrix);  
        m.translate(mMatrix, [-1.0, -1.0, 0.0], mMatrix);  
        m.scale(mMatrix, [s, s, 0.0], mMatrix)  
          
        m.multiply(tmpMatrix, mMatrix, mvpMatrix);  
        gl.uniformMatrix4fv(uniLocation, false, mvpMatrix);  
        gl.drawArrays(gl.TRIANGLES, 0, 3);  

        // refresh context
        gl.flush();

        // 递归调用自己, 以实现无限循环
        setTimeout(arguments.callee, 1000 / 30);
    }) ();

    // 从html标签中获取着色器代码并编译然后返回.
    function create_shader(id){
        // 着色器
        var shader;

        // 根据id获取script标签
        var scriptElement = document.getElementById(id);
        // 如果指定的script标签不存在则返回
        if (!scriptElement) {
            return;
        }
        // 判断script标签的属性
        switch(scriptElement.type) {
            // 如果是顶点着色器
            case 'x-shader/x-vertex':
                shader = gl.createShader(gl.VERTEX_SHADER);
                break;
            // 如果是片段着色器
            case 'x-shader/x-fragment':
                shader = gl.createShader(gl.FRAGMENT_SHADER);
                break;
            default:
                return;
        }

        // 将html标签中的代码分配给生成的着色器
        gl.shaderSource(shader, scriptElement.text);
        // 编译着色器
        gl.compileShader(shader);
        // 判断是否编译成功
        if (gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
            return shader;
        }
            else {
                alert(gl.getShaderInfoLog(shader));
            }
    }

    function create_program(vs, fs) {
        var program = gl.createProgram();

        // 向程序对象里分配着色器
        gl.attachShader(program, vs);
        gl.attachShader(program, fs);

        // 连接
        gl.linkProgram(program);

        // 判断是否连接成功?
        if (gl.getProgramParameter(program, gl.LINK_STATUS)) {
            // 如果成功 将程序对象设置为有效
            gl.useProgram(program);
            return program;
        }
        else {
            alert(gl.getProgramInfoLog(program));
        }
    }

    function create_vbo(data) {
        // 生成缓存对象
        var vbo = gl.createBuffer();

        // 绑定缓存
        gl.bindBuffer(gl.ARRAY_BUFFER, vbo);

        // 向缓存中写入数据
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(data), gl.STATIC_DRAW);

        // 将缓存设置为无效
        gl.bindBuffer(gl.ARRAY_BUFFER, null);

        // 返回生成的vbo
        return vbo;
    }

    // 从vbo(一个数组)绑定到缓存 
    function set_attribute(vbo, attL, attS) {
        for (var i in vbo) {
            // 1. 绑定缓存
            // 2. 将attributeLocation设置为有效
            // 3. 通知并添加attributeLocation  
            gl.bindBuffer(gl.ARRAY_BUFFER, vbo[i]);
            gl.enableVertexAttribArray(attL[i]);
            gl.vertexAttribPointer(attL[i], attS[i], gl.FLOAT, false, 0, 0);
        }
    }
};