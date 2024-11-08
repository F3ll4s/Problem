fn main() {
    let args: Vec<_> = std::env::args().collect();
    println!("{}",args.len());
    if (args.len()-1) == 3  {
        println!("Arguments provided {} {} {}", args[1] , args[2] ,args[3]);
    }else{
        println!("Error: Exactly 3 arguments are required. You provided {}",(args.len()-1))
    }
}