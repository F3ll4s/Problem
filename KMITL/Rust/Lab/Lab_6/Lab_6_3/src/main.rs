trait SimpleAnalyzable{
    fn mean_or_median
}

impl SimpleAnalyzable for Vec<f64>{
    fn mean(&self) -> f64{
        
    }
    fn median(&self) -> f64{

    }
}

struct SimpleDataSet{
    data:Vec<f64>
}

impl SimpleDataSet{
    fn new(data:Vec<f64>)-> Self{   

    }

    fn filter<F>(&self,predicate:F)->Self
    where
        F:Fn(&f64)->bool,
    {
        SimpleDataSet{
            data:self.data.iter().cloned.filter(predicate).collect(),
        }
    }
}

impl SimpleAnalyzable for SimpleDataSet{

}

fn main(){
    let data = SimpleDataSet::new(vec![1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]);
    println!("Mean {}",data.mean());
    println!("Median {}",data.median());
    let filtered_data = data.filter(|&x|x>4.0);
    println!("Filtered Mean: {}", filtered_data.mean());
    println!("Filtered Mean: {}", filtered_data.median());
}




