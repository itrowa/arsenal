#include <math.h>

/* 复数的表达 */

enum coordinate_type {RECTANGULAR, POLAR};
struct complex_struct
{
	enum coordinate_type t;					// 用于指定此结构体是直角坐标表示还是极坐标表示。
	double a, b;	
};

double real_part(struct complex_struct z) {
	if z.coordinate_type == RECTANGULAR 
		return z.x;
	else
		return ....
}

double img_part(struct complex_struct z) {
	return z.y;
}

double magnitude(struct complex_struct z){
	/* 从复数的直角坐标表达取出大小。 */
	return sqrt(z.x*z.x + z.y*z.y);
}

double angle(struct complex_struct z){
	/* 从负数的直角坐标表达取出*/
	return atan2(z.y, z.x);
}

struct complex_struct make_from_real_img(double x, double y){
	/* 从实部和虚部构造复数*/
	struct complex_struct z;
	z.x = x;
	z.y = y;
	return z;
}

struct complex_struct make_from_mag_ang(double r, double a){
	/* 从极径和极角构造复数*/
	struct complex_struct z;
	z.x = r*cos(a);
	z.y = r*sin(a);
	return z;
}

/*               */

struct complex_struct add_complex(struct complex_struct z1,
								  struct complex_struct z2)
{
	return make_from_real_img(real_part(z1) + real_part(z2),
								img_part(z1) + img_part(z2));
}

int main(void){
	struct complex_struct
	{
		double x, y;	
	} z1, z2;
}