mod restaurant;

fn main() {
    println!("Restaurant Management System");
    restaurant::back_of_house::hosting1::clean();
    restaurant::back_of_house::serving2::sleep();
    restaurant::front_of_house::hosting::eating();
    restaurant::front_of_house::serving::drinking();
    // restaurant::call_function();
    // Public mod will ccan be easily access to all the file 
    // mod will restrict you to go one by one like access file by file to function 
}
