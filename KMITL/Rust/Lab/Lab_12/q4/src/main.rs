use std::io::Write;
use std::io;
use std::io::Read;
fn main() {
    let mut file = std::fs::File::create("output.txt").unwrap();
    let mut input = String::new();

    loop{
        io::stdin().read_line(&mut input).expect("Failed to read");

        if input == "\r\n"{
            break;
        }else{
            file.write(format!("{}",input).as_bytes()).unwrap();
        }
        input.clear()

    }
    let mut file = std::fs::File::open("output.txt").unwrap();
        let mut contents = String::new();
        file.read_to_string(&mut contents).unwrap();
        println!("{}",contents.to_uppercase())

    
}
