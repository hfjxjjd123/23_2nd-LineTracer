#include <AFMotor.h>

AF_DCMotor motorLeft(1);
AF_DCMotor motorRight(2);

String LeftSpeed, RightSpeed;
int  i, leftInput, rightInput;
byte DataToRead[9];

void setup() {
  Serial.begin(9600);

  motorLeft.run(RELEASE);
  motorRight.run(RELEASE);
}

void loop() {
  // DataToRead Format == 'L100R020\n';
  DataToRead[8] = '\n';
  Serial.readBytesUntil(char(13), DataToRead, 8);
  
/* For Debugging -> Rpi */
  for (i = 0; i < 9; i++) {
    Serial.write(DataToRead[i]);
    if (DataToRead[i] == '\n') break;
  }

  LeftSpeed = "";
  RightSpeed = "";

  for (i=1; i<4; i++){
    LeftSpeed += DataToRead[i];
  }
  for (i=5; (i<8) && (DataToRead[i] != '\n'); i++){
    RightSpeed += DataToRead[i];
  }

  leftInput = LeftSpeed.toInt();
  rightInput = RightSpeed.toInt();

  motorLeft.run(FORWARD);
  motorRight.run(FORWARD);
  motorLeft.setSpeed(leftInput);
  motorRight.setSpeed(rightInput);
  //TODO Delay Setting
  delay(1000); 
  motorLeft.run(RELEASE);
  motorRight.run(RELEASE);
}
