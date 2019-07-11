## Installation

You can either get the source code and include it in your application manlually, or use pip instead.

```pip install iwPiWeather```

## Use example

Include your package, define the pins and initialize the thread object

```
import iwPiWeather
displayPinout = { "rs": 22, "en": 17, "d7": 18, "d6": 23, "d5": 24, "d4": 25 }
weather = prodWeather.weatherDisplay(apiKey='passyouroowmapikey', poolRate=120, dispPins=displayPinout, autoStart=True)
```
For the passed constructor arguments, you will have to provide your OWM API key. You can also control the rate for which the calls are made to the owm API (using the poolRate argument), and you can also specify different pinout in case you are not using the default one(dispPins). You can also toggle autoStart to false to prevent manual start of the thread and have it run in sleep mode at the beginning.
The created weather object will be actually a thread that runs in the background. So you can integrate this functionality in your application, this will run as a background process in a separate thread. 

You can temporarily pause the display update thread by calling
```weather.stopWatch()```
which will allow you for example to stop pooling and displaying the weather data on the display and use the display for something else in your integration. 

To restart the thread and keep reprinting the weather data you can use 
```weather.startWatch()```

To stop the thread and cleanup the object you can call 
```weather.stopThread()```.

This will kill the thread and you can safely stop the application.
