/* 
 * @requires Vector3
 */

// 定义相机 eye: 视点坐标; front: 正前方向; refup: 正上方
PerspectiveCamera = function(eye, front, up, fov) { this.eye = eye; this.front = front; this.refUp = up; this.fov = fov; };

PerspectiveCamera.prototype = {
    initialize : function() {
        this.right = this.front.cross(this.refUp);
        this.up = this.right.cross(this.front);
        this.fovScale = Math.tan(this.fov * 0.5 * Math.PI / 180) * 2;
    },

    // 从视点生成一道过影像平面的采样座标(x, y)的光线.
    generateRay : function(x, y) {
        var r = this.right.multiply((x - 0.5) * this.fovScale);
        var u = this.up.multiply((y - 0.5) * this.fovScale);
        return new Ray3(this.eye, this.front.add(r).add(u).normalize());
    }
};
