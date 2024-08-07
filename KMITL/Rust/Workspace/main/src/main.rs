use std::io;
use rand::Rng;

fn main(){
    println!("Guess the Number: ");
    let mut guess = String::new();
    let random = rand::thread_rng().gen_range(0..=101);
    let mut min = 0;
    let mut max = 100;
    loop{
    guess.clear();
    io::stdin().read_line(&mut guess).expect("Failed to read");
    let guess:i32 = match guess.trim().parse(){
        Ok(num) => num,
        Err(_) =>{
            println!("Enter the Number");
            0
        }
    };
        if guess > random{
            max = guess;
            println!("{} <???> {}", min , max);
        }else if guess < random{
            min = guess;
            println!("{} <???> {}", min , max);
        }else{
            println!("You win");
            break;
        }
    }
}