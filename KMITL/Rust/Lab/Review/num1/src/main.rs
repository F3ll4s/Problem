use std::io;

fn main() {
    let mut storage: Vec<(u32,String,u32)> = Vec::new();
    loop{
        println!("Warehouse Inventory Management:");
        println!("1. Add New Product");
        println!("2. Update the Stock Quantity");
        println!("3. Remove Product");
        println!("4. List all the product");
        println!("5. Exit");
        println!("Enter your choice: ");
        let mut number = String::new();
        io::stdin().read_line(&mut number).expect("Failed to read");
        match number.trim().parse(){
            Ok(1) =>{
                println!("ID of new product");
                let mut id = String::new();
                io::stdin().read_line(&mut id).expect("Failed to read"); 
                let mut id:u32 = match id.trim().parse(){
                    Ok(num) => num,
                    Err(_) => {
                        println!("Invalid Number");
                        continue;
                    }
                };  
                let mut id_exist = false; 
                for item in &storage{
                    if item.0 == id{
                        id_exist = true;
                        break;
                    }
                }
                if id_exist{
                    println!("ID already exist");
                    continue;
                }
                println!("Name of Product");
                let mut name = String::new();
                io::stdin().read_line(&mut name).expect("Failed to read");
                let mut name = name.trim().to_string();

                println!("Quantity of product");
                let mut quantity = String::new();
                io::stdin().read_line(&mut quantity).expect("Failed to read");
                let mut quantity: u32 = match quantity.trim().parse(){
                    Ok(num) => num,
                    Err(_) =>{
                        println!("Thats not a number");
                        continue;
                    }
                };
                storage.push((id,name,quantity));
            }
            Ok(2) =>{
                println!("Choose ID number: ");
                let mut id = String::new();
                io::stdin().read_line(&mut id).expect("Failed to read");
                let id:u32 = id.trim().parse().expect("Failed to read");
                for item in &mut storage{
                    if item.0 == id {
                        println!("Put quantity that want to change");
                        let mut stock = String::new();
                        io::stdin().read_line(&mut stock).expect("Failed to read");
                        let stock:u32 = stock.trim().parse().expect("Failed to read");
                        item.2 = stock;
                    }else{
                        println!("Thats id doesnt exist");
                        continue;
                    }
                }
            }
            Ok(3) =>{
                println!("Yippee"); 
            }
            Ok(4) =>{
                for item in 0..storage.len() {
                    println!("{},{},{}", storage[item].0, storage[item].1, storage[item].2);
                } 
            }
            Ok(5) =>{
                break;
            }
            Ok(any_number)=>{
                println!("Thats not in a choice ");
            }
            Err(_) =>{
                println!("Thats not a number");
            }
        }
    }
    // println!("{}",name);
    // let employee:(&str,u16,f32) = ("Alice",30,0.77);
    // println!("{}",employee.0);
    
}
