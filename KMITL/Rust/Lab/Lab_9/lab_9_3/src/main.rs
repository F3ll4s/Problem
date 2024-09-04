
struct Data{
    x:i32,
    y:f32,
    z:char,
    q:bool
}

fn as_bytes<T>(x: &T) -> &[u8]{
    unsafe{
        std::slice::from_raw_parts( 
            x as *const _ as *const u8,
            std::mem::size_of::<T>()
        )
    }
} 
    

fn main() {
let data = Data{
    x:1,
    y:1.0,
    z:'A',
    q:true
};
    println!("{:?}",as_bytes(&data));
    
    // let num:i32 = 127886767;
    // let big_endian = num.to_be(); // Convert to big-endian
    // let little_endian = num.to_le(); // Convert to little-endian
    // println!("{}",big_endian);
    // println!("{}",little_endian);
}