
unsigned long lastMillis = 0;
int timeDelay = 5000;
unsigned long counter = 0;

bool ledState = 0;
int ledPin = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
}

void loop() {
  if(Serial.available() > 0){
    int msg = Serial.parseInt();
    if(msg == 0){
      ledState = false;
    }else{
      ledState = true;
    }
    Serial.print("I received: ");
    Serial.println(msg);
  }
  digitalWrite(ledPin, ledState);
  // put your main code here, to run repeatedly:
  if(millis()- lastMillis > timeDelay){
    Serial.print("Hello Pi, I did ");
    Serial.print(counter);
    Serial.println(" turns so far");
    lastMillis = millis();
    counter ++;
  }
  

}
