
fn warmest_period(data:&Vec<(f64,u32,bool)>,count:usize) -> &[(f64,u32,bool)]{
    let mut avg:f64 = 0.0;
    let mut save = 0;
    for x in 0..=(data.len()-count){
        let mut result = 0.0;
        for y in 0..count{
            result += data[x+y].0
        }
        let average = result / count as f64;
            if avg < average{
                avg = average;
                save = x;
        }
    }
    return &data[save as usize..(save + count) as usize];
}
fn coldest_day(data:&Vec<(f64,u32,bool)>) -> i32 {
    let mut lowest = data[0].0;
    let mut save = 0;
    for i in 0..data.len(){
        let mut info = data[i].0;
        if lowest > info{
            lowest = info;
            save = i+1;
        }
    }
    return save as i32;
}
fn predict_rain(temp:f64, humid:u32) -> bool{
        let mut rain_prop = 0.005 * humid as f64 + 0.02 * temp - 1.0;
        if rain_prop > 0.5{
            return true
        }
        return false
}
fn count_rainy_days(data:&Vec<(f64,u32,bool)>) -> i32{
    let mut count = 0;
    for i in 0..data.len(){
        if data[i].2 == true{
            count += 1 
        }
    }
    return count
}

fn main() {
    let weather_data = vec![
        (25.0, 65, false), (26.2, 70, false), (24.8, 62, false), (23.5, 78, true), (22.1, 82, true),
        (20.7, 85, true), (21.3, 80, true), (22.8, 73, false), (24.0, 68, false), (25.5, 60, false),
        (27.1, 55, false), (28.3, 52, false), (27.9, 58, false), (26.6, 64, false), (25.2, 70, true),
        (23.8, 75, true), (22.4, 80, true), (21.0, 83, true), (20.5, 86, true), (21.8, 82, true),
        (23.2, 77, false), (24.5, 70, false), (25.8, 63, false), (26.4, 58, false), (27.0, 53, false),
        (26.7, 56, false), (25.3, 62, false), (24.9, 68, true), (23.1, 74, true), (21.7, 79, true)
    ];

    let warmest_period = warmest_period(&weather_data, 3);
    println!("Warmest 3-day period: {:?}", warmest_period);

    let coldest_day = coldest_day(&weather_data);
    println!("Coldest day: {}", coldest_day);

    let rainy_days_count = count_rainy_days(&weather_data);
    println!("Number of rainy days: {}", rainy_days_count);

    // Example rain prediction
    let (temperature, humidity, _) = weather_data[0];
    let will_rain = predict_rain(temperature, humidity);
    println!("Will it rain on the first day? {}", will_rain);
}