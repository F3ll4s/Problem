use crate::LibraryItem;
pub struct AudioBook{
    title:String,
    is_available:bool,
}

impl LibraryItem for AudioBook{
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


impl AudioBook{
    pub fn new(x:&str) -> Self{
        AudioBook{
            title:x.to_string(),
            is_available: true,
        }
    }
}