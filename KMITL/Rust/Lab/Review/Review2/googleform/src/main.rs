// use std::io;
// struct Book{
//     title:String,
//     author:String,
//     published_year:Option<u32>,
// }

// fn main() {
//     let mut input = String::new();
//     io::stdin().read_line(&mut input).expect("");
//     let input = input.trim().to_string();
//     let book = Book{
//         title: input,
//         author:String::from("nigga"),
//         published_year: Some(190),
//     };
//     match book.published_year {
//         Some(year) => println!("{} was published in {}", book.title, year),
//         None => println!("{} has no publication year", book.title),
//     }
// }

// struct Circle{
//     radius:f64,
// }

// impl Circle{
//     fn new(n:f64)-> Self{
//         Circle{
//             radius: n,
//         }
//     }
// }
// fn main() {
//     let circle = Circle::new(10.0);
//     println!("Circle with radius: {}", circle.radius);
// }

// fn fibo(number:i32) -> i32{
//     if number == 0 || number == 1{
//         return 1
//     }
//     fibo(number -1) + fibo(number-2)
// }

// fn main(){
//     let number = fibo(5);
//     println!("{}",number);
// }
fn main() {
    let s = String::from("Hello, World!");
    let result = get_substring(&s, 7, 12);
    println!("{}", result); // World
}

fn get_substring(text:&str,a:usize,b:usize)->String{
    text[a-1..b].to_string()
}