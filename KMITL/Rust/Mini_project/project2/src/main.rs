use crossterm::event::{read, Event, KeyCode};
use rand::Rng;
use std::io;
use crossterm::{execute, terminal::{Clear, ClearType}};
use std::io::{stdout,Write};

fn main() -> io::Result<()> {
    execute!(stdout(), Clear(ClearType::All)).unwrap();
    let mut choice = String::new();
    let mut money = 100; 
    println!("You start with {} money.", money);
    let begin = money;
    let mut bet = 0; 

    println!("(1) Purple x2 , (2) Green x14 , (3) Black x2 , (4) Special x7 , (9) Exit");
    loop {
        if money == 0 {
            println!("You ran out of money");
            break;
        }

        let event = read()?; 
        match event {
            Event::Key(event) => match event.code {
                KeyCode::Char('1') => choice = String::from("Purple"),
                KeyCode::Char('2') => choice = String::from("Green"),
                KeyCode::Char('3') => choice = String::from("Black"),
                KeyCode::Char('4') => choice = String::from("Special"),
                KeyCode::Char('9') => break,
                KeyCode::Enter => continue,
                _ => choice = String::from("None"),
            },
            _ => break,
        }

        if choice == "None" {
            println!("Invalid Input");
        } else {
            let mut check = false;
            while !check {
                bet = get_input("How much you wanna bet for: ").trim().parse::<i32>().unwrap();
                if money >= bet {
                    money -= bet;
                    check = true;
                } else {
                    println!("You don't have enough money. Please bet a smaller amount.");
                }
            }
            
            let mut result2 = String::new();
            let rng = rand::thread_rng().gen_range(1..=16);

            let (result, times, extra) = if rng == 9 {
                ("Green".to_string(), 14, 0)
            } else if rng == 16 {
                result2 = "Purple".to_string();
                ("Special".to_string(), 7, 2)
            } else if rng == 10 {
                result2 = "Black".to_string();
                ("Special".to_string(), 7, 2)
            } else if rng % 2 == 0 {
                ("Black".to_string(), 2, 0)
            } else {
                ("Purple".to_string(), 2, 0)
            };
            execute!(stdout(), Clear(ClearType::All)).unwrap();
            println!("It rolls {} {}", result, result2);

            let gain = if choice == result {
                bet * times
            } else if choice == result2 {
                bet * extra
            } else {
                0
            };

            if gain == 0 {
                println!("You lose the bet this time");
            } else {
                println!("You Won! you gain: {}", gain);
                money += gain;
            }

            println!();
            println!("Your balance is now: {}", money);
        }
        println!("(1) Purple x2 , (2) Green x14 , (3) Black x2 , (4) Special x7 , (9) Exit");

    }
    if money > begin {
        println!("You Have Made {} $ Profit!!!", money - begin);
    } else if money == begin {
        println!("You didn't gain or lose any money");
    } else {
        println!("You lost {} $", begin - money);
    }
    
    
    Ok(()) 
}

fn get_input(prompt: &str) -> String {
    let mut input = String::new();
    println!("{}", prompt);
    io::stdin().read_line(&mut input).expect("Failed to read line");
    input
}
