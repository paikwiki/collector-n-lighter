int RelayPin = 3;
int SwitchPin = 9;

int toggleValue = 0;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(RelayPin, OUTPUT);
  pinMode(SwitchPin, INPUT_PULLUP);
}

void loop() {
  if (toggleValue == 0) {
    Serial.println("HIGH");
    digitalWrite(RelayPin, HIGH);
    toggleValue = 1;
    delay(3000);
  } else {
    digitalWrite(RelayPin, LOW);
    toggleValue = 0;
    delay(3000);
  }
  
//  if (digitalRead(SwitchPin) == LOW) {
//    Serial.println("HIGH");
//    digitalWrite(RelayPin, HIGH);
//    delay(100);
//  } else {
//    digitalWrite(RelayPin, LOW);
//    delay(100);
//  }

//  if (toggleValue == 0) {
//    digitalWrite(RelayPin, HIGH);
//    toggleValue = 1;
//    delay(1000);
//  } else {
//    digitalWrite(RelayPin, LOW);
//    toggleValue = 0;
//    delay(1000);
//  }
}
