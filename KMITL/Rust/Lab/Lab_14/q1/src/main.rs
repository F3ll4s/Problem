use std::thread;

fn main(){
    let mut something = Vec::new();

    for i in 1..=5{
        let somethings = thread::spawn(move||{
            println!("Threads:{} Result:{}",i ,i*1);
        });
        something.push(somethings);  
    }

    for somethings in something{
        somethings.join().unwrap()
    }
    
}
