use std::io ;

fn main(){
    let mut warehouse: Vec<(u32,String,u32)> = Vec::new();
    loop{
        let mut choice = String::new();
        println!("Warehouse Inventory Management:");
        println!("1. Add New Product");
        println!("2. Update the Stock Quantity");
        println!("3. Remove Product");
        println!("4. List all the product");
        println!("5. Exit");
        println!("Enter your choice: ");
        io::stdin().read_line(&mut choice).expect("Failed to read line");
        match choice.trim().parse(){
            Ok(1) =>{
                
                let mut id = String::new(); 
                println!("ID of new product: ");
                io::stdin().read_line(&mut id).expect("This not number");
                let id: u32 = match id.trim().parse(){
                    Ok(num)=>num,
                    Err(_)=>{
                        println!("Invalid Number");
                        continue;
                    }
                };
                
                let mut id_exist = false;
                for item in &warehouse{
                    if item.0 == id{
                        id_exist = true;
                        break;
                    }
                }
                if id_exist{
                    println!("ID already Exist");
                    continue;
                }
                let mut name = String::new(); 
                println!("Name of Product: ");
                io::stdin().read_line(&mut name).expect("This is not name");
                let name = name.trim().to_string();
                

                let mut quantity = String::new(); 
                println!("Number of Stock: ");
                io::stdin().read_line(&mut quantity).expect("This is not name");
                let quantity: u32 = match quantity.trim().parse(){
                    Ok(num) => num,
                    Err(_) => {
                        println!("Invalid Number");
                        continue;
                    }
                };

                warehouse.push((id,name,quantity));

            }
            Ok(2) =>{
                let mut id: String = String::new();
                println!("Choose the ID number");
                io::stdin().read_line(&mut id).expect("Failed to load");
                let id: u32 = id.trim().parse().expect("Failed to Load");
                for item in &mut warehouse{
                    if item.0 == id{
                        println!("Update the Quantity: ");
                        let mut stock = String::new();
                        io::stdin().read_line(&mut stock).expect("Failed to load");
                        let stock: u32 = stock.trim().parse().expect("Failed to Load");
                        item.2 = stock;
                    }else{
                        println!("Not Existing ID");
                        continue;
                    }
                }
            }
            Ok(3) =>{
                let mut id: String = String::new();
                println!("Choose the ID number");
                io::stdin().read_line(&mut id).expect("Failed to load");
                let id: u32 = id.trim().parse().expect("Failed to Load");
                for i in 0..warehouse.len(){
                    if id == warehouse[i].0{
                        warehouse.remove(i);
                    }else{
                        println!("Not Existing ID");
                    }
                }
            }
            Ok(4) =>{
                for item in 0..warehouse.len(){
                    println!("{}, {},{}", warehouse[item].0,warehouse[item].1,warehouse[item].2);
                }
            }
            Ok(5) =>{
                break;
            }
            Ok(any_number) => {
                println!("Invalid input. Please enter a number.");
            }
            Err(_)=>{
                println!("Invalid input. Please enter a number.");
            }
        }
    }
}