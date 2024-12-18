use std::fs::{self, File};
use std::io::{self, BufRead, Write};
use std::path::Path;
use std::process::exit;

fn main() {
    let mut file_name: Option<String> = None;  // Use Option to track if a file is open
    let mut file_content: Vec<String> = Vec::new();
    loop{

        println!("User Input: ");
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");
        let choice = choice.trim();
        let choice_2 = choice.split_once(" ");
        let first:&str;
        let mut second = String::new();

        match choice_2{
            Some(x) => {
                first = choice_2.unwrap().0;
                second = choice_2.unwrap().1.to_string();
            }None => {
                first = choice
            }

        }
        match first {
            "open" => {
                let name = second.to_string();
                file_name = open_file(&mut file_content,name);  // Update file_name
            }
            "display" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    display_content(&file_content);
                }
            }
            "add" => {
                let name = second.to_string();
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    add_line(&mut file_content,name);
                }
            }
            "delete" => {
                let name = second.to_string();
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    delete_line(&mut file_content,name);
                }
            }
            "write" => {
                if let Some(ref file) = file_name {
                    write_file(file, &file_content);
                } else {
                    println!("No file open. Please open a file first.");
                }
            }
            "exit" => {
                println!("Exiting...");
                exit(0);
            }
            _ => {
                println!("Invalid choice. Please select an option from the menu.");
            }
        }
    }
}
fn open_file(file_content: &mut Vec<String>,name:String) -> Option<String> {

    if Path::new(&name).exists() {
        let file = File::open(&name).expect("Unable to open file");
        let reader = io::BufReader::new(file);
        file_content.clear();
        for line in reader.lines() {
            file_content.push(line.expect("Unable to read line"));
        }
        println!("File opened successfully.");
        Some(name)  // Return the file name
    } else {
        println!("File does not exist. Do you want to create a new file? (y/n)");
        let mut create_new = String::new();
        io::stdin().read_line(&mut create_new).expect("Failed to read line");
        if create_new.trim().eq_ignore_ascii_case("y") {
            file_content.clear();
            println!("New file created. You can now add lines and save the file.");
            Some(name)  // Return the new file name
        } else {
            println!("File not opened.");
            None  // No file name, return None
        }
    }
}

fn display_content(file_content: &[String]) {
    if file_content.is_empty() {
        println!("File is empty.");
    } else {
        println!("File content:");
        for (index, line) in file_content.iter().enumerate() {
            println!("{}: {}", index + 1, line);
        }
    }
}

fn add_line(file_content: &mut Vec<String>, name:String) {
    file_content.push(name.trim().to_string());
    println!("Line added.");
}

fn delete_line(file_content: &mut Vec<String>,name:String) {
    display_content(file_content);
    let name: usize = name.trim().parse().expect("Please enter a valid number");

    if name > 0 && name <= file_content.len() {
        file_content.remove(name - 1);
        println!("Line deleted.");
    } else {
        println!("Invalid line number.");
    }
}

fn write_file(file_name: &str, file_content: &[String]) {
    let mut file = File::create(file_name).expect("Unable to create file");
    for line in file_content {
        writeln!(file, "{}", line).expect("Unable to write line");
    }
    println!("File written successfully.");
}
