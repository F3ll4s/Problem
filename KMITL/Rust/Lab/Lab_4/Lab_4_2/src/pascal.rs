use std::io;
fn pascal(i:i32,j:i32)->i32{
    if j == 0{
        return 1;
    }
    if i == j{
        return 1;
    }else{
        return pascal(i-1,j-1) + pascal(i-1,j);
    }
}
// fn print_pascal_row
fn main(){
let n: i32 = loop{
    println!("Enter number between 1 and 9:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Invalid Number");
    match input.trim().parse(){
        Ok(num) if(1..=9).contains(&num) => break num,
        _ => print!("Please enter a valid number between 1 and 9"),}
    };
    for i in 0..n{
        for j in 0..(n-i)*2{
            print!(" ");
        }
        for j in 0..(i+1){
            print!("{:<4}",pascal(i,j));
        }
        println!("");
    }
}
