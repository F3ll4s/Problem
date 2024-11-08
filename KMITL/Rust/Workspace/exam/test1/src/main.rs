use std::thread;

fn main(){
    let mut something = Vec::new();
    for i in 1..=5{
        let somethings = thread::spawn(move||{
            println!("{} {}",i , i*i)
        });
        something.push(somethings)
    }
    for somethings in something{
        somethings.join().unwrap()
    }
}