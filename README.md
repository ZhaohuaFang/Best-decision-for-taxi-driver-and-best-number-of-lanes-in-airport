In this project, I made two mathematical models. The first model helps taxi drivers to determine whether they should wait in line at the "storage pool" to pick up  passengers who are going to arrive at airport from airplanes or they would better return to city center and profit from other customers. The second model tells government what is the best width of road in airport if they want to have a higher income.

# Backgorund one
Since most passengers have to go to destinations in the urban area (or surroundings) after getting off the plane, and taxis are more convenient than other means of transportation, taxis are a commonly used means of transportation.

Most domestic airports separate the drop-off (departure area) from the drop-off (arrival area).

Taxi drivers who drop off passengers to the airport will face two options: 

## (1) Go to the arrival area and wait in line to carry passengers back to the city.

At this time, the taxi must wait in the designated "storage pool". Taxis must wait in line on the basis of "first come, then come" to carry passengers. The length of the waiting time depends on the number of queued taxis and passengers, and a certain time cost is required.

## (2) Directly return to the city to solicit passengers. 

At this time, taxi drivers will pay no-load fees and may lose potential passenger revenue.

Due to the development of technology, the number of flights arriving in a certain period of time and the number of taxis already in the "storage pool" are observable by the driver.

If passengers want to "ride a taxi" after getting off the plane, they must line up in the designated "ride area" and ride in order. The airport taxi management staff is responsible for releasing the taxis into the "ride area" "in batches" and arranging a certain number of passengers to board the taxi.

### Therefore, the first model here tells drivers which option they should choose based on the specific time point.


# Backgorund two

Increasing the number of lanes would let customers getting off the plane picked up in a shorter time, which can also reduce the waiting costs of taxi drivers. 

However, increasing the number of lanes will result into great cost on government as the cost of road maintenance is also not to be underestimated. 

Hence, the government needs to charge taxi drivers who depart from the airport boarding area 30% of the proceeds.

### Therefore, the second model tells government what is the best width of road if they want to have a higher income while maximizing passenger flow.

I invent a very useful algorithm in time_interval.py, which can reduce the influence of random factors.

Partial output of these two models are presented as below. Some figures' labels may be different from what is shown in the code that I have shared.

![image](https://github.com/ZhaohuaFang/Best-decision-for-taxi-driver-and-best-number-of-lanes-in-airport/blob/master/time-varying%20number%20of%20taxis%20needed%20at%20Beijing%20Capital%20International%20Airport.png)

![image](https://github.com/ZhaohuaFang/Best-decision-for-taxi-driver-and-best-number-of-lanes-in-airport/blob/master/time-varying%20length%20of%20the%20queue.png)

![image](https://github.com/ZhaohuaFang/Best-decision-for-taxi-driver-and-best-number-of-lanes-in-airport/blob/master/time-varying%20actual%20waiting%20time.png)

![image](https://github.com/ZhaohuaFang/Best-decision-for-taxi-driver-and-best-number-of-lanes-in-airport/blob/master/the%20relation%20between%20annual%20government%20revenue%20and%20number%20of%20lanes.png)

We can conclude from the figures that from 0min to 82min and from 970min to 1500min（1440min to 1500min is in next day）, taxi drivers would better go to "storage pool" and wait in line to carry passengers back to the city. During the other time, taxi drivers would get higher profit if they directly return to the city to solicit passengers.

We can also make a conclusion that the best number of lanes is 6.
