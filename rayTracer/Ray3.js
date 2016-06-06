/* 
 * @requires Vector3
 * @requires Color
 */

// 摄像机需要起点座标和方向向量.
Ray3 = function(origin, direction) { this.origin = origin; this.direction = direction; }

Ray3.prototype = {
    // 直线在参数t上的求值得一个座标.
    getPoint : function(t) { return this.origin.add(this.direction.multiply(t)); }
};
