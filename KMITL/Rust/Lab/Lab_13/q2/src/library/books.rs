use crate::LibraryItem;
pub struct Book{
    title:String,
    is_available:bool,
}

impl LibraryItem for Book{
    fn title(&self) -> &str{
        &self.title
    }
    fn check_out(&mut self){
        self.is_available = false;
    }
    fn check_in(&mut self){
        self.is_available = true;
    }
    fn is_available(&mut self) -> bool{
        self.is_available
    }
}

impl Book{
    pub fn new(x:&str) -> Self{
        Book{
            title:x.to_string(),
            is_available: true,
        }
    }
}