/* 
* @requires Vector3
* @requires Ray3
* @requires IntersectResult
*/

// 将geometries并在一起, 以方便与光线求离视点最近的交点
Union = function(geometries) { this.geometries = geometries; };

Union.prototype = {
    initialize: function() {
        for (var i in this.geometries)
            this.geometries[i].initialize();
    },
    
    // 并集物体和光线求交, 取出离视点最近的交点
    intersect: function(ray) {
        var minDistance = Infinity;
        var minResult = IntersectResult.noHit;
        for (var i in this.geometries) {
            var result = this.geometries[i].intersect(ray);
            if (result.geometry && result.distance < minDistance) {
                minDistance = result.distance;
                minResult = result;
            }
        }
        return minResult;
    }
};
