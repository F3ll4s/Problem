use std::mem;

struct Point{
    x:i32,
    y:i32
}
struct Circle{
    center:Point,
    radius:f32
}

struct Rectangle{
    topleft:Point,
    bottomright:Point
}

enum Shape{
    Circle{center:Point,radius:f32},
    Rectangle{topleft:Point,bottomright:Point}
}

fn main() {
    println!("Size of Point {}",mem::size_of::<Point>());
    println!("Size of Circle {}",mem::size_of::<Circle>());
    println!("Size of Rectangle {}",mem::size_of::<Rectangle>());
    println!("Size of Shape {}",mem::size_of::<Shape>());
}
