fn main() {
    let args: Vec<_> = std::env::args().collect();
    if (args.len()-1) == 3  {
        println!("Arguments provided {} {} {}", args[1] , args[2] ,args[3]);
    }else{
        println!("Missing Arguments");
        std::process::exit(2);
    }

    let num1:i32 = args[1].parse().expect("Not an integer");
    let num2:i32 = args[3].parse().expect("Not an integer");
    let operator: &str = &args[2].clone();
    match operator{
        "+" =>{
            let total = num1 + num2;
            println!("Total = {}", total);
        }
        "-" =>{
            let total = num1 - num2;
            println!("Total = {}",total);
        }
        "*" => {
            let total = num1 * num2;
            println!("Total = {}",total)
        }
        "/" =>{
            if num2 == 0{
                std::process::exit(2);
            }else{
                let total = num1 / num2;
                println!("Total = {}",total)
            }
        }
        _ =>{
            println!("Error Operators");
        }
    }
}