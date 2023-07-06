function string_to_dict_datetime(string_to_conv){
    console.log(string_to_conv);
    const [date, time, year] = string_to_conv.split(" ")
    const [day, month] = date.split("/")
    const [hour, minute] = time.split(":");
    const dict_t = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "minute": minute
    }
    console.log(dict_t);
    return dict_t;
}