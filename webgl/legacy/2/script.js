//////////////////////////////////////////
// canvas对象的处理
//////////////////////////////////////////
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

    // 画面初始化的颜色设置
    gl.clearColor(0.0, 0.0, 0.0, 1.0);  
    // canvas初始化的深度
    gl.clearDepth(1.0);
    // canvas的初始化
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);  


    //////////////////////////////////////////
    // 着色器和程序相关对象的处理
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


    //////////////////////////////////////////
    // 模型数据
    //////////////////////////////////////////
    var vertex_position = [  
        // X,   Y,   Z  
         0.0, 1.0, 0.0,  
         1.0, 0.0, 0.0,  
        -1.0, 0.0, 0.0  
    ]; 

    var vertex_color = [
      // R,  G,  B,   A
        1.0, 0.0, 0.0, 1.0,  
        0.0, 1.0, 0.0, 1.0,  
        0.0, 0.0, 1.0, 1.0 
    ];

    //////////////////////////////////////////
    // VBO相关
    //////////////////////////////////////////

    // 生成vbo
    var position_vbo = create_vbo(vertex_position);
    var color_vbo = create_vbo(vertex_color);

    // 绑定vbo (位置vbo)
    gl.bindBuffer(gl.ARRAY_BUFFER, position_vbo);
    gl.enableVertexAttribArray(attLocation[0]);
    gl.vertexAttribPointer(attLocation[0], attStride[0], gl.FLOAT, false, 0, 0);

    // 绑定vbo (颜色vbo)
    gl.bindBuffer(gl.ARRAY_BUFFER, color_vbo);
    gl.enableVertexAttribArray(attLocation[1]);
    gl.vertexAttribPointer(attLocation[1], attStride[1], gl.FLOAT, false, 0, 0);

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

    //////////////////////////////////////////
    // 模型数据的矩阵变换
    //////////////////////////////////////////

    // create matIV obj
    var m = new matIV();

    var mMatrix = m.identity(m.create());   // 模型变换矩阵
    var vMatrix = m.identity(m.create());   // 视图变换矩阵
    var pMatrix = m.identity(m.create());   // 投影变换矩阵
    var mvpMatrix = m.identity(m.create()); // 最终的坐标变换矩阵

    // 视图变换坐标矩阵
    m.lookAt([0.0, 1.0, 3.0], [0, 0, 0], [0, 1, 0], vMatrix);
    // 投影坐标变换矩阵
    m.perspective(90, c.width / c.height, 0.1, 100, pMatrix);

    // P*v*m 得到mvpMatrix.
    m.multiply(pMatrix, vMatrix, mvpMatrix);
    m.multiply(mvpMatrix, mMatrix, mvpMatrix);

    // uniformLocation的获取  
    var uniLocation = gl.getUniformLocation(prg, 'mvpMatrix');  

    // 向uniformLocation中传入坐标变换矩阵  
    gl.uniformMatrix4fv(uniLocation, false, mvpMatrix);

    //////////////////////////////////////////
    // 绘制模型并刷新到画面上
    //////////////////////////////////////////
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.flush();
};