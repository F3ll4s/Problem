use crossterm::event::{read, Event, KeyCode};
use rand::Rng;
use std::io;
use std::io::Write; // Needed for flushing stdout
use std::time::Duration;
use std::thread::sleep;

fn main() -> io::Result<()> {
    let mut choice = String::new();
    let mut money = 100;
    println!("You start with {} money.", money);
    let begin = money;
    let mut bet = 0;

    loop {
        print_menu();
        if money == 0 {
            println!("You ran out of money");
            break;
        }

        // Event loop to wait for a valid key press
        loop {
            let event = read()?;
            if let Event::Key(event) = event {
                match event.code {
                    KeyCode::Char('1') => {
                        choice = String::from("Purple");
                        break;
                    }
                    KeyCode::Char('2') => {
                        choice = String::from("Green");
                        break;
                    }
                    KeyCode::Char('3') => {
                        choice = String::from("Black");
                        break;
                    }
                    KeyCode::Char('4') => {
                        choice = String::from("Special");
                        break;
                    }
                    KeyCode::Char('9') => return Ok(()),
                    _ => {
                        println!("Invalid Input");
                        sleep(Duration::from_millis(500));
                        // Reprint the menu immediately after invalid input
                        print_menu();
                        continue;
                    }
                }
            }
        }

        let mut check = false;
        while !check {
            bet = get_input("How much you wanna bet for: ")
                .trim()
                .parse::<i32>()
                .unwrap();
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

    if money > begin {
        println!("You Have Made {} $ Profit!!!", money - begin);
    } else if money == begin {
        println!("You didn't gain or lose any money");
    } else {
        println!("You lost {} $", begin - money);
    }

    Ok(())
}

fn print_menu() {
    println!("(1) Purple x2 , (2) Green x14 , (3) Black x2 , (4) Special x7 , (9) Exit");
    // Flush stdout to ensure the menu is displayed immediately
    io::stdout().flush().unwrap();
}

fn get_input(prompt: &str) -> String {
    let mut input = String::new();
    println!("{}", prompt);
    io::stdin().read_line(&mut input).expect("Failed to read line");
    input
}
