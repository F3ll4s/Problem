use std::io::Read;

fn main() {
    let args: Vec<_> = std::env::args().collect();
    if (args.len()-1) == 1{
        let path = args[1].clone();
        let mut file = std::fs::File::open(&path).unwrap();
        let mut contents = String::new();
        file.read_to_string(&mut contents).unwrap();
        let character = contents.len();
        let line = contents.lines().count();
        let mut word:i32 = 0;
        for i in contents.split_whitespace(){
            word += 1;
        }
        println!("File: {}",&path);
        println!("Lines: {}",line);
        println!("Words: {}",word);
        println!("Characters: {}",character);
    }else{
        println!("Missing File Path Argument");
        std::process::exit(2);
    }
}