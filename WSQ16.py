def average(cars):
    count = 0
    midPrice = 0
    cityPrice = 0
    highPrice = 0
    for line in cars:
        if(count % 2 == 0):
            mdp = float(line[42:46])
            midPrice = midPrice + mdp
            ctp = float(line[52:54])
            cityPrice = cityPrice + ctp
            hgp = float(line[55:57])
            highPrice = highPrice + hgp
        count = count + 1
        x = count / 2
        midrange = midPrice / x
        city = cityPrice / x
        highway = highPrice / x
    return(midrange, city, highway)

cars = open("cars.txt")
(midrange, city, highway) = average(cars)
print("Average midrange price: $",midrange)
print("Average gas mileage in city: ",city)
print("Average gas mileage on highway: ",highway)
