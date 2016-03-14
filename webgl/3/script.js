// 最简单的程序.
onload = function() {
    //////////////////////////////////////////
    // 初始化
    //////////////////////////////////////////

    // 从canvas初始化webgl
    var gl = getWebGLContext('canvas');

    // 设定清除颜色并用此颜色清空画面
    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);

    // 载入, 编译shader
    var v_shader = create_shader('vs');
    var f_shader = create_shader('fs');
    var prg = create_program(v_shader, f_shader);

    //////////////////////////////////////////
    // playground!
    //////////////////////////////////////////
    var vertices = new Float32Array([
        0.0, 0.5,
        -0.5, -0.5,
        0.5, -0.5
        ]);

    // 创建一个缓冲区, 然后绑定
    var vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

    // 获取shader program中, 变量a_Position的位置.
    var a_Position = gl.getAttribLocation(prg, 'a_Position');
    // 给这个地址指针写入数据,注意每个数据的分量值是2.
    gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, 0, 0);
    // 开启这个attrib
    gl.enableVertexAttribArray(a_Position);

    // 画!
    gl.drawArrays(gl.POINTS, 0, 3);


/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////


    // 初始化WebGL环境. 参数canvas是html中canvas的id, 函数返回一个gl对象.
    function getWebGLContext(canvas) {
        var c = document.getElementById(canvas);
        c.width = 300;
        c.height = 300;

        // get webgl context from canvas obj
        return c.getContext("webgl") || c.getContext("experimental-wegbl") || c.getContext("webkit-3d") || c.getContext("moz-webgl")
    }

    // 从html id中获取着色器代码并编译然后返回.
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

    // 创建shader的program并返回.
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

};