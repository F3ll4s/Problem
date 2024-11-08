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