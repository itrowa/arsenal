/* 
 * @requires Vector3, Ray3
 */

// 球体由中心点座标和半径定义.
Sphere = function(center, radius) { this.center = center; this.radius = radius; };

Sphere.prototype = {
    copy : function() { return new Sphere(this.center.copy(), this.radius.copy()); },

    initialize : function() {
        this.sqrRadius = this.radius * this.radius;
    },

    // 光线和球体求交点.
    intersect : function(ray) {
        var v = ray.origin.subtract(this.center);
        var a0 = v.sqrLength() - this.sqrRadius;
        var DdotV = ray.direction.dot(v);

        if (DdotV <= 0) {
            var discr = DdotV * DdotV - a0;
            if (discr >= 0) {
                var result = new IntersectResult();
                result.geometry = this;
                result.distance = -DdotV - Math.sqrt(discr);
                result.position = ray.getPoint(result.distance);
                result.normal = result.position.subtract(this.center).normalize();
                return result;
            }
        }

        return IntersectResult.noHit;
    }
};
