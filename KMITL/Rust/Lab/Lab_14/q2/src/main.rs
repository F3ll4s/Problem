use std::thread;
use std::sync::mpsc;

fn main(){
    let (tx,rx) = mpsc::channel();

    let handle = thread::spawn(move||{
        for i in 1..=5{
            let value = i;
            tx.send(value).unwrap()
        }
    });

    for i in 1..=5{
        let result = rx.recv().unwrap();
        thread::sleep(std::time::Duration::from_secs(2));
        println!("{}",result);
    }
    handle.join().unwrap()
}