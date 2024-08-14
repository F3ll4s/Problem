

fn fact(x:i32) -> i32{
    println!("Calculating factorial ({})", x);
    println!("Value {}, Memory Address {:p}", x, &x);
    if x == 0{
        return 1;
    }else{
        return  x*fact(x-1);
    }
}

fn main(){
    let x = 5;
    println!("Factorial result: {}", fact(x));
}


